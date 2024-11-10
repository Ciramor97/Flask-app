from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    # Fetch data from GitHub API, for example, public repositories of a specific user
    username = "Ciramor97"  # Replace with any GitHub username
    url = f"https://api.github.com/users/{username}/repos"
    
    # Make a GET request to fetch the data
    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()  # Parse the JSON data
        # transform json data in csv ()
        repos = traitement("fichier.csv")
        # import csv file and make traitement
        # Call your faonction to make the traitment
    else:
        repos = []  # Empty list if request fails
    
    # Render the data on the HTML page
    return render_template('index.html', repos=repos)

if __name__ == "__main__":
    app.run(debug=True)
