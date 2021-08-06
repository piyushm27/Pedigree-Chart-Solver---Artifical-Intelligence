from utils import *

class ChartNode:
    def __init__(self,level=1,col=1):
        self.level=level
        self.col=col
        self.gender=0
        self.parents=tuple() # paternal and maternal

        #self.alleles=tuple() # This may not be necessary, so kept for later

        self.identicalSiblings=[]
        self.children=[]
        self.phenotype=0 # 0=non-affected, 1=affected, 2=carrier
        #self.spouse=None


    """ ||| Functions below are to get values of Node ||| """

    def getLevel(self):
        return self.level

    def getPosition(self):
        return ((self.level,self.col))

    def getName(self):
        st=int_to_Roman(self.level)+str(self.col)
        return st
    
    def getGender(self):
        return self.gender

    '''
    def hasSpouse(self):
        return (not self.spouse==None)
    '''
    
    def isLeaf(self):
        return (len(self.children)==0)
    


    """ ||| Functions below are to set values to Node ||| """

    '''
    def setPosition(self,level=None,col=None):
        if level==None or level==0 or col==None col==0:
            print("Send value for level and col of node")
            return
        self.level=level
        self.col=col
        return
    '''

    def setGender(self, gender=None):
        ''' make male=1 and female=2 '''
        if ( (gender==None)or ((gender!=0) and (gender!=1) and(gender!=2)) ):
            print("Invalid gender sent to node:", self.getName())
            return
        self.gender=gender
        print("Gender of Node: ", self.getName(), " marked as ", self.gender)
        return

    def setParents(self, father=None, mother=None):
        ''' send nothing in case of first level or new, and send position in rest cases '''
        if(father==None) or (mother == None):
            if self.level==1:
                self.parents=((0,0),(0,0))
                print("Set [None] parents of level I node: ", self.getName())
                return
            
            else:
                print("New to family: ", self.getName())
                self.parents=((0,0),(0,0))
                return
        self.parents=(father,mother)
        print("Set parents of node: ", self.getName(), " as ", self.parents)
        return

    '''
    |||This may not be necessary, so kept for later|||

    def setAlleles(self, paternal=0,maternal=0): # make a=1 and A=2
        if(paternal==0) or (maternal==0):
            print("Illegal alleles sent. Please Check!")
            return
    '''
    def addSibling(self, sibling=None):
        ''' Send position of the identical sibling '''
        if(sibling==None):
            print("Send position of identical sibling to node: ", self.getName())
            return
        self.identicalSiblings.append(sibling)
        print("Identical Sibling: ", sibling, " added to node: ", self.getName())
        return

    def addChild(self, child=None):
        if(child==None):
            print("Send name of child to node: ", self.getName())
            return
        self.children.append(child)
        print("Child: ", child, " added to node: ", self.getName())
        return
    
    def setPhenotype(self, phenotype=None):
        ''' 0=normal phenotype, 1= affected, 2=carrier'''
        if(phenotype==None) or ((phenotype!=0)and(phenotype!=1)):
            print("Invalid phenotype sent to node:", self.getName())
            return
        self.phenotype=phenotype
        print("Phenotype: ", self.phenotype, " set for node: ", self.getName())

    '''
    def setSpouse(self, spouse=None):
        if(Spouse==None):
            print("Send a spouse to add for node: ", self.getName())
            return
        self.spouse=spouse
        print(spouse.getName()," is added as spouse of node: ", self.getName())
        return
    '''



