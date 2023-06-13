# Machine-Learning-Smoker-BMI-Prediciton

## Table of Contents

- [About](#about)
- [Summary](#summary)
- [Visualizations](#visualizations)

## About
**bmi model**
- Our team's goal was to have machine learning determine a person's bmi when entering their age. 

**smoker model**
- Our team's goal was to use machine learning to determine if a person is a smoker or non smoker based on the data points age, bmi, sex, and hospital charges. 

[Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)

Our dataset contained the following column headers:
- **age**: age of primary beneficiary
- **sex**: insurance contractor gender, female, male
- **bmi**: body mass index, providing an understanding of body, weights that are relatively high or low relative to height, objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9
- **children**: number of children covered by health insurance / Number of dependents
- **smoker**: smoker/non-smoker
- **region**: the beneficiary's residential area in the US, northeast, southeast, southwest, northwest.
- **charges**: individual medical costs billed by health insurance

## Summary
- We started by cleaning our dataset with Python, Pandas, and Numpy.
- Removed unwanted columns, converted data types, and converted text to float values.
- Separated the data into labels and features then reviewed our X and y variables. 
- Split our data into training and testing sets. 
- Incorporated scaling so our machine learning model would generalize the distance between our data points as being lower.
- Made predictions on our test data and evaluated the model (accuracy score .956)
- Allowed users to make necessary inputs (age, sex, charges, and bmi).
- bmi model: Ran our model to make a prediction of the user's bmi based on age.
- smoker model: Ran our model to make a prediction if the user is a smoker or non smoker based on the inputs above.

## Visualizations
![Screenshot 2023-06-07 at 7 11 43 PM](https://github.com/kburke119/Machine-Learning-Smoker-Prediction/assets/10196762/a4ecb805-4460-4eda-8cdc-e3e63e9bb32b)
![Visual 2](https://github.com/kburke119/Machine-Learning-Smoker-Prediction/assets/10196762/0a4840e8-2c4f-4b5e-8b65-b6d23ea9376c)

