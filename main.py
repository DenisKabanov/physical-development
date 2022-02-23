import eel
import cgi
from apps import determine_the_passport_age


eel.init("web")

eel.start("web_main.html", size=(1000, 1000))
#
# print(determine_the_passport_age('01/02/2022', '23/02/2022'))


form = cgi.FieldStorage()
dob = form.getvalue('dob')
print(dob)
