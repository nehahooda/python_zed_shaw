words =[
    'red', 'green', 'black','pink','green','red',
    'pink','red','orange','pink','black','pink',
    'green','red','pink','red','green','orange',
    'white','red','green','pink','green','red'

]

from collections import Counter
word_counts = Counter(words)
top_four = word_counts.most_common(4)
print(top_four)
