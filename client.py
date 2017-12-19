from framework import *
import framework_2
from policies.model.knn import *
from policies.preprocess.mean import *
import csv
with open("dataset.csv", 'rU') as f:
	reader = csv.reader(f)
	data = list(list(map(float, rec)) for rec in csv.reader(f, delimiter=','))  # reads csv into a list of lists

framework = Framework(data, invalids = ["nan",0,0,0,0,0,"nan","nan","nan"])
model, accuracy = framework.processData()
print("Model Object : ", model)
print("Accuracy : ",accuracy)
print()
query1 = [0,188,82,14,185,32.0,0.682,22,1]

string = """
Classification for : 
# times pregnant : 0
Plasma Glucose Concentration : 188
Diastolic Blood Pressure : 82
Triceps skinfold thickness : 14
2-Hour serum insulin : 185
Body Mass Index : 32
Diabetes Pedigree Function : 0.682
Age : 22

Onset of Diabetes? : """
print(string,"Yes" if model.classify(query1) else "No")



print()
framework = framework_2.Framework(data, preprocessPolicy = Mean(), normalizePolicy = Center(),  modelPolicy = KNN(), invalids = ["nan",0,0,0,0,0,"nan","nan","nan"])
model, accuracy = framework.processData()
print("Model Object : ", model)
print("Accuracy : ",accuracy)
print()

print(string,"Yes" if model.classify(query1) else "No")
