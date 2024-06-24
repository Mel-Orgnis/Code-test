import sys
num = int(sys.stdin.readline())
words = list(set([sys.stdin.readline().rstrip() for i in range(num)]))
for i in range(len(words)) :
    words[i] = f'{len(words[i]):02d}'+words[i]
words.sort()
for i in range(len(words)) :
    print(words[i][2:])




