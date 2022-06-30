

def readLines(name):
    file1 = open(name, 'r')
    return file1.readlines()
  
def writeFile(name, function):
    f = open(name + ".js", "w")
    f.write(function)
    f.close()   
    