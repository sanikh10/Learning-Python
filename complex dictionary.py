users_data = [
{
"id": 1,
"name": "Igor",
"url": "",
"description": "",
"link": "/wp/blog/author/admin/",
"slug": "admin",
"avatar_urls": {
"24": "http://2.gravatar.com/avatar/8d7a6e0f54977dbc6b6aa9f632f20ce3?s=24&d=identicon&r=g",
"48": "http://2.gravatar.com/avatar/8d7a6e0f54977dbc6b6aa9f632f20ce3?s=48&d=identicon&r=g",
"96": "http://2.gravatar.com/avatar/8d7a6e0f54977dbc6b6aa9f632f20ce3?s=96&d=identicon&r=g"
},
"meta": [],
"_links": {
"self": [
{
"href": "/wp/wp-json/wp/v2/users/1"
}
],
"collection": [
{
"href": "/wp/wp-json/wp/v2/users"
}
]
}
}
]


user_name = users_data[0].get('collection')
print(user_name)