from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'CI helper marker'

app.run(host='0.0.0.0', port=60080)

#new test fail

# def print_hi(name):
#     i = 1
#     while i == 1:
#         print("Hello " + name + " , it is the message from the test app")
# print_hi("everyone")
