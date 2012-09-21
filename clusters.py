from math import sqrt
import random
import pymongo
from sets import Set
import simplejson as json
# from PIL import Image,ImageDraw

# def readfile(filename):
# 	lines=[line for line in file(filename)]
# 	# print lines
# 	"""lines
# 		able\tcomputer\tstate\tgroup\tpc\tpiece\tusing\tever\tbetter\twent\tcontent\tbar\t
# 		three\tleft\tsuper\toffering\tdaily\tfinally\tdid\tamericans\tespecially\tacross\tmark
# 		\tdifferent\tpay\trunning\tcritical\tshare\tsomeone\teasily\thouse\tbuilt\tbuild\t
# 		find\tplease\titself\tyesterday\tbig\tbit\tgoogle\toften\teither\tbody\tothers\ttext
# 		\tlooks\tthought\thost\tphone\tmust\twriting\tfree\twanted\tplayers\tcheck\tlonger
# 		\twhite\tways\tcome\tblog\tearlier\tcalls\tfar\tgeneration\twindows\thit\thim\tart
# 		\tintelligence\tvarious\tuse\tc\tmoving\tcalled\tnotes\tapple\twomen\tchoose\tyork
# 		\tmyspace\tones\twords\tview\tbecause\tgetting\tbook\n
# 	"""
# 	# First line is the column titles 
# 	colnames=lines[0].strip().split('\t')[1:] 
# 	rownames=[]
# 	data=[]
# 	for line in lines[1:]:
# 		p=line.strip().split('\t')
# 		rownames.append(p[0])
# 		data.append([float(x) for x in p[1:]])
# 	return blognames,words,data

# def getusernames(filename):
# 	usernames = []
# 	t = open("datafiles/toppinners.txt")
# 	for line in t.readlines():
# 		username = line.strip()
# 		usernames.append(username)
# 	return usernames

# def getpinsource(usernames): #takes in a list of usernames and generate a SET of pinsource
# 	pin_dict = db.pinners.find()
# 	pinsource = Set()
# 	for pin in pin_dict: 
# 		for username in usernames: 
# 			if pin.get(username) != None: #try if username is
# 				sourcecount = pin.get(username) 
# 				"""sourcecount is a dictionary
# 						sourcecount = {u'manrepeller': 2, u'style-syndrome': 1,u'poketo': 2, u'youtube': 33, u'scene7': 4, u'diamondintherough': 6, u'orangebeautiful': 1, u'xcitefun': 1, u'thebeautyinsiders': 1, u'bodenimages': 2, u'lyst':2, u'blogg': 5}
# 				"""
# 				break
# 			else:
# 				continue
# 		onesource = sourcecount.keys()
# 		for source in onesource:
# 			pinsource.add(source)
# 	# print len(pinsource) # 15237
# 		"""pinsource is a set with over 15,000 domains

# 				Set([u'freespiritfabric', u'canalblog', u'audubonbirdcall', u'iscreativestudio', u'kissthegroom', u'mrslilien', u'viviancherry', u'douglasrosin', u'photoshopuser', u'eatlovedrink', u'leighbeischphotography', u'executiverealness', u'houyhnhnm', u'kelleyryden', u'hungrygirlporvida', u'onelovelylife', u'digitaltrends', u'triciajoyce', u'womansday', u'nthread'])
# 		"""
# 	return pinsource, sourcecount

def get_sources(pinners,min_val=1):
	sources = []
	for pinner in pinners:
		clean_pinner = {}
		clean_pinner['pins'] = { k:v for k,v in pinner['pins'].items() if v > min_val}
		# to screen out all the domain names that only has 1 or 
		# print "CLEAN PINNER", clean_pinner
		"""clean_pinner

			u'schoolhouseelectric': 2, u'ffffound': 19, u'gilt': 3, u'ikea': 3, u'gap': 5, u'bravetart': 3, u'kwestiasmaku': 3, u'rstyle': 14, u'familystylefood': 4, u'jonathanadler': 2, u'mindygayer': 3, u'designspiration': 4, u'thedieline': 5, u'marysiaswimstore': 2, u'caitlinmcgauley': 2, u'dvf': 2, u'sweetwilliamltd': 2, u'sweetapolita': 16, u'bedifferentactnormal': 6, u'bakersroyale': 9, u'iloveswmag': 4, u'projectwedding': 2, u'blogg': 2, u'littlefashiongallery': 2, u'greylikesweddings': 3, u'bonappetit': 11, u'thevitrine': 2, u'joylicious': 2, u'greenkitchenstories': 3, u'vdj-boutique': 2}}
		"""
		source = clean_pinner['pins'].keys()
		sources.extend(source)
	pinsources = list(set(sources)) #length is 4285
	""" pinsources

		u'nendo', u'highsnobiety', u'kitchenkapers', u'thehappyhomeblog', u'net-a-porter', u'ericaweiner', u'saturdaysnyc', u'thebutternyc', u'curbed', u'bonobos', u'glamourboysinc', u'nest-living', u'anediblemosaic', u'yelp', u'sodapopgirl', u'grassrootsmodern', u'lyst', u'blogs', u'peacockplume', u'eol', u'ryanfeerer', u'andredaloba', u'bbcgoodfood', u'petsmart', u'swoopbags', u'blogg', u'simoneleblanc']
	"""
	return pinsources

