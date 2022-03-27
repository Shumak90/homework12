from flask import Blueprint, render_template, request
from functions import post_json
import logging

logging.basicConfig(encoding="utf-8", level=logging.INFO)

main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates")


@main_blueprint.route('/')
def photo_showing():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_posts():
    try:
        search_post = request.args['s']
        logging.info(f'Слово для поиска: {search_post}')
        posts = [i for i in post_json() if search_post.lower() in i['content'].lower()]
        return render_template('post_list.html', search_post=search_post, posts=posts)
    except FileNotFoundError:
        return "Файл не найден"

