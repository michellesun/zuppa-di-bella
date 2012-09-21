from bs4 import BeautifulSoup
import requests
from collections import Counter
from collections import Counter, defaultdict
from operator import itemgetter
import pymongo
from sets import Set

def make_board_urllist(brand):
### make a list of first 5 pages of URLs based on brand search
	bs = brand.split()
	if len(bs) > 1:
		name = "+".join(bs)
		brand_url = "http://pinterest.com/search/?q=%s" %(name)
	else:
		brand_url = "http://pinterest.com/search/?q=%s" %(brand)
	url_list = []
	for i in range(1,11): #get the first 10 pages of results
		new_url = ( brand_url+"&page=%d") %i 
		url_list.append(new_url) 
	"""print "url_list", url_list

		url_list ['http://pinterest.com/search/?q=Cobra+Society&page=1', 'http://pinterest.com/search/?q=Cobra+Society&page=2', 'http://pinterest.com/search/?q=Cobra+Society&page=3', 'http://pinterest.com/search/?q=Cobra+Society&page=4', 'http://pinterest.com/search/?q=Cobra+Society&page=5', 'http://pinterest.com/search/?q=Cobra+Society&page=6', 'http://pinterest.com/search/?q=Cobra+Society&page=7', 'http://pinterest.com/search/?q=Cobra+Society&page=8', 'http://pinterest.com/search/?q=Cobra+Society&page=9', 'http://pinterest.com/search/?q=Cobra+Society&page=10']
	"""
	return url_list

def make_user_list(url_list):
	user_list = Set()
	for url in url_list:
		try:
			page = requests.get(url)
			pinsoup = BeautifulSoup(page.content)
			pinners = get_pinners(pinsoup)
			for pinner in pinners:
				user_list.add(pinner)
		except Exception,e:
			pass
	print "len(user_list)", len(user_list) # 19360
	return user_list #list of all users that have pinned in these brands

## new function!! ## 
def checkoverlap(url_list):
	check_overlap = []

	for url in url_list:
		try:
			page = requests.get(url)
			pinsoup = BeautifulSoup(page.content)
			pinners = get_pinners(pinsoup)
			print pinners
			check_overlap + pinners
		except Exception,e:
			pass
	return check_overlap

def make_indieuser_list(url_list): 
### now having the list of url, get list of users that pinned those pins
	user_list = []
	i = 0
	for url in url_list:
		each_list = []
		try:
			page = requests.get(url)
			pinsoup = BeautifulSoup(page.content)
			pinners = get_pinners(pinsoup)
			# print "url", url
			# print "pinners", pinners 
			for pinner in pinners:
				# print "pinner", pinner
				each_list.append(pinner)
		except Exception,e:
			pass
		i += 1
		# print "each_list", i, each_list	
		user_list.extend(each_list)	
	
	print "len of user list", url , len(user_list) # Derek Lam 463
	return user_list #list of users that pinned in 1 brand (with duplicated) around 450

def get_pinners(pinsoup):
### find sources of pins
	p = pinsoup.find_all('div', {'class': 'convo attribution clearfix'})
	# <a href="/ivanaamai/" title="Ivana Amai" class="ImgLink">
	"""	an item in p
		<div class="convo attribution clearfix">
		<a class="ImgLink" href="/rebecasantanna/" title="Rebeca Sant'Anna">
		<img alt="Profile picture of Rebeca Sant'Anna" src="http://media-cache-ec6.pinterest.com/avatars/rebecasantanna_1337063676.jpg"/>
		</a>
		<p>
		<a href="/rebecasantanna/">Rebeca Sant'Anna</a> onto <a href="/rebecasantanna/favorites/">Favorites</a>
		</p>
		</div>
    """
	pinners = []

	for item in p:
		pinner = item.contents[1]['href'][1:-2] #how do I access href??
		""" pinner
			'staciarose2'
			'christopherjo'
			'andreascarlsso'
			'faragodesig'
			'mistressnatali'
			'danielplanvie'
			'rebecasantann'
		"""
		pinners.append(pinner)
	# print 'pinners', pinners
	"""pinners
		pinners ['brooke_taylor1', 'aidinbelgane', 'lzampell', 'hypergenica1', 'debroahreze', 'lauramas', 'rast', 'snowpeaprinces', 'carolinebu', 'marycomett', 'tenditrend', 'magpieluc', 'uniquewa', 'grizzly112', 'kcopacinn', 'johannsenphot', 'palom', 'christineo201', 'jerseegir', 'marymichelott', 'ttownrussia', 'bridgetttaa', 'saar', 'kelkel101', 'born2boo', 'wlsca', 'kyladoyl', 'naebearb', 'angelada', 'riverrunn', 'lilgreylex']
		pinners ['wholeean', 'ayoung1', 'meev', 'sarahblat', 'sam', 'charlilo', 'suburban2', 'carmenstreete', 'carabmisle', 'efenhau', 'angelemateu', 'teogavala', 'tammybernin', 'eviasikarsk', 'pfredericka', 'starphia', 'akfranke', 'katieottewel', 'zizzie7', 'shelleyraymond', 'onyxroz', 'eleanorpasche6', 'gchga', 'brooke_taylor1', 'aidinbelgane', 'lzampell', 'hypergenica1', 'debroahreze', 'lauramas', 'rast', 'snowpeaprinces', 'carolinebu', 'marycomett']
	"""
	return pinners


