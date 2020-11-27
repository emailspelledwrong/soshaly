from flask import Blueprint, render_template #,jsonify, send_from_directory, request, redirect, url_for
#from wekzeug.utils import secure_filename
#import os, datetime

root_bp = Blueprint('root_bp', __name__,
    template_folder='templates',
    static_folder='static')
#    static_url_path='assets')

# /
@root_bp.route('/')
def root_root():
    page_title = 'Root'
    page_text = 'Hi! I''m a Flask Blueprint web app,<br>running in a Docker container, <br>behind an Nginx reverse-proxy,<br>in a separate container.'
    return render_template('root/index.html', page_title=page_title, page_text=page_text)

#root_bp.errorhandler() # register an error handler function
#root_bp.before_request() # execute an action before every request
#root_bp.after_request() # execute an action after every request
#root_bp.app_template_filter() #register a template filter at the application level