# FasTre ML

Flask app to deploy ML prediction on hospital waiting time

URL = http://IPADDRESS:PORT/predict

# Setup
* Clone repository
* Install requirements using `pip3 install -r requirements.txt`
* Set environment variable `FLASK_APP=main` to run using flask
* Run program using `flask run`

# Deployment in Google Cloud
This project is used to perform the data analysis model. To deploy the machine learning model, we first containerize our Flask application which imported the model. Then Cloud Run is deployed using the container (Stored in Container Registry) created a scalable deployment. Through GCP, we also use Firestore Database to store pieces of information about news and hospitals. Cloud Storage buckets are also created and used for additional objects such as images and the container itself.
* Clone source code in Cloud Shell
* Use `gcloud gcloud builds submit --tag gcr.io/PROJECT_ID/IMAGE_NAME` to submit container image to Container Registry
* Deploy image in Cloud Run

# Features Used for input
Features
| Features                | Description                                                             | 
| ----------------------- | ----------------------------------------------------------------------- | 
| Wait                    | Predicted Feature of wait time in minutes                               |
| DelayCount              | Number of delayed exams up to current time of day.                      |
| DelayCountLastHour      | Number of delayed exams in last hour.                                   |
| AheadCount              | Number of patients scheduled before current patient for the day.        |
| AbdominalCount          | Number of patients waiting for abdominal exam.                          |
| VascularCount           | Number of patients waiting for vascular exam.                           |
| MSKCount                | Number of patients waiting for musculoskeletal exam.                    |
| BeforeSlot              | Time since last appointment slot.                                       |
| AfterSlot               | Time until next appointment slot.                                       |
| IsLast                  | Last scheduled patient for the day.                                     |
| IsFirst                 | First scheduled patient for the day.                                    |
| DayOfWeek               | The day of the week the exam is scheduled.                              |
| Month                   | The month of the year the exam is scheduled.                            |
| DayOfYear               | The day of the year the exam is scheduled.                              |
| InProgressSize          | Number of exams in progress for facility.                               |
| NumCompletedToday       | Number of exams completed up to current of day.                         |
| NumCompletedInLastW1    | Number of exams completed in last 30, 60 and 120 minutes.               |
| NumCompletedInLastW2    | Number of exams completed in last 30, 60 and 120 minutes.               |
| NumCompletedInLastW3    | Number of exams completed in last 30, 60 and 120 minutes.               |   
| NumCustomersInLastW1    | Number of customers who have arrived in the last 30 minutes.            |
| NumCustomersInLastW2    | Number of customers who have arrived in the last 60 minutes.            |
| NumCustomersInLastW3    | Number of customers who have arrived in the last 120 minutes.           |
| OutpatientWaitingCount  | Number of outpatients waiting in line.                                  |
| MalesWaitingCount       | Number of male patients waiting in line.                                |
| NumAddOnsToday          | Number of people who have been added to the schedule for today.         |
| NumAddOnsLastW2         | Number of people who have been added to the schedule in last 60 minutes.|
| NumScheduledNextSlot    | Number of patients scheduled in next slot.                              |
| x_ScheduledHour         | Scheduled hour of patient's exam.                                       |
| x_ScheduledMinute       | Scheduled time of patient's exam.                                       |

Source data = https://www.kaggle.com/weirdolucifer/medical-facility-operational-data


Input body =  
```json
{
    "data":[
        [0,0,0,1,0,0,0,0,0,1,1,4,1,0,0,0,0,0,0,0,0,5,0,0,0,0,9,0]
    ]
}
```
28 values are required. To predict more than once, insert multiple 28 arrays (size of nx28)

Result data =  
```json
{"result": [5.218322277069092]}
```

Example of multiple predictions =
```json
{
  "result": [
    [
      718.8390502929688
    ],
    [
      420.23114013671875
    ],
    [
      275.3634033203125
    ]
  ]
}
```