def get_sources_b(pinners,min_val=0):
	sources = []
	for pinner in pinners:
		clean_pinner = {}
		clean_pinner['users'] = { k:v for k,v in pinner['users'].items() if v > min_val}
		# to screen out all the domain names that only has 1 or 
		# print "CLEAN PINNER", clean_pinner
		"""clean_pinner

			u'schoolhouseelectric': 2, u'ffffound': 19, u'gilt': 3, u'ikea': 3, u'gap': 5, u'bravetart': 3, u'kwestiasmaku': 3, u'rstyle': 14, u'familystylefood': 4, u'jonathanadler': 2, u'mindygayer': 3, u'designspiration': 4, u'thedieline': 5, u'marysiaswimstore': 2, u'caitlinmcgauley': 2, u'dvf': 2, u'sweetwilliamltd': 2, u'sweetapolita': 16, u'bedifferentactnormal': 6, u'bakersroyale': 9, u'iloveswmag': 4, u'projectwedding': 2, u'blogg': 2, u'littlefashiongallery': 2, u'greylikesweddings': 3, u'bonappetit': 11, u'thevitrine': 2, u'joylicious': 2, u'greenkitchenstories': 3, u'vdj-boutique': 2}}
		"""
		source = clean_pinner['users'].keys()
		sources.extend(source)
	pinsources = list(set(sources)) #length is 4285
	""" pinsources

		u'nendo', u'highsnobiety', u'kitchenkapers', u'thehappyhomeblog', u'net-a-porter', u'ericaweiner', u'saturdaysnyc', u'thebutternyc', u'curbed', u'bonobos', u'glamourboysinc', u'nest-living', u'anediblemosaic', u'yelp', u'sodapopgirl', u'grassrootsmodern', u'lyst', u'blogs', u'peacockplume', u'eol', u'ryanfeerer', u'andredaloba', u'bbcgoodfood', u'petsmart', u'swoopbags', u'blogg', u'simoneleblanc']
	"""
	return pinsources

def getnumbers(usernames,pinsources):
	pinner_list = db.pinners.find()
	numbers = [] #create a giant list of big lists by starting with an empty one
	for pinner in pinner_list: # loop through dictionary 
		onenumber = [] # this is individual big list
		for s in pinsources: # loop through the set
			# create a list so that [12, 0, 1, 23, 34 etc]
			number = pinner['pins'].get(s,0)
			if number > 1: 
				onenumber.append(number) # add to the data
				# stop when it ran out of pinsources 
	 			# and go back to pin_dict
		numbers.append(onenumber)
		# len(numbers) is 51
		# for number in numbers:
		# print "len(number) should be shorter", len(number) # it's 51 "4285"s !!!, eg, 
		""" numbers[2] is a list of 4285 digits
		"""
	return numbers

def getdomainnums(pinsources,numbers):
	pinner_list = db.pinners.find()

	n_height = len(numbers)
	n_width = len(numbers[0])
	domainnums = []
	for i in range(n_width):
		domainnums.append( [0] * n_height )
	for y in range(n_height):
		for x in range(n_width):
			domainnums[x][y] = numbers[y][x]

	"""domainnums

		[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
	"""
	return domainnums # a list of 15,000 lists that each has 51 digits

# def getdomainnums_b(pinsources,numbers):
# 	pinner_list = db.brands.find()

# 	n_height = len(numbers)
# 	n_width = len(numbers[0])
# 	domainnums = []
# 	for i in range(n_width):
# 		domainnums.append( [0] * n_height )
# 	for y in range(n_height):
# 		for x in range(n_width):
# 			domainnums[x][y] = numbers[y][x]

