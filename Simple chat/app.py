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
    
class DeleteMessages(Resource):
    def get(self):
        global messages
        messages.clear()
        return {"message" : "chat cleared"}


        
api.add_resource(SendMessages,"/chat/<string:username>/<string:message>")
api.add_resource(GetMessages,'/chat/getmessages')
api.add_resource(DeleteMessages,'/chat/delete')

@app.route("/")
def homePage():
    return render_template("home.html")

@app.route("/start")
def chatApp():
    return render_template("chat.html")


if __name__ == '__main__':
    app.run()
