from flask import Blueprint, render_template, request
from functions import post_json, uploaded_json
import logging

logging.basicConfig(encoding="utf-8", level=logging.INFO)

loader_blueprint = Blueprint('loader_blueprint', __name__, url_prefix='/post', static_folder='static', template_folder="templates")


@loader_blueprint.route("/form/")
def form():
    return render_template("post_form.html")


@loader_blueprint.route("/upload/", methods=["GET", "POST"])
def upload():
    try:
        file = request.files['picture']
        file_name = file.filename
        content = request.values['content']
        posts = post_json()
        posts.append({
            "pic": f'/uploads/images/{file_name}',
            "content": content
        })
        uploaded_json(posts)
        file.save(f'uploads/images/{file_name}')
        if file_name.split(".")[-1] not in ["png", "jpeg", "jpg"]:
            logging.info("Загруженный файл - не картинка ")
            return "<h1>Загруженный файл - не картинка /h1>"
    except FileNotFoundError:
        logging.error("Ошибка загрузки файла")
        return "<h1>Файл не найден</h1>"
    else:
        return render_template("post_uploaded.html", pic=f'/uploads/images/{file_name}', content=content)
