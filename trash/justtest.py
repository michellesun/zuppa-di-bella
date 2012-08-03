from bs4 import BeautifulSoup
import requests
from collections import Counter, defaultdict
from operator import itemgetter


def get_soup(link):
### turn HTML into soup
	p = requests.get(link)
	soup = BeautifulSoup(p.content)
	return soup


def get_amzn(soup):
	amzn_only = soup.select('a[href*="etsy.com/"]')
	print "amazon only", amzn_only
	"""etsy_only
		# return a list of <a href> 
		### etsy_only =
		#[ <a href="http://www.etsy.com/shop/thiefandbanditkids" rel="nofollow" target="_blank">thiefandbanditkids</a>, 
		# <a href="http://www.etsy.com/listing/100848212/big-heart-tank-in-fluorescent-plaid-with" rel="nofollow" target="_blank">etsy.com</a> ]
	"""
	# return a list of links ['www.etsy.com/shop/theifandbanditkids',...] etc
	amzn_links = []
	for a in amzn_only:
		amzn_links.append(a['href'])
	print "amzn links" amzn_links
	"""etsy_links
	 # [u'http://www.etsy.com/shop/Gingiber', 
	 # u'http://www.etsy.com/listing/95659221/giraffe-reusable-fabric-wall-decal-large', 
	 # u'http://www.etsy.com/shop/Gingiber', 
	 # u'http://www.etsy.com/listing/95659126/zebra-reusable-fabric-wall-decal-large']
	 """

