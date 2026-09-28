import csv,random
from pathlib import Path
rng=random.Random(9028);root=Path(__file__).parent; (root/'data').mkdir(exist_ok=True)
with (root/'data/salaries.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['id','experience','role','region','education','remote','salary'])
 for i in range(1200):
  exp=rng.randint(0,18);role=rng.choice(['software','data','platform']);region=rng.choice(['midwest','northeast','west']);edu=rng.choice(['bachelors','masters']);remote=rng.choice(['yes','no'])
  salary=48000+exp*4100+{'software':6000,'data':9000,'platform':11000}[role]+{'midwest':0,'northeast':9000,'west':18000}[region]+(edu=='masters')*6000+(remote=='yes')*2000+rng.gauss(0,11000+exp*200)
  w.writerow([f'S{i:04}',exp,role,region,edu,remote,round(max(26000,salary))])
