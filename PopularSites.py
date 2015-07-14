__author__ = 'achmat'

import collections


#specify path to apache log (can be any log with some tweaking)
logfile = open("/path/to/folder/httpd-access.log","r")

clean_log=[]

for line in logfile:
    try:
        clean_log.append(line.[line.index("GET")+4:line.index("HTTP")])
    except:
        pass

counter=collections.Counter(clean_log)

for count in counter.most_common(50):
    print (str(count[1]) + "\t" + str(count[0]))

logfile.close()