class Chart:
    def __init__(self):
        self.nodes={} #make this a dictionary of {position-tuple: node}
        self.leaves=[]
        self.news=[]
        self.listOfAll=[]

    #spouse, has spouse, has kids, is new, new to fam, is leave, leaves

    '''
    def extractPositions(st):
        list0=st.split(',')
        lev=int(list0[0])
        co=int(list0[1])
        return lev,co

    def extractPositionsTuple(st):
        list0=st.split(',')
        lev=int(list0[0])
        co=int(list0[1])
        pos=(lev,co)
        return pos
    '''

    def makeChart(self, filename="inputs/1.txt"):
        inputfile=open(filename,'r')

        k=1
        listOfNodes=[]

        for line in inputfile:
            #position|phenotype|gender|father|mother|no. of children|no. of identical siblings|child1|child2|....|childn|sibling1|sibling2|...|sibingn
            if line[0] != '>':
                continue
            line=line[1:]
            line=line.strip('\n')
            line=line.replace('(','')
            line=line.replace(')','')
            list0=line.split('|')

            #Let's start making the node
            level,col=extractPositions(list0[0])
            newnode=ChartNode(level=level,col=col)
            print("Node successfully made for: ", (level,col))

            if k==level:
                listOfNodes.append(newnode.getPosition())
            else:
                self.listOfAll.append((list(listOfNodes),k))
                listOfNodes=[]
                k=k+1
                listOfNodes.append(newnode.getPosition())

            newnode.setPhenotype(int(list0[1]))
            newnode.setGender(int(list0[2]))
            if list0[3]=='0':
                newnode.setParents()
                self.news.append(newnode.getPosition())
            else:
                father=extractPositionsTuple(list0[3])
                mother=extractPositionsTuple(list0[4])
                newnode.setParents(father,mother)
            n_children= int(list0[5])

            if(n_children==0):
                self.leaves.append(newnode.getPosition())

            n_siblings= int(list0[6])

            for i in range(7,7+n_children):
                child=list0[i]
                childnode=extractPositionsTuple(child)
                newnode.addChild(childnode)
            
            for i in range(7+n_children,7+n_children+n_siblings):
                sibling=list0[i]
                siblingnode=extractPositionsTuple(sibling)
                newnode.addSibling(siblingnode)

            self.nodes[newnode.getPosition()]=newnode 
        
        self.listOfAll.append((list(listOfNodes),k))
        return


#def backtrackingSearchAuto(chart=None):

