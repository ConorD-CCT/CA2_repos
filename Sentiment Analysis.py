import io
import re
import nltk
import textblob
import PyPDF2
import statistics
import pandas as pd

def get_sentiment_scores(pdf_path):
  # Open the PDF file and extract the text
  with open(pdf_path, 'rb') as f:
    pdf_reader = PyPDF2.PdfReader(f)
    text = ""
    for page in range(len(pdf_reader.pages)):
      text += pdf_reader.pages[page].extract_text()
  
  # Split the text into sentences
  sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
  sentences = sent_detector.tokenize(text)
  
  
  # Remove stopwords from the sentences
  stopwords = nltk.corpus.stopwords.words('english')
  # stopwords = ['the','of','a','or','at','in','for']

  filtered_sentences = []
  for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    filtered_words = [word for word in words if word.lower() not in stopwords]
    filtered_sentence = " ".join(filtered_words)
    filtered_sentences.append(filtered_sentence)
  
  
  
  
  
  # Get the sentiment scores for each sentence
  scores = []
  scoresDF = pd.DataFrame()
  for sentence in filtered_sentences:
    sentiment = textblob.TextBlob(sentence).sentiment.polarity
    scores.append(sentiment)
  scoresDF['Sentences'] = filtered_sentences
  scoresDF['Scores'] = scores
    

  return statistics.mean(scores),scoresDF

meanScores, df = get_sentiment_scores('../CA2/Annual Review and Outlook for Agriculture, Food and the Marine 2022.pdf')

