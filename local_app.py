# imports
from urllib.request import urlopen as url_req

import certifi
import pymongo
import requests
from bs4 import BeautifulSoup as bs
from flask import Flask, request, render_template

app = Flask(__name__)  # initialising the flask app with the name 'local_app'


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        searchString = request.form['content'].replace(" ", "-")  # Obtaining the search string entered in the form
        try:
            ca = certifi.where()

            dbConn = pymongo.MongoClient(
                f"mongodb+srv://sach7:sach7@cluster0.mhg7e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
                tlsCAFile=ca)
            # Add <userID> & <Password> for MongoDB Atlas cloud

            # dbConn = pymongo.MongoClient("mongodb://localhost:27017/") # Opening a connection with MongoDB Compass (Local)
            db = dbConn[
                'reviewScrapperDB']  # Connecting to (or Creating if not available) the database called reviewScrapperDB
            reviews = []  # initializing an empty list for reviews

            if searchString in db.list_collection_names():  # if there is a collection with searched keyword, and it has record in it.
                reviews = list(db[searchString].find())
                return render_template('result.html', reviews=reviews)  # Show the result to user
            else:
                # 'iphone7' is a string and following webpage is used for testing
                # https://www.flipkart.com/apple-iphone-7-jet-black-128-gb/p/itmen6dakdgkpy6n?pid=MOBEMK62VCQ2UMT8&lid=LSTMOBEMK62VCQ2UMT8IY1JYN&marketplace=FLIPKART&q=iphone7&store=tyy%2F4io&srno=s_1_2&otracker=search&iid=50a7bb2d-9366-4d0e-8d4d-320cc0788c53.MOBEMK62VCQ2UMT8.SEARCH&ssid=dwdokklwdc0000001644130287471&qH=c848b7081ba96a14

                flipkart_url = 'https://www.flipkart.com/search?q=' + searchString  # preparing a URL to search the product on flipkart
                req_page = url_req(flipkart_url)  # Requesting the webpage from the internet
                flipkart_page = req_page.read()  # Reading the webpage
                req_page.close()  # closing the connection ti the web server
                flipkart_html = bs(flipkart_page, 'html.parser')  # Parsing the webpage as HTML
                bigboxes = flipkart_html.findAll('div', {
                    'class': '_1AtVbE col-12-12'})  # searching for appropriate tag to redirect to product link
                del bigboxes[
                    0:3]  # the first 3 members of the list does not contain relevent information, hence deleted.
                box = bigboxes[0]  # taking the first iteration (for demo)
                productLink = 'https://www.flipkart.com' + box.div.div.div.a[
                    'href']  # extracting the actual product link
                prod_page = requests.get(productLink)  # Getting the product page from server
                prod_html = bs(prod_page.text, 'html.parser')  # parsing the product page as HTML
                commentboxes = prod_html.find_all('div', {
                    'class': '_16PBlm'})  # finding the HTML section containing the customer comments

                table = db[searchString]

                # iterating over the comment section to ger the details of customer and their comments

                for commentbox in commentboxes:
                    try:
                        name = commentbox.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text
                    except:
                        name = "No Name"

                    try:
                        rating = commentbox.div.div.div.div.text
                    except:
                        rating = "No Rating"

                    try:
                        commentHead = commentbox.div.div.div.p.text
                    except:
                        commentHead = "No Comment Heading"

                    try:
                        comments = commentbox.div.div.find_all('div', {'class': ''})
                        cust_comments = comments[0].div.text
                    except:
                        cust_comments = "No Customer Comment"

                    mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
                              "Comment": cust_comments}  # Saving all details to dictionary
                    table.insert_one(
                        mydict)  # inserting the dictionary containing the review comments to the collection
                    reviews.append(mydict)
                return render_template('result.html', reviews=reviews)  # showing review to the user
        except:
            return 'Something is Wrong'
    else:
        return render_template('index.html')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(port=8000, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
