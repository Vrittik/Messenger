from flask import Flask,send_from_directory
from memebot import opencv123
from flask import request
from memebot import downloader
from pymessenger.bot import Bot

bot = Bot("EAACzAIK1v8QBAKkekJZCHMHJNnSkEcyN2SHD7lGfKsmd3vukvmCbC3yA8e5PUkMEKqv9ndR0rQe3M7PSkC6NyZCZACWO0VZAQjvL93wjPRMF9p7uf6MObrkReGFCIkA9gS957wAG2SgzRKQtH7wgcqTW9a1X6ZC0Ept3sJZCQHzmZAmUfI2Lpjy")
server_loc="https://9f9c30d2.ngrok.io/"
app = Flask(__name__)

@app.route("/temp/<path>", methods=["GET"])
def images(path):
    return send_from_directory("temp",path)




@app.route("/", methods=["GET"])
def verify():
    if request.args.get("hub.challenge"):
        return request.args.get("hub.challenge")
    else :
        return "Please run it on facebook dev"


@app.route("/", methods=["POST"])
def message():

    data = request.get_json()

    print(data)

    if data.get("entry"):
        for entry in data["entry"]:
            if entry.get("messaging"):
                for message in entry["messaging"]:
                    if message.get('message'):
                        # Facebook Messenger ID for user so we know where to send response back to
                        user = message['sender']['id']
                        if message['message'].get('text'):
                            text = message['message']['text'] + " by bot"
                            bot.send_text_message(user, text)

                        if message['message'].get('attachments'):  #json beautifier query
                                for attachment in message['message']['attachments']:
                                    link = attachment['payload']['url']

                                    loc=downloader.download(link)
                                    
                                    bot.send_image_url(user, server_loc+loc)
    return "Message recieved"

app.run()