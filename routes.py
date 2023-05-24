from __main__ import app

# The default functions contained in this file match with the base.html values

# Don't change the function names

@app.route("/") # Main page, containing list of users
def main():
    pass

@app.route("/login") # Login page, handles both get and post
def login():
    pass

@app.route("/signup") # Signup page, handles both get and post
def signup():
    pass

@app.route("/createpost") # Create post page, handles both get and post
def create_post():
    pass

@app.route("/logout") # get is essentially post, handles logout
def logout():
    pass

