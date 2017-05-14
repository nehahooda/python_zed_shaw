def reverse(word):
    x=''
    for i in range(len(word)):
        x+=word[len(word)-1-i]
        return x
word = raw_input('give me words:\n')
x=reverse(word)
if x== word:
    print"PALIDROME"
else:
    print"NOT A PALIDROME"