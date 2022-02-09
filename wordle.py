def getLetters(words):
    letters = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

    for word in words:
        for letter in word:
            letters[letter] += 1

    return [item[0] for item in sorted(letters.items(), key=lambda item:item[1])]

def rateWord(word, letters):
    score = 0
    for i, letter in enumerate(letters):
        for l in word:
            if letter == l:
                score += i
    
    return (word, score)


def getSortedWords(wordList):
    letters = getLetters(wordList)
    return sorted([rateWord(word, letters) for word in wordList], key=lambda word: word[1], reverse=True)

guess = input("Guess: ")
words = []

with open("words.txt") as f:
    words = [word.strip() for word in f.readlines()]


while True:
    for i in range(5):
        status = int(input("Letter " + str(i) + ": "))

        words_updated = []

        if status == 0:
            for word in words:
                if guess[i] not in word:
                    words_updated.append(word)

        elif status == 1:
            for word in words:
                if word[i] == guess[i]:
                    words_updated.append(word)

        elif status == 2:
            for word in words:
                if word[i] != guess[i] and guess[i] in word:
                    words_updated.append(word)

        words = words_updated
    
    print(getSortedWords(words))

    if input("Again? ").lower() != "y":
        break

    guess = input("Guess: ")