# 	"""domainnums

# 		[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# 	"""
# 	return domainnums # a list of 15,000 lists that each has 51 digits


def get_numbers(pinners, pinsources):
	numbers = []
	usernames = []
	for pinner in pinners:
		onenumber = []
		for pinsource in pinsources:
			number = pinner['pins'].get(pinsource,0)
			onenumber.append(number) 			
		numbers.append(onenumber)
		usernames.append(pinner['username'])
	return (usernames, numbers) # now the numbers are 51 lists of 4285 digits

def get_numbers_b(pinners, pinsources):
	numbers = []
	usernames = []
	for pinner in pinners:
		onenumber = []
		for pinsource in pinsources:
			number = pinner['users'].get(pinsource,0)
			onenumber.append(number) 			
		numbers.append(onenumber)
		usernames.append(pinner['brand'])
	return (usernames, numbers) # now the numbers are 51 lists of 4285 digits


def accessmongo(database):
	pin_dict = db.pinners.find() # return all dictionaries
	"""pin_dict
		{
	    "_id": {
	        "$oid": "5018c369e1d6bd1062ecd704"
	    },
	    "janew": {
	        "falconenamelware": 1,
	        "marketwire": 1,
	        "audubonbirdcall": 1,
	        "henryroad": 2,
	        "6pm": 1,
	        "stelton": 1,
	        "hearthsong": 2,
	        "no6store": 1,
	        "seavees": 2
	        }
	}
	"""
	all_pinners = list(db.pinners.find())
	pinsources = get_sources(all_pinners)
	# usernames = getusernames("datafiles/toppinners.txt")
	# pinsource = getpinsource(usernames)
	# pinsource,sourcecount = getpinsource(usernames)
	(usernames, numbers) = get_numbers(all_pinners, pinsources)
	return usernames, pinsources, numbers

def accessmongo_b(database):
	pin_dict = db.brands.find() # return all dictionaries
	all_pinners = list(db.brands.find())
	pinsources = get_sources_b(all_pinners)
	# usernames = getusernames("datafiles/toppinners.txt")
	# pinsource = getpinsource(usernames)
	# pinsource,sourcecount = getpinsource(usernames)
	(usernames, numbers) = get_numbers_b(all_pinners, pinsources)
	return usernames, pinsources, numbers


def pearson(v1,v2):
	# Simple sums
	sum1=sum(v1)
	sum2=sum(v2)
	# print "v1",v1
	# Sums of the squares
	sum1Sq=sum([pow(v,2) for v in v1])
	sum2Sq=sum([pow(v,2) for v in v2])
	# Sum of the products
	pSum=sum([v1[i]*v2[i] for i in range(len(v1))])
	# Calculate r (Pearson score)
	num=pSum-(sum1*sum2/len(v1))
	den=sqrt((sum1Sq-pow(sum1,2)/len(v1))*(sum2Sq-pow(sum2,2)/len(v1)))
	if den==0: return 0
	return 1.00-num/den

class bicluster:
	def __init__(self,vec,left=None,right=None,distance=0.0,id=None):
		self.left=left
		self.right=right
		self.vec=vec ## what is vec? 
		self.id=id
		self.distance=distance

def hcluster(rows,distance=pearson):
	## rows return # of pin sources for each user eg, 
	## ['michelle', 1,2,3,455,666]
	distances = {} ## create an empty dictionary of distances 
	currentclustid = -1 ## why start with -1
	# Clusters are initially just the rows 
	clust = [bicluster(rows[i],id=i) for i in range(len(rows))]
	# print "clust", clust
	print "clust", clust

	while len(clust)>1: # repeat until only one cluster remains
		lowestpair = (0,1) # what does that mean
		closest= distance(clust[0].vec, clust[1].vec)
		print "closest", closest

		#loop through every pair looking for the smallest distance
		for i in range(len(clust)):
			for j in range(i+1, len(clust)):
				# distances is the storage of distance calculation. 
				## it's good to store the correlation results for each pair 
				## until the items are merged into another cluster
				if (clust[i].id,clust[j].id) not in distances:
					distances[(clust[i].id,clust[j].id)] = distance(clust[i].vec,clust[j].vec)
					## not sure what this does...

				d = distances[(clust[i].id, clust[j].id)]
				print "d",d

				if d<closest:
					closest=d
					lowestpair=(i,j)

		# calculate the average of the two clusters
		mergevec = [ (clust[lowestpair[0]].vec[i]+clust[lowestpair[1]].vec[i])/2.0 for i in range(len(clust[0].vec)) ]
		print "mergevec = average of two clusters", mergevec
		# create the new cluster
		newcluster = bicluster(mergevec,left=clust[lowestpair[0]],right=clust[lowestpair[1]],distance=closest, id=currentclustid)
		print "newcluster", newcluster.left, newcluster.right

		# cluster ids that weren't in the original set are negative
		currentclustid -= 1 ## decrease count each time it's merged
		del clust[lowestpair[1]]
		del clust[lowestpair[0]]
		clust.append(newcluster)

	return clust[0]

