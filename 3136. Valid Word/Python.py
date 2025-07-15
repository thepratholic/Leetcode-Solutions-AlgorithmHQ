# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def isValid(self, word: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        if not word or len(word) < 3: # invalid case
            return False

        vowel = False
        consonant = False

        for ch in word:
            if not ch.isalnum(): # if other char is there apart from alpha-numeric
                return False

            if ch.isalpha():
                if ch in vowels:  # if it iis vowel then it's True
                    vowel = True

                else:
                    consonant = True # else it is consonant

        return vowel and consonant # return True if both are True else False