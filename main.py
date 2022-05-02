import eel
import cgi
import json
import re


def save_common_info(last_name, first_name, dad_name, dob, doi):
    return last_name, first_name, dad_name, dob, doi


@eel.expose
def convert_value_py(last_name, first_name, dad_name, dob, doi):
    return save_common_info(last_name, first_name, dad_name, dob, doi)


if __name__ == '__main__':
    eel.init("web")
    eel.start("web_main.html", size=(900, 800))



