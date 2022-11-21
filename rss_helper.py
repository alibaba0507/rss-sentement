'''
 use this for python 3.8 and lower to avoid 
 "TypeError: 'type' object is not subscriptable" because of  -> list[str] 
'''
from __future__ import annotations
from datetime import date, datetime,timedelta,timezone
import pytz
import feedparser
import dateutil.parser as parser
import pprint
import re

class RSSHelper:
    def __init__(self) -> None:
        return

    def get_rss_titles(self, rss_feed) -> list[str]:
        rss_feed = feedparser.parse(rss_feed)
        return [entry.title for entry in rss_feed.entries]

    def get_rss_links(self, rss_feed,beforeDays = 1) -> list[str]:
        current_time = datetime.now() - timedelta(days=beforeDays)
        #final time format
        format = "%Y-%m-%d %H:%M:%S.%f"

        #newformat = "%a, %d %b %Y %H:%M:%S %Z"
        newformat = "%Y-%m-%dT%H:%M:%SZ"
        new_current_time = datetime.strptime(str(current_time),format)
        #new_current_time = current_time.strptime(newformat)
        rss_feed = feedparser.parse(rss_feed)
     
        return [entry.link for entry in rss_feed.entries if datetime.strptime(entry.published,newformat) > new_current_time]

    def get_rss_source(self, rss_feed) -> list[str]:
        rss_feed = feedparser.parse(rss_feed)
        return [entry.source for entry in rss_feed.entries]
    
    def get_rss_descr(self, rss_feed) -> list[str]:
        rss_feed = feedparser.parse(rss_feed)
        return [entry.description for entry in rss_feed.description]    
    def get_posts_details(self,rss=None,beforeDays = 1,rssProp=None,searchFor=None) -> list[str]:
        if len(searchFor) == 0:
            searchFor = None
        current_time = datetime.now() - timedelta(days=int(beforeDays))
        #final time format
        format = "%Y-%m-%d %H:%M:%S.%f"

        #newformat = "%a, %d %b %Y %H:%M:%S %Z"
        newformat = "%Y-%m-%dT%H:%M:%SZ"
        new_current_time = datetime.strptime(str(current_time),format)
        pprint.pprint(new_current_time)
        date_time = parser.parse(str(current_time))
        pprint.pprint(date_time)
        #new_current_time = current_time.strptime(newformat)
        """
        Take link of rss feed as argument
        """
        if rss is not None:
            
            # import the library only when url for feed is passed
            #import feedparser
            #rss = rss.strip('\"')
            #rss = rss.strip("\'")
            # parsing blog feed
            blog_feed = blog_feed = feedparser.parse(rss)
              
            # getting lists of blog entries via .entries
            posts = blog_feed.entries
            pprint.pprint(blog_feed.feed)
            pprint.pprint(rss)
            # dictionary for holding posts details
            
            t = "NA"
            if blog_feed.feed.title:
                t = blog_feed.feed.title
            l = "NA"
            if blog_feed.feed.link:
                l = blog_feed.feed.link
            
            posts_details = {"Blog title" : "NA",
                            "Blog link" : "NA"}
              
            post_list = []
              
            # iterating over individual posts
            for post in (post for post in posts if parser.parse(post.published).replace(tzinfo=timezone.utc) > current_time.replace(tzinfo=timezone.utc)):
                temp = dict()
                  
                # if any post doesn't have information then throw error.
                try:
                    if rssProp is None:
                        temp["title"] = post.title
                        temp["link"] = post.link
                        temp["author"] = post.author
                        temp["time_published"] = post.published
                        temp["tags"] = [tag.term for tag in post.tags]
                        temp["authors"] = [author.name for author in post.authors]
                        temp["summary"] = post.summary
                        temp["description"] = post.description
                    elif rssProp.lower() == "description" and searchFor is None or searchFor is not None and re.search(searchFor.lower(),post.description.lower()):
                        temp["description"] = post.description
                    elif rssProp.lower() == "summary" and searchFor is None or searchFor is not None and re.search(searchFor.lower(),post.summary.lower()):
                        temp["summary"] = post.summary
                    elif rssProp.lower() == "title" and searchFor is None or searchFor is not None and re.search(searchFor.lower(),post.title.lower()):
                        temp["title"] = post.title
                    else:
                        continue
                except:
                    pass
                  
                post_list.append(temp)
              
            # storing lists of posts in the dictionary
            posts_details["posts"] = post_list 
              
            return posts_details # returning the details which is dictionary
        else:
            return None
        
