#!C:\Program Files\Python37\python

import calendar

def calendar1(yy,mm):
    print(calendar.month(int(yy), int(mm)))
    

import cgi
print("context-type:text/html\n")
print("<html>")
print("<head> <title>my second cgi program</title>")
print("</head>")
print("<body>")

form=cgi.FieldStorage()
yy=form.getvalue("first")
mm=form.getvalue("second")


print('<form method ="post" action="calender.py">')
print('<p>enter the year<input type ="text" name ="first"></p>')
print('<p>enter the month<input type ="text" name ="second"></p>')

print('<input type="submit" value="submit"/>')
print('<br>')
print('<br>')
print("</body>")
print("</html>")

print("\n")

calendar1(yy,mm)
