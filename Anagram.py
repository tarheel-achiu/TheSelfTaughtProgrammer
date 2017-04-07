# determine if two words are anagrams by
# sorting the letters in each word alphabetically and testing
# if they are the same

def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)

print(anagram("iceman", "cinema"))
print(anagram("leaf", "tree"))