class Problem:
    def __init__(self,chart=Chart()):
        self.chart=chart
        return

    def initializeDomainsAuto0(self):
        #Auto0 is autosomal dominant
        #INCOMPLETE
        domains={}
        #print(" check1")
        for sublist in self.chart.listOfAll:
            for cn in sublist[0]:
                nodeHere= self.chart.nodes[cn]
                #print(" check2")

                if nodeHere.parents[0][0]==0:
                    #what to do when parents not given?
                    #give them all they deserve for their pehnotype
                    if(nodeHere.phenotype==2):
                        return False,domains
                    if(nodeHere.phenotype==0):
                        setOfVal={('A','A'),('A','a'),('a','A')}
                        domains[cn]=setOfVal
                    if(nodeHere.phenotype==1):
                        setOfVal={('a','a')}
                        domains[cn]=setOfVal
                    #print(" check3")
                else:

                    if(nodeHere.phenotype==2):
                        return False,domains
                    if(nodeHere.phenotype==0):
                        setOfVal={('A','A'),('A','a'),('a','A')}
                        domains[cn]=setOfVal
                    if(nodeHere.phenotype==1):
                        setOfVal={('a','a')}
                        domains[cn]=setOfVal

                    newSet=domains[cn].copy()
                    for val in newSet:
                        flag=0
                        for pval in domains[nodeHere.parents[0]]:
                            if((val[0]!=pval[0]) and (val[0]!=pval[1])):
                                continue
                            else:
                                flag=1
                                break
            
                        if(flag==0):
                            domains[cn].remove(val)
                            continue

                        flag=0
                        for mval in domains[nodeHere.parents[1]]:
                            if((val[1]!=mval[0])and (val[1]!=mval[1])):
                                continue
                            else:
                                flag=1
                                break
            
                        if(flag==0):
                            domains[cn].remove(val)
                            continue

                if(len(domains[cn])==0):
                    status=False
                    return status, domains
                
                #print(cn,domains[cn])

        #seek phenotype
        #seek for parents
        #look at phenotype and parents and give them something

        #if any domain is empty, return failure
        return True, domains
        

    def initializeDomainsAuto1(self):
        #Auto0 is autosomal dominant
        #INCOMPLETE
        domains={}
        #print(" check1")
        for sublist in self.chart.listOfAll:
            for cn in sublist[0]:
                nodeHere= self.chart.nodes[cn]
                #print(" check2")

                if nodeHere.parents[0][0]==0:
                    #what to do when parents not given?
                    #give them all they deserve for their pehnotype
                    if(nodeHere.phenotype==2):
                        return False,domains
                    if(nodeHere.phenotype==0):
                        setOfVal={('A','A')}
                        domains[cn]=setOfVal
                    if(nodeHere.phenotype==1):
                        setOfVal={('a','a'),('A','a'),('a','A')}
                        domains[cn]=setOfVal
                    #print(" check3")
                else:

                    if(nodeHere.phenotype==2):
                        return False,domains
                    if(nodeHere.phenotype==0):
                        setOfVal={('A','A')}
                        domains[cn]=setOfVal
                    if(nodeHere.phenotype==1):
                        setOfVal={('a','a'),('A','a'),('a','A')}
                        domains[cn]=setOfVal

                    newSet=domains[cn].copy()
                    for val in newSet:
                        flag=0
                        for pval in domains[nodeHere.parents[0]]:
                            if((val[0]!=pval[0]) and (val[0]!=pval[1])):
                                continue
                            else:
                                flag=1
                                break
            
                        if(flag==0):
                            domains[cn].remove(val)
                            continue

                        flag=0
                        for mval in domains[nodeHere.parents[1]]:
                            if((val[1]!=mval[0])and (val[1]!=mval[1])):
                                continue
                            else:
                                flag=1
                                break
            
                        if(flag==0):
                            domains[cn].remove(val)
                            continue

                if(len(domains[cn])==0):
                    status=False
                    return status, domains
                
                #print(cn,domains[cn])

        #seek phenotype
        #seek for parents
        #look at phenotype and parents and give them something

        #if any domain is empty, return failure
        return True, domains


    def initializeDomainsX0(self):
        #Auto0 is autosomal dominant
        #INCOMPLETE
        domains={}
        #print(" check1")
        for sublist in self.chart.listOfAll:
            for cn in sublist[0]:
                nodeHere= self.chart.nodes[cn]
                #print(" check2")

                if nodeHere.parents[0][0]==0:
                    #what to do when parents not given?
                    #give them all they deserve for their pehnotype
                    if(nodeHere.phenotype==2):
                        if(nodeHere.gender==2):
                            setOfVal={('XA','Xa'),('Xa','XA')}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==1):
                            print "Chart has a carrier male which is absurd"
                            return False, domains
                    if(nodeHere.phenotype==0):
                        if(nodeHere.gender==1):
                            setOfVal={'XA'}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==2):
                            setOfVal={('XA','XA'),('XA','Xa'),('Xa','X')}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==0):
                            print "Assuming sex unspecified node to be male. If it's not a child, it'll create problem."
                            nodeHere.setGender(1)
                            setOfVal={'XA'}
                            domains[cn]=setOfVal
                    if(nodeHere.phenotype==1):
                        if(nodeHere.gender==1):
                            setOfVal={'Xa'}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==2):
                            setOfVal={('Xa','Xa')}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==0):
                            print "Assuming sex unspecified node to be male. If it's not a child, it'll create problem."
                            nodeHere.setGender(1)
                            setOfVal={'Xa'}
                            domains[cn]=setOfVal
                    #print(" check3")
                else:

                    if(nodeHere.phenotype==2):
                        if(nodeHere.gender==2):
                            setOfVal={('XA','Xa'),('Xa','XA')}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==1):
                            print "Chart has a carrier male which is absurd"
                            return False, domains
                    if(nodeHere.phenotype==0):
                        if(nodeHere.gender==1):
                            setOfVal={'XA'}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==2):
                            setOfVal={('XA','XA'),('XA','Xa'),('Xa','XA')}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==0):
                            print "Assuming sex unspecified node to be male. If it's not a child, it'll create problem."
                            nodeHere.setGender(1)
                            setOfVal={'XA'}
                            domains[cn]=setOfVal
                    if(nodeHere.phenotype==1):
                        if(nodeHere.gender==1):
                            setOfVal={'Xa'}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==2):
                            setOfVal={('Xa','Xa')}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==0):
                            print "Assuming sex unspecified node to be male. If it's not a child, it'll create problem."
                            nodeHere.setGender(1)
                            setOfVal={'Xa'}
                            domains[cn]=setOfVal

                    newSet=domains[cn].copy()
                    for val in newSet:

                        if(nodeHere.gender==2):
                            flag=0
                            for pval in domains[nodeHere.parents[0]]:
                                if(val[0]!=pval):
                                    continue
                                else:
                                    flag=1
                                    break
                                    
                            if(flag==0):
                                domains[cn].remove(val)
                                continue

                            flag=0
                            for mval in domains[nodeHere.parents[1]]:
                                if((val[1]!=mval[0])and (val[1]!=mval[1])):
                                    continue
                                else:
                                    flag=1
                                    break
            
                            if(flag==0):
                                domains[cn].remove(val)
                                continue

                        if(nodeHere.gender==1):
                            flag=0
                            for mval in domains[nodeHere.parents[1]]:
                                if((val!=mval[0])and (val!=mval[1])):
                                    continue
                                else:
                                    flag=1
                                    break
            
                            if(flag==0):
                                domains[cn].remove(val)
                                continue


                if(len(domains[cn])==0):
                    status=False
                    return status, domains
                

                #print(cn,domains[cn])

        #seek phenotype
        #seek for parents
        #look at phenotype and parents and give them something

        #if any domain is empty, return failure
        return True, domains

    def initializeDomainsX1(self):
        #Auto0 is autosomal dominant
        #INCOMPLETE
        domains={}
        #print(" check1")
        for sublist in self.chart.listOfAll:
            for cn in sublist[0]:
                nodeHere= self.chart.nodes[cn]
                #print(" check2")

                if nodeHere.parents[0][0]==0:
                    #what to do when parents not given?
                    #give them all they deserve for their pehnotype
                    #print "check1"
                    if(nodeHere.phenotype==2):
                        if(nodeHere.gender==2):
                            setOfVal={('XA','Xa'),('Xa','XA')}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==1):
                            print "Chart has a carrier male which is absurd"
                            return False, domains
                    if(nodeHere.phenotype==0):
                        if(nodeHere.gender==1):
                            setOfVal={'XA'}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==2):
                            setOfVal={('XA','XA'),('XA','Xa'),('Xa','X')}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==0):
                            print "Assuming sex unspecified node to be male. If it's not a child, it'll create problem."
                            nodeHere.setGender(1)
                            setOfVal={'XA'}
                            domains[cn]=setOfVal
                    if(nodeHere.phenotype==1):
                        if(nodeHere.gender==1):
                            setOfVal={'Xa'}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==2):
                            setOfVal={('Xa','Xa')}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==0):
                            print "Assuming sex unspecified node to be male. If it's not a child, it'll create problem."
                            nodeHere.setGender(1)
                            setOfVal={'Xa'}
                            domains[cn]=setOfVal
                    #print(" check3")
                else:

                    if(nodeHere.phenotype==2):
                        if(nodeHere.gender==2):
                            setOfVal={('XA','Xa'),('Xa','XA')}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==1):
                            print "Chart has a carrier male which is absurd"
                            return False, domains
                    if(nodeHere.phenotype==1):
                        if(nodeHere.gender==1):
                            setOfVal={'XA'}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==2):
                            setOfVal={('XA','XA'),('XA','Xa'),('Xa','XA')}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==0):
                            print "Assuming sex unspecified node to be male. If it's not a child, it'll create problem."
                            nodeHere.setGender(1)
                            setOfVal={'XA'}
                            domains[cn]=setOfVal
                    if(nodeHere.phenotype==0):
                        if(nodeHere.gender==1):
                            setOfVal={'Xa'}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==2):
                            setOfVal={('Xa','Xa')}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==0):
                            print "Assuming sex unspecified node to be male. If it's not a child, it'll create problem."
                            nodeHere.setGender(1)
                            setOfVal={'Xa'}
                            domains[cn]=setOfVal

                    newSet=domains[cn].copy()
                    for val in newSet:

                        if(nodeHere.gender==2):
                            flag=0
                            for pval in domains[nodeHere.parents[0]]:
                                if(val[0]!=pval):
                                    continue
                                else:
                                    flag=1
                                    break
                                    
                            if(flag==0):
                                domains[cn].remove(val)
                                continue

                            flag=0
                            for mval in domains[nodeHere.parents[1]]:
                                if((val[1]!=mval[0])and (val[1]!=mval[1])):
                                    continue
                                else:
                                    flag=1
                                    break
            
                            if(flag==0):
                                domains[cn].remove(val)
                                continue

                        if(nodeHere.gender==1):
                            flag=0
                            for mval in domains[nodeHere.parents[1]]:
                                if((val!=mval[0])and (val!=mval[1])):
                                    continue
                                else:
                                    flag=1
                                    break
            
                            if(flag==0):
                                domains[cn].remove(val)
                                continue


                if(len(domains[cn])==0):
                    status=False
                    return status, domains
                

                #print(cn,domains[cn])

        #seek phenotype
        #seek for parents
        #look at phenotype and parents and give them something

        #if any domain is empty, return failure
        return True, domains


    def initializeDomainsY(self):
        #Auto0 is autosomal dominant
        #INCOMPLETE
        domains={}
        #print(" check1")
        for sublist in self.chart.listOfAll:
            for cn in sublist[0]:
                nodeHere= self.chart.nodes[cn]
                #print(" check2")

                if nodeHere.parents[0][0]==0:
                    #what to do when parents not given?
                    #give them all they deserve for their pehnotype
                    if(nodeHere.phenotype==2):
                        if(nodeHere.gender==1):
                            print "Chart has a carrier male which is absurd"
                            return False, domains
                    if(nodeHere.phenotype==0):
                        if(nodeHere.gender==1):
                            setOfVal={'Y'}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==2):
                            setOfVal={'0'}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==0):
                            print "Assuming sex unspecified node to be male. If it's not a child, it'll create problem."
                            nodeHere.setGender(1)
                            setOfVal={'Y'}
                            domains[cn]=setOfVal
                    if(nodeHere.phenotype==1):
                        if(nodeHere.gender==1):
                            setOfVal={'Y*'}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==2):
                            setOfVal={'0'}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==0):
                            print "Assuming sex unspecified node to be male. If it's not a child, it'll create problem."
                            nodeHere.setGender(1)
                            setOfVal={'Y*'}
                            domains[cn]=setOfVal
                    #print(" check3")
                else:

                    if(nodeHere.phenotype==2):
                        if(nodeHere.gender==1):
                            print "Chart has a carrier male which is absurd"
                            return False, domains
                    if(nodeHere.phenotype==0):
                        if(nodeHere.gender==1):
                            setOfVal={'Y'}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==2):
                            setOfVal={'0'}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==0):
                            print "Assuming sex unspecified node to be male. If it's not a child, it'll create problem."
                            nodeHere.setGender(1)
                            setOfVal={'Y'}
                            domains[cn]=setOfVal
                    if(nodeHere.phenotype==1):
                        if(nodeHere.gender==1):
                            setOfVal={'Y*'}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==2):
                            setOfVal={'0'}
                            domains[cn]=setOfVal
                        if(nodeHere.gender==0):
                            print "Assuming sex unspecified node to be male. If it's not a child, it'll create problem."
                            nodeHere.setGender(1)
                            setOfVal={'Y*'}
                            domains[cn]=setOfVal

                    newSet=domains[cn].copy()
                    for val in newSet:

                        if(nodeHere.gender==1):
                            flag=0
                            for pval in domains[nodeHere.parents[0]]:
                                if(val!=pval):
                                    continue
                                else:
                                    flag=1
                                    break
            
                            if(flag==0):
                                domains[cn].remove(val)
                                continue


                if(len(domains[cn])==0):
                    status=False
                    return status, domains
                

                #print(cn,domains[cn])

        #seek phenotype
        #seek for parents
        #look at phenotype and parents and give them something

        #if any domain is empty, return failure
        return True, domains

            

