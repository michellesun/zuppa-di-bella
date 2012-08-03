from bs4 import BeautifulSoup
import requests

def make_url_list(pin_num,pboard_url):
	if int(pin_num) % 50 != 0:
		page_num = int(pin_num) / 50 + 1
	else:
		page_num = int(pin_num) / 50
	url_list = [pboard_url]
	i = 2
	while i <= page_num:
		new_url = ( pboard_url+"?page=%d") %i
		url_list.append(new_url) 
		i += 1
	return url_list


pboard_url = "http://pinterest.com/michellelsun/beauty"
pinb = requests.get(pboard_url)
pinsoup = BeautifulSoup(pinb.content)
pin_num_div = pinsoup.find("div",{"id":"BoardStats"})
try: 
	pin_num = pin_num_div.contents[3].contents[0]
	print pin_num
except Exception,e: 
	pass #or print error
url_list = make_url_list(pin_num,pboard_url)
print url_list