# pin_source_list = 
# 	[u'yogurtyoga.tumblr.com', u'tumblr.com', u'loseweight-safe.com', u'danceisuniversal.tumblr.com', u'dare-to-be-healthy.tumblr.com', u'fit-not-thin.tumblr.com', u'fitsugar.com', u'flickr.com', u'migas.tumblr.com', u'tumblr.com', u'tumblr.com', u'tumblr.com', u'theathenenoctua.tumblr.com', u'awelltraveledwoman.tumblr.com', u'fit-toned4summer.tumblr.com', u'youtube.com', u'tumblr.com', u'sexydangerous.tumblr.com', u'thinisalwaysbetter.tumblr.com', u'google.com', 
# 	u'29.media.tumblr.com', u'fitisthenewbeautiful.tumblr.com', u'beautifulday4running.tumblr.com', u'downtownn.tumblr.com', u'thehealthychange.tumblr.com', u'weheartit.com', u'fitmindandbody.tumblr.com', u'health-heaven.tumblr.com', u'thefancy.com', u'raspberryandred.blogspot.com', u'rstyle.me', u'25.media.tumblr.com', u'mostbeautifull.net', u'threadflip.com', u'rstyle.me', u'kingsunderlavenderskies.tumblr.com', u'chrisanthemums.tumblr.com', u'laurenconrad.com', u'whyilovetoshop.com', u'iknowhair.com', u'rstyle.me', u'shopbop.com', u'community.boden.co.uk', u'zimbio.com', u'glamour.com', u'themessesofmen.tumblr.com', u'cupcakesandcashmere.com', u'preppie-bettie.tumblr.com', u'audrey1.org', u'jlmcouture.com', u'weheartit.com', u'fancydresses.tumblr.com', u'jcrewing.tumblr.com', u'dare-to-be-healthy.tumblr.com', u'fitnessinspiration.tumblr.com', u'laurenconrad.com', u'tumblr.com', u'tumblr.com', u'tumblr.com', u'tumblr.com', u'26.media.tumblr.com', u'tumblr.com', u'moderndayfairytale.tumblr.com', u'ashley-ringmybell.blogspot.com', u'ashley-ringmybell.blogspot.com', u'tumblr.com', u'thebeautydepartment.com', u'1.bp.blogspot.com', u'tumblr.com', u'tumblr.com', u'tumblr.com', u'tumblr.com', u'tumblr.com', u'suicideblonde.tumblr.com', u'weheartit.com', u'weheartit.com', u'newyorktoparis.tumblr.com', u'tumblr.com', u'tumblr.com', u'tumblr.com', u'tumblr.com', u'tumblr.com', u'tumblr.com', u'tumblr.com', u'tumblr.com', u'tumblr.com', u'tumblr.com', u'tumblr.com', u'fuckyeahaudreyhepburn.tumblr.com', u'hellyeahmarioncotillard.tumblr.com', u'minkette.rebeccaminkoff.com', u'jlmcouture.com', u'couldihavethat.blogspot.com', u'starstyleinc.com', u'google.com', u'shopbop.com', u'vincentpetersphotography.com', u'vincentpetersphotography.com', u'makeup4all.com', u'google.com', u'25.media.tumblr.com', u'frommygreydeskblog.com', u'nicolesandiko.blogspot.com', u'e-wigs.com', u'bridalmusings.com', u'rapsodistanbul.tumblr.com', u'refinery29.com', u'howtobefierce.tumblr.com', u'howtobefierce.tumblr.com', u'howtobefierce.tumblr.com', u'howtobefierce.tumblr.com', u'nuandao.diandian.com', u'sweetsassyclassy.tumblr.com', u'noskinnybitcheshere.tumblr.com', u'theneotraditionalist.com', u'lookbook.nu', u'25.media.tumblr.com', u'google.com.hk', u'google.com.hk', u'weheartit.com', u'google.com', u'etsy.com', u'i-n-vogue.tumblr.com', u'eur0trash.tumblr.com', u'eur0trash.tumblr.com', u'eur0trash.tumblr.com', u'shopbop.com', u'bourbonandpearls.tumblr.com', u'sundaycrossbow.blogspot.com', u'tumblr.com', u'tumblr.com', u'enchantingdesign.tumblr.com', u'enchantingdesign.tumblr.com', u'style-files.com', u'enchantingdesign.tumblr.com', u'enchantingdesign.tumblr.com', u'plastolux.tumblr.com', u'plastolux.tumblr.com', u'tumblr.com', u'ca-ffeine.tumblr.com', u'whereisthecool.com', u'tumblr.com', u'tumblr.com', u'tumblr.com', u'somewhere71.tumblr.com', u'tumblr.com', u'pinterest.com', u'imgfave.com', u'luxuria-jewellery.blogspot.com', u'google.com', u'ydnar.com', u'observando.net', u'modernhepburn.tumblr.com', u'imgfave.com', u'a3.sphotos.ak.fbcdn.net', u'bobalexrasman.onsugar.com', u'wes-anderson.tumblr.com', u'fossil.com', u'tumblr.com', u'itsparisbabe.tumblr.com', u'mollyjacquesillustration.blogspot.com', u'design-milk.com', u'visualgraphic.tumblr.com', u'google.com.mx', u'makeupadviser.info', u'29.media.tumblr.com', u'ffffound.com', u'fromupnorth.com', u'hervisualdiary.tumblr.com', u'holyprepster.tumblr.com', u'pushthemovement.tumblr.com', u'motivationintohabit.tumblr.com', u'etsy.com', u'katespadeny.tumblr.com', u'tumblr.com', u'granvillehouse.blogspot.com', u'imgfave.com', u'everythingfab.com', u'tumblr.com', u'google.com', u'tumblr.com', u'26.media.tumblr.com', u'a7.sphotos.ak.fbcdn.net', u'tumblr.com', u'tumblr.com', u'thebeeskneesbaby.tumblr.com', u'allsassandshag.tumblr.com', u'theberry.com', u'flickr.com', u'sayingimages.com', u'adventuresinthenightgarden.tumblr.com', u'google.com', u'chasingkristina.tumblr.com', u'thebeeskneesbaby.tumblr.com', u'howtobefierce.tumblr.com', u'howtobefierce.tumblr.com', u'thehappyparade.tumblr.com', u'jennyanddukefamily.blogspot.com', u'fbcdn-sphotos-a.akamaihd.net', u'happilymaintaining.tumblr.com', u'weheartit.com', u'flickr.com', u'piccsy.com', u'somewhere71.tumblr.com', u'howaboutorange.blogspot.com', u'imgfave.com', u'thechive.com', u'weheartit.com', u'bleubirdvintage.typepad.com', u'27.media.tumblr.com', u'killmydaynow.com', u'thismodernromance.com', u'28.media.tumblr.com', u'weheartit.com', u'mashable.com', u'weheartit.com', u'tumblr.com', u'honeyglazedlife.tumblr.com', u'tumblr.com', u'camilalsantos.wordpress.com', u'livinglife1quoteatatime.tumblr.com', u'imgfave.com', u'ispwp.com', u'vincentpetersphotography.com', u'vincentpetersphotography.com', u'stylemepretty.com', u'aisle-candy.com', u'bourbonandpearls.tumblr.com', u'softbeauty.tumblr.com', u'google.co.uk', u'joannagoddard.blogspot.com', u'bippityboppityboo.tumblr.com', u'ilovephoto.info', u'howtobefierce.tumblr.com', u'theneotraditionalist.com', u'100layercake.com', u'clarkwalkerstudio.com', u'viabliss.tumblr.com', u'stylemepretty.com', u'tumblr.com', u'hearthecolors.tumblr.com', u'veryculinary.com', u'firstlookthencook.com', u'blog.belovedgreen.com', u'susikochenundbacken.blogspot.com', u'online.wsj.com', u'flickr.com', u'laylita.com', u'inspiredbycharm.com', u'marthastewart.com', u'pinerly.com', u'nytimes.com', u'blogs.babble.com', u'squaremeal.tumblr.com', u'dare-to-be-healthy.tumblr.com', u'laurenconrad.com', u'momofukufor2.com', u'returntosundaysupper.com', u'whatthefucksarah.tumblr.com', u'bevcooks.com', u'designyoutrust.com', u'thekitchn.com', u'tumblr.com', u'google.com', u'28cooks.blogspot.com', u'delight.tumblr.com', u'smokinchestnut.com', u'hervisualdiary.tumblr.com', u'damndelicious.tumblr.com', u'images.fastcompany.com', u'michellelsun.tumblr.com', u'japon.typepad.fr', u'lava360.com', u'lava360.com', u'designboom.com', u'socialmediatoday.com', u'mashable.com', u'stateofsearch.com', u'ryanfmc.co.uk', u'simpliflying.com', u'informationarchitects.jp', u'pandodaily.com', u'holykaw.alltop.com', u'socialvelocity.net', u'udemy.com', u'lh6.googleusercontent.com', u'nbrii.com', u'mashable.com', u'techinasia.com', u'mashable.com', u'visualoop.tumblr.com', u'digitalbuzzblog.com', u'digitalbuzzblog.com', u'digitalbuzzblog.com', u'mediabistro.com', u'socialtimes.com', u'digitalbuzzblog.com', u'digitalbuzzblog.com', u'soshable.com', u'pandodaily.com', u'simplyzesty.com', u'atelierdecor.blogspot.com', u'socialwayne.com', u'theleanstartup.com', u'static8.businessinsider.com', u'unbounce.com', u'mindbodygreen.com', u'blog.jess3.com', u'socialmediaexaminer.com', u'blog.massivehealth.com', u'publicrelationships.blogspot.com', u'flowtown.com', u'aclu.org', u'mashable.com', u'mashable.com', u'thefancy.com', u'img2.etsystatic.com', u'rstyle.me', u'thecdock.com', u'weddinggawker.com', u'ninjablocks.com', u'etsy.com', u'society6.com', u'shopedisen.com', u'tumblr.com', u'etsy.com', u'cafepress.com', u'anthropologie.com', u'popandshorty.bigcartel.com', u'reasonstobreathe.tumblr.com', u'tumblr.com', u'tumblr.com', u'shoptigertree.com', u'lamadesigns.com', u'attic-lifestyle.com', u'theneotraditionalist.com', u'artjamming.com', u'weheartit.com', u'google.com', u'stylemepretty.com', u'tumblr.com', u'somewhere71.tumblr.com', u'500px.com', u'500px.com', u'500px.com', u'yelp.com', u'laughinglotus.com', u'smittenicecream.com', u'500px.com', u'500px.com', u'thevintageseason.tumblr.com', u'thefancy.com', u'designbeep.com', u'designbeep.com', u'smashinghub.com', u'quora.com', u'quora.com', u'skytechgeek.com', u'skytechgeek.com', u'onextrapixel.com', u'onextrapixel.com', u'\n', u'\n', u'\n', u'\n', u'\n', u'\n', u'\n', u'\n', u'\n', u'\n']


