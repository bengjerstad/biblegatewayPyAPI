import api.biblegateway_api
import sys
import json
import sqlite3
import time

#make dbfile
conn = sqlite3.connect('esv.db')
c = conn.cursor()


bg_api = api.biblegateway_api

with open('esvverse_counts.json') as data_file:    
    data = json.load(data_file)

for books in data:
	verselist = data[books]
	print(books)
	#new table for each book
	try:
		c.execute("Create Table '"+books+"' (chapter text,verse text,text text)")
	except:
		1
	conn.commit()
	time.sleep(5)
	for chapter,verses in enumerate(verselist):
		#time.sleep(1)
		for verse in range(verses):
			#already in db?
			c.execute("SELECT * FROM '"+books+"' WHERE chapter='"+str(chapter)+"' AND verse='"+str(verse)+"' ")
			find = c.fetchone()
			if (find is None):
				search = books+" "+str(chapter+1)+":"+str(verse+1)
				print(search)

				result = bg_api.get_passage(search,numeration=False, title=False)
				#result = search
				if result == 'empty':
					print(result)
				else:
					result = result['text']
					print(result)
					c.execute("INSERT INTO '"+books+"' VALUES (?,?,?)",(str(chapter),str(verse),result))
					conn.commit()
					time.sleep(.5)

			

