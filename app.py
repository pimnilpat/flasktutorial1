
from init import init
from json_encoder import json

i = init()
i.__init__
app = i.get_init()

@app.route("/", methods=["GET"])
def index():
    #dict_string = dict.fromkeys(app.config)
    
    return str(app.te)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)

# print(app.config["APPLICATION_NAME"])
# print(app.config["APPLICATION_DESCRIPTION"])
# print(app.config["ENV"])
# print(app.config["PERMANENT_SESSION_LIFETIME"])
# print(app.config["SECRET_KEY"])
# print(app.config["DEBUG"])

# print(type(str(app.config["DEBUG"])))



