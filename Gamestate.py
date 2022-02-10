class Gamestate:
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    def __init__(self):
        self.words = Gamestate.getWords("words.txt")
        self.unknown = list(range(5))
        self.guess = ""
        self.guesses = 0
    
    def nextGuess(self):
        guess = self.getBestWord()
        print("Guess: " + guess)
        status = [int(n) for n in input("Status: ")]

        for i, s in enumerate(status):
            if s == 0:
                updated_words = []

                for word in self.words:

                    for j, letter in enumerate(word):
                        if status[j] == 2 and letter == guess[i]:
                            updated_words.append(word)

                    if guess[i] not in word:
                        updated_words.append(word)

                self.words = updated_words

            elif s == 1:
                self.words = [word for word in self.words if word[i] == guess[i]]
                if i not in self.unknown:
                    self.unknown.remove(i)

            elif s == 2:
                self.words = [word for word in self.words if word[i] != guess[i] and guess[i] in word]

        
    def getBestWord(self):
        ratedLetters = self.rateLetters()
        return max(self.words, key=lambda word: self.rateWord(word, ratedLetters))

    def rateWord(self, word, scores):
        score = 0
        for letter, value in scores.items():
            if letter in "".join([l for i, l in enumerate(word) if i in self.unknown]):
                score += value
        return score

    def rateLetters(self):
        scores = dict.fromkeys(Gamestate.letters, 0)
        for word in self.words:
            for letter in word:
                scores[letter] += 1
        return scores

    @staticmethod
    def getWords(fileName):
        with open(fileName, "r") as file:
            return [word.strip() for word in file.readlines()]
            
    def start():
        print("started")
        
    def reset():
        print("reseted")
