## change from letters to letter placement for rating

def rateLetters(words, letters):
    scores = dict.fromkeys(letters, 0)
    for word in words:
        for letter in word:
            if letter in letters:
                scores[letter] += 1

    return scores

def rateWord(word, letters):
    score = 0
    for letter, value in letters.items():
        if letter in word:
            score += value
    
    return score


def getSortedWords(words, letters):
    letters = rateLetters(words, letters)
    return sorted(words, key=lambda word: rateWord(word, letters), reverse=True)

def getBestWord(words, letters):
    letters = rateLetters(words, letters)
    return max(words, key=lambda word: rateWord(word, letters))

with open("words.txt") as f:
    words = [word.strip() for word in f.readlines()]

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for _ in range(6):
    guess = getBestWord(words, letters)
    print("Guess: " + guess)

    status = [int(i) for i in input("Staus: ")]
    
    if status == [1, 1, 1, 1, 1]:
        print("Yay!")
        break

    for i, s in enumerate(status):
        if s == 0:
            updated_words = []

            for word in words:

                for j, letter in enumerate(word):
                    if status[j] == 2 and letter == guess[i]:
                        updated_words.append(word)

                if guess[i] not in word:
                    updated_words.append(word)

            words = updated_words

        elif s == 1:
            words = [word for word in words if word[i] == guess[i]]
            try:
                letters.remove(guess[i])
            except ValueError:
                pass

        elif s == 2:
            words = [word for word in words if word[i] != guess[i] and guess[i] in word]
