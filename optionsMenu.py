import StringIO

#Class to encapsulate the options menu that allows users to perform operations, add datasets, print results, etc.
class optionsMenu:
	def __init__(self):
		print "Options menu initiated"

	def launchMenu(self, dist, dat, printFlag, saveFlag, saveFile):
            #User must enter the number of the option listed below to activate the option
            optionsList = ["1. Load dataset", "2. Normalize", "3. Use distance metric","4. Add new instance"]

            print '\n'
            for i in range (0, len(optionsList)):
                print optionsList[i]

            #Asks user to enter number corresponding to each feature option, which allows the program to perform the feature
            us = raw_input("\nType number of desired option or q to quit\n")
            while (us != 'q'):
                
                #Program will ask for dataset file name and try to copy the data into the program's dataset object
                if us == '1':
                    dataList = []
                    dataFile = raw_input("Enter name of file (including extension) containing dataset: ")

                    try:
                        f = open(dataFile, 'r')

                        #error handling for line format
                        for line in f:
                            arr = line.split()
                            dataList.append(arr)
                        dat.datSet = dataList
                        print "New dataset loaded \n"
                    except IOError:
                        print("Cannot open %r \n" % dataFile)

                #Dataset will be normalized using the function defined in the class file dataSet.py
                elif us == '2':
                    if (dat.datSet):
                        dat.normalize()
                    else:
                        print "\n No dataset loaded \n"
                
                #User can choose to use distance metrics or add new one
                elif us == '3':
                    dist.listMetrics()

                    x = dist.metricChoice(dat.datSet)

                    if (printFlag):
                        print "Metric result: {}".format(x)
                        print "Distance metric finished"

                    if (saveFlag):
                        with open(saveFile, "a") as f:
                            f.write(str(x))

                #User can add new instance to the program's new instance class variable contained by dist
                elif us == '4':
                    filename = raw_input("\n Enter file name of new instance (including extension) \n")
                    dist.addInstanceFromFile(filename)                        
                
                else:
                    assert False, "unhandled option \n"

                # The options list will continue to be printed until the user enters 'q'
                for i in range (0, len(optionsList)):
                    print optionsList[i]
                us = raw_input("New command?\n")
            
            print "\n Program closed"