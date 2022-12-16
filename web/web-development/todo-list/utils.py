from datetime import datetime

def parse_form(formdata):
  form_values = {e.split('=')[0]: e.split('=')[1].replace('+',' ') for e in formdata.split('&')}
  return form_values
