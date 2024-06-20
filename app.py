# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/index")
def home():

    name = "Armaan Kapoor" # write your name
    age = "13" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def home():

    name =" Pankaj Kapoor" # write your name
    age = "45" # write your age

    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def home():

    name = "Diksha Kapoor" # write your name
    age = "41" # write your age

    return render_template('mother.html' , name = name , age = age)

# define the route to friends webpage]
@app.route("/friend")
def home():

    name = "Taj Singh" # write your name
    age = "12" # write your age

    return render_template('friend.html' , name = name , age = age)


# add other routes, if you want
@app.route("/sister")
def home():

    name = "Pawthny Kapoor" # write your name
    age = "11" # write your age

    return render_template('sister.html' , name = name , age = age)




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
