def word_count(text):
  """Counts the frequency of words in a given text.

  Args:
    text: The input text.

  Returns:
    A dictionary containing word frequencies.
  """

  words = text.split()
  word_count = {}
  for word in words:
    word_count[word] = word_count.get(word, 0) + 1
  return word_count

# Example usage:
text = "This is a sample text. This text is for testing word count."
result = word_count(text)
print(result)