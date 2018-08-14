# diabetes_use_case

The files in this repository are meant to provide a reproducible example use case for interpretable machine learning techniques applied to a basic health care use case. The [Jupyter notebook herein](Binary-Classification-Readmit.ipynb) will be presented at the [Xavier AI in Healthcare conference](https://www.xavierhealth.org/ai-summit-day2/).

The training data for this use case is available [here](https://www.kaggle.com/brandao/diabetes). The data set contains demographic and medical information about many patients. It is used to create a white-box classifier for predicting who will be readmitted to a hospital within 30 days of discharge. This notebook attempts to showcase the use of a complex, but transparent, nonlinear classifier as an alternative to more traditional linear model approaches.

Typically it requires many different methods to properly interpret a nonlinear classifier. Several different types of interpretation and explanation methods are used here including global, local, low-fidelity, and high-fidelity methods including:

* Global and local Shapley variable importance
* Partial dependence
* Individual conditional expectation (ICE)
* Surrogate decision trees

# Dockerfile instructions:

A [Dockerfile](anaconda_py35_h2o_xgboost_graphviz_shap/Dockerfile) is provided to build a docker container with all necessary packages and dependencies. This is the easiest way to use the example [notebook](Binary-Classification-Readmit.ipynb) if you are on Mac OS X, \*nix, or Windows 10. To do so:</br>

1. Install and start [docker](https://www.docker.com/).

The from a terminal run:

2. Create a directory for the Dockerfile.</br>
`$ mkdir anaconda_py35_h2o_xgboost_graphviz_shap`

3. Fetch the Dockerfile.</br>
`$ curl https://raw.githubusercontent.com/jphall663/diabetes_use_case/master/anaconda_py35_h2o_xgboost_graphviz_shap/Dockerfile > anaconda_py35_h2o_xgboost_graphviz_shap/Dockerfile`

4. Build a docker image from the Dockefile.</br>
`$ docker build --no-cache anaconda_py35_h2o_xgboost_graphviz_shap`

5. Display docker image IDs. You are probably interested in the most recently created image. </br>
`$ docker images`

6. Start the docker image and the Jupyter notebook server.</br>
`$ docker run -i -t -p 8888:8888 <image_id> /bin/bash -c "/opt/conda/bin/conda install jupyter -y --quiet && /opt/conda/bin/jupyter notebook --notebook-dir=/diabetes_use_case --ip='*' --port=8888 --no-browser"`</br>

(If you need `root` priviledges to run docker, try this command:`$ sudo docker run -i -t -p 8888:8888 <image_id> /bin/bash -c "/opt/conda/bin/conda install jupyter -y --quiet && /opt/conda/bin/jupyter notebook --notebook-dir=/diabetes_use_case --ip='*' --port=8888 --no-browser --allow-root"`</br>

7. Then navigate to port 8888 on your machine, probably `http://localhost:8888/`.

# Manual Installation

For users with older Windows machines or others who can't/don't use docker, the notebook dependencies can be installed manually:

1. Anaconda Python 5.1.0 from the [Anaconda archives](https://repo.continuum.io/archive/).
2. [Java](https://java.com/download).
3. The latest stable [h2o](https://www.h2o.ai/download/) Python package.
4. [Git](https://git-scm.com/downloads).
5. [XGBoost](https://github.com/dmlc/xgboost) with Python bindings.
6. [GraphViz](http://www.graphviz.org/).
7. Install the [shap](https://github.com/slundberg/shap) Python package.

Anaconda Python, Java, Git, and GraphViz must be added to your system path.

From a terminal:

7. Clone the repository with examples.</br>
`$ git clone https://github.com/jphall663/diabetes_use_case.git`

8. `$ cd interpretable_machine_learning_with_python`

9. Start the Jupyter notebook server.</br>
`$ jupyter notebook`

10. Navigate to the port Jupyter directs you to on your machine, probably `http://localhost:8888/`.
