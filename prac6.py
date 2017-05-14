wrd = raw_input("please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("PALIDROME")
else:
    print("NOT A PALIDROME")