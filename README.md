# rss-sentement
 rss-sentement
 Read rss parse and examine the sentement
 
 Python Api:  Sentements of forex rss news:
user input: 
 startDate: if null : today
 endDate: if null: today - 1d
 pairs: ["GBPUSD","EURUSD" ,...] if null => ["GBPUSD","EURUSD","USDJPY"]
 rss: [] if null ["http://actionforex"]
 
 return {pair:{"GBPUSD":{"NEG":0.0,"POS":0.0,"OVERALL":0.0}
				,{"EURUSD":{....}}
			}
		}