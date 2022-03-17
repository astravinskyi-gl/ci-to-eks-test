from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'REGULAR TEST 19:30'

app.run(host='0.0.0.0', port=81)

# def print_hi(name):
#     i = 1
#     while i == 1:
#         print("SUPER TEST 19:00")
    
# print_hi("everyone")
