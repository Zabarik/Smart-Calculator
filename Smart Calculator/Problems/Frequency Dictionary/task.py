# put your python code here
words = input().lower().split()
words_set = set(words)
for w in words_set:
    print(w, words.count(w))
