import matplotlib.pyplot as plt
yr=[1950,1970,1990,2010]
pop=[2.519,3.692,5.263,6.972]

yr=[1800,1850,1900]+ yr
pop=[1.0,1.256,1.79]+ pop

plt.plot(yr,pop)
plt.xlabel('YEAR')
plt.ylabel('POPULATION')
plt.title('WORLD POPULATION')
plt.yticks([0,2,4,6,8,10],
           ['0','2B','4B','6B','8B','10B'])
plt.show()


#scatter plot
plt.scatter(yr,pop)
plt.show()

#histogram
v=[0,0.6,1.4,1.6,2.2,2.5,2.6,3.9,4.5,6]
plt.hist(v,bins=3)
plt.show()
