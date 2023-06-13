import random
import keyboard
import time

CORRECTSHIFT = 1
WRONGSHIFT = int(input('Enter number of extra word re-iterations per misremembrance: '))

PAUSELENGTH = int(input('Enter flashcard delay in seconds: '))

allmastered = False

DicFile = open('grewords.txt', 'r')

entries = DicFile.readlines()

DicFile.close()

n = len(entries)

class word:
    def __init__(self, string = ':'):
        if string.count(':') != 1:
            print('Invalid entry, "' + string + '"')
        [self.value, self.meaning] = string.split(': ')
        self.showagain = 0
        self.ismastered = False
    def display(self):
        print(self.value)
        time.sleep(PAUSELENGTH/2)
        print('... means ...')
        time.sleep(PAUSELENGTH/2)
        print(self.meaning)
    def gotright(self):
        self.showagain -= CORRECTSHIFT
        if self.showagain < 0:
            self.ismastered = True
    def gotwrong(self):
        self.showagain += WRONGSHIFT
    
wordlist = []

for i in range(n):
    currentword = word(entries[i])
    wordlist.append(currentword)

print('\n')

while not allmastered:
    currentwordno = random.randint(0, n-1)
    if wordlist[currentwordno].ismastered:
        continue
    wordlist[currentwordno].display()
    print('Did you know that? (Press Y/N)')
    ans = keyboard.read_key()
    #ans = input()[0]
    if ans == 'y' or ans == 'Y':
        wordlist[currentwordno].gotright()
        print('y')
    else:
        wordlist[currentwordno].gotwrong()
        print('n')
    allmastered = True
    numMastered = 0
    for w in wordlist:
        if w.ismastered:
            numMastered+=1
        else:
            allmastered = False
    print('\n\n' + str(numMastered) + ' out of ' + str(n) + ' words mastered.\n\n')

input('Congrats, you\'ve mastered all of the things.')
