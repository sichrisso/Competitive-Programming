def isPalindrome(self, s: str) -> bool:
      for i in s:
          if not i.isalnum():
              s= s.replace(i, '')
      s = s.lower()
      l = 0 
      r = len(s) - 1
      while l < r:
          if s[l] != s[r]:
              return False
          l += 1
          r -= 1
      return True
 def isPalindrome(self, s: str) -> bool:
      alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
      word = s.lower().split()
      palindrome = ''.join(word)
      i = 0

      # removing non-alphabetic char
      while i < len(palindrome):
          if palindrome[i] in alphabet:
              i += 1
          else:
             palindrome =  palindrome.replace(palindrome[i], '')

      # checking if ispalindrome
      l = 0 
      r = len(palindrome) - 1
      while l < r:
          if palindrome[l] == palindrome[r]:
              l += 1
              r -= 1
          else:
              return False
      return True
