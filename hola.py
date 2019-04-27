def readFile(filename):
    f = open(filename, "r")
    return f.readlines()

def getIdFromLine(line):
    return line.split("|")[0]