# output = defaultdict(lambda: 0)
# for source in pin_source_list:
# 	try:
# 		domain = source.split(".")[-2]
# 		output[domain] += 1
# 	except IndexError:
# 		pass
# # print sorted(output.items())
# # print "itemgetter", output.sort(key=operator.itemgetter(1))
# print "defaultdict", sorted(output.iteritems(),key=lambda (k,v): v,reverse=True)

# try 2

# result = []
# domain = source.split(".")[-2]
# count = domain.count
# for source in pin_source_list:
# 	## split by "."
# 	try:
# 	# print domain
# 		result_tuple = (count(domain),domain)
# 		result.append(result_tuple)
# 		print result_tuple
# 	except IndexError:
# 		print source.split(".")
# result.sort()
# print result
""" result print out 
	(1, u'tumblr'), (1, u'tumblr'), (1, u'tumblr'), (1, u'tumblr'), 
	(1, u'tumblr'), (1, u'tumblr'), (1, u'tumblr'), (1, u'tumblr'), 
	(1, u'tumblr'), (1, u'tumblr'), (1, u'tumblr'), (1, u'tumblr'), 
	(1, u'tumblr'), (1, u'tumblr'), (1, u'tumblr'), (1, u'tumblr'), 
	(1, u'tumblr'), (1, u'tumblr'), (1, u'tumblr'), (1, u'tumblr'), 
	(1, u'typepad'), (1, u'typepad'), (1, u'udemy'), (1, u'unbounce'), (1, u'veryculinary'), (1, u'vincentpetersphotography'), (1, u'vincentpetersphotography'), (1, u'vincentpetersphotography'), (1, u'vincentpetersphotography'), (1, u'weddinggawker'), (1, u'weheartit'), (1, u'weheartit'), (1, u'weheartit'), (1, u'weheartit'), (1, u'weheartit'), (1, u'weheartit'), (1, u'weheartit'), (1, u'weheartit'), (1, u'weheartit'), (1, u'weheartit'), (1, u'whereisthecool'), (1, u'whyilovetoshop'), (1, u'wordpress'), (1, u'wsj'), (1, u'ydnar'), (1, u'yelp'), (1, u'youtube'), (1, u'zimbio')]
"""
### WHERE IT WAS LEFT OFF. 

