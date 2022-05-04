import camelot
import csv
class FileManager():
    def __init__(self,PATH):
        self.PATH = PATH
        tables= camelot.read_pdf(self.PATH)
        print(tables[0],)
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
        print(self.FinalList[0][0])

            

            
            


    


            

