# from newspaper import Article
# import random
# import string
# import nltk
# from sklearn.feature_extraction import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np
# import warnings
# warnings.filterwarnings("ignore")


# #Download punkt package
# # nltk.download("punkt")

# #Get articles
# article1 = Article("https://www.infoworld.com/article/3204016/what-is-python-powerful-intuitive-programming.html")
# article1.download()
# article1.parse()
# article1.nlp()
# corpus1 = article1.text

# article2 = Article("https://www.infoworld.com/article/3204016/what-is-python-powerful-intuitive-programming.html?page=2")
# article2.download()
# article2.parse()
# article2.nlp()
# corpus2 = article2.text

# text = corpus1 + corpus2

# #Tokenization
# sentence_list = nltk.sent_tokenize(text) # A list of sentences

# def index_sort(list_var):
#     length = len(list_var)
#     list_index = list(range(0, length))
    
#     x = list_var
#     for i in range(length):
#         for j in range(length):
#             if x[list_index[i]] > x[list_index[j]]:
#                 #Swap
#                 temp = list_index[i]
#                 list_index[i] = list_index[j]
#                 list_index[j] = temp
                
#     return list_index


# #function to return a random greeting response to users greeting
# def greeting_response(text):
#     text = text.lower()
    
#     #bot greeting respnses
#     bot_greetings = ["hello there", "hi", "hey", "good day to you, sir", "sup", "how do you do?"]
#     #user greetings
#     user_greetings = ["hello there", "hi", "hey", "good day to you, sir", "sup", "how do you do?", "hello", "hola", "wassup"]
    
#     for word in text.split():
#         if word in user_greetings:
#             return random.choice(bot_greetings)
        

# #create bots response
# def bot_response(user_input):
#     user_input = user_input.lower()
#     sentence_list.append(user_input)
#     bot_response = ""
#     cm = CountVectorizer().fit_transform(sentence_list)
#     similarity_scores = cosine_similarity(cm[-1], cm)
#     similarity_scores_list = similarity_scores.flatten()
#     index = index_sort(similarity_scores_list)
#     index = index[1:]
#     response_flag = 0
    
    