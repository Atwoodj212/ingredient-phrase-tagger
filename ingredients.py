from bs4 import BeautifulSoup
import constant
import json
import re
import nltk

recipe1 = open("recipe1.html", "r")

#Given HTML for Allrecipes website, returns list of ingredients w quantities + measurements
def findIngs(recipeWebpage):

    soup = BeautifulSoup(recipeWebpage, 'html.parser')
    scripts = []
    for script in soup.find_all('script'):
        if script.attrs == constant.JSONTYPE:
            scripts.append(script.contents)

    tag = str(scripts[0])
    json_text = re.search(r'(?<=recipeIngredient":)[^\]]*', tag)
    data = str(json_text[0])
    data = data.replace('"', '')
    data = data.replace('[', '')
    data = data.replace("  ", '')
    ingList = data.split('\\n')

    return ingList

def tagIngs(ingList):
    tokenized = []
    
    for ing in ingList:
        tokenized += nltk.word_tokenize(ing)
        
    
    return tokenized
    
    
ingredients = findIngs(recipe1)


for ing in ingredients:
    for word,pos in ing:
        if(pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
            print(word)
#print(tagIngs(ingredients))










# from html.parser import HTMLParser
# import json

# class MyHTMLParser(HTMLParser):
#     def __init__(self):
        
    
#     def handle_starttag(self, tag, attrs):
#         if tag == "script":
#             print ("Start tag:", tag)
#             for attr in attrs:
#                 print("    attr:", attr)
#     def handle_endtag(self, tag):
#         if tag == "/script":
#             print("End tag:    ", tag)
#     def handle_data(self, data):
#         #if(data.)
#         print("Data:       ", data)
# f = open("recipe1.html", "r")
# parser = MyHTMLParser()
# i = 0
# while i < 200:
#     parser.feed(f.readline())
#     i = i+1

