def route(path):
    

def render_template(template_name='index.html'):
    return f"<h1>Hello</h1>"

def app(environ, start_response):
    path = environ.get('PATH_INFO')
    
    for k, v in environ.items():
        print(k, v)
    data = render_template()
    data = data.encode("utf-8")
    start_response(
        f"200 OK", [
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data)))
        ]
    )
    return iter([data])

if __name__ == '__main__':
    app()