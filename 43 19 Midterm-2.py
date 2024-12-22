import numpy as np
User_ID = []
Age = []
Gender = []
Total_App_Usage_Hours = []
Daily_Screen_Time_Hours = []
Number_of_Apps_Used = []
Social_Media_Usage_Hours = []
Productivity_App_Usage_Hours = []
Gaming_App_Usage_Hours = []
Location = []

data = open('E:\Study\Python\Edge Course\mobile_usage_behavioral_analysis.csv','r')
head = data.readline()
body = data.readline()
while (len(body)>0):
    arr = body.strip().split(',')
    User_ID.append(int(arr[0]))
    Age.append(int(arr[1]))
    Gender.append(arr[2])
    Total_App_Usage_Hours.append(float(arr[3]))
    Daily_Screen_Time_Hours.append(float(arr[4]))
    Number_of_Apps_Used.append(float(arr[5]))
    Social_Media_Usage_Hours.append(float(arr[6]))
    Productivity_App_Usage_Hours.append(float(arr[7]))
    Gaming_App_Usage_Hours.append(float(arr[8]))
    Location.append(arr[9])
    body = data.readline()
data.close()