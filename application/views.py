from flask import escape, url_for, request, render_template, Markup
from application import app


@app.route('/')
def index():
    return 'Index Page'


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
