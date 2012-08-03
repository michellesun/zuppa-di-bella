from bs4 import BeautifulSoup
import requests
import traceback

def main():
	soup = get_soup("http://pinterest.com/ohjoy/oh-baby/")
	noimage = get_image(soup)
	link_list = get_link_list(noimage) # not sure where this fits
	for link in link_list:
		etsy_soup = get_soup(link)
		etsy_links = get_etsy(etsy_soup)
	etsy_pinobjects = []
	for link in etsy_links:
		print link
		try:
			etsy_pin = Pin(link)
			etsy_pinobjects.append(etsy_pin)
		except Exception, e:
			traceback.print_exc()
	# return etsy_pinobjects
	pin = Pin("http://www.etsy.com/listing/102135880/rainbow-summer-chevron-stripes-pride")
	return pin.title, pin.image_link, pin.pdt_link, pin.price

	""" pinobj 
		[<__main__.Pin object at 0x10ac10450>, <__main__.Pin object at 0x10ac99550>,
		<__main__.Pin object at 0x10ad247d0>, <__main__.Pin object at 0x10adafa50>,
		<__main__.Pin object at 0x10ae3fb50>, <__main__.Pin object at 0x10ae77e10>,
		<__main__.Pin object at 0x10aed6150>, <__main__.Pin object at 0x10af5e790>,
		<__main__.Pin object at 0x10ae3f910>, <__main__.Pin object at 0x10ad8e050>]
	"""
	# amzn_soup = get_soup("http://www.amazon.com/dp/0307888908/?ref=cm_sw_r_pi_dp_hvbUpb011QNH7")
	# amzn_links = get_amzn(amzn_soup)

	# pin = Pin("http://www.etsy.com/listing/102135880/rainbow-summer-chevron-stripes-pride")
	# [ pin, pin1, pin2 ]
	# print pin.title
	# print pin.image_link


def find_pin_source(username, boardname):
### find the popular sources by injecting boardname
	#make URL of pinterest
	pboard_url = "http://pinterest.com/%s/%s" %(username,boardname)
	pinb = requests.get(pboard_url)
	pinsoup = BeautifulSoup(pinb.content)
	all_linked_pins = pinsoup.find_all("div","convo attribution clearfix")
	"""	
		<div class="convo attribution clearfix">
		<p class="NoImage">
		<a href="http://weheartit.com/entry/23003667" rel="nofollow" target="_blank">weheartit.com</a>
		</p>
		</div>
	"""
	pin_source = []
	i = 0
	for item in all_linked_pins:
		pin_source.append(all_linked_pins[i].a.contents[0])
		i += 1
	return pin_source

def get_soup(link):
### turn HTML into soup
	p = requests.get(link)
	soup = BeautifulSoup(p.content)
	return soup

def get_image(soup):
### from soup to list of ahref
	### find all <p> tags with class "noimage", which tags source links for each pin
	noimage = soup.find_all("p","NoImage")
	return noimage
	"""	
		Eg, noimage = ...
		# [<p class="NoImage">
		# <a href="http://raspberryandred.blogspot.com/2010_06_01_archive.html" rel="nofollow" target="_blank">raspberryandred.blogspot.com</a>
		# </p>, ... ] 
	"""

def get_link_list(noimage):
### create a list of links
	link_list = []
	for item in noimage:
		item_s = str(item)
		new_item = item_s.split('\n')
		link_list.append(new_item[1])
	return link_list
	"""
		# ['<a href="http://vanessajackman.blogspot.com/search?updated-max=2012-06-24T16:01:00%2B01:00&amp;max-results=20&amp;start=12&amp;by-date=false" rel="nofollow" target="_blank">
		vanessajackman.blogspot.com
		</a>', ]
	"""

def get_etsy(etsy_soup):
### search etsy only
	etsy_only = etsy_soup.select('a[href*="etsy.com/listing/"]')
	"""etsy_only
		# return a list of <a href> 
		### etsy_only =
		#[ <a href="http://www.etsy.com/shop/thiefandbanditkids" rel="nofollow" target="_blank">thiefandbanditkids</a>, 
		# <a href="http://www.etsy.com/listing/100848212/big-heart-tank-in-fluorescent-plaid-with" rel="nofollow" target="_blank">etsy.com</a> ]
	"""
	# return a list of links ['www.etsy.com/shop/theifandbanditkids',...] etc
	etsy_links = []
	for a in etsy_only:
		etsy_links.append(a['href'])
	return etsy_links
	"""etsy_links
	 # [u'http://www.etsy.com/shop/Gingiber', 
	 # u'http://www.etsy.com/listing/95659221/giraffe-reusable-fabric-wall-decal-large', 
	 # u'http://www.etsy.com/shop/Gingiber', 
	 # u'http://www.etsy.com/listing/95659126/zebra-reusable-fabric-wall-decal-large']
	 """

