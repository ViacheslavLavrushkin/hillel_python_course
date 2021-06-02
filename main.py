import sqlite3

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


# crud operations for phones
@app.route('/phones/create/')
def phones_create():
    query_params = request.args
    id = query_params.get('id')
    value = query_params.get('value')

    import sqlite3

    con = sqlite3.connect("./phones.db")
    cur = con.cursor()
    sql = """
    INSERT INTO phones
    values (null, '{id}', '{value}')
    """
    cur.execute(sql)
    con.commit()
    con.close()

    return 'Phones was created'


@app.route('/phones/delete/')
def phones_delete():
    import sqlite3

    con = sqlite3.connect("./phones.db")
    cur = con.cursor()
    sql = """
    DELETE FROM phones;
    """
    cur.execute(sql)
    con.commit()
    con.close()

    return 'All phones were deleted'


@app.route('/phones/list/')
def phones_list():
    import sqlite3

    con = sqlite3.connect("./phones.db")
    cur = con.cursor()
    sql = """
    SELECT * FROM phones;
    """
    cur.execute(sql)
    phones_list = cur.fetchall()
    con.close()

    return str(phones_list)


@app.route('/phones/update/')
def phones_update():
    query_params = request.args
    value = query_params.get('value')

    import sqlite3

    con = sqlite3.connect("./phones.db")
    cur = con.cursor()
    sql = """
    UPDATE phones SET value = {value};
    """
    cur.execute(sql)
    con.commit()
    con.close()

    return 'All phones were update'


if __name__ == '__main__':
    app.run(port='5000')
