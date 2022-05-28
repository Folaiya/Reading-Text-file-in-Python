# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

with open('./story.txt') as f:
    contents = f.read()
    print(contents)


text = open('./story.txt', 'r')
d = dict()
for line in text:
    line = line.strip()
    line = line.lower()
    words = line.split(' ')
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
for key in list(d.keys()):
    print(key, ':', d[key])
    

text = open('./story.txt', 'rt')
story = text.read()
words = story.split()
print(len(words))
