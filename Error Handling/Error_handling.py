import requests
import logging

root_logger = logging.getLogger()
root_logger.setLevel(logging.WARNING)
handler = logging.FileHandler('example.log', 'w', 'utf-8')
root_logger.addHandler(handler)


try:
    r = requests.get('https://abcdefighjt.com/nothinghere')
except requests.exceptions.RequestException as err:
    print('Requests Exception Found.')
    logging.warning(err)
    
print('program carries on down here')

