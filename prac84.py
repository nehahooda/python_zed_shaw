n= raw_input("Name>>")
print("captital letters",sum(1 for c in n if c.isupper()))
print(n.lower())
print("no. of P and p's are",sum(1 for c in n if c is 'p' or c is "P"))
print("no of words are",len(n.split()))
print("NUMBER of vowels are",sum(1 for c in n if c in {'a','e','i','o','u'}))
print("NUmber of consonants are",sum(1 for c in n if c not in {'a','e','i','o','u'} ))
print("digits",sum(1 for c in n if c.isdigit()))
print("spaces",sum(1 for c in n if c.isspace()))