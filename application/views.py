from flask import escape, url_for, request, render_template, Markup, redirect, flash, send_from_directory, abort
from flask.helpers import make_response
from application import app, ALLOWED_EXTENSIONS
from werkzeug.utils import secure_filename
import os


@app.route('/')
def index():
    return render_template('index.html')


# 使用 route() 装饰器来把函数绑定到 URL
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    # name包含HTML时将自动转义，如 /hello/<br>blood&gt;hahhaa
    return render_template('hello.html', name=Markup(name))


@app.route('/user/<username>')
def show_user_profile(username):
    """
    不指定转换器（缺省值） 接受任何不包含斜杠的文本
    """
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    """
    使用转换器，为变量指定规则为 int类型（正整数）
    """
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    """
    使用转换器，为变量指定规则为 path类型（类似 string ，但可以包含斜杠）
    """
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


@app.route('/projects/')
def projects():
    """
    类型文件夹路径的写法，访问 /projects 时将自动重定向到 /projects/
    """
    return 'The project page'


@app.route('/about')
def about():
    """
    类型文件路径的写法，只能通过 /about 访问，这样可以保持 URL 唯一，并帮助 搜索引擎避免重复索引同一页面。
    """
    return 'The about page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    route() 装饰器的 methods 参数来处理不同的 HTTP 方法
    """
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'blood' and request.form['password'] == 'p@ssw0rd':
            return '<h1>Welcome %s, login was successful.</h1>' % request.form['username']
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))


@app.route('/flask_icon')
def flask_icon():
    """
    通常静态文件位于应用的 /static 中。
    使用 render_template() 方法可以渲染模板
    """
    # 访问静态文件
    url_for('static', filename='images/flask-icon.png')
    return render_template('flask_icon.html')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """
    上传文件
    """
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)  # 获取到安全的文件名
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # 上传成功后，重定向到该文件
            return render_template('upload.html', filename=filename)
    return render_template('upload.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """
    文件上传成功后，在 upload.html 中获取服务器 http://ip:port 的文件路径
    """
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/test_cookies')
def cookies():
    """
    Cookies 保存在请求对象的 cookies属性中
    可以使用响应对象的 set_cookie 方法来设置 cookies 。
    在 Flask 中，如果使用 会话 ，那么就不要直接使用 cookies ，因为 会话 比较安全一些。
    """
    # 读取 cookies
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a KeyError if the cookie is missing.
    # 储存 cookies:使用 make_response() 生成响应对象，在更改响应的 Cookies
    resp = make_response(render_template('cookies.html'))
    resp.set_cookie('username', 'the username')
    return resp


@app.route('/secret')
def secret():
    """
    使用 redirect() 函数可以重定向。
    使用 abort() 可以更早退出请求，并返回错误代码
    """
    abort(401)  # 401 表示禁止访问

    # 下面代码不会被执行
    print("Hello")
