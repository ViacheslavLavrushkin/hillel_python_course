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

# crud operation for users
@app.route('/users/creat/')
def users_create():

    query_params = request.args
    first_name = query_params.get('first_name')
    age = int(query_params.get('age'))

    import sqlite3

    con = sqlite3.connect("./users.db")
    cur = con.cursor()
    sql = """
    INSERTS INTO users
    values (null, '{first_name}', '{age}')
    """
    cur.execute(sql)
    con.commit()
    con.close()
    return 'User was Created'

# crud operation for users delete
@app.route('/users/delete/')
def users_delete():

    import sqlite3

    con = sqlite3.connect("./users.db")
    cur = con.cursor()
    sql = """
    DELETE FROM users;
    """
    cur.execute(sql)
    con.commit()
    con.close()
    return 'All users were delete'



@app.route('/users/list/')
def users_list():

    import sqlite3

    con = sqlite3.connect("./users.db")
    cur = con.cursor()
    sql = """
    SELECT * FROM users;
    """
    cur.execute(sql)
    users_list = cur.fetchall()
    # breackpoint()
    con.commit()
    con.close()
    return 'All users were delete'

@app.route('/users/update/')
def users_update():

    query_params = request.args
    first_name = query_params.get('first_name')
    age = int(query_params.get('age'))

    import sqlite3

    con = sqlite3.connect("./users.db")
    cur = con.cursor()
    sql = """
    UPDATE users SET age = '{age}';
    """
    cur.execute(sql)
    con.commit()
    con.close()
    return 'All users were update'

if __name__ == '__main__':
    app.run(port='5000')
