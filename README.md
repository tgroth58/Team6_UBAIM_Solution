## Cancer Patient Survival Predicition 

Team Members: Ted , Lama , and Vaishnavi.

Link to AIM Datathon: https://www.kaggle.com/c/aimdatathon2020/leaderboard <br>
Link to Google Collab Notebook: https://colab.research.google.com/drive/1GFtlNPVoSZ1RHcb2DvUzaLY8mEgdqeAV?usp=sharing
### Contents

* [Problem](#Problem)
* [ML Pipeline](#ML-Pipeline)
* [Data Management](#Data-Management)
* [Study Design](#Study-Design)
* [Validation Strategies (Train and Test Data Pre-processing, Training/Validation Split)](#Validation-Strategies)
* [Model Training,Tuning (Random Forest, ANN, AUC performance metric)](#Model-Training_and_Tuning)
* [Results,Model Performance,Interpretability](#Results_Model-Performance_and_Interpretability)
* [Solution Video](#Solution-Video)
  * Link a short video (unlisted Youtube link) that walks through your approach from github and code from google collab.
* [Acknowledgments](#acknowledgments)
#### Problem
- Physcians are overwhlemed with patient cancer data, and would benefit from a system that outlines indiviaulized patients risk factors such as gender, date of birth, enthicity, medical family history, smoking habits, medications, dietary routines, physical activtiy, cancer stage, and grading to augment their clinical decision making. 
#### ML-Pipeline
Workflow:
![image](https://user-images.githubusercontent.com/20275395/110195557-00058080-7e0c-11eb-88fe-b7c90dcf6b78.png)
- Link to code(https://colab.research.google.com/drive/1aLeYEjiFDu4nlSXN7JPgqdYrjO3Uml3v?usp=sharing).
#### Data-Management/Feature engineering
-Columns in the data frame with the fraction of null entries more than 80% were dropped.
-Discrete data we removed nas and features with high homogeneity.
-Continuous data was scaled using standard normalization and log transformation.
-Cateogrical features where converted to numeric using onehotencoding. The onehotencoded features with class imbalance (0,1) less than 0.15 where dropped.
-After, the different datatype columns were preproccessed they were merged together to obtain the training data.
-Feature selection was perfromed using feature modeling (logisitc regression with L1 penalty) to get the weights. The top and bottom ten features based on the cofficients from logistic regression were used.
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
* After the train and test Data was pre-processed. The training data was split into train and validation set. The test data was kept aside for evaluation of the models.
#### Model-Training_and_Tuning
* For the RandomForest model GridSearchCV was used to optimize the hyperparameters. For the ANN model, RandomizedCV was used where not all parameter values are tried out, but rather a fixed number of parameter settings was sampled from the specified distributions.
#### Results_Model-Performance_and_Interpretability
* For the Random Forest, the conufision matrix,  f1-score and recall were obtained.
AUC score for the RandomForest was 0.76
* For the ANN the accuracy and loss per epoch where plotted to see how the model is performance as it trains.
The conufision matrix,  f1-score and recall were also obtained.
AUC score for the ANN model was 0.77
#### Solution-Video

#### Acknowledgement
We would like to thank the UBAIM club eboard for organizing this Datathon and providing us the dataset to hack over the weekend (<48hrs)

