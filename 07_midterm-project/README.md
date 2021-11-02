## **7. Midterm Project**

<br>

### **Project** : **_Allstate Claims Severity_**  (How severe is an insurance claim?)
<br>

<span>
  <img src="https://www.kaggle.com/static/images/site-logo.png" width="90" title="Kaggle">  
</span>

[AllState](https://www.kaggle.com/c/allstate-claims-severity)

<br>

### **Description**

When you’ve been devastated by a serious car accident, your focus is on the things that matter the most: family, friends, and other loved ones.   
Pushing paper with your insurance agent is the last place you want your time or mental energy spent.   
This is why [Allstate](https://www.allstate.com/), a personal insurer in the United States, is continually seeking fresh ideas to improve their claims service for the over 16 million households they protect.  

![alt text](https://storage.googleapis.com/kaggle-competitions/kaggle/5325/media/allstate_banner-660x120.png)

<br>

### **Goal**  

Predict how severe insurance claims will be for AllState  
Using ensemble machine learning algorithms  

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
- Cloud  deployment

<br>

### **Data**  

- Look `data` folder  

<br>

### **Dependency and enviroment management**  

`pip install -r requirements.txt`  

<br>

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
