import unittest
from buzz import generator

class Testing(unittest.TestCase):
  def test_sample_single_word(self):
    wordList = ('foo', 'bar', 'foobar')
    word = generator.sample(wordList)
    assert word in wordList

  def test_sample_multiple_words(self):
    wordList = ('foo', 'bar', 'foobar')
    words = generator.sample(wordList, 2)
    assert len(words) == 2
    assert words[0] in wordList
    assert words[1] in wordList
    assert words[0] is not words[1]

  def test_generate_buzz_of_at_least_five_words(self):
      phrase = generator.generate_buzz()
      assert len(phrase.split()) >= 5

if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()