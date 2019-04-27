def readFile(filename):
    with open(filename) as file:
        return file.readlines()

def getValuesFromSampleLine(line):
    split = line.split("|")
    return split[0],split[3]

def getValuesFromSCLLine(line):
    split = line.split(",")
    return split[4],split[0],split[3]

def getIdFromSampleLine(line):
    # split = line.split("|")
    return getValuesFromSampleLine(line)[0]

def getIdFromSCLLine(line):
    # split = line.split(",")
    return getValuesFromSCLLine(line)[0]

def filtrarDosArchivos(sampleFile, sclFile):
    sclLines = readFile(sclFile)
    sampleLines = readFile(sampleFile)

    outputLines = []
    for sclLine in sclLines:
        for sampleLine in sampleLines:
            sclVal = getValuesFromSCLLine(sclLine)
            sampleVal = getValuesFromSampleLine(sampleLine)
            if sclVal[0] == sampleVal[0]:
                newline = f"{sclVal[0]},{sclVal[1]},{sclVal[2]},{sampleVal[1]}"
                outputLines.append(newline)
    return outputLines

def processFiles(sampleFile, sclFile, outputFile):
    outputlines = filtrarDosArchivos(sampleFile, sclFile)
    with open(outputFile, "w") as file:
        file.writelines(outputlines)
