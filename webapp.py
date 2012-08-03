from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import os
import sys
import beautifulsoup as bs
import find_pin as fp
import traceback

#create our application! :) 
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent = True)
# allow environment variable called FLASKR SETTINGS, 
# not complain if no such env key is set

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/source_", methods=['GET'])
def pin2():
	username = "username"
	board_url_list = []	
	board_list = fp.find_board_list(username)
	renamed_list = fp.transform_boardname(board_list)
	for board in renamed_list: 
		# print find_board_url(username,board)
		if fp.find_board_url(username, board) == None: 
			continue
		if len(fp.find_board_url(username, board)) == 0:
			continue
		else:
			board_url_list.extend(fp.find_board_url(username, board))
	pin_source_list = fp.make_pin_source_list(board_url_list)
	source_count = fp.count_source(pin_source_list)
	return source_count
	return render_template("source.html", source_count=source_count)

@app.route("/source", methods=['GET'])
def pin():
	username = "username"
	soup = bs.get_soup("http://pinterest.com/%s"%username)
	noimage = bs.get_image(soup)
	link_list = bs.get_link_list(noimage) 
	etsy_soup = bs.get_soup("http://www.etsy.com/listing/102135880/rainbow-summer-chevron-stripes-pride")
	etsy_links = bs.get_etsy(etsy_soup)
	etsy_pinobjects = []
	for link in etsy_links:
		print link
		try:
			etsy_pin = Pin(link)
			bs.etsy_pinobjects.append(etsy_pin)
		except Exception, e:
			traceback.print_exc()
	pin = Pin("http://www.etsy.com/listing/102135880/rainbow-summer-chevron-stripes-pride")
	# return etsy_pinobjects
	return render_template("source.html", item_title = pin.item_title, price=pin.price )

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)