def selectVariable(assigned={},csp=None, domains={}):
    if(csp==None):
        print("Illegal arguments passed to function: selectVariable" )
        return
    
    for tup in csp.chart.listOfAll:
        for key in tup[0]:
            if key in assigned:
                continue
            return key

def selectVariableX(assigned={},csp=None, domains={}):
    if(csp==None):
        print("Illegal arguments passed to function: selectVariable" )
        return
    
    for tup in csp.chart.listOfAll:
        for key in tup[0]:
            if key in assigned:
                continue
            return key

def selectVariableY(assigned={},csp=None, domains={}):
    if(csp==None):
        print("Illegal arguments passed to function: selectVariable" )
        return

    for tup in csp.chart.listOfAll:
        for key in tup[0]:
            if key in assigned:
                continue
            return key

def orderValues(key=None,assigned={},csp=Problem(),domains={}):
    if(csp==None):
        print("Illegal arguments (csp) passed to function: orderValues")
    if(key==None):
        print("Illegal arguments (key) passed to function: orderValues")

    valueDict={}
    nodeHere=csp.chart.nodes[key]

    for value in domains[key]:

        count=0
        for child in nodeHere.children:
            #search in domains[child]
            
            for childVal in domains[child]:
                if((childVal[nodeHere.gender-1]!=value[0]) and (childVal[nodeHere.gender-1]!=value[1])):
                    count=count+1
        
        valueDict[value]=count

    orderList=[]
    while len(valueDict)!=0:
        key_min = min(valueDict.keys(), key=(lambda k: valueDict[k]))
        orderList.append(key_min)
        del valueDict[key_min]
        
    return orderList

