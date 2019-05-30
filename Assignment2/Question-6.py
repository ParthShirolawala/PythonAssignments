#write a program to calculate length of each word in a sentence.

sentence = input("Enter a sentence:")

def countLengthOfWords():
    wordfreq = {}
    words = sentence.split(" ")
    for word in words:
        length = len(word)
        wordfreq[word] = length

    print wordfreq


countLengthOfWords()
