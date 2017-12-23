Design Patterns Project

Implements Template Method with Policies for each step in the Template

Data Science Framework : 

- Pre-process Data : To fill in missing values
	- Mean
	- Mode
	- Random fill
- Normalization : 
	- Center around mean
	- Squash
- Build Model : 
	- Naive Bayes
	- KNN
- Testing : 
	- K-Fold
	- Train Test Validation
	
	
To run the pre loaded demo : 
Run client.py using python2.7
To use the policies, include the modules from the packages named preprocess, normalize, model, and test, and use the respective policies necessary.
To use the framework, 
1) Initialise the framework using the constructor of Framework class.
2) Provide as parameters the policy objects that were created, or use default parameters.
3) Provide the dataset in list of lists format which contains the whole data, and a list of invalids for each column, if nothing is given, 0 is assumed to be the invalid field in every column. If there are no invalids for each column, provide a list of 0s.
