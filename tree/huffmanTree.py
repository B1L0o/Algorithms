def getFrequency(word):
    freq = {} 
    for letter in word:
        freq[letter] = 1 if letter not in word else freq[letter]+1
    return freq
