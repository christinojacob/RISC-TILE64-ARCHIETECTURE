class FileStream:
    def __init__(self,fileName,filePath,opcodes,aarr,barr):
        self.fileName=fileName
        self.filePath=filePath
        self.opcodes=opcodes
        self.aarr = aarr
        self.barr = barr

    def processFile(self):
        file=open(self.fileName,"r")
        f= file.read()
        lala=f.split()
        l=len(lala)
        self.opcodes=[lala[i] for i in range(l) if (i%3==0)]
        self.aarr=[lala[i+1] for i in range(l) if (i%3==0)]
        self.barr=[lala[i+2] for i in range(l) if (i%3==0)]
        self.number=len(self.opcodes)

    def readOpcodes(self):
        file=open(self.fileName,"r")
        f1=file.read()
        f1split=f1.split()
        l1=len(f1split)
        getopcode=[f1split[i+1] for i in range(l1) if (i%2==0)]
        return getopcode

