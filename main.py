from flask import Flask, render_template, request
from post import Post 
import requests

blog_data = requests.get("https://api.npoint.io/e6f5688753dec2463132").json()
post_objects = []
post_obj_id_1 = (blog_data[0]["id"])
post_obj_title_1 = (blog_data[0]["title"])
post_obj_subtitle_1 = (blog_data[0]["subtitle"])
post_obj_body_1 = (blog_data[0]["body"])
post_obj_1 = Post(post_obj_id_1,post_obj_title_1,post_obj_subtitle_1,post_obj_body_1)
post_objects.append(post_obj_1)

post_obj_id_2 = (blog_data[1]["id"])
post_obj_title_2 = (blog_data[1]["title"])
post_obj_subtitle_2 = (blog_data[1]["subtitle"])
post_obj_body_2 = (blog_data[1]["body"])
post_obj_2 = Post(post_obj_id_2,post_obj_title_2,post_obj_subtitle_2,post_obj_body_2)
post_objects.append(post_obj_2)

post_obj_id_3 = (blog_data[2]["id"])
post_obj_title_3 = (blog_data[2]["title"])
post_obj_subtitle_3 = (blog_data[2]["subtitle"])
post_obj_body_3 = (blog_data[2]["body"])
post_obj_3 = Post(post_obj_id_3,post_obj_title_3,post_obj_subtitle_3,post_obj_body_3)
post_objects.append(post_obj_3)


app = Flask(__name__)

@app.route("/")
def get_HP() :
    return render_template("index.html", post=post_objects)

@app.route("/contact")
def contact() :
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/form-submitted-successfully", methods=["POST"])
def receive_and_send_data():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email_received = request.form["email"]
    msg = request.form["message"]

    import smtplib
    email = "chaditya789@gmail.com"
    password = "rlviotwrmmwomwez"
    to_address = "chaditya972@gmail.com"

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(from_addr=email,to_addrs=to_address,msg=f"subject: Message from Aditya's Blog\n\nName : {first_name} {last_name}\ne-mail: {email_received} \nMessage : {msg}")
    connection.close()

    return render_template("form_submission.html")
    


if __name__ == "__main__" :
    app.run(debug=True)