# File "make_board_pin_list.py", line 25
#     print result


# for source in pin_source_list:
# 	if "tumblr" in source:
# 		print source

# def pin_analyzer(pin_source_list):
# ### feed all sources and generate a list of tuples with (count, domain)


# board_pin_list = []
# url_list = [u'http://pinterest.com/michellelsun/fitness/', u'http://pinterest.com/michellelsun/beauty/', u'http://pinterest.com/michellelsun/beauty/?page=2', u'http://pinterest.com/michellelsun/beauty/?page=3', u'http://pinterest.com/michellelsun/home-sweet-home/', u'http://pinterest.com/michellelsun/home-sweet-home/?page=2', u'http://pinterest.com/michellelsun/words/', u'http://pinterest.com/michellelsun/words/?page=2', u'http://pinterest.com/michellelsun/sweetness/', u'http://pinterest.com/michellelsun/wanderlust/', u'http://pinterest.com/michellelsun/fooodism/', u'http://pinterest.com/michellelsun/infographics/', u'http://pinterest.com/michellelsun/items/', u'http://pinterest.com/michellelsun/nature/', u'http://pinterest.com/michellelsun/love-in-the-bay/', u'http://pinterest.com/michellelsun/web-design/', u'http://pinterest.com/michellelsun/demo-videos/']

# for url in url_list:
# 	try:
# 		new_pinb = requests.get(url)
# 		pinsoup = BeautifulSoup(new_pinb.content)
# 		pin_source = get_pin_source(pinsoup)
# 		board_pin_list.extend(pin_source)
# 	except Exception,e:
# 		pass
# print board_pin_list


# def get_pin_source(pinsoup):
# 	all_linked_pins = pinsoup.find_all("div","convo attribution clearfix")
# 	"""	an item in all_linked_pins
# 		<div class="convo attribution clearfix">
# 		<p class="NoImage">
# 		<a href="http://weheartit.com/entry/23003667" rel="nofollow" target="_blank">weheartit.com</a>
# 		</p>
# 		</div>
# 	"""
# 	pin_source = []
# 	""" error message 
# 		<type 'NoneType'>
# 		<class 'bs4.element.Tag'>
# 		<class 'bs4.element.Tag'>
# 		<class 'bs4.element.Tag'>
# 		<class 'bs4.element.Tag'>
# 		<class 'bs4.element.Tag'>
# 		<class 'bs4.element.Tag'>
# 		<class 'bs4.element.Tag'>
# 		<type 'NoneType'>
# 	"""
# 	# i = 0
# 	for item in all_linked_pins:
# 	 	if item.a == None:
# 			continue
# 		else:
# 			pin_source.append(item.a.contents[0])
# 		# i += 1
# 	return pin_source
# 	""" sample pin_source
# 		[u'thefancy.com', u'raspberryandred.blogspot.com', 
# 		u'rstyle.me', u'25.media.tumblr.com', u'mostbeautifull.net', 
# 		u'threadflip.com', u'rstyle.me', u'kingsunderlavenderskies.tumblr.com', 
# 		u'chrisanthemums.tumblr.com', u'laurenconrad.com', 
# 		u'whyilovetoshop.com', u'iknowhair.com', u'rstyle.me',
# 		 u'shopbop.com', u'community.boden.co.uk', u'zimbio.com', 
# 		 u'glamour.com', u'themessesofmen.tumblr.com']
# 	"""