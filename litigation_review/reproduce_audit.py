from pathlib import Path
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats
p=Path(__file__).parent
d=pd.read_csv(p/'reconstructed_table_and_checks.csv')
d['control']=(d.rivercrest+d.hillendale)/2
d['excess']=d.chapin-d.control
d['heat']=d.ambient>=90
print(d.groupby('heat')[['ambient','chapin','control','excess']].agg(['count','mean']))
for y in ['chapin','control','excess']:
 f=sm.OLS(d[y],sm.add_constant(d.ambient)).fit()
 print(y, f.summary())
print('Two-sided Welch test of between-regime excess:',stats.ttest_ind(d.loc[d.heat,'excess'],d.loc[~d.heat,'excess'],equal_var=False))
l=d.melt(id_vars=['date','ambient','heat'],value_vars=['chapin','rivercrest','hillendale'],var_name='site',value_name='lst')
l['interaction']=((l.site=='chapin') & l.heat).astype(int)
print(smf.ols('lst ~ C(site)+ambient+interaction',l).fit().summary())
print('Era means:',d.assign(phase=pd.cut(pd.to_datetime(d.date).dt.year,[1993,2008,2018,2026],labels=['pre','removal','post'])).groupby('phase',observed=True).excess.mean())
# Tests above are transparent exploratory diagnostics, not validated causal inference.
