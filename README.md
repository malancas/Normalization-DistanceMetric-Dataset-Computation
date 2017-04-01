Basic-Machine-Learning-Computation
Used for introductory machine learning class computation. Expanded into a project.
Written in Python 2.7.10


The program uses the following command lines arguments and flags:
	-i, --import: Used with the normalize and distance flags. Takes txt filename as argument, Will import a dataset from file within the program's directory into the program. The dataset can be overwritten at any time
	-n, --normalize: No argument, Will normalize any dataset previously loaded into the program
	-a, --add: Used with the distance flag. Takes text file name as argument. Reads in and save a new instance from a file within the program's directory. The new instance can be overwritten at any time
	-c, --choice: Used with the distance flag. The user enters the number of a instance that appears in the file read into the program using the import flag
	-d, --distance: Takes text file name as argument, When both a dataset, new instance, and choosen instance from the dataset have been previously loaded into the program, this command will use the funtion containd within the argument file as a distance metric and perform the operation on the program's current dataset and new instance.
	-s, --save: Takes text file name as argument. Saves any computational output to the file provided as the flag's argument.
	-p, --print: Prints computation done in the program to the terminal screen.

DATASET FORMAT
	The text file containing a dataset that the user wants to import must only contain the dataset. The dataset in question must adhere to the following format, each line representing a different instance. There should be no comments or anything else in this file other than the dataset:
	
	5.1,3.5,1.4,0.2,A
	4.9,3.0,1.4,0.2,B
	4.7,3.2,1.3,0.2,C
	4.6,3.1,1.5,0.2,A

	There should be no spaces between each value nor punctuation around any nominal class values. Only numerical instance attribute values are currently supported.

NEW INSTANCE FORMAT
	A file containing a new instance must obey the same rules as a dataset file. Instead of multiple lines, the file will only contain
	one line, which will be a single instance. Only numerical instance attribute values are currently supported:

	4.7,3.2,1.3,0.2,C

Instances must have the same number of attribute values for the distance metric to work correctly

ADDING DISTANCE METRICS/DISTANCE METRIC FORMAT
	If a user wants to use a distance metric other than Manhattan or Eucildean, one can do so by adding a python function representing this
	metric to the bottom of the distanceMetrics.py file. After adding the the function to this file, add a dictionary pair to the class'
	dictionary variable dispatcher. For example, after adding the definition of the metric 'myMetric' to the bottom of the class file,
	add 'myMetric': self.myMetric to self.dispatcher after the manhattan metric dictionary pair. This will allow the 


	A file containing a distance metric must only contain the function that serves the distance metric in question.
	For example, such a file would look like:

		def myDistanceMetric(datasetX):
			#Do something

	A distance metric function have two arguments, the first representing the dataset, the second representing the new instance