#!/usr/bin/env python3.6
import logging
import sys
import os

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

logging.info("%s disconnected from %s" % (common_name,ip))
sys.exit(0)