def orderValuesX(key=None,assigned={},csp=Problem(),domains={}):
    if(csp==None):
        print("Illegal arguments (csp) passed to function: orderValues")
    if(key==None):
        print("Illegal arguments (key) passed to function: orderValues")

    valueDict={}
    nodeHere=csp.chart.nodes[key]
    nodeSex=nodeHere.gender

    for value in domains[key]:

        count=0
        for child in nodeHere.children:
            #search in domains[child]
            childSex=csp.chart.nodes[child]
            
            if(nodeSex==2):
                if(childSex==2):
                    for childVal in domains[child]:
                        if((childVal[1]!=value[0]) and (childVal[1]!=value[1])):
                            count=count+1

                if(childSex==1):
                    for childVal in domains[child]:
                        if((childVal!=value[0]) and (childVal!=value[1])):
                            count=count+1

            if(nodeSex==1):
                if(childSex==2):
                    for childVal in domains[child]:
                        if((childVal[0]!=value)):
                            count=count+1

        
        valueDict[value]=count

    orderList=[]
    while len(valueDict)!=0:
        key_min = min(valueDict.keys(), key=(lambda k: valueDict[k]))
        orderList.append(key_min)
        del valueDict[key_min]
        
    return orderList


def orderValuesY(key=None,assigned={},csp=Problem(),domains={}):
    if(csp==None):
        print("Illegal arguments (csp) passed to function: orderValues")
    if(key==None):
        print("Illegal arguments (key) passed to function: orderValues")

    valueDict={}
    nodeHere=csp.chart.nodes[key]
    nodeSex=nodeHere.gender

    for value in domains[key]:

        count=0
        for child in nodeHere.children:
            #search in domains[child]
            childSex=csp.chart.nodes[child]
            
            if(nodeSex==2):
                count=1

            if(nodeSex==1):
                if(childSex==1):
                    for childVal in domains[child]:
                        if((childVal!=value)):
                            count=count+1

        
        valueDict[value]=count

    orderList=[]
    while len(valueDict)!=0:
        key_min = min(valueDict.keys(), key=(lambda k: valueDict[k]))
        orderList.append(key_min)
        del valueDict[key_min]
        
    return orderList



