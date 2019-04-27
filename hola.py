def readFile(filename):
    with open(filename) as file:
        return file.readlines()

def getIdFromSampleLine(line):
    return line.split("|")[0]

def getIdFromSCLLine(line):
    return line.split(",")[-1]

def filtrarDosArchivos(sampleFile, sclFile):
    sclLines = readFile(sclFile)
    sampleLines = readFile(sampleFile)

    outputLines = []
    for sclLine in sclLines:
        for sampleLine in sampleLines:
            sclID = getIdFromSCLLine(sclLine)
            sampleID = getIdFromSampleLine(sampleLine)
            if sclID == sampleID:
                newline = f"{sclID},{sclLine.split(',')[3]},{sampleLine.split('|')[3]}"
                outputLines.append(newline)
    return outputLines


    