def printclust(clust,labels=None,n=0):
	# indent to make a hierarchy layout
	for i in range(n): ## but n = 0???
		print '    '
		print clust.id
		if clust.id < 0:
			# negative id means that this is branch
			print '---'
		else: 
			# positive id means that this is an endpoint
			if labels == None: 
				print clust.id
			else: 
				print labels[clust.id]
		# now print the right and left branches
			if clust.left != None: 
				printclust(clust.left, labels=labels, n = n+1)
			if clust.right != None: 
				printclust(clust.right, labels=labels, n = n+1)

def getheight(clust):
	# Check if it is an endpoint? Then height is just 1
	if clust.left == None and clust.right == None: return 1
	# Otherwise the height is the same of heights of each branch
	## else is implicit here
	return getheight(clust.left) + getheight(clust.right)

def getdepth(clust):
	## need to know the total error of root node
	## error depth of a node is max poss error from each of branches
	# distance of endpoint is 0.0
	if clust.left == None and clust.right == None: 
		return 0
	# distance of branch is greater of two sides plus own distance
	return max(getdepth(clust.left),getdepth(clust.right))+clust.distance

def drawdendrogram(clust,labels,jpeg='clusters.jpg'):
	# height and width
	h = getheight(clust)*20
	w = 1200
	depth = getdepth(clust)

	# width is fixed, so scale distances accordingly
	scaling = float(w-150) / depth ### WHY w-150?

	# Create new image with a light blue background
	img = Image.new('RGB',(w,h),(153,204,255))
	draw = ImageDraw.Draw(img)

	draw.line((0,h/2,10,h/2),fill=(255,0,0))

	# Draw the first node
	drawnode(draw,clust,10,(h/2),scaling,labels)
	img.save(jpeg,'JPEG')

def drawnode(draw,clust,x,y,scaling,labels):
	if clust.id<0:
		h1 = getheight(clust.left)*20
		h2 = getheight(clust.right)*20
		top = y - (h1+h2)/2
		bottom = y +(h1+h2)/2
		# line length
		ll = clust.distance*scaling
		# Vertical line from this cluster to children
		draw.line((x,top+h1/2,x,bottom-h2/2),fill=(255,0,0))

		# Horizontal line to left item
		draw.line((x,top+h1/2,x+ll,top+h1/2),fill=(155,0,0))

		# Horizontal line to rigth item
		draw.line((x,bottom-h2/2,x+ll,bottom-h2/2),fill=(55,0,0))

		# Call the function to draw the left and right nodes
		drawnode(draw,clust.left,x+ll,top+h1/2,scaling,labels)
		drawnode(draw,clust.right,x+ll, bottom-h2/2,scaling,labels)
	else:
		# if this is an endpoint, draw the item label
		draw.text((x+5,y-7),labels[clust.id],(0,0,0))

def onesimilarity(rows,distance=pearson):
	similarity = {}
	print "len(rows)", len(rows)
	for i in range(1,len(rows)):
		print "rows[i]", rows[i]
		d = distance(rows[0],rows[i])
		if d != 1.0:
			similarity[i] = d
	return similarity

