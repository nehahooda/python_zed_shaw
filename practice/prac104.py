import pandas as pd
heights=[59,20,62,65,63,65,64]
data={'heights':heights,'sex':'M'}
results = pd.DataFrame(data)
print(results)
results.index=['A','B','C','D','E','F','G']
print(results)



dict = {"country":["brazil","russia","India","China","South Africa"],
        "capital":["Brasilia","Moscow","New delhi","Beijing","Pretoria"],
        "area":[8.523,17.78,3.289,9.879,1.23],
        "population":[200.4,143.5,1252,1357,52.98]}

brics= pd.DataFrame(dict)
print(brics)
brics.index=['1','2','3','4','5']
print(brics)



cars = pd.read_csv('cars.csv')
print(cars)