from flask import Flask, escape, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


# 使用 route() 装饰器来把函数绑定到 URL
@app.route('/hello')
def hello():
    return 'Hello, World！'


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


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

    # url_for() 函数用于构建指定函数的 URL。
    with app.test_request_context():
        print(url_for('index'))
        print(url_for('login'))
        print(url_for('login', next='/'))
        print(url_for('profile', username='HEY-BLOOD'))
