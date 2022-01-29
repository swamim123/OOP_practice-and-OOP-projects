import re
str='''Virat54@gmail.com If you’re sending an email to a recruiter, there are some things to know if you want them to respond (and some mistakes to avoid).

So after working for almost 5 years as a recruiter, I’m going to share how to email a recruiter with email samples, examples of what not to do, and more.

What we’ll cover: new123@gmail.com


How to cold email a recruiter Harry@gmail.com

How to email a recruiter for a job posting you saw online
How to email your resume to a recruiter (and why you shouldn’t do this in a first email)
How to respond to a recruiter email after they contacted you
How to end an email to a recruiter for best results'''

email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+",str)
print(email)