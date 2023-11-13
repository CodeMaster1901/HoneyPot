"""
Usage:
    HoneyPot --config FILE
Options:
    --config FILE   path to configuration options .ini file
    -h --help           show this screen 
"""

# from docopt import docopt
# args = docopt(__doc__) # this __doc__ will be the quoted text at the top
# logger.info("config file is: %s", args['[config_filepath]'])

import configparser
from HoneyPot import HP
import sys
# import logging - helps logging it in 

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

#TODO replace with docopt args[]
# config_filepath = '/etc/honeypot.ini'
config_filepath = 'honeypot.ini' #relative path

config = configparser.ConfigParser()
config.read(config_filepath)

ports = config.get('default' , 'ports' , raw=True , fallback="22,80,443,8080,8888,9999,3306")
log_filepath = config.get('default' , 'logfile' , raw=True , fallback="/var/log/honeypot.log")

#to check wether the ini file contents are being loaded in correctly
# logger.info("[*]ports: ",ports)
# logger.info("[*]Logfile: ",log_filepath)

ports_list = []
try:
    ports_list = ports.split(',')
except Exception as e:
    print("[[x]] Error parsing the ini file for ports: \n Exiting the process",ports) 
    sys.exit(1)

hp = HP(ports_list,log_filepath)
hp.run()