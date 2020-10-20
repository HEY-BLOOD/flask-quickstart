from flask import Flask
import os

app = Flask(__name__)

app_dir = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(app_dir, 'static\\uploads\\')
os.mkdir(UPLOAD_FOLDER) if not os.path.exists(UPLOAD_FOLDER) else None
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 最大上传 16M的文件

from application import views, errors
