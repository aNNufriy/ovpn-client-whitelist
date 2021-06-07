#!/usr/bin/env python3.6
import logging
import sys
import os
import getpass

if(len(sys.argv)<3):
    sys.exit(-1);

logfile = sys.argv[2]

str_level = 'INFO'
level = getattr(logging, str_level)

logging.basicConfig(filename=logfile,format='%(asctime)s - %(levelname)s - %(message)s',level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(level)

common_name = os.getenv('common_name', 'NOT_AVAILABLE')
ip = os.getenv('untrusted_ip', 'NOT_AVAILABLE')

with open(sys.argv[1]) as cnf:
    contents = cnf.readlines()
    for line in contents:
        if(line.rstrip() == common_name):
            logging.info("%s connected from %s" % (common_name,ip))
            sys.exit(0)
    logging.warn("%s not in whitelist (connected from %s)" % (common_name,ip))
    sys.exit(1)

