import nltk
nltk.download('punkt')
text = "Hey How you doing"


from nltk.tokenize import sent_tokenize
sent_tokenize_list = sent_tokenize(text)
print("\nSentence tokenizer:")
print(sent_tokenize_list)


from nltk.tokenize import word_tokenize
print ("\nWord tokenizer:")
print (word_tokenize(text))

from nltk.tokenize import WordPunctTokenizer
WordPunctTokenizer().tokenize(text)
print ("\nPunkt word tokenizer:")
print (WordPunctTokenizer().tokenize(text))

from nltk.tokenize import WordPunctTokenizer
word_punct_tokenizer = WordPunctTokenizer()
print ("\nWord punct tokenizer:")
print (word_punct_tokenizer.tokenize(text))
