from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homePage.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        attack_type = request.form['attack_type']
        if attack_type == 'mail':
            # Execute code for mail attack
            return redirect(url_for('mail'))
        elif attack_type == 'website':
            # Execute code for website attack
            return redirect(url_for('website'))
        elif attack_type == 'message':
            # Execute code for message attack
            return redirect(url_for('message'))
        elif attack_type == 'whatsapp':
            # Execute code for WhatsApp attack
            return redirect(url_for('whatsapp'))
        else:
            # Handle invalid option
            return "Invalid option selected"

@app.route('/mail')
def mail():
    # Code for mail attack
    return render_template('mails.html')

@app.route('/website')
def website():
    # Code for website attack
    return render_template('website.html')

@app.route('/message')
def message():
    # Code for message attack
    return render_template('message.html')

@app.route('/whatsapp')
def whatsapp():
    # Code for WhatsApp attack
    return render_template('whatsapp.html')

if __name__ == '__main__':
    app.run(debug=True)