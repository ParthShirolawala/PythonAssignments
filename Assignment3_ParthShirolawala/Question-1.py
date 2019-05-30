input_sentence = input("Enter a Sentence :")
words = []

def my_split(input_sentence):

    curr = ""
    for char in input_sentence:
        if char == " ":
            words.append(curr)
            curr = ""
        else:
            curr += char

    if curr != "":
        words.append(curr)
    print(words)

def my_sort(words):

   n = len(words)
   for i in range(n):
       words[i] = words[i].lower()          #I had problem here as when i type a Uppercase letter in input sentence
                                            #it took Ascii value greater as Uppercase has higher Ascii. So i need to handle it by converting
                                            #all elements to lower case.

   for i in range(n):                       #I used bubble sort to sort all strings in list.
       for j in range(0,n-i-1):
           if words[j] > words[j+1]:
               words[j], words[j+1] = words[j+1], words[j]

   print words

def my_elementsort(words):
  new_words = []
  for word in words:
      n = len(word)
      char_list = []
      for i in range(0, n):
          char_list.append(word[i])

      for i in range(0,n):
          for j in range(0, n-i-1):
              if char_list[j] > char_list[j+1]:
                  char_list[j], char_list[j+1] = char_list[j+1], char_list[j]

      word = ''
      for i in range(0, n):
          word = word+char_list[i]
      new_words.append(word)

  print new_words


my_split(input_sentence)
my_sort(words)
my_elementsort(words)