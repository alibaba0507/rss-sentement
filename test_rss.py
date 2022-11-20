import pprint
import spacy
from rss_helper import RSSHelper
from html_parser import HTML_Parser
from sentiment import Sentiment
#import en_core_web_sm

rss_feed = 'https://finance.yahoo.com/news/rssindex'

rsh = RSSHelper()
links = rsh.get_rss_links(rss_feed)
pprint.pprint(links[0])
parser = HTML_Parser()
'''
 This range [0:1] is just for test
'''
text_content = [parser.extract_text_from_single_web_page(url) for url in links[0:1]]
cleaned_textual_content = [text for text in text_content if str(text) != 'nan']

s  = Sentiment()
[s.sentiment_scores(t) for t in cleaned_textual_content]
pprint.pprint(cleaned_textual_content[0])