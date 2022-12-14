# Emotion Based Emoji Suggestion
## About
Usually chat services suggest emojis based on the literal meaning of the last word in a text message instead of taking the whole message into account, an alternative and better way is to have it suggest an emoji based on the emotion of the full text or conversation.  
The emotions considered in this project are: joy😃 fear😱 sadness😢 anger😡 surprise😯 love🥰
## Dataset
Three datasets were used 
1. <a href="https://www.clarin.si/repository/xmlui/handle/11356/1048">Emoji Sentiment Ranking</a>
2. <a href="https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp?resource=download&select=val.txt">Emotions dataset for NLP</a>
3. <a href="https://www.kaggle.com/datasets/rexhaif/emojifydata-en?select=emojitweets-01-04-2018.txt">EmojifyData-EN: English tweets, with emojis</a>
## Process
1. Use transformers for emotion classification of text
2. Use tweets as input for transfer learning
3. After finding the emotions of tweets, classify emojis by emotion creating a -tweet, emoji, emotion- dataset
4. Merge the newly created dataset with <a href="https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp?resource=download&select=val.txt">the emotions dataset for NLP</a>
5. Create a random forest model that takes text messages and suggests an emoji
## Limitations
1. Only 25 unique emojis 
## Future work
1. Add the ability to process a full conversation
2. Use a larger and more comprehensive (text – emotion – emoji) dataset to add to the 25 emojis
3. Train a deep learning model and compare results 

## Interface 
<img src="data\interface.png"> 

