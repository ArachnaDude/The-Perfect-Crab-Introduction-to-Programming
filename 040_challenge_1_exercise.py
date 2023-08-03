# Video alternative: https://youtu.be/qDWyR0XpJtQ&t=1295s

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
  ten_plus = filter_ten_or_longer(words)
  not_hyphenated = filter_hyphen(ten_plus)
  trimmed_and_ellipsis = shorten_fifteen_plus(not_hyphenated)
  return format_results(trimmed_and_ellipsis)



def filter_ten_or_longer(words):
  passing_words = []
  for word in words:
    if len(word) >= 10:
      passing_words.append(word)
  print(passing_words)
  return passing_words

def filter_hyphen(words):
  passing_words = []
  for word in words:
    if "-" not in word:
      passing_words.append(word)
  print(passing_words)
  return passing_words

def shorten_fifteen_plus(words):
  passing_words = []
  for word in words:
    if len(word) > 15:
      passing_words.append(f"{word[0:15]}...")
    else:
      passing_words.append(word)
  print(passing_words)
  return passing_words

def format_results(words):
  list_length = len(words)
  str = "These words are quite long: "
  for i in range(list_length):
    if i == list_length -1 :
      str += words[i]
    else:
      str += f"{words[i]}, "
  return str

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