def isAssignmentAllowed(value,key,assigned,csp=Problem(), domains={}):
    nodeHere=csp.chart.nodes[key]
    father=nodeHere.parents[0]
    mother=nodeHere.parents[1]
    assigned[key]=value
    if(father[0]!=0):
        #recheck with parents
        if((value[0]!=assigned[father][0]) and (value[0]!=assigned[father][1])):
            return False, domains
        if((value[1]!=assigned[mother][0]) and (value[1]!=assigned[mother][1])):
            return False, domains
    #redefine domain for that variable
    del domains[key]
    domains[key]={value}
    #recursively redifine for its bloodline
    status = True
    #status , newDomains=refreshDomain(value,key,assigned,csp,domains)
    rStack=Stack()
    for child in nodeHere.children:
        rStack.push(child)

    while(not rStack.isEmpty()):
        keyNow=rStack.pop()
        nodeNow=csp.chart.nodes[keyNow]
        for child in nodeNow.children:
            rStack.push(child)
        if(len(domains[keyNow])==0):
            status=False
            return status, domains
        
        newSet=domains[keyNow].copy()
        for val in newSet:
            flag=0
            for pval in domains[nodeNow.parents[0]]:
                if((val[0]!=pval[0]) and (val[0]!=pval[1])):
                    continue
                else:
                    flag=1
                    break
            
            if(flag==0):
                domains[keyNow].remove(val)
                continue

            flag=0
            for mval in domains[nodeNow.parents[1]]:
                if((val[1]!=mval[0])and (val[1]!=mval[1])):
                    continue
                else:
                    flag=1
                    break
            
            if(flag==0):
                domains[keyNow].remove(val)
                continue

        if(len(domains[keyNow])==0):
            status=False
            return status, domains

    if(status):
        #print(key," successfully assigned ", value)
        return True, domains
    else:
        #print(key," failed to assign ", value)
        return False, domains
    


