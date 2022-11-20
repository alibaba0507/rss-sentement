'''
 use this for python 3.8 and lower to avoid 
 "TypeError: 'type' object is not subscriptable" because of  -> list[str] 
'''
from __future__ import annotations
from datetime import date, datetime,timedelta
import feedparser

class RSSHelper:
    def __init__(self) -> None:
        return

    def get_rss_titles(self, rss_feed) -> list[str]:
        rss_feed = feedparser.parse(rss_feed)
        return [entry.title for entry in rss_feed.entries]

    def get_rss_links(self, rss_feed,beforeDays = 1) -> list[str]:
        current_time = datetime.now() - timedelta(days=beforeDays)
        #final time format
        format = "%Y-%m-%d %H:%M:%S.%S"

        newformat = "%a, %d %b %Y %H:%M:%S %Z"
        new_current_time = datetime.strptime(str(current_time),format)
        #new_current_time = current_time.strptime(newformat)
        rss_feed = feedparser.parse(rss_feed)
     
        return [entry.link for entry in rss_feed.entries if datetime.strptime(entry.published,newformat) > new_current_time]

    def get_rss_source(self, rss_feed) -> list[str]:
        rss_feed = feedparser.parse(rss_feed)
        return [entry.source for entry in rss_feed.entries]
        
    def get_posts_details(self,rss=None):
    
        """
        Take link of rss feed as argument
        """
        if rss is not None:
            
            # import the library only when url for feed is passed
            #import feedparser
              
            # parsing blog feed
            blog_feed = blog_feed = feedparser.parse(rss)
              
            # getting lists of blog entries via .entries
            posts = blog_feed.entries
              
            # dictionary for holding posts details
            posts_details = {"Blog title" : blog_feed.feed.title,
                            "Blog link" : blog_feed.feed.link}
              
            post_list = []
              
            # iterating over individual posts
            for post in posts:
                temp = dict()
                  
                # if any post doesn't have information then throw error.
                try:
                    temp["title"] = post.title
                    temp["link"] = post.link
                    temp["author"] = post.author
                    temp["time_published"] = post.published
                    temp["tags"] = [tag.term for tag in post.tags]
                    temp["authors"] = [author.name for author in post.authors]
                    temp["summary"] = post.summary
                    temp["description"] = post.description
                except:
                    pass
                  
                post_list.append(temp)
              
            # storing lists of posts in the dictionary
            posts_details["posts"] = post_list 
              
            return posts_details # returning the details which is dictionary
        else:
            return None
        