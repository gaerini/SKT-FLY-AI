# Azure를 이용한 머신 러닝

[Azureml 노션링크] (https://helloailab.notion.site/Azure-MLOps-20cb9b49216a4f13a5cd585e723dde65)  


1. 워크스페이스 생성
``` python
from azureml.core import Workspace
ws = Workspace.from_config()
print('Workspace name:' + ws.name,
      'Azure region:' + ws.location,
      'Subscription ID:' + ws.subscription_id,
      'Resource Group:' + ws.resource_group
)
```

2.  

``` python
from azureml.core import Experiment
experiment = Experiment(workspace = ws, name = 'diabetes-experiment')
```

3. 당뇨병 샘플 데이터를 판다스 데이터 프레임으로 가져오기  
``` python
from azureml.opendatasets import Diabetes
from sklearn.model_selection import train_test_split

x_df = Diabetes.get_tabular_dataset().to_pandas_dataframe().dropna() # dropna()는 빈 정보를 없애주는 커맨드이다.
```

4.  
``` python
from azureml.opendatasets import Diabetes
from sklearn.model_selection import train_test_split

x_df = Diabetes.get_tabular_dataset().to_pandas_dataframe().dropna()
y_df = x_df.pop("Y")

x_train, x_test, y_train, y_test = train_test_split(x_df, y_df, test_size = 0.2, random_state = 66)
print(x_train)
```

5. 학습을 위한 작업들  
``` python
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib
import math

#10번 반복하게 된다.
alphas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 0.8, 0.9, 1.0]

#실험 수행
for alpha in alphas:
    run = experiment.start_logging()
    run.log('alpha_value', alpha)

    #Ridge 알고리즘 사용
    model = Ridge(alpha = alpha)
    model.fit(X=x_train, y=y_train)

    y_pred = model.predict(X = x_test)

    rmse = mean_squared_error(y_true = y_test, y_pred = y_pred)

    run.log('rmse')

    model_name = 'model_alpha_' + str(alpha) + '.pkl'

    filename = 'outputs/' + model_name

    joblib.dump(value = model, filename = filename)

    run.complete()

    #alpha 값을 치환해서 출력
    print(f'{alpha} exp completed')



```

결과가 다음과 같이 나오게 된다.  
``` python
0.1 exp completed
0.2 exp completed
0.3 exp completed
0.4 exp completed
0.5 exp completed
0.7 exp completed
0.8 exp completed
0.9 exp completed
1.0 exp completed
```

5. document로 보여준다.  
```pyhton
experiment
```

6. rmse 의 metric 가져오기  
``` python
minimum_rmse_runid = None
minimum_rmse = None

for run in experiment.get_runs():
    run_metrics = run.get_metrics()
    run_details = run.get_details()
    # each logged metric becomes a key in this returned dict
    run_rmse = run_metrics["rmse"]
    run_id = run_details["runId"]
    
    if minimum_rmse is None:
        minimum_rmse = run_rmse
        minimum_rmse_runid = run_id
    else:
        if run_rmse < minimum_rmse:
            minimum_rmse = run_rmse
            minimum_rmse_runid = run_id

print("Best run_id: " + minimum_rmse_runid)
print("Best run_id rmse: " + str(minimum_rmse))
```

7. best model download  
``` python
minimum_rmse_runid = None
minimum_rmse = None

for run in experiment.get_runs():
    run_metrics = run.get_metrics()
    run_details = run.get_details()
    # each logged metric becomes a key in this returned dict
    run_rmse = run_metrics["rmse"]
    run_id = run_details["runId"]
    
    if minimum_rmse is None:
        minimum_rmse = run_rmse
        minimum_rmse_runid = run_id
    else:
        if run_rmse < minimum_rmse:
            minimum_rmse = run_rmse
            minimum_rmse_runid = run_id

print("Best run_id: " + minimum_rmse_runid)
print("Best run_id rmse: " + str(minimum_rmse))
```

``` python
from azureml.core import Run
best_run = Run(experiment=experiment, run_id=minimum_rmse_runid)
print(best_run.get_file_names())
```
``` python
best_run.download_file(name=str(best_run.get_file_names()[0]))
```

8. datastore에 등록
``` python
import numpy as np
from azureml.core import Dataset

np.savetxt('features.csv', X_train, delimiter=',')
np.savetxt('labels.csv', y_train, delimiter=',')

datastore = ws.get_default_datastore()
datastore.upload_files(files=['./features.csv', './labels.csv'],
                       target_path='diabetes-experiment/',
                       overwrite=True)

input_dataset = Dataset.Tabular.from_delimited_files(path=[(datastore, 'diabetes-experiment/features.csv')])
output_dataset = Dataset.Tabular.from_delimited_files(path=[(datastore, 'diabetes-experiment/labels.csv')])
```

9. best model 등록  
``` python
import sklearn

from azureml.core import Model
from azureml.core.resource_configuration import ResourceConfiguration


model = Model.register(workspace=ws,
                       model_name='diabetes-experiment-model',
                       model_path=f"./{str(best_run.get_file_names()[0])}", 
                       model_framework=Model.Framework.SCIKITLEARN,  
                       model_framework_version=sklearn.__version__,  
                       sample_input_dataset=input_dataset,
                       sample_output_dataset=output_dataset,
                       resource_configuration=ResourceConfiguration(cpu=1, memory_in_gb=0.5),
                       description='Ridge regression model to predict diabetes progression.',
                       tags={'area': 'diabetes', 'type': 'regression'})

print('Name:', model.name)
print('Version:', model.version)
# 등록을 하게 되면 내 azure ml에 모델에 저장된다. 
```