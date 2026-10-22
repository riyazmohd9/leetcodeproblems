class Solution(object):

  def numberOfSpecialChars(self, word):
    """:type word: str

    :rtype: int
    """
    count = 0
    # Check all lowercase letters from 'a' to 'z'
    for c in range(ord('a'), ord('z') + 1):
      lower_char = chr(c)
      upper_char = chr(c).upper()

      # If both lowercase and uppercase exist in the word
      if lower_char in word and upper_char in word:
        count += 1

    return count