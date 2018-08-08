import random
maxerror = 0.001
step = 0.0001
cities = {} # cities format name:city object
class Node:
    value = 0
    description = ""
    cons = {}#connections format: node:weight
    def setVal(self,value):
        self.value = value
    def getVal(self):
        return self.value
    def connect(self,nextNode):
        w = random.random()#setting random weightage
        self.cons[nextNode] = w
        nextNode.cons[self] = w
class InputNode(Node):
    pass
class OutputNode(Node):
    pass
class MiddleNode(Node):
    pass

class Minute(InputNode):
    description = "minutes"
    def setVal(self,minutes):
        self.value = minutes/59

class Hour(InputNode):
    description = "hours"
    def setVal(self,hours):
        self.value = hours/23

class Day(InputNode):
    description = "day"
    def setVal(self,day):
        self.value = (day-1)/30
class Month(InputNode):
    description = "month"
    def setVal(self,month):
        self.value = (month-1)/11
class Year(InputNode):
    description = "year"
    def setVal(self,year):
        self.value = year/99

class Layer :
    nodes = [] # nodes in the current layer
    prevNodes = [] #nodes in the previous layer
    connections = [] 
    def __init__(self,prevNodes,nodes):
        self.nodes = nodes
        self.prevNodes = prevNodes
        if (prevNodes == None) : return
        for pn in self.prevNodes :
            for n in self.nodes:
               pn.connect(n)
    
class City :
    def __init__(self,name,crimes):
        self.name = name
        self.crimes= crime
        self.ilayer = Layer(None,[Minute(),Hour(),Day(),Month(),Year()])
        nodes = []
        
        for i in range(10):
            nodes.append(MiddleLayer())
        
        self.mlayer = Layer(self.ilayer.nodes,nodes)
        nodes.clear()
        for crime in crimes:
            self.crimes[crime] = OutputLayer()
                       
            nodes.append(self.crimes[crime])
            nodes[-1].name = crime
        self.olayer = Layer(self.mlayer,nodes)
    
    def predict(self):
        for mnode in self.mlayer:
            for inode in self.ilayer:
                mnode.value = mnode.value + (inode.value*mnode.cons[inode])
            mnode.value = mnode.value/5
        for onode in self.olayer:
            for mnode in self.mlayer:
                onode.value = onode.value + (mnode.value*onode.cons[mnode])
            onode.value = onode.value/10
        print("Prediction :")
        for onode in self.olayer:
            print(onode.name+" : "+onode.value)
    
    def adjust(self):
        for mnode in self.mlayer:
            lvalue = rvalue = 0
            lmaxnode= rmaxnode = None
            error = 1
            lmaxval = rmaxval = 0
            val = 0
            while ((error>-maxerror)or(error<maxerror)):
                for inode in self.ilayer:
                    val = inode.value*mnode[inode]
                    lvalue = lvalue + val
                    if val > lmaxval 
                       lmaxval = val
                       lmaxnode = inode
                   
                
                for onode in self.olayer:
                    val = onode.value/mnode[onode]
                    ovalue = ovalue + val
                    if val > rmaxval :
                        rmaxval = val
                        rmaxnode = onode
                error = rvalue -lvalue
                if (error>maxerror):
                    val = rmaxnode.cons[mnode]
                    val = val - step
                    rmaxnode.cons[mnode] = val
                    mnode.cons[rmaxnode] = val
                elif (error<maxerror):
                    val = lmaxnode.cons[mnode]
                    val = val - step
                    lmaxnode.cons[mnode] = val
                    mnode.cons[lmaxnode] = val
        return
        
        
def addCrime(city,crime):
    if crime not in city.crimes:
        onode = OutputNode()
        onode.name = crime
        city.crimes[crime] = onode
        city.olayer.append(crime)
        for mnode in city.mlayer:
            onode.connect(mnode)

def delCrime(city,crime):
    if city not in cities:
        return
    if crime in city.crimes:
        for mnode in city.mlayer:
            del mnode[city.crimes[crime]]
        city.crimes[crime].__del__()



def createNetwork():
    name = input("Enter city name:")
    n = int(input("Enter number of crimes:"))
    i = 0
    crimes = []
    while (i<n):
        crimes.append(input("Enter crime name:"))
        i = i+1
    city = City(name,crimes)
    cities[name] = city
    return city
    
def learn(city):
    f = open("database","r")
    s = f.readline()
    data = None
    while(s!=""):
        data = s.split()
        l = len(data)
        for i in range(l):
            data[i] = int(data[i])
        for i in range(5) :
            city.ilayer.nodes[i].setVal(data[i])
            
        for i in city.olayer:
            i.setVal(0)
        for i in range(6:l):
            city.olayer.nodes[data[6-i]] = 1
        city.adjust()
        s = s.deadline()
    f.close()
    
    
 
