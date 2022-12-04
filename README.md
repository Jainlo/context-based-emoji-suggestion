# Context Based Emoji Suggestion
## About
Usually chat services suggest emojis based on the literal meaning of a word, an alternative and better way is to have it suggest an emoji based on the context or emotion of the conversation. So instead of classifying text as positive, neutral or negative, the model should classify text based on the following emotions (joy, fear, sadness, anger, surprise, love). each emotion is associated with different emojis - The process and analysis of emoji sentiment ranking is described in the paper: Kralj Novak P, Smailović J, Sluban B, Mozetič I (2015) Sentiment of Emojis. PLoS ONE 10(12): e0144296. 
doi:10.1371/journal.pone.0144296 
http://hdl.handle.net/11356/1048.
## Dataset
Two datasets were used 
1. <a href="https://www.clarin.si/repository/xmlui/handle/11356/1048">Emoji Sentiment Ranking</a>
2. <a href="https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp?resource=download&select=val.txt">Emotions dataset for NLP</a>
### merged into one dataset
| Sentence      | Label         | Emoji         |
| ------------- | ------------- | ------------- |
| i didnt feel  | sadness       |               |
| i am ever fe  | joy           |               |
## Process
1. Train the model to classify text based on labels
2. Each label forms a cluster of emojis
3. The final emoji suggestion is the centroid of the clusterSS

