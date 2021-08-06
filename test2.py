def makeChart(filename="inputs/1.txt"):
        inputfile=open(filename,'r')
        for line in inputfile:
            if line[0] != '>':
                continue
            line=line[1:]
            line=line.strip('\n')
            line=line.replace('(','')
            line=line.replace(')','')
            list0=line.split('|')
            print(list0[7:])

makeChart()