def kcluster(rows,distance=pearson,k=4): # default is 4 centroids
	# Determine the minimum and maximum values for each point
	ranges=[(min([row[i] for row in rows]),max([row[i] for row in rows])) for i in range(len(rows[0]))]
	# print "ranges", ranges
	# Create k randomly placed centroids
	clusters=[[random.random( )*(ranges[i][1]-ranges[i][0])+ranges[i][0]
		for i in range(len(rows[0]))] for j in range(k)]
	print len(clusters)
	lastmatches=None
	for t in range(10):
		print 'Iteration %d' % t
		bestmatches=[[] for i in range(k)]
		print "line 372", bestmatches

		# Find which centroid is the closest for each row
		for j in range(len(rows)):
			row=rows[j]
			bestmatch=0
			for i in range(k):
				d = distance(clusters[i],row)
				if d<distance(clusters[bestmatch],row): bestmatch=i
			bestmatches[bestmatch].append(j)
		
		# If the results are the same as last time, this is complete
		if bestmatches==lastmatches: 
			print "385", bestmatches
			break
		lastmatches = bestmatches

	# Move the centroids to the average of their members
		for i in range(k):
			avgs=[0.0]*len(rows[0])
			if len(bestmatches[i])>0:
				for rowid in bestmatches[i]:
					for m in range(len(rows[rowid])):
						avgs[m]+=rows[rowid][m]
				for j in range(len(avgs)):
					avgs[j]/=len(bestmatches[i])
				clusters[i]=avgs
	# print bestmatches
	""" evidence that it worked 
		$ python clusters.py
		ranges [(0, 11), (0, 23), (0, 6), (0, 7), (0, 7)]
		Iteration 0
		Iteration 1
		[[3], [1], [0, 2, 4, 5]]
	"""
	"""bestmatches

		[[1, 4, 5, 7, 8, 9, 13, 16, 17, 18, 19, 22, 24, 25, 29, 37, 46, 47, 49], 
		[0], [10, 12, 21, 30, 42], [2, 3, 11, 23, 27, 32, 33, 34, 35, 36, 38, 40, 41, 43, 50], [14], [], [6, 26, 39, 45, 48], [15, 20, 31, 44], [], [28]]
	"""
	return bestmatches, clusters

def maketuples(bestmatches,clusters): #easier to read than a tuple of (bestmatch,(15,000) long centroid)
	# return a list of tuples with centroid id
	zipped = zip(bestmatches, clusters)
	print "421", zipped
	return zipped

def makenodes(bestmatches,usernames): # a function to turn clusters from numbers to usernames
	raw_nodes = []
	# print len(usernames)
	i = 1
	for bestmatch in bestmatches: # [9,14,17,25]
		for x in bestmatch: # loop through 4 times
			node_dict = {}
			node_dict['name'] = usernames[x]
			node_dict['group'] = i
			# print node_dict
			raw_nodes.append(node_dict)
		i += 1  #  nodes:[{nodeName:"Myriel", group:1},
	"""raw_nodes

		[{'group': 1, 'nodeName': 1}, {'group': 1, 'nodeName': 4}, {'group': 1, 'nodeName': 7}, {'group': 1, 'nodeName': 8}, {'group': 1, 'nodeName': 9}, {'group': 1, 'nodeName': 10}, {'group': 1, 'nodeName': 13}, {'group': 1, 'nodeName': 16}, {'group': 1, 'nodeName': 17}, {'group': 1, 'nodeName': 19}, {'group': 1, 'nodeName': 20}, {'group': 1, 'nodeName': 22}, {'group': 1, 'nodeName': 24}, {'group': 1, 'nodeName': 25}, {'group': 1, 'nodeName': 29}, {'group': 1, 'nodeName': 37}, {'group': 1, 'nodeName': 46}, {'group': 1, 'nodeName': 47}, {'group': 3, 'nodeName': 26}, {'group': 4, 'nodeName': 3}, {'group': 4, 'nodeName': 6}, {'group': 4, 'nodeName': 23}, {'group': 4, 'nodeName': 27}, {'group': 4, 'nodeName': 31}, {'group': 4, 'nodeName': 32}, {'group': 4, 'nodeName': 33}, {'group': 4, 'nodeName': 34}, {'group': 4, 'nodeName': 35}, {'group': 4, 'nodeName': 36}, {'group': 4, 'nodeName': 38}, {'group': 4, 'nodeName': 40}, {'group': 4, 'nodeName': 41}, {'group': 4, 'nodeName': 42}, {'group': 4, 'nodeName': 43}, {'group': 4, 'nodeName': 45}, {'group': 4, 'nodeName': 50}, {'group': 5, 'nodeName': 2}, {'group': 5, 'nodeName': 11}, {'group': 5, 'nodeName': 15}, {'group': 5, 'nodeName': 48}, {'group': 6, 'nodeName': 5}, {'group': 6, 'nodeName': 12}, {'group': 6, 'nodeName': 18}, {'group': 6, 'nodeName': 28}, {'group': 6, 'nodeName': 30}, {'group': 6, 'nodeName': 44}, {'group': 6, 'nodeName': 49}, {'group': 7, 'nodeName': 0}, {'group': 7, 'nodeName': 39}, {'group': 8, 'nodeName': 21}, {'group': 9, 'nodeName': 14}]

	"""
	nodes = json.dumps(raw_nodes)
	# print "nodes 434", nodes
	return nodes

