# biblegatewayPyAPI
Unofficial Python API for BibleGateway Implementation
by nardin

This API implements method for 

get_passage : search a specific passage (es. John 3:16)
params:
    passage: it explain itself
    version: es. ESV
    numeration: show verse number or not
    title: show passage title or not
output:
    dictionary(reference,version,text)


get_search_results : search specific words (es. Fruit Spirit)
params:
    search: words to search
    version: es. ESV
    searchype: Possible search type ALL, ANY, PHRASE
output:
    dictionary(reference,text)


getVOTD : show verse of the day
params:
    version: es. ESV
output:
    dictionary(reference,version,text)




Execution of Example.py


****** Result for passage John 3:1-15 ********
Reference :John 3:1-15
Version :ESV

You Must Be Born Again

3
Now there was a man of the Pharisees named Nicodemus, a ruler of the Jews. ²This man came to Jesus by night and said to him, “Rabbi, we know that you are a teacher come from God, for no one can do these signs that you do unless God is with him.” ³Jesus answered him, “Truly, truly, I say to you, unless one is born again he cannot see the kingdom of God.” ⁴Nicodemus said to him, “How can a man be born when he is old? Can he enter a second time into his mother's womb and be born?” ⁵Jesus answered, “Truly, truly, I say to you, unless one is born of water and the Spirit, he cannot enter the kingdom of God. ⁶That which is born of the flesh is flesh, and that which is born of the Spirit is spirit. ⁷Do not marvel that I said to you, ‘You must be born again.’ ⁸The wind blows where it wishes, and you hear its sound, but you do not know where it comes from or where it goes. So it is with everyone who is born of the Spirit.”⁹Nicodemus said to him, “How can these things be?” ¹⁰Jesus answered him, “Are you the teacher of Israel and yet you do not understand these things? ¹¹Truly, truly, I say to you, we speak of what we know, and bear witness to what we have seen, but you do not receive our testimony. ¹²If I have told you earthly things and you do not believe, how can you believe if I tell you heavenly things? ¹³No one has ascended into heaven except he who descended from heaven, the Son of Man. ¹⁴And as Moses lifted up the serpent in the wilderness, so must the Son of Man be lifted up, ¹⁵that whoever believes in him may have eternal life.


****** Result for searching Fruit Spirit ********
Reference: Galatians 5:22
Text: But the fruit of the Spirit is love, joy, peace, patience, kindness, goodness, faithfulness,
Reference: Isaiah 32:15
Text: until the Spirit is poured upon us from on high, and the wilderness becomes a fruitful field, and the fruitful field is deemed a forest.


****** Verse of the Day ********
Reference :Psalm 23:1-3
Version :ESV
The Lord is my shepherd; I shall not want.
    He makes me lie down in green pastures.
He leads me beside still waters.
    He restores my soul.
He leads me in paths of righteousness
    for his name's sake.


