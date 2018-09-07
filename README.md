# Diabetes data use case

**Contents**

* [Motivation](https://github.com/jphall663/diabetes_use_case#motivation)
* [Usage](https://github.com/jphall663/diabetes_use_case#usage)
  * [Docker Install](https://github.com/jphall663/diabetes_use_case#dockerfile-instructions)
  * [Manual Install](https://github.com/jphall663/diabetes_use_case#manual-installation)

## Motivation

### Interpretability: The missing link between machine learning, healthcare, and the FDA?

*Recent advances enable practitioners to break open machine learning’s “black box”.*

August 20, 2018

**Andrew Langsner**, Co-founder / Managing Partner, Sphaeric.ai</br>
**Patrick Hall**, Senior Director of Product, H2O.ai

From machine learning algorithms guiding analytical tests in drug manufacture, to predictive models recommending courses of treatment, to sophisticated software that can read images better than doctors, machine learning has promised a new world of healthcare where algorithms can assist, or even outperform, professionals in consistency and accuracy, saving money and avoiding potentially life-threatening mistakes. But what if your doctor told you that you were sick but could not tell you why? Imagine a hospital that hospitalized and discharged patients but was unable to provide specific justification for these decisions. For decades, this was a roadblock for the adoption of machine learning algorithms in healthcare: they could make data-driven decisions that helped practitioners, payers, and patients, but they couldn’t tell users why those decisions were made.

Today, recent advances in machine learning research and implementation may have cracked open the black box of algorithmic decision making. A flurry of research into interpretation, or “the ability to explain or to present in understandable terms to a human,” has resulted in a growing body of credible literature and tools for accurate models with interpretable inner-workings, accountability and fairness of algorithmic decision-making, and post-hoc explanation of complex model predictions,. Can this research really be applied to healthcare, and if so, where would it be most immediately impactful? Three suggestions and an example use case are put forward below.

#### Three Hurdles to Black Box Algorithms

**FDA and drug development**

The FDA has notoriously stringent requirements for the approval of new drugs. This could pose a challenge to drug companies experimenting with machine learning to enforce quality control and even to analyze test results to better detect the presence and proper concentrations of drug compounds. The FDA requires full transparency and replicability for all analytical tests involved in the manufacture of new drugs. In the past this has involved providing lists of formulas and methods for analyzing test results (e.g. chromatography tests). But questions remain about how the FDA would treat a new drug application (NDA) that relied on a complex black box machine learning model to maintain quality in the manufacturing process. Interpretable machine learning techniques could help address some of these questions.

**Medical devices**

This year, for the first time the FDA approved an artificial intelligence device. This marks a major milestone for medical devices using proprietary black box algorithms that can diagnose diseases from images. The device was approved through the FDA’s De Novo premarket review pathway which provides a review process for novel devices that represent a low to moderate risk. The low to moderate risk classification is key to a successful De Novo review. But the FDA has yet to approve a device determined to have a high potential risk to patient outcomes. For example, a diagnostic algorithm where a false positive could lead to an invasive and risky procedure. Extra controls would likely be needed on such an algorithm and with the latest model interpretability techniques, it may be possible to have those additional checks.

Another possibility for bringing machine learning into medical devices came about in late 2016 when congress passed the 21st Century Cures Act. The act excludes what is commonly referred to as clinical decision support (CDS) software from FDA purview under certain conditions; namely, that the healthcare provider using the software can independently review the basis for the software’s recommendation. In December 2017 the FDA published guidance stating that “the sources supporting the recommendation or underlying the rationale for the recommendation should be identified and easily accessible to the intended user, understandable by the intended user (e.g., data points whose meaning is well understood by the intended user) …”  Traditional machine learning software would not meet this criterion due to the black box nature of most machine learning models. However, with recent advances in interpretability, it is possible to display explanations for every decision made by a machine learning model, potentially enabling a user to verify the soundness of the rationale behind the automated recommendation.

**Risk based guidance**

Much attention has been given to hospital readmissions since passage of the Affordable Care Act and the beginning of the Hospital Readmissions Reduction Program. Predictive models developed with machine learning have shown to be successful at predicting avoidable hospital readmissions and some health systems have already adopted machine learning based models successfully. At the same time, interest into the use of machine learning to develop automated fraud and waste detection on incoming medical claims has been growing amongst government entities and private insurance companies. Now it should be possible for these models to explain their decisions to practitioners, payers, and patients, allowing users to investigate the actual reasons behind automated medical decision making and determine if an individual decision was reasonable or could be improved.

### Toward the Application of Interpretable Machine Learning in Healthcare

Since more deliberations about the ethical, medical, and economic implications of interpretable machine learning in healthcare are certainly necessary, an example risk based guidance use case has been provided for the sake of furthering such discussions. The example use case should be similar to the methods that organizations are already using for predicting 30-day readmissions, but instead of using an older linear modeling approach, the example uses a nonlinear, “white box” machine learning approach to achieve about a 1% increase in readmission prediction accuracy. Explanatory techniques are then used to describe both the internal mechanisms of the model and every prediction the model makes.

It is left to practitioners and domain experts to determine whether the example techniques truly surpass more established methods by any number of criteria, e.g. ability to handle heterogeneous data, accuracy, or interpretability. The only explicit argument made here is: when people's lives are being affected by mathematical models, it does seem prudent to investigate and evaluate potentially impactful new modeling and analysis techniques.

The open source and freely available example use case is available here:

https://github.com/jphall663/diabetes_use_case/blob/master/Binary-Classification-Readmit.ipynb

The authors look forward to continuing this discussion online and at the upcoming Xavier Healthcare AI summit.

## Usage

The files in this repository are meant to provide a reproducible example for interpretable machine learning techniques applied to a basic health care use case. The [Jupyter notebook herein](Binary-Classification-Readmit.ipynb) will be presented at the [Xavier AI in Healthcare conference](https://www.xavierhealth.org/ai-summit-day2/).

The training data for this use case is available [here](https://www.kaggle.com/brandao/diabetes). The data set contains demographic and medical information about many patients. It is used to create a white-box classifier for predicting who will be readmitted to a hospital within 30 days of discharge. This notebook attempts to showcase the use of a complex, but transparent, nonlinear classifier as an alternative to more traditional linear model approaches.

Typically it requires many different methods to properly interpret a nonlinear classifier. Several different types of interpretation and explanation methods are used here including:

* Global and local Shapley variable importance
* Partial dependence
* Individual conditional expectation (ICE)
* Surrogate decision trees

### Dockerfile instructions:

A [Dockerfile](anaconda_py35_h2o_xgboost_graphviz_shap/Dockerfile) is provided to build a docker container with all necessary packages and dependencies. This is the easiest way to use the example [notebook](Binary-Classification-Readmit.ipynb) if you are on Mac OS X, \*nix, or Windows 10. To do so:</br>

1. Install and start [docker](https://www.docker.com/).

The from a terminal run:

2. Create a directory for the Dockerfile.</br>
`$ mkdir anaconda_py36_h2o_xgboost_graphviz_shap`

3. Fetch the Dockerfile.</br>
`$ curl https://raw.githubusercontent.com/jphall663/diabetes_use_case/master/anaconda_py36_h2o_xgboost_graphviz_shap/Dockerfile > anaconda_py36_h2o_xgboost_graphviz_shap/Dockerfile`

4. Build a docker image from the Dockefile.</br>
`$ docker build --no-cache anaconda_py36_h2o_xgboost_graphviz_shap`

5. Display docker image IDs. You are probably interested in the most recently created image. You will need it for the command directly below. </br>
`$ docker images`

6. Start the docker image and the Jupyter notebook server.</br>
`$ docker run -i -t -p 8888:8888 <image_id> /bin/bash -c "/opt/conda/bin/conda install jupyter -y --quiet && /opt/conda/bin/jupyter notebook --notebook-dir=/diabetes_use_case --ip='*' --port=8888 --no-browser"`</br>

(If you need `root` priviledges to run docker, try this command:`sudo docker run -i -t -p 8888:8888 <image_id> /bin/bash -c "/opt/conda/bin/conda install jupyter -y --quiet && /opt/conda/bin/jupyter notebook --notebook-dir=/diabetes_use_case --ip='*' --port=8888 --no-browser --allow-root"`</br>

7. Then navigate to port 8888 on your machine, probably `http://localhost:8888/`.

### Manual Installation

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

8. `$ cd diabetes_use_case`

9. Start the Jupyter notebook server.</br>
`$ jupyter notebook`

10. Navigate to the port Jupyter directs you to on your machine, probably `http://localhost:8888/`.
