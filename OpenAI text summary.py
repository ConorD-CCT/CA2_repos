# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 21:55:45 2023

@author: cdillon
"""
'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'
'../CA2/Annual Review and Outlook for Agriculture, Food and the Marine 2022.pdf'

# import openai
# from getpass import getpass
# openai.api_key = getpass()


# prompt = "I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\". Q: Who is the greatest investor of all time?\n\n"
# engine = 'text-davinci-003'
# response = openai.Completion.create(
#   engine=engine, 
#   prompt=prompt,
#   temperature=0.3, # The temperature controls the randomness of the response, represented as a range from 0 to 1. A lower value of temperature means the API will respond with the first thing that the model sees; a higher value means the model evaluates possible responses that could fit into the context before spitting out the result.
#   max_tokens=140,
#   top_p=1, # Top P controls how many random results the model should consider for completion, as suggested by the temperature dial, thus determining the scope of randomness. Top P’s range is from 0 to 1. A lower value limits creativity, while a higher value expands its horizons.
#   frequency_penalty=0,
#   presence_penalty=1
# )

# print(response)

import openai
import PyPDF2
import numpy as np

# Set the OpenAI API key
openai.api_key = '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'

# Open the PDF file
with open('../CA2/Annual Review and Outlook for Agriculture, Food and the Marine 2022.pdf', "rb") as file:
    # Create a PDF object
    pdf = PyPDF2.PdfReader(file)
    
    # Extract the text from the PDF
    text = ""
    for page in range(len(pdf.pages)):
        text += pdf.pages[page].extract_text()


words = text.split(" ")

chunks = np.array_split(words,70)

for i in range(len(chunks)):
    chunks[i] = ' '.join(list(chunks[i]))


#chunkNum = chunks[0]
summaryAll = []
for chunkNum in chunks:

    # Use the TLDR model to summarize the text
    model_engine = "text-davinci-002"
    prompt = (f"{chunkNum}\n\ntl;dr:")
    
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    # Print the summary
    summary = completions.choices[0].text
    print(summary)
    summaryAll.append(summary)
    
#%%
import nltk
import pandas as pd
import textblob
import statistics

sentences = summaryAll


# Remove stopwords from the sentences
stopwords = nltk.corpus.stopwords.words('english')
filtered_sentences = []
for sentence in sentences:
  words = nltk.word_tokenize(sentence)
  filtered_words = [word for word in words if word.lower() not in stopwords]
  filtered_sentence = " ".join(filtered_words)
  filtered_sentences.append(filtered_sentence)





# Get the sentiment scores for each sentence
scores = []
scoresDF = pd.DataFrame()
for sentence in sentences:
  sentiment = textblob.TextBlob(sentence).sentiment.polarity
  scores.append(sentiment)
scoresDF['Sentences'] = sentences
scoresDF['Scores'] = scores

avgSentiment = statistics.mean(scoresDF['Scores'])
    

