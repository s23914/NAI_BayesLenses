from FileMenager import FileManager
from CalculatePossibilities import CalculatePossibilities
class main():
    PATH="bayes-lenses.pdf"
    file=FileManager(PATH)
    Format=[]
    Format.append("young")
    Format.append("myope")
    Format.append("no")
    Format.append("reduced")
    Format.append("soft")
    print(Format)
    # Algorithm=CalculatePossibilities(file,Format)



