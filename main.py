import problem
import sys

def printSolution(chart=problem.Chart(),result={}):

    print("The genotypes of the individuals are as follows:")
    for key in result:
        nodeHere= chart.nodes[key]
        nameOfNode=nodeHere.getName()
        st=nameOfNode+" : "+ result[key][0]+result[key][1]
        print(st)#[0],result[key[1]])

def printSolution1(chart=problem.Chart(),result={}):

    print("The genotypes of the individuals are as follows:")
    for key in result:
        nodeHere= chart.nodes[key]
        nameOfNode=nodeHere.getName()
        st=nameOfNode+" : "+ result[key][0]+result[key][1]
        st2=''
        for i in range(len(st)):
            if st[i]=='A':
                st2=st2+'a'
            elif st[i]=='a':
                st2=st2+'A'
            else:
                st2=st2+st[i]
        print(st2)#[0],result[key[1]])

def printSolutionX(chart=problem.Chart(),result={}):

    print("The genotypes of the individuals are as follows:")
    for key in result:
        nodeHere= chart.nodes[key]
        nameOfNode=nodeHere.getName()
        nodeSex=nodeHere.gender
        if(nodeSex==1 or nodeSex==0):
            st=nameOfNode+" : "+ result[key]
            print(st)#[0],result[key[1]])
        if(nodeSex==2):
            st=nameOfNode+" : "+ result[key][0]+result[key][1]
            print(st)#[0],result[key[1]])

def printSolutionX1(chart=problem.Chart(),result={}):

    print("The genotypes of the individuals are as follows:")
    for key in result:
        nodeHere= chart.nodes[key]
        nameOfNode=nodeHere.getName()
        nodeSex=nodeHere.gender
        if(nodeSex==1 or nodeSex==0):
            st=nameOfNode+" : "+ result[key]
            #print(st)#[0],result[key[1]])
        if(nodeSex==2):
            st=nameOfNode+" : "+ result[key][0]+result[key][1]
        st2=''
        for i in range(len(st)):
            if st[i]=='A':
                st2=st2+'a'
            elif st[i]=='a':
                st2=st2+'A'
            else:
                st2=st2+st[i]
        print(st2)

def printSolutionY(chart=problem.Chart(),result={}):

    print("The genotypes of the individuals are as follows:")
    for key in result:
        nodeHere= chart.nodes[key]
        nameOfNode=nodeHere.getName()
        nodeSex=nodeHere.gender
        if(nodeSex==1):
            st=nameOfNode+" : "+ result[key]
            print(st)#[0],result[key[1]])


###||||||||||||||| MAIN PART BEGINS HERE |||||||||||||||###

#taking input file as argument

l=len(sys.argv)
listArg=sys.argv

if l==1:
    inputFile="1.txt"
#inputFile="2.txt"
else:
    inputFile=listArg[1]

#setting the output file
sys.stdout = open('outputs/{}'.format(inputFile),'wt')

#First we make chart data structure from text files
newchart=problem.Chart()
newchart.makeChart(filename="inputs/{}".format(inputFile))

print("||||||||||||||||||||||||||||||||||||")
print("CHART HAS BEEN MADE")
print("||||||||||||||||||||||||||||||||||||")
#print(newchart.nodes)

#Then we make a CSP from it
newproblem=problem.Problem(newchart)

### AUTOSOMAL DOMINANT ###

# We initialize the domains 
status, domains=newproblem.initializeDomainsAuto0()
if(status):
    searchstatus,searchresult, domain=problem.backtrackingSearchAuto(newproblem,domains)
    if searchstatus:
        print
        print("Pattern of Inheritance: Autosomal dominant fits")
        print
        printSolution(newchart,searchresult)
    
    else:
        print("Pattern of Inheritance: Autosomal dominant does't fit")

    
else:
    print("Pattern of Inheritance: Autosomal dominant does't fit")

### AUTOSOMAL RECESSIVE ###

# We initialize the domains 
status, domains=newproblem.initializeDomainsAuto1()
if(status):
    searchstatus,searchresult, domain=problem.backtrackingSearchAuto(newproblem,domains)
    if searchstatus:
        print
        print("Pattern of Inheritance: Autosomal recessive fits")
        print
        printSolution(newchart,searchresult)
    
    else:
        print("Pattern of Inheritance: Autosomal recessive does't fit")

    
else:
    print("Pattern of Inheritance: Autosomal recessive does't fit")



### X-LINKED DOMINANT ###

# We initialize the domains 
status, domains=newproblem.initializeDomainsX0()
if(status):
    searchstatus,searchresult, domain=problem.backtrackingSearchX(newproblem,domains)
    if searchstatus:
        print
        print("Pattern of Inheritance: X-linked dominant fits")
        print
        printSolutionX(newchart,searchresult)
    
    else:
        print("Pattern of Inheritance: X-linked dominant does't fit")

    
else:
    print("Pattern of Inheritance: X-linked dominant does't fit")


### X-LINKED RECESSIVE ###

# We initialize the domains 
status, domains=newproblem.initializeDomainsX1()
if(status):
    searchstatus,searchresult, domain=problem.backtrackingSearchX(newproblem,domains)
    if searchstatus:
        print
        print("Pattern of Inheritance: X-linked recessive fits")
        print
        printSolutionX(newchart,searchresult)
    
    else:
        print("Pattern of Inheritance: X-linked recessive does't fit")

    
else:
    print("Pattern of Inheritance: X-linked recessive does't fit")


### Y-LINKED ###

# We initialize the domains 
status, domains=newproblem.initializeDomainsY()
if(status):
    searchstatus,searchresult, domain=problem.backtrackingSearchY(newproblem,domains)
    if searchstatus:
        print
        print("Pattern of Inheritance: Y-linked fits")
        print
        printSolutionY(newchart,searchresult)
    
    else:
        print("Pattern of Inheritance: Y-linked does't fit")

    
else:
    print("Pattern of Inheritance: Y-linked does't fit")


'''
print(searchstatus)
print(domain)
print(len(newchart.nodes))
print(newchart.listOfAll)
for tup in newchart.listOfAll:
    print(tup[0])
print(newchart.news)
print(newchart.leaves)
'''