def isAssignmentAllowedX(value,key,assigned,csp=Problem(), domains={}):
    nodeHere=csp.chart.nodes[key]
    nodeSex=nodeHere.gender
    father=nodeHere.parents[0]
    mother=nodeHere.parents[1]
    assigned[key]=value
    
    #redefine domain for that variable
    del domains[key]
    domains[key]={value}
    #recursively redifine for its bloodline
    status = True
    #status , newDomains=refreshDomain(value,key,assigned,csp,domains)
    rStack=Stack()
    for child in nodeHere.children:
        rStack.push(child)

    while(not rStack.isEmpty()):
        keyNow=rStack.pop()
        nodeNow=csp.chart.nodes[keyNow]
        sexNodeNow=nodeNow.gender
        for child in nodeNow.children:
            rStack.push(child)
        if(len(domains[keyNow])==0):
            status=False
            return status, domains

        newSet=domains[keyNow].copy()
        for val in newSet:

            if(nodeNow.gender==2):
                flag=0
                for pval in domains[nodeNow.parents[0]]:
                    if(val[0]!=pval):
                        continue
                    else:
                        flag=1
                        break
                                
                if(flag==0):
                    domains[keyNow].remove(val)
                    continue

                flag=0
                for mval in domains[nodeNow.parents[1]]:
                    if((val[1]!=mval[0])and (val[1]!=mval[1])):
                        continue
                    else:
                        flag=1
                        break
        
                if(flag==0):
                    domains[keyNow].remove(val)
                    continue
            if(nodeNow.gender==1):
                flag=0
                for mval in domains[nodeNow.parents[1]]:
                    if((val!=mval[0])and (val!=mval[1])):
                        continue
                    else:
                        flag=1
                        break
            
                if(flag==0):
                    domains[keyNow].remove(val)
                    continue
 
        '''
        newSet=domains[keyNow].copy()
        for val in newSet:
            flag=0
            for pval in domains[nodeNow.parents[0]]:
                if((val[0]!=pval[0]) and (val[0]!=pval[1])):
                    continue
                else:
                    flag=1
                    break
            
            if(flag==0):
                domains[keyNow].remove(val)
                continue

            flag=0
            for mval in domains[nodeNow.parents[1]]:
                if((val[1]!=mval[0])and (val[1]!=mval[1])):
                    continue
                else:
                    flag=1
                    break
            
            if(flag==0):
                domains[keyNow].remove(val)
                continue
            '''
        if(len(domains[keyNow])==0):
            status=False
            return status, domains

    if(status):
        #print(key," successfully assigned ", value)
        return True, domains
    else:
        #print(key," failed to assign ", value)
        return False, domains
    

def isAssignmentAllowedY(value,key,assigned,csp=Problem(), domains={}):
    nodeHere=csp.chart.nodes[key]
    nodeSex=nodeHere.gender
    father=nodeHere.parents[0]
    mother=nodeHere.parents[1]
    assigned[key]=value
    
    #redefine domain for that variable
    del domains[key]
    domains[key]={value}
    #recursively redifine for its bloodline
    status = True
    #status , newDomains=refreshDomain(value,key,assigned,csp,domains)
    rStack=Stack()
    for child in nodeHere.children:
        rStack.push(child)

    while(not rStack.isEmpty()):
        keyNow=rStack.pop()
        nodeNow=csp.chart.nodes[keyNow]
        sexNodeNow=nodeNow.gender
        for child in nodeNow.children:
            rStack.push(child)
        if(len(domains[keyNow])==0):
            status=False
            return status, domains

        newSet=domains[keyNow].copy()
        for val in newSet:

            if(nodeNow.gender==1):
                flag=0
                for pval in domains[nodeNow.parents[0]]:
                    if(val!=pval):
                        continue
                    else:
                        flag=1
                        break
            
                if(flag==0):
                    domains[keyNow].remove(val)
                    continue
 
        if(len(domains[keyNow])==0):
            status=False
            return status, domains

    if(status):
        #print(key," successfully assigned ", value)
        return True, domains
    else:
        #print(key," failed to assign ", value)
        return False, domains
    





