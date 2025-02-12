from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def register():
    return render_template('sign-up.html')

@app.route('/app', methods=['POST'])
def registration():
    Name=request.form.get('user_ka_name')
    Mail_id=request.form.get('user_ka_email_id')
    Password=request.form.get('user_ka_password')
    Confirmed_Password=request.form.get('user_ka_confirmed_password')
    return Name + " " + Mail_id + " " + Password + " " + Confirmed_Password
    

if __name__ == "__main__": 
    app.run(debug=True)