def makelinks(zipped, numbers,distance=pearson):
	raw_links = []
	i = 1 # centroid id
	# _id = 0
	for pair in zipped: 
		for _id in pair[0]: # 10, 12, etc.
			# turn id into a list of coordinates 
			dist_dict = {}
			number = numbers[_id]
			print "number 442", number
			print "pair[1] 443", pair[1]
			# distances['_id'] = _id
			dist_dict['value'] = distance(number,pair[1])
			# print distances['value']
			dist_dict['source'] = _id 
			dist_dict['target'] = i 
			raw_links.append(dist_dict)
			# print "each distance", dist_dict	
			# print links		
			# _id += 1
		i += 1
		# print "!!!links!!!", links
		"""raw_links len(raw_links)


			links = [{'centroid': 1, 'userid': 9, 'value': 0}, {'centroid': 1, 'userid': 17, 'value': 0}, {'centroid': 1, 'userid': 24, 'value': 0}, {'centroid': 1, 'userid': 25, 'value': 0}, {'centroid': 1, 'userid': 39, 'value': 0.11}]
		"""
	links = json.dumps(raw_links) # turns dict into a string for js update
	# print "links 463", links
	return links


def makecorr(bestmatches, brands, rows, distance=pearson):

	# [[1, 4, 5, 7, 8, 9, 13, 16, 17, 18, 19, 22, 24, 25, 29, 37, 46, 47, 49], 
	# [0], [10, 12, 21, 30, 42], [2, 3, 11, 23, 27, 32, 33, 34, 35, 36, 38, 40,
	# 41, 43, 50], [14], [], [6, 26, 39, 45, 48], [15, 20, 31, 44], [], [28]]

	# write a function that generate top 10 correlation coefficient 
	# target outcome is a list of dictionaries
	# [{ "Gucci": [{ 'brand' : name, 'correlation': .2 }, { 'brand': name, 'correlation': 0.4}, etc]} , ..] 
	corr = []
	for num in bestmatches[0]:
		brandpair = {}
		corrlist = []
		for othernum in bestmatches[0]:
			onecorr = {}
			d = distance(rows[num],rows[othernum])
			onecorr['brand'] = brands[othernum]
			onecorr['dist'] = d
			print "onecorr", onecorr, 
			corrlist.append(onecorr)

		corrlist = sorted(corrlist[:10], key=lambda k: k['dist'])
		print "***** corrlist ***** ", corrlist, 
		brandpair[brands[num]] = corrlist
		print "##### brandpair ##### ", brandpair
		# append to main list of dictionary
		corr.append(brandpair)
	return corr

def writejs(nodes,links): #for writing pinner json
	fo = open("pinners.json", "w")
	# fo.write( "var miserables = {\n")
	fo.write( "{\"nodes\": \n")
	fo.write(nodes)

	fo.write( ",\n  \"links\": \n")
	fo.write(links)
	fo.write("}")

	fo.close()

def writedjs(nodes,links): # for writing domain json
	fo = open("domains.json", "w")
	# fo.write( "var miserables = {\n")
	fo.write( "{\"nodes\": \n")
	fo.write(nodes)

	fo.write( ",\n  \"links\": \n")
	fo.write(links)
	fo.write("}")

	fo.close()
 
def writebjs(nodes,links): # for writing domain json
	fo = open("allbrands.json", "w")
	# fo.write( "var miserables = {\n")
	fo.write( "{\"nodes\": \n")
	fo.write(nodes)

	fo.write( ",\n  \"links\": \n")
	fo.write(links)
	fo.write("}")

	fo.close()


