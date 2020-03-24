import os

def changeText():
    string2edit = input("What string do you want to edit? ")
    string2output = input("What do you want to replace it with? ")
    for fileName in os.listdir("."):
        os.rename(fileName, fileName.replace(string2edit, string2output))

            
if __name__ == "__main__":
    changeText()
