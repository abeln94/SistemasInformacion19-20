from bottle import run, template, get, post, request


@get('/')
def main():
    return template('main')


@get('/contact')
def contact():
    return template('contact', sent=False)


@post('/contact.post')
def contact():
    return template('contact', sent=True)


@post('/login')
def login():
    firstname = request.forms.get('firstname')
    lastname = request.forms.get('lastname')
    return template('login', name=firstname + " " + lastname)


if __name__ == '__main__':
    run(host='localhost', port=8080)
