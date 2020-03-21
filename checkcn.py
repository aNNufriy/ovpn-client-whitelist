#!/usr/bin/env python2.7
import logging
import sys
import os
import getpass

if(len(sys.argv)<3):
    sys.exit(-1);

common_name = os.getenv('common_name', 'NOT_AVAILABLE')
ip = os.getenv('untrusted_ip', 'NOT_AVAILABLE')

str_level = 'INFO'
level = getattr(logging, str_level)

logfile = sys.argv[2] 
logging.basicConfig(filename=logfile,format='%(asctime)s - %(levelname)s - %(message)s',level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(level)

with open(sys.argv[1]) as wlf:
    whitelist = wlf.readlines()

    username = getpass.getuser()
    for line in whitelist:
        if(line.rstrip() == common_name):
            logging.info("%s connected from %s" % (common_name,ip))
            sys.exit(0)
    logging.warn("%s not in whitelist (connected from %s)" % (common_name,ip))
    sys.exit(1)