def scaledown(data,distance=pearson, rate=0.01):
# view data in multidimensional scaling (vs. dendrogram's two dimension flowchart)
	n = len(data)
	# The real distances between every pair of items
	realdist = [[ distance(data[i],data[j]) for j in range(n)] 
			for i in range(0,n)]
	outersum = 0.0 
	# Randomly initialize the starting points of locations in 2D
	## for each datapoint in data
	loc = [[ random.random(), random.random()] for i in range(n)]
	fakedist = [[0.0 for j in range(n)] for i in range(n)]
	## WHAT DOES THIS DO??  Why do we need that?
	### so fakedist = [ [0 x n] , [0 x n] , [0 x n] (total of n)]
	##### Oh, its just defining a variable that is a list of lists.. i think

	lasterror = None  ## define a variable called lasterror
	for m in range(0,1000):
		# Find projected distances
		for i in range(n):
			for j in range(n):
				fakedist[i][j] = sqrt(sum([pow(loc[i][x] - loc[j][x],2)
					for x in range(len(loc[i]))])) # <= that's the longest ")]]" i've seen
			# what the f does this do??

	# Move points
		grad = [[0.0, 0.0] for i in range(n)] ## create a variable called grad

		totalerror = 0
		for k in range(n):
			for j in range(n):
				if j==k:
					continue
				# The error is percent difference between the distances
				## makes sense
				errorterm = (fakedist[j][k]-realdist[j][k])/realdist[j][k]

				# Each point needs to be moved away from or towards the other
				# point in proportion to how much error it has
				grad[k][0] += ((loc[k][0] - loc[j][0]) / fakedist[j][k]) * errorterm
				grad[k][1] += ((loc[k][1] - loc[j][1]) / fakedist[j][k]) * errorterm

				# Keep track of the total error
				totalerror += abs(errorterm)
			print totalerror

		# If the answer got worse by moving the points, we are done
		if lasterror and lasterror<totalerror: 
			break
		lasterror = totalerror

		# Move each of the points by the learning rate times the gradient
		for k in range(n):
			loc[k][0] -= rate*grad[k][0]
			loc[k][1] -= rate*grad[k][1]

	return loc

def draw2d(data,labels,output="mds2d.png"):
	img = Image.new('RGB',(2000,2000),(255,255,255))
	draw = ImageDraw.Draw(img)
	for i in range(len(data)):
		x=(data[i][0]+0.5) * 1000
		y=(data[i][1]+0.5) * 1000
		draw.text((x,y), labels[i], (0,0,0))
	img.save(output,'PNG')


def connect_db():
	connect_string = "mongodb://pinterestalgo:pinterest2012@ds035617.mongolab.com:35617/pinterest"
	# mongodb://%s:%s@%s:%d/%s" % \
 #            (user, password, host, port, db_name)
	c = pymongo.connection.Connection(connect_string)
	return c['pinterest']

def connect_db_b(): # changed for brands db 
	connect_string = "mongodb://pinterestalgo:pinterest2012@ds037047.mongolab.com:37047/brands"
	# mongodb://%s:%s@%s:%d/%s" % \
 #            (user, password, host, port, db_name)
	c = pymongo.connection.Connection(connect_string)
	return c['brands']

p = None

