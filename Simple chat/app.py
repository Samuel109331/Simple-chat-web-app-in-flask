from flask import Flask,redirect,render_template
from flask_restful import Api,Resource




messages = []

app = Flask(__name__)
api = Api(app)

class SendMessages(Resource):
    def get(self,username,message):
        global messages
        if username != "" and message != "":
            response= {
                "username" : username,
                "message" : message
            }
            messages.append(response)
            return {"messages" : messages}
        else:
            return {"message": "both username and message is required"}
        
class GetMessages(Resource):
    def get(self):
        global messages
        return {"messages" : messages}


        
api.add_resource(SendMessages,"/chat/<string:username>/<string:message>")
api.add_resource(GetMessages,'/chat/getmessages')


@app.route("/")
def homePage():
    return render_template("home.html")

@app.route("/start")
def chatApp():
    return render_template("chat.html")


if __name__ == '__main__':
    app.run(debug=True)