from flask import Flask
from flask import request
from flask import redirect


app = Flask(__name__)

def super_cool_logic():
    return redirect("http://localhost:8000")

@app.route('/', methods=['POST', 'GET'])

def hello():
    a = request.form.get('number1')
    b = request.form.get('number2')
    
    # return "olá" + super_cool_logic()
    return  "<h1>"+ "O resultado X("+ a+ ") * Y("+b+") é : " +str(int(a) * int(b)) + "</h1>" + "<br><br>" + "<a href='http://localhost:8000'>refazer</a>"
# def super_cool_logic():
#     return redirect("http://localhost:8000")


if __name__ == '__main__':
    app.run()

# def conta(req, res):
#     a = res.number1 * res.number2
#     return a;