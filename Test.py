words = []
fh = open("romeo.txt")
for line in fh:
     for word in line.split():
          if word not in words:
               words.append(word)
words.sort()
print words
