from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    data = request.form #returns whatever gets posted
    if request.method == 'POST':
        pass
    else:
        pass
    return render_template('views/index.html')