# FasTre ML

Flask app to deploy ML prediction on hospital waiting time

URL = http://IPADDRESS:PORT/predict

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