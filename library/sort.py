import re
from collections import OrderedDict

f=open("daoRebuild.txt")

s=f.read()


stack={}
for line in re.split("\n", s):
	if line in stack:
		stack[line]+=1
	else:
		stack[line]=1


w=open ("daoSorted.txt", "w")
for key in OrderedDict(sorted(stack.items(), key=lambda t: t[1])):
	print (key+" ")
	print (stack[key])
	print ("\n")
	if stack[key] >=2 and stack[key] < 26:
		w.write(key+"\n")
	

