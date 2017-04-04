from FileStream import FileStream
from ALU import ALU
import timeit
import time
import serial
import syslog
import matplotlib.pyplot as plt
class InstructionDecoder:

    def printRegs(self,a,b):
        print "CPU stores first number as ",a
        print "CPU stores second number as ",b


    def execute(self):
        fileS = FileStream("test.txt","","","","")
        fileOpcode=FileStream("ins.txt","","","","")
        opcodesArray=[]
        fileS.processFile()
        opcodesArray=fileOpcode.readOpcodes()
        i=0
        result=0
        quot=0
        timearray=[]
        acc=0
        binStng=""
        operationName=[]
        #for opcode in fileS.opcodes:
        while i<len(fileS.opcodes):
            currentOpcode=fileS.opcodes[i]

            if currentOpcode==opcodesArray[0]:
                operationName.append(opcodesArray[0])
                if fileS.aarr[i]=="acc":
                    self.printRegs(bin(acc)[2:].zfill(8),fileS.barr[i])
                    aluCtrl=ALU(acc,int(fileS.barr[i],2),0)
                elif fileS.barr[i]=="acc":
                    self.printRegs(fileS.aarr[i],bin(acc)[2:].zfill(8))
                    aluCtrl=ALU(int(fileS.aarr[i],2),acc,0)
                else:
                    self.printRegs(fileS.aarr[i],fileS.barr[i])
                    aluCtrl=ALU(int(fileS.aarr[i],2),int(fileS.barr[i],2),0)
                start = timeit.default_timer()
                result=aluCtrl.add()
                binStng=bin(result)[2:].zfill(8)
                stop = timeit.default_timer()
                timearray.append(stop - start)
                print "The operation is ADD "
                print "The final result in binary is ",binStng
                print "The final result in decimal is ",result
                acc=result
                print "Accumulator value is ",acc
                print "Elapsed time is ",(stop-start)

            elif currentOpcode==opcodesArray[1]:
                operationName.append(opcodesArray[1])
                if fileS.aarr[i]=="acc":
                    self.printRegs(bin(acc)[2:].zfill(8),fileS.barr[i])
                    aluCtrl=ALU(acc,int(fileS.barr[i],2),0)
                elif fileS.barr[i]=="acc":
                    self.printRegs(fileS.aarr[i],bin(acc)[2:].zfill(8))
                    aluCtrl=ALU(int(fileS.aarr[i],2),acc,0)
                else:
                    self.printRegs(fileS.aarr[i],fileS.barr[i])
                    aluCtrl=ALU(int(fileS.aarr[i],2),int(fileS.barr[i],2),0)
                start = timeit.default_timer()
                result=aluCtrl.subtract()
                binStng=bin(result)[2:].zfill(8)

                print "The operation is SUB "
                print "The final result in binary is ",binStng
                print "The final result in decimal is ",result
                acc=result
                print "Accumulator value is ",acc
                stop = timeit.default_timer()
                timearray.append(stop - start)
                print "Elapsed time is ",(stop-start)

            elif currentOpcode==opcodesArray[2]:
                operationName.append(opcodesArray[2])
                if fileS.aarr[i]=="acc":
                    self.printRegs(bin(acc)[2:].zfill(8),fileS.barr[i])
                    aluCtrl=ALU(acc,int(fileS.barr[i],2),0)
                elif fileS.barr[i]=="acc":
                    self.printRegs(fileS.aarr[i],bin(acc)[2:].zfill(8))
                    aluCtrl=ALU(int(fileS.aarr[i],2),acc,0)
                else:
                    self.printRegs(fileS.aarr[i],fileS.barr[i])
                    aluCtrl=ALU(int(fileS.aarr[i],2),int(fileS.barr[i],2),0)
                start = timeit.default_timer()
                result=aluCtrl.multiply()
                binStng=bin(result)[2:].zfill(8)

                print "The operation is MUL "
                print "The final result in binary is ",binStng
                print "The final result in decimal is ",result
                acc=result
                print "Accumulator value is ",acc
                stop = timeit.default_timer()
                timearray.append(stop - start)
                print "Elapsed time is ",(stop-start)

            elif currentOpcode==opcodesArray[3]:
                operationName.append(opcodesArray[3])
                if fileS.aarr[i]=="acc":
                    self.printRegs(bin(acc)[2:].zfill(8),fileS.barr[i])
                    aluCtrl=ALU(acc,int(fileS.barr[i],2),0)
                elif fileS.barr[i]=="acc":
                    self.printRegs(fileS.aarr[i],bin(acc)[2:].zfill(8))
                    aluCtrl=ALU(int(fileS.aarr[i],2),acc,0)
                else:
                    self.printRegs(fileS.aarr[i],fileS.barr[i])
                    aluCtrl=ALU(int(fileS.aarr[i],2),int(fileS.barr[i],2),0)
                start = timeit.default_timer()
                (result,quot)=aluCtrl.div()
                binStng=bin(result)[2:].zfill(8)

                print "The operation is DIV "
                print "The final Quotient in binary is ",binStng
                print "The final Quotient in decimal is ",result
                print "The final Remainder in binary is ",bin(quot)[2:].zfill(8)
                print "The final Remainder in decimal is ",quot
                acc=result
                print "Accumulator value is ",acc
                stop = timeit.default_timer()
                timearray.append(stop - start)
                print "Elapsed time is ",(stop-start)

            elif currentOpcode==opcodesArray[4]:
                operationName.append(opcodesArray[4])
                if fileS.aarr[i]=="acc":
                    self.printRegs(bin(acc)[2:].zfill(8),fileS.barr[i])
                    aluCtrl=ALU(acc,int(fileS.barr[i],2),0)
                elif fileS.barr[i]=="acc":
                    self.printRegs(fileS.aarr[i],bin(acc)[2:].zfill(8))
                    aluCtrl=ALU(int(fileS.aarr[i],2),acc,0)
                else:
                    self.printRegs(fileS.aarr[i],fileS.barr[i])
                    aluCtrl=ALU(int(fileS.aarr[i],2),int(fileS.barr[i],2),0)
                start = timeit.default_timer()
                result=aluCtrl.andop()
                binStng=bin(result)[2:].zfill(8)

                print "The operation is AND "
                print "The final result in binary is ",binStng
                print "The final result in decimal is ",result
                acc=result
                print "Accumulator value is ",acc
                stop = timeit.default_timer()
                timearray.append(stop - start)
                print "Elapsed time is ",(stop-start)

            elif currentOpcode==opcodesArray[5]:
                operationName.append(opcodesArray[5])
                if fileS.aarr[i]=="acc":
                    self.printRegs(bin(acc)[2:].zfill(8),fileS.barr[i])
                    aluCtrl=ALU(acc,int(fileS.barr[i],2),0)
                elif fileS.barr[i]=="acc":
                    self.printRegs(fileS.aarr[i],bin(acc)[2:].zfill(8))
                    aluCtrl=ALU(int(fileS.aarr[i],2),acc,0)
                else:
                    self.printRegs(fileS.aarr[i],fileS.barr[i])
                    aluCtrl=ALU(int(fileS.aarr[i],2),int(fileS.barr[i],2),0)
                start = timeit.default_timer()
                result=aluCtrl.orop()
                binStng=bin(result)[2:].zfill(8)

                print "The operation is OR "
                print "The final result in binary is ",binStng
                print "The final result in decimal is ",result
                acc=result
                print "Accumulator value is ",acc
                stop = timeit.default_timer()
                timearray.append(stop - start)
                print "Elapsed time is ",(stop-start)

            elif currentOpcode==opcodesArray[6]:
                operationName.append(opcodesArray[6])
                if fileS.aarr[i]=="acc":
                    self.printRegs(bin(acc)[2:].zfill(8),fileS.barr[i])
                    aluCtrl=ALU(acc,int(fileS.barr[i],2),0)
                elif fileS.barr[i]=="acc":
                    self.printRegs(fileS.aarr[i],bin(acc)[2:].zfill(8))
                    aluCtrl=ALU(int(fileS.aarr[i],2),acc,0)
                else:
                    self.printRegs(fileS.aarr[i],fileS.barr[i])
                    aluCtrl=ALU(int(fileS.aarr[i],2),int(fileS.barr[i],2),0)
                start = timeit.default_timer()
                result=aluCtrl.xorop()
                binStng=bin(result)[2:].zfill(8)

                print "The operation is XOR "
                print "The final result in binary is ",binStng
                print "The final result in decimal is ",result
                acc=result
                print "Accumulator value is ",acc
                stop = timeit.default_timer()
                timearray.append(stop - start)
                print "Elapsed time is ",(stop-start)

            elif currentOpcode==opcodesArray[9]:
                port = '/dev/ttyACM0'
                ard = serial.Serial(port,9600,timeout=6)
                readvalue=[]
                readvalue.append(ard.read())
                readvalue.append(ard.read())
                readvalue.append(ard.read())
                readval=''.join(readvalue)
                acc=int(readval)
                time.sleep(3)


            #elif currentOpcode==opcodesArray[8]:
            elif currentOpcode==opcodesArray[10]:

                addrin=fileS.aarr[i]
                datain=acc
                port = '/dev/ttyACM0'


                ard = serial.Serial(port,9600,timeout=6)

                iter = 0

                while (iter < 1):
                    # Serial write section

                    setTempCar1 = addrin
                    setTempCar2 = acc
                    ard.flush()
                    setTemp1 = str(setTempCar1)
                    setTemp2 = str(setTempCar2)
                    print ("Python value sent: ")
                    print (setTemp2)
                    ard.write(setTemp2)
                    time.sleep(4)

                    # Serial read section

                    iter = iter + 1
                else:
                    print "Exiting"
                exit()



            elif currentOpcode==opcodesArray[7]:
                operationName.append(opcodesArray[7])
                print "Jumping"
                start = timeit.default_timer()
                jmpIndex=fileS.aarr.index(fileS.barr[i])
                i=jmpIndex
                stop = timeit.default_timer()
                timearray.append(stop - start)
                print "Elapsed time is ",(stop-start)

            elif currentOpcode==opcodesArray[8]:
                continue

            i=i+1
            print "\n"
        return timearray
