## **12. Capstone Project**

<br>

### **Project** : **_Rossmann Store Sales_**  (Forecast sales using store, promotion, and competitor data)
<br>

<span>
  <img src="https://www.kaggle.com/static/images/site-logo.png" width="90" title="Kaggle">  
</span>

[Rossmann Store Sales](https://www.kaggle.com/c/rossmann-store-sales)

<br>

### **Description**

Rossmann operates over 3,000 drug stores in 7 European countries. Currently, Rossmann store managers are tasked with predicting their daily sales for up to six weeks in advance. Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality. With thousands of individual managers predicting sales based on their unique circumstances, the accuracy of results can be quite varied. 

![alt text](img/rossmann.jpeg)

<br>

### **Goal**  

Forecast the "Sales" column

<br>

###  **Plan**  

- Dataset overview
- EDA
- Data cleaning & Pre-processing
- Outlier treatment
- Feature selection
- Modeling
- Hyperparameter tuning
- Model validation
- Deployment using Flask or FastAPI
- Containerization via Docker
- Cloud  deployment (GCP, AWS or Azure)

<br>


### **Clone repo**

- Clone this repo

`git clone https://github.com/oussou-dev/ML_Engineer_ZoomCamp.git`  


- Change into the `07_midterm-project` directory  

`cd ML_Engineer_ZoomCamp/07_midterm-project`   


<br>

### **Dependency and enviroment management**  

`pip install -r requirements.txt`  

<br>


### **Run Notebooks (preference) or scripts**  

- Notebooks  

`1_EDA_Cleaning_Baseline.ipynb`  

`2_Model_Loss_Prediction`    


- Scripts

`python3 scripts/train_data.py`


### **Containerization**

- Install Docker  
https://docs.docker.com/get-docker/  


- Build the Docker image by running  
`docker build -t flask-heroku:latest .`  


- And then run it using    
`docker run -d -p 5000:5000 flask-heroku`  

<br>

### **Cloud deployment**


- Install Heroku CLI  
https://devcenter.heroku.com/articles/heroku-cli#download-and-install  


- Deploying the container to Heroku 

`heroku container:login`  

`heroku create` or `heroku create yourawesomeapp`  

`heroku container:release web --app yourawesomeapp`  


Now it is time to check out our awesome app running on Heroku  
https://yourawesomeapp.herokuapp.com
