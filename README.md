## Cancer Patient Survival Predicition 

Team Members: Ted , Lama , and Vaishnavi.

Link to AIM Datathon: https://www.kaggle.com/c/aimdatathon2020/leaderboard <br>
Link to Google Collab Notebook: https://colab.research.google.com/drive/1GFtlNPVoSZ1RHcb2DvUzaLY8mEgdqeAV?usp=sharing
### Contents

* [Problem](#Problem)
* [ML Pipeline](#ML-Pipeline)
* [Data Management](#Data-Management)
* [Study Design](#Study-Design)
* Exploratory Analysis (add if applicable)
* [Validation Strategies (Train and Test Data Pre-processing, Training/Validation Split)](#Validation-Strategies)
* Feature Engineering (add if applicable)
* [Model Training,Tuning (Logistic Regression, XGBoost, AUC performance metric)](#Model-Training_and_Tuning)
* [Results,Model Performance,Interpretability](#Results_Model-Performance_and_Interpretability)
* [Solution Video](#Solution-Video)
  * Link a short video (unlisted Youtube link) that walks through your approach from github and code from google collab.
* [Acknowledgments](#acknowledgments)

#### Problem
- Physcians are overwhlemed with patient cancer data, and would benefit from a system that outlines indiviaulized patients risk factors such as gender, date of birth, enthicity, medical family history, smoking habits, medications, dietary routines, physical activtiy, cancer stage, and grading to augment their clinical decision making. 

#### ML-Pipeline

- Add a link to your code(Google Colab). Refer to this [sample notebook](https://colab.research.google.com/drive/1GFtlNPVoSZ1RHcb2DvUzaLY8mEgdqeAV?usp=sharing) for further details.
#### Data-Management
Refer to Data Pre-Processing subtitle in the [Google Collab notebook](https://colab.research.google.com/drive/1GFtlNPVoSZ1RHcb2DvUzaLY8mEgdqeAV?usp=sharing) for more detail. 
- Data Pre-processing/ Cleansing/Transformations(Changing column names, Merging different data sources, etc). 
- Methods for removing and selection of outliers
- Methods for poor quality or missing data
- Descriptive statistics(Pairwise correlation, ANOVA, Univariate Analysis, Odds Ratio).
#### Study-Design
( Below are answer templates that can be used to formulate a paragraph for Study Design based on the goal and exploratory data analysis)
Refer to Race,FamilY History, Male and Female Primary Site, Histology, Grade and Stage Distribution subtitles in the [Google Collab notebook](https://colab.research.google.com/drive/1GFtlNPVoSZ1RHcb2DvUzaLY8mEgdqeAV?usp=sharing) for more detail. 
-   Identify clinical goal (Prediction of cancer patient survival.)
-   Define prediction outcome (Predict cancer patient survival for quality review and better clinical decision making.)
-   Participant inclusion/exclusion criteria 
(2000 patients with various cancer types were included. A diverse patient population race was involved including whites (1860 [93%]),  African Americans (88 [4.5%]), American Indians (12 [0.6%]), Asians (7 [0.35%]),  Alaskan Natives (12 [1%]), Native Hawaiians (2 [0.15%]), and from other races (7 [0.45%]). The median age (interquartile range) was 62 (54-70) years old.  
36% of the patients had a paternal history with cancer and the greatest proportion was 10% prostate cancer. 39% of the patients had a maternal history with cancer and the greatest proportion was 11% breast cancer. 
Out of 785 males,the majority of the tumors were from the prostate gland as the primary site (371[47.2%]),adenocarcinoma(496 [63%]), grade III: Poorly differentiated , dedifferentiated (369 [47%]), and stage 1 (478[60%]) . 
Out of 1215 females, the majority of the tumors were from the breast upper outer quadrant primary site(300 [24.69%]), infiltrating duct carcinoma(535 [44%]), grade II: moderately differentiated, intermediate differentiated (522 [43%]), and stage 1 (737 [60%]).

#### Validation-Strategies 
Refer to Train and Test Data Pre-processing, Training/Validation Split subtitles in the [Google Collab notebook](https://colab.research.google.com/drive/1GFtlNPVoSZ1RHcb2DvUzaLY8mEgdqeAV?usp=sharing) for more detail. 

-Train and Test Data Pre-processing
-Training/Validation Split

#### Model-Training_and_Tuning
Refer to Logistic Regression and XGBoost subtitles in the [Google Collab notebook](https://colab.research.google.com/drive/1GFtlNPVoSZ1RHcb2DvUzaLY8mEgdqeAV?usp=sharing) for more detail. 

#### Results_Model-Performance_and_Interpretability
Refer to Results,.... subtitles in the [Google Collab notebook](https://colab.research.google.com/drive/1GFtlNPVoSZ1RHcb2DvUzaLY8mEgdqeAV?usp=sharing) for more detail. 

-Include Summary of Results/Discussion and Picture of Results here.


-Logistic Regression

![Image](https://github.com/aimsymposium/Project-sample/blob/main/LogisiticRegression.PNG)


-XGBoost

![Image](https://github.com/aimsymposium/Project-sample/blob/main/XGBoost.PNG)

#### Solution-Video

[![Watch the video](https://github.com/Code-and-Response/Liquid-Prep/blob/master/images/IBM-interview-video-image.png)](https://youtu.be/vOgCOoy_Bx0)


#### Acknowledgments