def count_source(per_brand_user_list):
### feed all sources and generate a list of tuples with (count, domain)
	output = defaultdict(lambda: 0)
	for user in per_brand_user_list:
	# because there are duplicates
		output[user] += 1

 	# source_count = sorted(output.iteritems(),key=lambda (k,v): v,reverse=True)		
	# user_count = sorted(output.iteritems(),key=lambda (k,v): v,reverse=True)
	# print "source_count", sorted(output.iteritems(),key=lambda (k,v): v,reverse=True)
	return output

def connect_db():
	connect_string = "mongodb://pinterestalgo:pinterest2012@ds037047.mongolab.com:37047/brands"
	# mongodb://%s:%s@%s:%d/%s" % \
 #            (user, password, host, port, db_name)
	c = pymongo.connection.Connection(connect_string)
	return c['brands']

def main():
	global db
	db = connect_db()
	# db = db['brand'] #get collection named pinterest
	t = open("/Users/honeysnow/Desktop/python/beautifulsoup/datafiles/topbrands_shopbop2.txt")
	# url_list = []
	for line in t.readlines():
		brand = line.strip()
		all_pinners_list = []	
		url = make_board_urllist(brand)
		# url_list.extend(url) 
		# """url_list a list of urls for all brands, all pages

		# 	 'http://pinterest.com/search/?q=seven-jeans&page=0', 'http://pinterest.com/search/?q=seven-jeans&page=1', 'http://pinterest.com/search/?q=seven-jeans&page=2', 'http://pinterest.com/search/?q=seven-jeans&page=3', 'http://pinterest.com/search/?q=seven-jeans&page=4', 'http://pinterest.com/search/?q=seven-jeans&page=5', 'http://pinterest.com/search/?q=tom-ford&page=0', 'http://pinterest.com/search/?q=tom-ford&page=1', 'http://pinterest.com/search/?q=tom-ford&page=2', 'http://pinterest.com/search/?q=tom-ford&page=3', 'http://pinterest.com/search/?q=tom-ford&page=4', 'http://pinterest.com/search/?q=tom-ford&page=5']
		# """
		# unindent the following 5 lines
		# user_list = make_user_list(url_list) #make a large SET userlist that includes all users that pinned from all brands all pages ## What is this for???

		# t = open("/Users/honeysnow/Desktop/python/beautifulsoup/datafiles/topbrands_shopbop.txt")
		# for line in t.readlines():
		# 	# now get a list of users( with duplicates ) 
		# 	brand = line.strip()
		# no need for now

		url_list = make_board_urllist(brand)
		per_brand_user_list = make_indieuser_list(url_list)
		# print "per_brand_user_list", brand, per_brand_user_list
		output = count_source(per_brand_user_list)
		# print 'output', output
		# print 'len(output), size of dictionary', len(output)
		output_dict = {}
		output_dict['brand'] = brand
		output_dict['users'] = output
		# print 'output_dict', output_dict

		lenlog = open('datafiles/length.txt','a')
		lenlog.write("%s\t%d\n" % (brand,len(output_dict['users'])))
		lenlog.close()
		# keep track of length of each dictionary

		if len(output_dict) == 0:
			f = open('datafiles/emptybrand.txt','w')
			f.write(brand)
			f.close()
			# keep track of empty returns and rerun. 


		brands = db.brands
		brands.insert(output_dict)
	
if __name__ == '__main__':
	main()