def main():
	global db, p
	# db = connect_db()
	# usernames,pinsources,numbers = accessmongo(db)	
	db = connect_db_b()
	brands,pinners,numbers = accessmongo_b(db)
	print "usernames but should be brands", brands
	print "pinsources but should be pinners", pinners
	print "length of pinners", len(pinners)	
	# brands = 43, users = 1143

	print "numbers should just be numbers", numbers

	# usernames = ["mic", "jess", "andree", "lauren","laura","ashley"]
	# pinsource = ["tumblr","goog","amazon","mongo", "printer"]
	# numbers = [ [0,0,3,4,5],[9,2,0,0,0],[0,0,4,6,7],[11,23,4,0,0],[0,0,4,5,0],[0,0,6,7,0]]
	# # clust = hcluster(numbers)
	### THIS WORKS ###
	# printclust(clust,labels=usernames,6)
	# drawdendrogram(clust,labels=usernames,jpeg='pinclust.jpg')
	# print "two important lengths", len(numbers) , len(numbers[0]) #51 4285

	# similarity = onesimilarity(numbers)
	# print similarity

	# # bestmatches, clusters = kcluster(numbers,k=10)

	# zipped = maketuples(bestmatches,clusters)
	# links = makelinks(zipped,numbers)
	# nodes = makenodes(bestmatches,brands)
	# writebjs(nodes,links)

	bestmatches = [[11, 14, 24, 37, 70, 176, 183, 249, 344, 354, 357, 371, 422, 433, 470, 491, 520], [0, 4, 7, 18, 25, 27, 36, 46, 61, 67, 76, 107, 129, 134, 135, 138, 139, 146, 147, 155, 161, 163, 178, 193, 195, 207, 229, 240, 275, 294, 301, 302, 308, 345, 359, 362, 368, 389, 390, 403, 409, 427, 437, 439, 445, 449, 464, 486, 498, 503, 504, 508, 512, 526, 527, 531, 541, 547], [2, 3, 49, 57, 110, 124, 136, 152, 170, 191, 233, 271, 298, 323, 330, 339, 385, 441, 447, 466, 474, 485, 511, 532, 536], [9, 16, 28, 30, 33, 55, 59, 68, 77, 82, 96, 100, 101, 105, 106, 114, 123, 156, 164, 197, 222, 225, 235, 260, 264, 268, 273, 279, 283, 306, 326, 329, 335, 373, 406, 418, 419, 424, 469, 482, 501, 506, 528], [6, 20, 34, 35, 38, 45, 88, 93, 120, 125, 140, 141, 166, 182, 185, 190, 204, 220, 226, 230, 288, 311, 347, 352, 361, 365, 387, 398, 404, 414, 423, 432, 443, 446, 450, 467, 478, 489, 500, 517, 539, 545, 546, 548], [1, 19, 21, 26, 47, 48, 50, 52, 58, 63, 72, 83, 90, 91, 94, 98, 108, 122, 144, 148, 149, 162, 173, 186, 189, 202, 205, 210, 224, 232, 237, 242, 243, 247, 248, 258, 263, 265, 270, 272, 289, 290, 293, 296, 299, 300, 310, 315, 318, 319, 325, 340, 350, 358, 377, 386, 394, 400, 402, 407, 415, 438, 453, 455, 460, 463, 465, 472, 475, 481, 483, 492, 515, 519, 522, 540, 549, 552, 555], [5, 8, 13, 22, 39, 44, 51, 56, 74, 75, 79, 86, 95, 97, 99, 103, 109, 112, 115, 117, 118, 121, 132, 133, 150, 160, 165, 167, 168, 172, 181, 184, 199, 201, 206, 208, 209, 211, 212, 213, 214, 216, 218, 221, 227, 228, 234, 236, 238, 244, 245, 246, 255, 259, 261, 266, 269, 276, 277, 285, 287, 291, 304, 307, 309, 314, 317, 320, 322, 324, 328, 331, 333, 338, 341, 346, 348, 355, 364, 369, 374, 379, 388, 391, 392, 395, 401, 405, 410, 417, 420, 430, 435, 448, 452, 456, 462, 468, 471, 480, 484, 487, 488, 496, 497, 499, 510, 513, 514, 516, 518, 524, 529, 530, 534, 535, 542, 543, 553], [10, 15, 17, 40, 53, 62, 66, 81, 85, 113, 119, 128, 137, 145, 151, 153, 159, 177, 179, 187, 200, 217, 231, 257, 280, 282, 286, 295, 303, 327, 332, 334, 342, 356, 360, 367, 372, 383, 436, 454, 458, 476, 502, 521], [23, 41, 64, 69, 71, 80, 84, 89, 102, 104, 127, 130, 131, 142, 143, 154, 157, 158, 169, 171, 180, 194, 196, 198, 203, 219, 223, 239, 250, 251, 252, 253, 254, 262, 278, 292, 297, 316, 321, 337, 343, 349, 353, 376, 378, 381, 382, 384, 396, 397, 399, 408, 411, 416, 421, 426, 429, 434, 440, 442, 444, 451, 457, 459, 461, 479, 495, 505, 523, 533, 537, 538, 544, 551, 554, 556], [12, 29, 31, 32, 42, 43, 54, 60, 65, 73, 78, 87, 92, 111, 116, 126, 174, 175, 188, 192, 215, 241, 256, 267, 274, 281, 284, 305, 312, 313, 336, 351, 363, 366, 370, 375, 380, 393, 412, 413, 425, 428, 431, 473, 477, 490, 493, 494, 507, 509, 525, 550]]

	corr = makecorr(bestmatches,brands,numbers)
	print corr
	# sort to get the top 10 of this list

## for transforming domain matrix DONT TOUCH ###
	# domainnums = getdomainnums(pinsources,numbers) 
	# bestmatches, clusters = kcluster(domainnums,k=100)

	# zipped = maketuples(bestmatches,clusters)
	# links = makelinks(zipped,domainnums)
	# nodes = makenodes(bestmatches,pinsources)
	# writebjs(nodes,links)


if __name__ == '__main__':
	main()


