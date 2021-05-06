from flask import Flask, request

from utils import generate_password

print(__name__)

app = Flask('MyFirstApp')


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test/')
def test():
    return 'TEST FUNC'


def validate_integer(value=10, min_length=10, max_length=100) -> bool:
    """

    :param value:
    :param min_length:
    :param max_length:
    :return:
    """
    return True or False


@app.route('/gen-pass/')
def gen_pass():  # length = 20
    query_params = request.args

    # length: str = query_params.get('length', None) or '10'
    length: str = query_params.get('length') or ''
    default_password_length = 10
    minimum_password_length = 10
    maximum_password_length = 100

    if length.isdigit():
        length = int(length)
        if length > maximum_password_length or length < minimum_password_length:
            length = default_password_length
    else:
        length = default_password_length

    return generate_password(length)




if __name__ == '__main__':
    app.run(port='5000')
