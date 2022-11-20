import pprint
from rss_helper import RSSHelper
from html_parser import HTML_Parser

rss_feed = 'https://finance.yahoo.com/news/rssindex'

rsh = RSSHelper()
links = rsh.get_rss_links(rss_feed)
pprint.pprint(links[0])
parser = HTML_Parser()
'''
 This range [0:1] is just for test
'''
text_content = [parser.extract_text_from_single_web_page(url) for url in links[0:1]]
pprint.pprint(text_content[0])