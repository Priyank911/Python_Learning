def ispalindrome(a):
  if a==a[::-1]:
    print("{} is palindrome".format(a))
  else:
    print("{} is not palindrome".format(a))
ispalindrome("parul")
ispalindrome("nitin")