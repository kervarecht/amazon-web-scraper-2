from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
import requests
from bs4 import BeautifulSoup
import re
import json
import sys
from scraper import amazon_deals, amazon

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/deals', methods=['GET'])
def result():
    target = request.query_string.decode('UTF-8')
    amazon_response = amazon_deals(target)
    return(jsonify(amazon_response))



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
