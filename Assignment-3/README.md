The data file Corona_NLP_test.csv contains tweets that have been pulled from Twitter.  

In this dataset used the text data in the “OriginalTweet” column and performed the following:

a) Convert the text corpus into tokens. 

- Tokenized the text corpus by splitting it into individual words using the word_tokenize() function from NLTK.

b) Perform stop word removal. 

- Defined a function clean_str() to remove special characters from each token.
- Loaded the stop words for the English language using stopwords.words('english'). 
- Iterated over the tokens and applied the clean_str() function to each token. 
- Removed tokens that are in the stop words list or are not alphabetic.

c) Count Word frequencies 
- Use the Counter() function from collections module to count the frequencies of each token in the cleaned token list.

d) Create word clouds. 
- Created a WordCloud object with a white background. 
- Generated the word cloud visualization from the word frequencies using generate_from_frequencies().