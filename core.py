from pathlib import Path
import json,math
import numpy as np,pandas as pd,joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error,r2_score
ROOT=Path(__file__).parent;FEATURES=['experience','role','region','education','remote']
def train():
 df=pd.read_csv(ROOT/'data/salaries.csv')
 if df.id.duplicated().any() or df[FEATURES+['salary']].isna().any().any():raise ValueError('Duplicate IDs or missing values')
 fit,test=train_test_split(df,test_size=.2,random_state=28);train,cal=train_test_split(fit,test_size=.25,random_state=28)
 assert not (set(train.id)&set(test.id) or set(train.id)&set(cal.id) or set(cal.id)&set(test.id))
 prep=ColumnTransformer([('number',StandardScaler(),['experience']),('category',OneHotEncoder(handle_unknown='error'),FEATURES[1:])]);model=make_pipeline(prep,Ridge(alpha=10))
 model.fit(train[FEATURES],train.salary);base=DummyRegressor(strategy='median').fit(train[FEATURES],train.salary)
 residuals=np.abs(cal.salary-model.predict(cal[FEATURES]));level=min(1,math.ceil((len(cal)+1)*.9)/len(cal));radius=float(np.quantile(residuals,level,method='higher'))
 pred=model.predict(test[FEATURES]);metrics={'test_mae_usd':round(mean_absolute_error(test.salary,pred),2),'baseline_mae_usd':round(mean_absolute_error(test.salary,base.predict(test[FEATURES])),2),'test_r2':round(r2_score(test.salary,pred),4),'interval_coverage':round(float(np.mean(np.abs(test.salary-pred)<=radius)),4),'interval_radius_usd':round(radius,2),'split_sizes':{'train':len(train),'calibration':len(cal),'test':len(test)},'test_ids':test.id.tolist(),'train_ids':train.id.tolist(),'calibration_ids':cal.id.tolist(),'data':'synthetic; no empirical labor-market validity'}
 (ROOT/'artifacts').mkdir(exist_ok=True);joblib.dump({'model':model,'radius':radius},ROOT/'artifacts/model.joblib');(ROOT/'artifacts/evaluation.json').write_text(json.dumps(metrics,indent=2));return metrics

def predict(p):
 x={k:p.get(k,d) for k,d in zip(FEATURES,[3,'software','midwest','masters','yes'])};x['experience']=float(x['experience'])
 if not math.isfinite(x['experience']) or not 0<=x['experience']<=18:raise ValueError('Experience must be 0–18 years')
 for k,allowed in {'role':['software','data','platform'],'region':['midwest','northeast','west'],'education':['bachelors','masters'],'remote':['yes','no']}.items():
  if x[k] not in allowed:raise ValueError('Unsupported '+k)
 if not (ROOT/'artifacts/model.joblib').exists():raise ValueError('Model missing; run python train.py')
 saved=joblib.load(ROOT/'artifacts/model.joblib');y=float(saved['model'].predict(pd.DataFrame([x]))[0]);return y,saved['radius']
def analyze(p):
 y,r=predict(p);m=json.loads((ROOT/'artifacts/evaluation.json').read_text())
 return dict(metrics={'Illustrative estimate':f'${y:,.0f}','90% calibrated interval':f'${max(0,y-r):,.0f}–${y+r:,.0f}','Holdout MAE':f"${m['test_mae_usd']:,.0f}",'Observed coverage':f"{m['interval_coverage']:.1%}"},notice='Synthetic USD compensation model. Calibration coverage relies on exchangeability; this is not a real-world salary estimate.',bars=[{'label':'Median baseline MAE','value':m['baseline_mae_usd']},{'label':'Ridge MAE','value':m['test_mae_usd']}],details=m)
