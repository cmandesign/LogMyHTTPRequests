
import datetime
import os
from flask import Flask, jsonify, request
import codecs

app = Flask(__name__)


@app.route('/<path:any>', methods=['POST'])
def catchItPOST (any):
    today = datetime.datetime.today()
    file_url = today.strftime("%Y-%m-%d") + ".log"
    with codecs.open(file_url, 'a', "utf-8") as the_file:
        the_file.write("IP: " + str(request.remote_addr) + '\n')
        the_file.write("Time: " + today.strftime("%Y-%m-%d %H:%M:%S") + '\n')
        the_file.write("URL: " + unicode(request.url) + '\n')
        the_file.write("Headers: \n" + unicode(request.headers) + '\n')
        the_file.write(u"Body: \n" + unicode(request.data) + u'\n===================================================\n')

    return jsonify(True)


@app.route('/<path:any>', methods=['GET'])
def catchItGET (any):
    today = datetime.datetime.today()
    file_url = today.strftime("%Y-%m-%d") + ".log"
    with codecs.open(file_url, 'a', "utf-8") as the_file:
        the_file.write("IP: " + str(request.remote_addr) + '\n')
        the_file.write("Time: " + today.strftime("%Y-%m-%d %H:%M:%S") + '\n')
        the_file.write("URL: " + unicode(request.url) + '\n')
        the_file.write("Headers: \n" + unicode(request.headers) + '\n')
        the_file.write(u"QueryString: \n" + unicode(request.query_string) + u'\n===================================================\n')

    return jsonify(True)


app.run(host="0.0.0.0", port="8080", debug=True)
