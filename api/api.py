from flask import Blueprint, render_template

api_bp = Blueprint('api_bp', __name__, 
    template_folder='templates',
    static_folder='static')
#    static_url_path='assets')

# /api/
@api_bp.route('/')
def api_root():
    page_title = 'Api'
    page_text = 'Hello, I''m a Flask Blueprint API,<br>running in a Docker container,<br>behind an Nginx reverse-proxy,<br>in a separate container.'
    return render_template('api/index.html', page_title=page_title, page_text=page_text)

#api_bp.errorhandler() # register an error handler function
#api_bp.before_request() # execute an action before every request
#api_bp.after_request() # execute an action after every request
#api_bp.app_template_filter() #register a template filter at the application level