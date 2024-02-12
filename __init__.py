from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') #comm2

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route('/paris/')
def meteo():
    response = urlopen('https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fsamples.openweathermap.org%2Fdata%2F2.5%2Fforecast%3Flat%3D0%26lon%3D0%26appid%3Dxxx&data=05%7C02%7Celawson4%40myges.fr%7C30939271ffac424e273a08dc2bdfa3f1%7Cc371d4f5b34f4b069e66517fed904220%7C0%7C0%7C638433486745400761%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=0ZYCDtEDjudI3uiqTJVDBUv8DnZsCimaXdlYdFMVcgk%3D&reserved=0')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15 # Conversion de Kelvin en °c
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)
  
@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

@app.route("/histogramme/")
def monhistogramme():
    return render_template("histogramme.html")
  
@app.route("/commits/")
def commits():
    return render_template("commits.html")
  
if __name__ == "__main__":
  app.run(debug=True)
