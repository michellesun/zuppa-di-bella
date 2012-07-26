import requests

p = requests.get("http://pinterest.com/ohjoy/oh-baby/")
r = requests.get("http://www.etsy.com/listing/102135880/rainbow-summer-chevron-stripes-pride")

print "pinterest", p.content
# print "TEXT", r.text[0]

# print "JSON", r.json

# print "Status", r.status_code

# print "headers", r.headers

# {'content-length': '19048', 
# 'content-encoding': 'gzip', 
# 'set-cookie': 'etala=111461200.1692878.1343169672.1343169672.1343169672.1.0; expires=Fri, 25-Jul-2014 10:18:44 GMT; path=/; domain=.etsy.com, etalb=111461200.1.10.1343169672; expires=Tue, 24-Jul-2012 23:11:12 GMT; path=/; domain=.etsy.com, last_browse_page=http%3A%2F%2Fwww.etsy.com%2Fshop%2FModernSwitch; path=/; domain=.etsy.com, uaid=uaid%3Dw-JOp8JpO_zdGpyVG4gkaim8h7oN%26_now%3D1343169672%26_slt%3D-HA8dkJk%26_kid%3D1%26_ver%3D1%26_mac%3DsQ2IdIZSic9JN98L3NKd1-z8PcCw9APv0b3tL37Nv0U.; expires=Thu, 24-Jul-2014 22:41:12 GMT; path=/; domain=.etsy.com; httponly, autosuggest_split=1; expires=Wed, 25-Jul-2012 22:41:12 GMT; path=/; domain=.etsy.com, user_prefs=1&2596706699&q0tPzMlJLaoEAA==; expires=Wed, 24-Jul-2013 22:41:12 GMT; path=/; domain=.etsy.com', 
# 'expires': 'Thu, 19 Nov 1981 08:52:00 GMT', 
# 'vary': 'Accept-Encoding', 
# 'x-cnection': 'close', 
# 'server': 'Apache', 
# 'connection': 'keep-alive', 
# 'pragma': 'no-cache', 
# 'cache-control': 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0', 
# 'date': 'Tue, 24 Jul 2012 22:41:12 GMT', 
# 'content-type': 'text/html; charset=UTF-8'}

