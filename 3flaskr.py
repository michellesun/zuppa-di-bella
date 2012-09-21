from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("forceddirected1.html")

@app.route("/pinners")
def pinners(nodes,links):
	fo = open("pinners.json", "w")
	# fo.write( "var miserables = {\n")
	fo.write( "{\"nodes\": \n")
	fo.write(nodes)

	fo.write( ",\n  \"links\": \n")
	fo.write(links)
	fo.write("}")

	fo.close()
	return render_template("domains.html", json_data=domains.js)

if __name__ == '__main__':
    app.run()