def etsy_price(etsy_soup):
#### get price from etsy's source page
	# etsy_soup = get_soup(link)
	# EG: etsy_soup = get_soup("http://www.etsy.com/listing/102135880/rainbow-summer-chevron-stripes-pride")
	price_tag = etsy_soup.find_all("div","item-amount")
	price_w_crcy = "%s$ %s" %(str(price_tag[0].contents[3].contents[0].text), str(price_tag[0].contents[2]))
	return price_w_crcy
	# 'USD$ 13.00 '
	"""
		# return a list of 2 item-amounts (div class "item price " and "item price 2")
		## [<div class="item-amount">
		## <span class="currency-symbol">$</span>13.00 <a class="" href="#currency-select"><span class="currency-code">USD</span></a>
		## <span class="highlight"></span>
		## </div> ]
	"""

def etsy_item_title(etsy_soup):
### get item title from source page
	item_title = etsy_soup.find("div", {"id": "item-title"})
	return str(item_title.contents[1].contents)
 	# Rainbow Summer Chevron Stripes Pride Home Decor Light Switch Plate and Outlet Cover Set - MADE TO ORDER

def etsy_img_link(etsy_soup):
### get img link from source page
	# etsy_soup = get_soup("http://www.etsy.com/listing/102135880/rainbow-summer-chevron-stripes-pride")
	img_link = etsy_soup.find("div", {"id": "fullimage_link1"})
	img_link.contents
	### HOW TO GET THE A HREF OUT? ###
	"""img_link
		[<a href="http://img2.etsystatic.com/000/0/5265952/il_fullxfull.345569342.jpg" target="_blank">
		<img alt="Rainbow Summer Chevron Stripes Pride Home Decor Light Switch Plate and Outlet Cover Set - MADE TO ORDER" src="http://img2.etsystatic.com/000/0/5265952/il_570xN.345569342.jpg" width="570"/> 
		</a>]

	"""
### make individual objects with pdt name, pdt link, img link, price

def get_amzn(soup):
	amzn_only = soup.select('a[href*="amazon.com/"]')
	print "amazon only", amzn_only
	"""amzn_only
		# return a list of <a href> 
		### etsy_only =
		#[ <a href="http://www.etsy.com/shop/thiefandbanditkids" rel="nofollow" target="_blank">thiefandbanditkids</a>, 
		# <a href="http://www.etsy.com/listing/100848212/big-heart-tank-in-fluorescent-plaid-with" rel="nofollow" target="_blank">etsy.com</a> ]
	"""
	# return a list of links ['www.etsy.com/shop/theifandbanditkids',...] etc
	amzn_links = []
	for a in amzn_only:
		amzn_links.append(a['href'])
	print "amzn links", amzn_links
	"""amzn_links
	 # [u'http://www.etsy.com/shop/Gingiber', 
	 # u'http://www.etsy.com/listing/95659221/giraffe-reusable-fabric-wall-decal-large', 
	 # u'http://www.etsy.com/shop/Gingiber', 
	 # u'http://www.etsy.com/listing/95659126/zebra-reusable-fabric-wall-decal-large']
	 """

def amzn_price(soup):
	price_tag = amzn_soup.find("span",{"id": "actualPriceValue"})
	price_w_crcy = "%s$ %s" %(str(price_tag[0].contents[3].contents[0].text), str(price_tag[0].contents[2]))


class Pin(object):
	def __init__ (self, link):
		soup = get_soup(link)
		self.title = etsy_item_title(soup)
		self.price = etsy_price(soup)
		self.image_link = etsy_img_link(soup)
		self.pdt_link = link

# etsy = Pin("http://www.etsy.com/listing/102135880/rainbow-summer-chevron-stripes-pride")

"""
	item_title.contents = [u'\n', <h1>Rainbow Summer Chevron Stripes Pride Home Decor Light Switch Plate and Outlet Cover Set - MADE TO ORDER</h1>, u'\n', <p class="shop-name">From <a href="/shop/ModernSwitch?ref=seller_info">ModernSwitch</a></p>, 
	u'\n']
"""

def get_amzn():
### THAT'S WHERE IT WORKED TILL JULY 24 ###
	pass
	
if __name__ == '__main__':
	main()

