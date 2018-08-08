# diabetes_use_case
Sample use case for Xavier AI in Healthcare conference: https://www.xavierhealth.org/ai-summit-day2/

# Dockerfile instructions:

`$ mkdir anaconda_py35_h2o_xgboost_graphviz_shap`

`$ curl https://raw.githubusercontent.com/jphall663/diabetes_use_case/master/anaconda_py35_h2o_xgboost_graphviz_shap/Dockerfile > anaconda_py35_h2o_xgboost_graphviz_shap/Dockerfile`

`$ sudo docker build anaconda_py35_h2o_xgboost_graphviz_shap`

`$ sudo docker images`

`$ sudo docker run -i -t -p 8888:8888 <image_id> /bin/bash -c "/opt/conda/bin/conda install jupyter -y --quiet && /opt/conda/bin/jupyter notebook --notebook-dir=/diabetes_use_case --ip='*' --port=8888 --no-browser"`
