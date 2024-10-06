from week04 import CircularQueue
from random import randint

class TicketCounterSimulation:
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        self._arriveprob = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes
        self.served = 0
        self._passenger = CircularQueue()
        self._Agents = [None]*numAgents
        for i in range(numAgents):
            self._Agents[i] = TicketAgent(i + 1)
        self._totalWaitTime = 0
        self._numpassenger = 0
    
    def run(self):
        for curTime in range(self._numMinutes + 1):
            self.handleArrivals(curTime)
            self.handleServices(curTime)
            self.handleEndservices(curTime)
        self.printResults()
            
    def handleArrivals(self, curTime):
        prob = randint(0.0, 100.0)/100
        if 0.0 <= prob and prob <= self._arriveprob:
            person = Passenger(self._numpassenger + 1, curTime)
            self._passenger.enqueue(person)
            self._numpassenger += 1
            print("time {} : passenger {} arrived".format(curTime, person.getPID()) )
            
            
    def handleServices(self, curTime):
        i = 0
        while i < len(self._Agents):
            if self._Agents[i].isFree() and not self._passenger.isEmpty() and curTime != self._numMinutes:
                passenger = self._passenger.dequeue()
                self.served +=1
                stoptime = curTime + self._serviceTime
                self._Agents[i].startService(passenger,stoptime)
                self._totalWaitTime += (curTime - passenger.timeArrival())
                print("time {} : agent {} started serving passenger {} ".format(curTime,self._Agents[i].getAID(), passenger.getPID()))
            i+=1
                
    def handleEndservices(self, curTime):
        i = 0
        while i < len(self._Agents):
            if self._Agents[i].isFinished(curTime):
                passenger = self._Agents[i].stopService()
                print("time {} agent {} stopped serving passenger {}".format(curTime,self._Agents[i].getAID(),passenger.getPID()))
            i += 1
    def printResults(self):
        numServed = self._numpassenger - len(self._passenger)
        avgwait = float(self._totalWaitTime) / numServed
        print("")
        print("number of passengers served = {}".format(numServed))
        print("number of passengers remaining in line = {}".format(len(self._passenger)))
        print("The averages wait time was {:.2f} minutes".format(avgwait))

class Passenger:
    def __init__(self, pId = 0, atime = 0) -> None:
        self.pID = pId
        self._arrivalTime = atime        
    def getPID(self):
        return self.pID
    def timeArrival(self):
        return self._arrivalTime
    
class TicketAgent:
    
    def __init__(self, aid) -> None:
        self._aID = aid
        self._passenger = None
        self._stopTime = -1
        
    def getAID(self):
        return self._aID
    def isFree(self):
        return self._passenger is None
    
    def isFinished(self, curTime):
        return self._passenger is not None and curTime == self._stopTime

    def startService (self, Passenger, stopTIme):
        self._passenger = Passenger
        self._stopTime = stopTIme
    def stopService(self):
        p = self._passenger
        self._passenger = None
        return p
    