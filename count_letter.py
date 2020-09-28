def count() :
    word = input("Please enter a word: ")
    letter = input("Please enter a letter: ")
    count = 0
    for iletter in word:
        if iletter == letter:
            count = count + 1
    print('"',word,'"','has',count,'"',letter,'"')
count()
