class dataSet:
        def __init__(self, dSet=[]):
                self.datSet = dSet

        def addDatasetFromFile(filename):
                dataList = []
                try:
                        with open(dataFile, 'r') as f:
                                for line in f:
                                        line = map(str.strip, line.split(','))
                                        for i in range(0, len(line)-1):
                                                line[i] = float(line[i])
                                                dataList.append(line)
                                                self.datSet = dataList
                        print "{} dataset loaded".format(dataFile)
                except IOError:
                        print("Cannot open %r \n" % dataFile)
                        sys.exit(2)

        #Normalizes the dataset contained by the dataSet class variable datSet
        def normalize(self):
                # Using numberOfAttributes will insure that any math is not performed on
                # class variables which may be characters, not numerical values
                numberOfAttributes = len(self.datSet[0])-1

                # These lists are used to determine the smallest and biggest attributes
                # that appear in each each instance
                self.maxAtt = [float("inf") * -1] * numberOfAttributes
                self.minAtt = [float("inf")] * numberOfAttributes

                # The double for loop records the smallest and largest attributes of each
                # instnace in minAtt or maxAtt, respectively
                for i in range (0,len(self.datSet)):
                        for k in range(0, numberOfAttributes):
                                if self.datSet[i][k] < self.minAtt[k]:
                                        self.minAtt[k] = self.datSet[i][k]

                                if self.datSet[i][k] > self.maxAtt[k]:
                                        self.maxAtt[k] = self.datSet[i][k]
        
                # Math is performed on each instance in datSet using the minAtt and maxAtt numbers
                # that correspond to the instance's place in datSet (ex. the values at minAtt[2] and maxAtt[2]
                # are used with the instance stored at datSet[2])
                for y in range (0,len(self.datSet)):
                        for z in range(0, numberOfAttributes):
                                self.datSet[y][z] = (self.datSet[y][z]-self.minAtt[z])/(self.maxAtt[z]-self.minAtt[z])

                print "Dataset has been normalized \n"