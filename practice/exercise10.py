tc="\t I'm tabbed in."
pc="I'm split \n on a line."
bc="I'm \\a\\cat."
fc="""
ill do a list:
\t*cat food
\t*fisheries
\t* catnip\n\t* Grass
"""
print tc
print pc
print bc
print fc
 while True:        for i in ["/","-" ,"|","\\","|"]:            print "%s\r" % i,
