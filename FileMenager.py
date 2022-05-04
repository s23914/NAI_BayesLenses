import camelot
import csv
class FileManager():
    def __init__(self,PATH):
        self.PATH = PATH
        tables= camelot.read_pdf(self.PATH)
        tables[0].to_csv("Tables.csv")
        self.FilePath="Tables.csv"
        self.list = []
        File=open(self.FilePath)
        spamreader=csv.reader(File, delimiter=',', quotechar='"')
        self.FinalList=[]
        boolean=False
        for row in spamreader:
                list=[]
                for value in row:
                    list.append(value)
                self.FinalList.append(list)
        self.GetAttributes()
    

    def GetAttributes(self):
        listofAttributes= []
        for i in range(len(self.FinalList[0])):
            list=[]
            print(i)
            for j in range(1,len(self.FinalList)-1):
                    list.append(self.FinalList[j][i])
            j=0
            uniqelist =set(list)
            listofAttributes.append(uniqelist)
        print(listofAttributes)
                







            

            
            


    


            

