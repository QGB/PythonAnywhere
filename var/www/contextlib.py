from __future__ import absolute_import

import sys
#,os,traceback
f=open('/home/qmm/contextlib.txt','w')
#print( traceback.format_exc() ,file=f)
print( '\n',sys.path,'\n\n',len(sys.modules),list(sys.modules),'\n',sys.modules ,file=f)
import pprint
print(pprint.pformat([[n,k,v] for n,(k,v) in enumerate(sys.modules.items())],width=222),file=f)
#f.close()
sys.path=['/usr/lib/python38.zip','/usr/lib/python3.8','/usr/lib/python3.8/lib-dynload','/home/qmm/.local/lib/python3.8/site-packages','/usr/lib/python3.8/site-packages','/var/www','/home/qmm/']
print(sys.modules.pop('contextlib') ,file=f)
#sys.path.append('/home/qmm/')
from qgb import py
print(py,file=f)


#f.close()
#from contextlib import *

try:
 from qgb import U
 import contextlib
 print( contextlib ,file=f)
except Exception as e:
 import traceback
 print(e,type(e),23333,traceback.format_exc() ,file=f)
f.close()
from contextlib import *



