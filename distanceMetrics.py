import math

class distM(object):
        def __init__(self, nwInt=[]):
                #Dictionary contains built in distance metric names and corresponding function calls. New metrics are added
                #here after the Manhattan entry
                self.dispatcher = {'euclidean': self.euclidean, 'manhattan': self.manhattan}
                #The class object's new instance class variable
                self.new_Instance = nwInt

        #Lists the each metric with corresponding list number, allowing user to choose which to use
        def listMetrics(self):
                i = 1
                for key in self.dispatcher.keys():
                        print "{}. {}".format(i, key)
                        i = i+1

        #'ch' argument represents the metric chosen by user, datSet is the dataset
        #Checks that dataset and instance are presnt. Checks that user's choice exists within the metric dictionary
        def metricChoice(self, datSet):
                choice = raw_input("Enter the name of chosen metric \n")

                if self.new_Instance == []:
                        print "New instance not found. Add new instance \n"
                elif self.dispatcher.has_key(choice) == 0:
                        print "Metric not found"
                        return
                elif datSet == []:
                        print "No dataset loaded. Load new set \n"
                        return
                else:
                        datasetInst = raw_input("Choose the number of an instance from the dataset to work with \n")
                        datasetInst = int(datasetInst)-1
                        if datasetInst < 0 or datasetInst >= len(datSet):
                                print "Not valid index choice"
                                return
                        
                        return self.deployMetric(choice, datSet, datasetInst)             
        
        #Attemps to add new instance from filename to replace the value of new_Instance
        def addInstanceFromFile(self, filename):
                try:
                        f = open(filename, 'r')
                        for line in f:
                                line = map(str.strip, line.split(','))
                                for i in range(0, len(line)-1):
                                        line[i] = float(line[i])
                                self.new_Instance = line 
                        print "New instance added"
                except IOError:
                        print("ERROR: Could not read %r \n" % filename)

        #Calls specified distance metric
        def deployMetric(self, choice, datSet, datasetInst):
                return self.dispatcher[choice](datSet[datasetInst], self.new_Instance)

        #Returns true if new_Instance has a value
        def hasNewInstance(self):
                return len(self.new_Instance) > 0


        #####DISTANCE METRICS##############################
        
        #Implementation of euclidean distance metric
        def euclidean(self,oldInst,newInst):
                print "Euclidean started"

                length = len(oldInst)-1
                x = 0

                for i in range(0, length):
                        x += math.pow((oldInst[i]-newInst[i]),2)

                return math.sqrt(x)

        #Implementation of manhattan distance metric
        def manhattan(self,oldInst,newInst):
                print "Manhattan started"
                
                length = len(oldInst)-1
                x = 0

                for i in range(0, length):
                        x += math.fabs(oldInst[i]-newInst[i])

                return x 

        #Functions for new metrics are defined here