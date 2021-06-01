# FasTre ML

Flask app to deploy ML prediction on hospital waiting time

URL = http://IPADDRESS:PORT/predict

Features
| Features                | Description                                                             | 
| ----------------------- |:-----------------------------------------------------------------------:| 
| Wait                    | Predicted Feature                                                       |
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
  "data": [
    [
      0,0,9,1,0,0,6,
      17,13,1,0,4,7,
      212,1,62,3,8,13,2,
      3,12,1,0,3,0,0,18
    ]
  ]
}
```
28 values are required. To predict more than once, insert multiple 28 arrays (size of nx28)

Result data =  
```json
{"result": [718.8391723632812]}
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