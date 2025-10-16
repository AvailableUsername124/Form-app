from flask import Flask, url_for, render_template, request
import random

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

#Perpexlity link to when I used AI: https://www.perplexity.ai/search/how-do-i-make-it-so-that-in-py-yrs8MAysTG6OXh8Mpcw_zQ

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p2")
def render_page2():
    return render_template('page2.html')
    
@app.route("/p1")
def render_page1():
    return render_template('page1.html')

@app.route("/response")
def render_response():
    dogcat = request.args['dogcat']
    if dogcat.lower() == 'dogs':
        responses = ["Husky", "GoldenRetriever", "Beagle", "Bulldog", "Poodle", "Corgi", "Affenpinscher", "Rottweiler", "Chihuahua"]
        reply1 = random.choice(responses)
    elif dogcat.lower() == 'cats':
        responses = ["ExoticShortHair", "RussianBlue", "AmericanWireHair", "Birman", "MaineCoon", "Ragdoll", "Ragamuffin", "SelkirkRex"]
        reply1 = random.choice(responses)
    else:
        reply1 = "only enter cats or dogs"
        return render_template('response.html', response1=reply1)
    
    n = int(request.args['multNum'])
    reply2 = str((2*n))
    return render_template('response.html', response1 = reply1 + reply2 )
    
if __name__=="__main__":
    app.run(debug=True)
