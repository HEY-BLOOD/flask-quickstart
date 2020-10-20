from application import app

@app.route('/flask-icon')
def flask_icon():
    """
    通常静态文件位于应用的 /static 中。
    """
    return url_for('static', filename='images/flask-icon.png')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

    # url_for() 函数用于构建指定函数的 URL。
    with app.test_request_context():
        from flask import url_for
        print(url_for('index'))
        print(url_for('login'))
        print(url_for('login', next='/'))
        print(url_for('profile', username='HEY-BLOOD'))

    # 操作请求数据，本地环境，一般用于单元测试
    with app.test_request_context('/hello', method='POST'):
        from flask import request
        # now you can do something with the request until the
        # end of the with block, such as basic assertions:
        assert request.path == '/hello'
        assert request.method == 'POST'
