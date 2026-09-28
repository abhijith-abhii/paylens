import json,pytest
from core import ROOT,predict,FEATURES

def test_split_separation():
 m=json.loads((ROOT/'artifacts/evaluation.json').read_text());a,b,c=[set(m[k]) for k in ['train_ids','test_ids','calibration_ids']];assert not (a&b or a&c or b&c)
 assert 'salary' not in FEATURES

def test_prediction():
 y,r=predict({});assert y>0 and r>0
@pytest.mark.parametrize('p',[{'experience':-1},{'experience':'nan'},{'role':'unknown'},{'experience':50}])
def test_invalid(p):
 with pytest.raises(ValueError):predict(p)
