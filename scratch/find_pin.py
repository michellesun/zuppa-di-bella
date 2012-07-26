from bs4 import BeautifulSoup
import requests
from collections import Counter
from collections import Counter, defaultdict
from operator import itemgetter

def main():
	username = "triketora"
	board_url_list = []	
	board_list = find_board_list(username)
	renamed_list = transform_boardname(board_list)
	# print "BOARD LIST", renamed_list
	""" BOARD LIST / renamed_list 
	[u'fitness', u'beauty', u'home-sweet-home', u'words', u'sweetness',
 	u'wanderlust', u'fooodism', u'infographics', u'items', u'nature', 
 	u'love-in-the-bay', u'web-design', u'books ', u'demo-videos']
	"""
	for board in renamed_list: 
		# print find_board_url(username,board)
		if find_board_url(username, board) == None: 
			continue
		if len(find_board_url(username, board)) == 0:
			continue
		else:
			board_url_list.extend(find_board_url(username, board))
	# print "BOARD URL LIST", board_url_list
	"""BOARD URL LIST / board_url_list 
		[u'http://pinterest.com/michellelsun/fitness/', u'http://pinterest.com/michellelsun/beauty/', u'http://pinterest.com/michellelsun/beauty/?page=2', 
		u'http://pinterest.com/michellelsun/beauty/?page=3', 
		u'http://pinterest.com/michellelsun/home-sweet-home/', u'http://pinterest.com/michellelsun/home-sweet-home/?page=2', u'http://pinterest.com/michellelsun/words/', u'http://pinterest.com/michellelsun/words/?page=2', 
		u'http://pinterest.com/michellelsun/sweetness/', u'http://pinterest.com/michellelsun/wanderlust/', u'http://pinterest.com/michellelsun/fooodism/', u'http://pinterest.com/michellelsun/infographics/', 
		u'http://pinterest.com/michellelsun/items/', u'http://pinterest.com/michellelsun/nature/', u'http://pinterest.com/michellelsun/love-in-the-bay/', u'http://pinterest.com/michellelsun/web-design/', 
		u'http://pinterest.com/michellelsun/demo-videos/']
	"""
	pin_source_list = make_pin_source_list(board_url_list)
	"""pin_source_list 
		[u'yogurtyoga.tumblr.com', u'tumblr.com', u'loseweight-safe.com', 
		u'danceisuniversal.tumblr.com', u'dare-to-be-healthy.tumblr.com',
		u'fit-not-thin.tumblr.com', u'fitsugar.com', u'flickr.com', 
		u'migas.tumblr.com', u'tumblr.com', u'tumblr.com', u'tumblr.com', 
		u'theathenenoctua.tumblr.com', u'awelltraveledwoman.tumblr.com',
		u'fit-toned4summer.tumblr.com', u'youtube.com', u'tumblr.com', 
		u'sexydangerous.tumblr.com'...] 
		total length : 371 out of 461 total pins
	"""
	source_count = count_source(pin_source_list)
	print source_count

def find_board_list(username):
### find a list of boards by inserting username
	user_url = "http://pinterest.com/%s" %(username)
	u = requests.get(user_url)
	user_soup = BeautifulSoup(u.content)
	user_boards = user_soup.find_all("div", "pin pinBoard")
	board_list = []
	i = 0
	for item in user_boards:
		if user_boards[i] == None:
			continue
		else:
			name = user_boards[i].contents[1].contents[0].text
			board_list.append(name)
		i += 1
	return board_list

def transform_boardname(board_list):
### change names of boards with more than 1 word to link up with hyphens
### eg, "home sweet home" to "home-sweet-home"
	renamed_list = []
	for name in board_list:
		namelist = name.split()
		if len(namelist) > 1:
			name = '-'.join(namelist)
			renamed_list.append(name)
		else:
			renamed_list.append(name)
	return renamed_list
	""" board_list
			[u'fitness', u'beauty', u'home sweet home', u'words', u'sweetness', 
			u'wanderlust', u'fooodism', u'infographics', u'items', u'nature', 
			u'love in the bay', u'web design', u'books ', u'demo videos']
	"""
	""" renamed_board
			[u'fitness', u'beauty', u'home-sweet-home', u'words', u'sweetness', 
			u'wanderlust', u'fooodism', u'infographics', u'items', u'nature', 
			u'love-in-the-bay', u'web-design', u'books ', u'demo-videos']
	"""

