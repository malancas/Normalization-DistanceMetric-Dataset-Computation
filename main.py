import getopt, sys, dataSet, distanceMetrics, optionsMenu, StringIO
def main(argv):
    try:
        opts, args = getopt.getopt(argv, "a:i:nd:s:pc:", ["add=", "instance=", "normalize", "distance=", "save=", "print", "choice="])

    #Prints error message concerning unrecognized option
    except getopt.GetoptError as err:
        print str(err)
        sys.exit(2)
    
    # Below are variables used with command line options to flag whether an option has been chosen
    # and save any arguments an option requires 
    dat = []
    dist = distanceMetrics.distM()
    saveFlag = 0
    printFlag = 0
    normalizeFlag = 0
    addFlag = 0
    newInstanceFlag = 0
    distanceFlag = 0
    choiceFlag = 0

    saveFile = ""
    outputFile = ""
    dataFile = ""
    newInstanceFile = ""
    distanceMetricFile = ""
    instanceChoice = ""

    # The for loop checks if the current letter represented by opt is identical to any of the
    # options accounted for by the program. If it does, its corresponding flag will be set to 1
    # and any argument will saved to the corresponding variable. If the letter does not correspond
    # to any option, the program will provide an error message and exit
    for opt, arg in opts:
        if opt in ("-s", "--save"):
            #saveObj = saveOption.saveOption(1)
            saveFlag = 1
            saveFile = arg
        
        elif opt in ("-p", "--print"):
            printFlag = 1
        
        elif opt in ("-a", "--add"):
            addFlag = 1
            dataFile = arg
        
        elif opt in ("-i", "--instance"):
            newInstanceFlag = 1
            newInstanceFile = arg
        
        elif opt in ("-n", "--normalize"):
            normalizeFlag = 1
        
        elif opt in ("-d", "--distance"):
            distanceFlag = 1
            distanceMetricChoice = arg
        
        elif opt in ("-h", "--help"):
            help = helpOp.helpOp()
            help.printMessage()
            sys.exit(0)

        elif opt in ("-c", "--choice"):
            choiceFlag = 1
            instanceChoice = int(arg)-1

            if instanceChoice < 0:
                print "Not a valid instance choice"
                system.exit(2)

        else:
            print "Command not recognized \n"
            system.exit(-1)

    # After all arguments and options have been read, raising appropiate flags,
    # program will carry out the corresponding operations
    
    # The program will attempt to read in the dataset from the file represented by dataFile
    # into the dataSet object dat
    if (addFlag):
        dataList = []
        try:
            with open(dataFile, 'r') as f:
                for line in f:
                    line = map(str.strip, line.split(','))
                    for i in range(0, len(line)-1):
                        line[i] = float(line[i])
                    dataList.append(line)
                dat = dataSet.dataSet(dataList)
            print "{} dataset loaded".format(dataFile)
        except IOError:
            print("Cannot open %r \n" % dataFile)
            system.exit(2)

    # The program will attempt to add a new instance from newInstanceFile
    if (newInstanceFlag):
        dist.addInstanceFromFile(newInstanceFile)

    # The program will attempt to normalize the dataset kept in the dat.datSet variable
    if (normalizeFlag):
        if (dat):
            dat.normalize()
        else:
            print "No dataset loaded \n"

    # The program will check that the index of the chosen instance (used for distance metric calculation)
    # is within the limits of datSet's length, insuring the choice doesn't go off the end of the list 
    if (choiceFlag):
        if dat.datSet == []:
            print "ERROR: No dataset loaded"
            sys.exit(2)

        if instanceChoice >= len(dat.datSet):
            print "ERROR: Not a valid instance choice"
            sys.exit(2)
    
    # After insuring that a metric has been chosen, a new instance exists, and the choice flag has been
    # raised, which signifies that the user has chosen an instance to be used in the distance metric,
    # the program will attempt to perform the chosen distance metric on the parameters provided
    if (distanceFlag):
        if distanceMetricChoice and dist.hasNewInstance() and choiceFlag:
            x = dist.dispatcher[distanceMetricChoice](dat.datSet[instanceChoice], dist.new_Instance)
            
            if (printFlag):
                print "Metric result: {}".format(x)
                print "Distance metric finished"

            if (saveFlag):
                with open(saveFile, "a") as f:
                    f.write(str(x))

        else:
            print "Not enough arguments provided \n"

    # After the command line arguments have been satisfied,
    # a menu will launch, allowing the user to perform more operations
    print '\n'
    menu = optionsMenu.optionsMenu()
    menu.launchMenu(dist, dat, printFlag, saveFlag, saveFile)

    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv[1:])