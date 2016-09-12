import api.biblegateway_api

bg_api = api.biblegateway_api

#get a passage from Bible
result = bg_api.get_passage("john 3:1-15")

"""
Rules for parsing:
    Chapters are surrounded by # (ex #3#)
    Paragraph Title are surrounded by * (ex. *For God So Loved the World*)
"""
print("****** Result for passage John 3:1-15 ********")
print("Reference :"+result['reference'])
print("Version :"+result['version'])

#breaks on windows command line.
try: print(result['text'].replace('*', '\n\n').replace('#', '\n'))
except UnicodeEncodeError:
	#I need to find the best way to convert this. 
    print("UnicodeEncodeError.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

#search result in bible getting a dictionary (reference,text)
results = bg_api.get_search_result("Fruit Spirit")

print("\n\n****** Result for searching Fruit Spirit ********")
for (reference, text) in list(results.items()):
    print("Reference: "+reference)
    print("Text: "+text)


#get verse of the day
result = bg_api.getVotd()
print("\n\n****** Verse of the Day ********")
print("Reference :"+result['reference'])
print("Version :"+result['version'])
print(result['text'])