def find_board_url(username, boardname):
	pboard_url = "http://pinterest.com/%s/%s/" %(username,boardname)
	pinb = requests.get(pboard_url)
	pinsoup = BeautifulSoup(pinb.content)
	pin_num_div = pinsoup.find("div",{"id":"BoardStats"})
	try: 
		pin_num = pin_num_div.contents[3].contents[0]
		url_list = make_url_list(pin_num,pboard_url)
		return url_list
	except Exception,e: 
		pass #or print error
### find url_list (page 1-2) by injecting boardname
"""
	['http://pinterest.com/michellelsun/beauty', 
	'http://pinterest.com/michellelsun/beauty?page=2', 
	'http://pinterest.com/michellelsun/beauty?page=3']
"""

def make_pin_source_list(url_list):
### now having the list of board url, get list of pins
	pin_source_list = []
	for url in url_list:
		try:
			new_pinb = requests.get(url)
			pinsoup = BeautifulSoup(new_pinb.content)
			pin_source = get_pin_source(pinsoup)
			pin_source_list.extend(pin_source)
		except Exception,e:
			pass
	print pin_source_list, len(pin_source_list)
	return pin_source_list

def make_url_list(pin_num,pboard_url):
### make URL in infinite scrolling 
### http://pinterest.com/michellelsun/beauty/?page=3
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

def get_pin_source(pinsoup):
### find sources of pins
	all_linked_pins = pinsoup.find_all("div","convo attribution clearfix")
	"""	an item in all_linked_pins
		<div class="convo attribution clearfix">
		<p class="NoImage">
		<a href="http://weheartit.com/entry/23003667" rel="nofollow" target="_blank">weheartit.com</a>
		</p>
		</div>
	"""
	pin_source = []
	""" error message 
		<type 'NoneType'>
		<class 'bs4.element.Tag'>
		<class 'bs4.element.Tag'>
		<class 'bs4.element.Tag'>
		<class 'bs4.element.Tag'>
		<class 'bs4.element.Tag'>
		<class 'bs4.element.Tag'>
		<class 'bs4.element.Tag'>
		<type 'NoneType'>
	"""
	# i = 0
	for item in all_linked_pins:
	 	if item.a == None:
			continue
		else:
			pin_source.append(item.a.contents[0])
		# i += 1
	# print "GET_PIN_SOURCE", pin_source
	return pin_source
	""" sample pin_source
		[u'thefancy.com', u'raspberryandred.blogspot.com', 
		u'rstyle.me', u'25.media.tumblr.com', u'mostbeautifull.net', 
		u'threadflip.com', u'rstyle.me', u'kingsunderlavenderskies.tumblr.com', 
		u'chrisanthemums.tumblr.com', u'laurenconrad.com', 
		u'whyilovetoshop.com', u'iknowhair.com', u'rstyle.me',
		 u'shopbop.com', u'community.boden.co.uk', u'zimbio.com', 
		 u'glamour.com', u'themessesofmen.tumblr.com']
	"""

def count_source(pin_source_list):
### feed all sources and generate a list of tuples with (count, domain)
	# count = pin_source_list.count
	# for source in pin_source_list:
	# 	## split by "."
	# 	domain = source.split(".")
	# source_count = [(count(item),item) for item in set(pin_source_list)]
	# source_count.sort()
	# source_count.reverse()
	# return source_count
	output = defaultdict(lambda: 0)
	for source in pin_source_list:
		try:
			domain = source.split(".")[-2]
			output[domain] += 1
		except IndexError:
			pass
	source_count = sorted(output.iteritems(),key=lambda (k,v): v,reverse=True)
	# print "source_count", sorted(output.iteritems(),key=lambda (k,v): v,reverse=True)
	return source_count


if __name__ == '__main__':
	main()

