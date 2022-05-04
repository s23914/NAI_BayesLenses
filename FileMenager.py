import camelot
class FileManager():
    def __init__(self,PATH):
        self.PATH = PATH
        tables= camelot.read_pdf(self.PATH)
        print(tables[0].df)
        

    
        
        