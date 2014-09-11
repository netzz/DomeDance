 # -*- coding: cp1251

import re


f=open ("dao.txt")

s=f.read()

w=open("daoRebuild.txt", "w");


s=re.sub(r'\n\n\d+\n\n\n\n', r' ', s)
s=re.sub(r'[\[\]]', r' ', s)
s=re.sub(r'[\*-]', r' ', s)
s=re.sub(r'[\(\)\.\,\?\:\;\"\!]', r' ', s)

# s=re.sub(r'[ився]\s+', r' ', s)


s=re.sub(r'\s+', r' ', s)
s=re.sub(r'\s', r'\n', s)
s=re.sub(r'р', r'p', s)

w.write(s.lower())