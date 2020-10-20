from application import app

if __name__ == "__main__":
    # app.run(host="0.0.0.0", debug=True)

    # url_for() 函数用于构建指定函数的 URL。
    with app.test_request_context():
        from flask import url_for
        print(url_for('index'))
        print(url_for('login'))
        print(url_for('login', next='/'))
        print(url_for('profile', username='HEY-BLOOD'))
