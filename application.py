from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

from flask_mail import Mail, Message


application=Flask(__name__)
app=application

mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
#app.config['MAIL_USERNAME'] = 'experimentaws@gmail.com'
#app.config['MAIL_PASSWORD'] = 'iNeuron@interns'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

#mail = Mail(app)


@app.route('/',methods=['GET']) #route to display the home
@cross_origin()
def homepage():
    return render_template("index.html")

@app.route('/send',methods=['POST','GET']) #route to show predicting result in a web UI
@cross_origin()
def index():
    if request.method=='POST':
        try:
            #reading the inputs given by the user
            sm = str(request.form['sendermail'])
            sp = str(request.form['senderpassword'])
            rm = str(request.form['receivermail'])
            body = str(request.form['body'])

            app.config['MAIL_USERNAME'] = sm
            app.config['MAIL_PASSWORD'] = sp
            mail = Mail(app)

            msg = Message('Hello', sender=sm, recipients=[rm])
            msg.body = body
            mail.send(msg)
            #return "Sent"


            return render_template('results.html')#,prediction=round(prediction[0],2))

        except Exception as e:
            return 'Error showing: {}'.format(e)

    else:
        return  render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)

