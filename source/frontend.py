import random
import re
import sys
import html
import requests
from flask import Flask, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def main():
    displaytext= ""
    response = requests.get("http://10.0.3.10:8989/checkout")
    if response.status_code == 200:
        checkoutresponse= "200 OK"
    else:
        checkoutresponse= "[{Error:'Checkout endpoint is not responding!!'}]"

    response = requests.get("http://10.0.3.11:8990/ad")
    if response.status_code == 200:
        adresponse= "200 OK"
    else:
        adresponse== "[{Error:'ad endpoint is not responding!!'}]"

    response = requests.get("http://10.0.3.12:8991/recommend")
    if response.status_code == 200:
        recommendresponse= "200 OK"
    else:
        recommendresponse = "[{Error:'Recommend endpoint is not responding!!'}]"

    response = requests.get("http://10.0.3.15:8994/productcatalog")
    if response.status_code == 200:
        productcatalogresponse= "200 OK"
    else:
        productcatalogresponse= "[{Error: 'Productcatalog endpoint is not responding!!'}]"

    response = requests.get("http://10.0.3.16:8995/shipping")
    if response.status_code == 200:
        shippingresponse= "200 OK"
    else:
        shippingresponse= "[{Error: 'shipping endpoint is not responding!!'}]"

    response = requests.get("http://10.0.3.17:8996/currency")
    if response.status_code == 200:
        currencyresponse= "200 OK"
    else:
        currencyresponse= "[{Error: 'Currency endpoint is not responding!!'}]"

    response = requests.get("http://10.0.3.18:8997/carts")
    if response.status_code == 200:
        cartsresponse= "200 OK"
    else:
        cartsresponse= "[{Error: 'Currency endpoint is not responding!!'}]"

    return render_template('index.html', title="page", checkout=checkoutresponse, ad=adresponse, recommend=recommendresponse, productcatalog=productcatalogresponse, shipping=shippingresponse, currency=currencyresponse, carts=cartsresponse)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
