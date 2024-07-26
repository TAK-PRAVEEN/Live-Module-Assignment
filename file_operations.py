def read_file(file_name):
    file = open(file_name, "r")
    print(file.read())
    file.close()
    
def write_file(file_name,text):
    file = open(file_name, "w")
    file.write(text)
    file.close()
    
def append_file(file_name,text):
    file = open(file_name, "a")
    file.write(text)
    file.close()
    
def create_file(file_name):
    with open(file_name,"x") as file:
        pass
    
def readlines(file_name):
    with open(file_name,"r") as file:
        print(file.readlines())