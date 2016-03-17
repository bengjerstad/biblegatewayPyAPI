import json
import urllib2
import re
import configparser
import logging
from bs4 import BeautifulSoup

#Importing configuration params
config = configparser.ConfigParser()
config.read('api/biblegateway_api.cfg')

urls = config['URL']
defaults = config['DEFAULT']
EMPTY = defaults['empty_message']
default_version = defaults['version']

def strip_markdown(string):
    return string.replace('*', '').replace('_', '').replace('`', '')

"""
Search a specific passage (es. John 3:16)
params:
    passage: it explain itself
    version: es. ESV
    numeration: show verse number or not
    title: show passage title or not
output:
    dictionary(reference,version,text)
"""
def get_passage(passage, version=default_version, numeration=True, title=True):

    def to_sup(text):
        sups = {u'0': u'\u2070',
                u'1': u'\xb9',
                u'2': u'\xb2',
                u'3': u'\xb3',
                u'4': u'\u2074',
                u'5': u'\u2075',
                u'6': u'\u2076',
                u'7': u'\u2077',
                u'8': u'\u2078',
                u'9': u'\u2079',
                u'-': u'\u207b'}
        return ''.join(sups.get(char, char) for char in text)

    BG_URL = urls['passage']

    search = urllib2.quote(passage.lower().strip())
    url = BG_URL.format(search, version)

    try:
      result = urllib2.urlopen(url)
    except urllib2.URLError, e:
      logging.warning('Error fetching passage:\n' + str(e))

    html = result.read()
    soup = BeautifulSoup(html, 'lxml').select_one('.passage-text')

    if not soup:
        return EMPTY

    WANTED = 'bg-bot-passage-text'
    UNWANTED = '.passage-display, .footnote, .footnotes, .crossrefs, .publisher-info-bottom'

    if not numeration:
        UNWANTED += ', .chapternum, .versenum'
    if not title:
        UNWANTED += ', h1, h2, h3, h4, h5, h6'


    title = soup.select_one('.passage-display-bcv').text
    reference = strip_markdown(title.strip())

    for tag in soup.select(UNWANTED):
        tag.decompose()

    for tag in soup.select('h1, h2, h3, h4, h5, h6'):
        tag['class'] = WANTED
        text = tag.text.strip().replace('\\', ' ')
        tag.string = '*' + strip_markdown(text) + '*'

    needed_stripping = False

    for tag in soup.select('p'):
        tag['class'] = WANTED
        bad_strings = tag(text=re.compile('(\*|\_|\`)'))
        for bad_string in bad_strings:
            stripped_text = strip_markdown(unicode(bad_string))
            bad_string.replace_with(stripped_text)
            needed_stripping = True

    if needed_stripping:
        logging.info('Stripped markdown')

    for tag in soup.select('br'):
        tag.name = 'span'
        tag.string = '\n'

    for tag in soup.select('.chapternum'):
        num = tag.text.strip()
        if numeration:
            tag.string = '#' + strip_markdown(num) + '#'
        else:
            tag.string = ''

    for tag in soup.select('.versenum'):
        num = tag.text.strip()
        tag.string = to_sup(num)

    for tag in soup.select('.text'):
        tag.string = tag.text.rstrip()

    final_text = ''
    for tag in soup(class_=WANTED):
        final_text += tag.text.strip()

    return {'reference': reference, 'version': version, 'text': final_text.strip()}


"""
Search specific words (es. Fruit Spirit)
params:
    search: words to search
    version: es. ESV
    searchype: Possible search type ALL, ANY, PHRASE
output:
    dictionary(reference,text)
"""

def get_search_result(search, version=default_version, searchtype='ALL'):

    BG_URL = urls['search']

    search = search.strip().replace(' ', '+')

    url = BG_URL.format(search, version, searchtype)

    try:
      result = urllib2.urlopen(url)
    except urllib2.URLError, e:
      logging.warning('Error fetching passage:\n' + str(e))

    html = result.read()
    soup = BeautifulSoup(html, 'lxml').select_one('.search-result-list')

    if not soup:
        return EMPTY

    WANTED = ''
    UNWANTED = '.bible-item-extras '

    list_results = {}

    for tag in soup.select(UNWANTED):
        tag.decompose()

    for item in soup.select('.bible-item'):

        tag_title = item.select_one('.bible-item-title')

        tag_text = item.select_one('.bible-item-text')
        text = tag_text.text.strip().replace('\\', ' ')
        tag_text.string = strip_markdown(text)

        list_results[tag_title.string] = tag_text.string


    return list_results

"""
Show verse of the day
params:
    version: es. ESV
output:
    dictionary(reference,version,text)
"""
#Verse of the day multi version implementation
def getVotd(version=default_version):

    url = urls['votd']
    response = urllib2.urlopen(url)
    data = json.loads(response.read())

    return {'reference': data['votd']['reference'], 'version': version, 'text': get_passage(data['votd']['reference'], version=default_version, numeration=False, title=False)['text']}