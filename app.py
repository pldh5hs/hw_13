from flask import Flask, request, render_template, send_from_directory
from functions import *

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    tags = find_tags()
    return render_template('index.html', tags=tags)


@app.route("/tag")
def page_tag():
    query = request.args.get("tag")
    posts_tag = posts_with_tag(query)
    return render_template('post_by_tag.html', tags=query, posts_tag=posts_tag)


@app.route("/post", methods=["GET"])
def page_post_write():
    return render_template('post_form.html')


@app.route("/post", methods=["POST"])
def page_post_create():
    pic = request.files.get("picture")
    content = request.values.get("content")
    if pic:
        address_pic = f"uploads/images/{pic.filename}"
        pic.save(address_pic)
        new_post(address_pic, content)
        return render_template('post_uploaded.html', address=address_pic, text=content)

    return "ошибка загрузки"

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

