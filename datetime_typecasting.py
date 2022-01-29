from datetime import datetime
#string to date
datestr="2021-10-20"
dateType= datetime.strptime(datestr,"%Y-%m-%d")
print(dateType)

#date to string
date=datetime.now()
datestr=datetime.strftime(date ,'%A,%B,%d,%Y')
print(datestr)
