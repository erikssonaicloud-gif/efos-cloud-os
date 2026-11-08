"""Re-extract nearest-pixel LST and QA at the report's stated coordinates.
Install: pip install requests pandas rasterio planetary-computer
Run from this directory: python reproduce.py
Uses saved STAC responses; signed asset access tokens are requested at runtime.
"""
import json
from pathlib import Path
import pandas as pd
import rasterio
from rasterio.warp import transform
import planetary_computer as pc

ROOT = Path(__file__).resolve().parent
SITES = {'chapin': (-122.61601, 45.33286),
         'rivercrest': (-122.60766, 45.34510),
         'hillendale': (-122.59703, 45.32901)}
rows = []
for _, claim in pd.read_csv(ROOT / 'scene_validation.csv').iterrows():
    catalog = json.loads((ROOT / f"stac_{claim['date']}.json").read_text())
    feature = next(f for f in catalog['features'] if f['id'] == claim['matched_scene_id'])
    thermal = next(k for k, a in feature['assets'].items()
                   if k.startswith('lwir') and 'temperature' in a.get('roles', []))
    for key in [thermal, 'qa_pixel', 'qa_radsat', 'qa']:
        asset = feature['assets'][key]
        with rasterio.open(pc.sign(asset['href'])) as ds:
            xs, ys = transform('EPSG:4326', ds.crs,
                               [p[0] for p in SITES.values()],
                               [p[1] for p in SITES.values()])
            samples = ds.sample(zip(xs, ys))
            for site, x, y, sample in zip(SITES, xs, ys, samples):
                dn = int(sample[0])
                row, col = ds.index(x, y)
                rows.append(dict(date=claim['date'], scene_id=feature['id'],
                                 site=site, asset_key=key, raw_dn=dn,
                                 pixel_row=row, pixel_col=col,
                                 retrieved_lst_f=((dn * .00341802 + 149 - 273.15) * 1.8 + 32)
                                 if key == thermal and dn else None,
                                 asset_url=asset['href']))
pd.DataFrame(rows).to_csv(ROOT / 'reproduced_samples.csv', index=False)
print('Re-extraction complete.')
