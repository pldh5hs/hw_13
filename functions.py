import json

#__all__ = ['find_tags', 'posts_with_tag']

def _write_json():
    with open("posts.json", "r", encoding='utf-8') as f:
        posts = json.load(f)
    return posts

def find_tags():
    tags = []
    posts = _write_json()
    for post in posts:
        words = post["content"].split()
        for word in words:
            if word.startswith("#"):
                tags.append(word[1:])
    tags = set(tags)
    return tags

def posts_with_tag(query):
    posts_tag = []
    posts = _write_json()
    for post in posts:
        if f'#{query}' in post["content"]:
            posts_tag.append(post)
    return posts_tag

def new_post(address_pic, content):
    post = {"pic": address_pic, "content": content}
    posts = _write_json()
    posts.append(post)
    with open("posts.json", "w", encoding='utf-8') as f:
        json.dump(posts, f)