def backtrackingSearchAuto(csp=None, domains={}):
    if(csp==None):
        print("Problem absent for function: backtrackingSearchAuto")
        return
    assigned={}
    # See if you can send domains as arguments
    #domains= csp.initializeDomainsAuto0()#DEFINE THIS
    return recursiveBacktrackingSearchAuto(assigned,csp,domains)

def backtrackingSearchX(csp=None, domains={}):
    if(csp==None):
        print("Problem absent for function: backtrackingSearchAuto")
        return
    assigned={}
    #print "check1"
    # See if you can send domains as arguments
    #domains= csp.initializeDomainsAuto0()#DEFINE THIS
    return recursiveBacktrackingSearchX(assigned,csp,domains)

def backtrackingSearchY(csp=None, domains={}):
    if(csp==None):
        print("Problem absent for function: backtrackingSearchAuto")
        return
    assigned={}
    #print "check1"
    # See if you can send domains as arguments
    #domains= csp.initializeDomainsAuto0()#DEFINE THIS
    return recursiveBacktrackingSearchX(assigned,csp,domains)

def recursiveBacktrackingSearchAuto(assigned={},csp=None,domains={}):
    if(len(assigned)==len(csp.chart.nodes)):
        return True ,assigned, domains 
    key=selectVariable(assigned,csp)

    for value in orderValues(key,assigned,csp,domains):

        checkStatus, checkDomains =isAssignmentAllowed(value,key,assigned,csp, domains)

        if checkStatus:
            assigned[key]=value
            revisedDomains=checkDomains
            status,result,newDomains=recursiveBacktrackingSearchAuto(assigned,csp,revisedDomains)
            if status == True:
                return True, result, newDomains
            else:
                del assigned[key]
        else:
            del assigned[key]
    
    return False,{},{}

def recursiveBacktrackingSearchX(assigned={},csp=None,domains={}):
    if(len(assigned)==len(csp.chart.nodes)):
        return True ,assigned, domains 
    key=selectVariableX(assigned,csp)

    #print "check2"
    #print(domains)

    for value in orderValuesX(key,assigned,csp,domains):

        #print "assign"
        #print (key,value)

        checkStatus, checkDomains =isAssignmentAllowedX(value,key,assigned,csp, domains)

        if checkStatus:
            assigned[key]=value
            revisedDomains=checkDomains
            status,result,newDomains=recursiveBacktrackingSearchX(assigned,csp,revisedDomains)
            if status == True:
                #print "HAHA"
                #print (newDomains)
                return True, result, newDomains
            else:
                #print "NANA"
                #print "assign fail 2"
                #print (key,value)
                del assigned[key]
        else:
            #print "assign fail 1"
            #print (key,value)
            del assigned[key]

    #print "WTF"
    
    return False,{},{}

def recursiveBacktrackingSearchY(assigned={},csp=None,domains={}):
    if(len(assigned)==len(csp.chart.nodes)):
        return True ,assigned, domains 
    key=selectVariableX(assigned,csp)

    #print "check2"
    #print(domains)

    for value in orderValuesX(key,assigned,csp,domains):

        #print "assign"
        #print (key,value)

        checkStatus, checkDomains =isAssignmentAllowedX(value,key,assigned,csp, domains)

        if checkStatus:
            assigned[key]=value
            revisedDomains=checkDomains
            status,result,newDomains=recursiveBacktrackingSearchX(assigned,csp,revisedDomains)
            if status == True:
                #print "HAHA"
                #print (newDomains)
                return True, result, newDomains
            else:
                #print "NANA"
                #print "assign fail 2"
                #print (key,value)
                del assigned[key]
        else:
            #print "assign fail 1"
            #print (key,value)
            del assigned[key]

    #print "WTF"
    
    return False,{},{}


