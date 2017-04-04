from random import randint
from InstructionDecoder import InstructionDecoder
import time
print "--------------------------- RISC TILE64 IMPLEMENTATION IN PYTHON ------------------------------"
class Core(object):
	def __init__(self,rank):
		self.rank=rank
		self.insdecoderObject=InstructionDecoder()

core={}
for i in range(64):
	core[i]=Core(i)


#x=randint(1,64)
file=open("coreselect.txt",'r')
f=file.read()
selectCore=f.split()
x=int(selectCore[1])
print "Executing in core %d"%(x)
core[x].insdecoderObject.execute()
