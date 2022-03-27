import json

POST_PATH = "posts.json"


def post_json():
    with open(POST_PATH, "r", encoding="utf-8") as read_file:
        posts = json.load(read_file)
    return posts


def uploaded_json(posts):
    with open(POST_PATH, "w", encoding="utf-8") as file:
        json.dump(posts, file, ensure_ascii=False)



