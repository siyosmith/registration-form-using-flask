from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('forms.html')

# @app.route('/<int:num>')
# def number(num):
#     return f'number is {num}'

# @app.route('/orders/<int:num1>')
# def numb(num1):
#     if num1<18:
#         return "not allowed"

#     return 'allowed'


# @app.route('/fact/<int:number>')
# def factor(number):
#     factt=1
#     if number==0:
#         return '1'
#     elif number<0:
#         return "sorry"
#     else:
#         for i in range(1,number+1):
#             factt=factt*i
#         return f'{factt}'       

    

    


# @app.route('/abouts')
# def myntra():
#     return render_template('forms.html')

@app.route('/abou',methods=['POST'])
def regis():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    return render_template('table.html', fname=fname, lname=lname, email=email)

if __name__=='__main__':
    app.run(debug=True)