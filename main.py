
from flask import Flask, render_template, request, redirect, url_for,flash

import webbrowser
from threading import Timer


app = Flask(__name__)


msg = "זכית בזוג כרטיסים לקבלת הפרס מלא את הפרטים בלינק הבא :\n"
msg = "https://ticketsforyou.000webhostapp.com/ " + msg
subject = "זכית!!!"



num_of_emp = 0

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
            return redirect('website')
        elif attack_type == 'message':
            # Execute code for message attack
            return redirect(url_for('message'))
        elif attack_type == 'whatsapp':
            # Execute code for WhatsApp attack
            return redirect(url_for('whatsapp'))
        elif attack_type == 'showdata':
            # Execute code for WhatsApp attack
            return showdata()
        else:
            # Handle invalid option
            return "Invalid option selected"


def showdata():
    from statistics import show_statistics

    show_statistics()
    return render_template('homePage.html')


@app.route('/mail')
def mail():
    # Code for mail attack
    return render_template('mails.html')


@app.route('/submit-mail', methods=['POST'])
def submit_mail():

    from send_mails import mail_attack
    # Code for mail attack
    global num_of_emp

    if request.method == 'POST':
        mails_list = request.form['name-list']
        mail_post = request.form['mail-post']
        mails = mails_list.split(',')
        num_of_emp = len(mails)
        for mail in mails:
            mail = mail + '@' + mail_post
            str = mail_attack(mail)
    return redirect(url_for('mail'))


@app.route('/website')
def website():
    # Code for website attack
    return render_template('website.html')


@app.route('/submit-whatsapp', methods=['POST'])
def submit_whatsapp():

    from whatsapp_attack import whatsapp_atk_using_twilio

    # Code for mail attack
    global num_of_emp

    if request.method == 'POST':
        mobile_numbers = request.form['mobile-numbers']
        numbers = mobile_numbers.split(',')
        num_of_emp = len(numbers)
        for mobile in numbers:
            whatsapp_atk_using_twilio(mobile)

    return redirect(url_for('whatsapp'))



@app.route('/message')
def message():
    # Code for message attack
    return render_template('message.html')

@app.route('/submit-message', methods=['POST'])
def submit_message():

    from sms_sender import send_sms

    # Code for mail attack
    global num_of_emp
    if request.method == 'POST':
        mobile_numbers = request.form['mobile-numbers']
        numbers = mobile_numbers.split(',')
        num_of_emp = len(numbers)
        for mobile in numbers:
            send_sms(mobile)
    return redirect(url_for('message'))


@app.route('/whatsapp')
def whatsapp():
    # Code for WhatsApp attack
    return render_template('whatsapp.html')


def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")


if __name__ == '__main__':
    Timer(1, open_browser).start()
    # app.run(debug=True)

    app.run()
