__author__ = 'bob.zhu'
import json
data=u'''{  "UDID": "7211b9754480c6ad07744002a1f832f78d57933e",          "batteryCurrent": 100,          "cpu": 50,          "memory": 20,          "networkTraffic": 20,          "createTime": "2015-08-13 14:07:00"            } '''
j= json.loads(data)
print j
exit()
