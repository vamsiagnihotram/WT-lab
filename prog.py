#!C:\Program Files\Python37\python

def calculate(a,b,op):
    if op=='add':
        print(int(a)+int(b))
    elif op=='subtract':
        print(int(a)-int(b))
    elif op=='mul':
        print(int(a)*int(b))
    elif op=='div':
        print(int(a)/int(b))
    elif op=='modulas':
        print(int(a)%int(b))
    
   
import cgi
print("context-type:text/html\n")
print("<html>")
print("<head> <title>my second cgi program</title>")
print("</head>")
print("<body>")

form=cgi.FieldStorage()
a=form.getvalue("first")
b=form.getvalue("second")
op=form.getvalue("operation")

print('<form method ="post" action="prog.py">')
print('<p>enter the first number:<input type ="text" name ="first"></p>')
print('<p>enter the second number:<input type ="text" name ="second"></p>')
print('<p> select op:</p><select name="operation"><option>add</option><option>subtract</option><option>mult</option><option>div</option><option>modulas</option></select>')
print('<input type="submit" value="submit"/>')
print('<br>')
print('<br>')
print("</body>")
print("</html>")

print("\n")

calculate(a,b,op)


    
