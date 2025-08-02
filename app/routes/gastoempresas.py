from flask import Blueprint, render_template

gasto_bp = Blueprint('gastoempresas', __name__, url_prefix='/gastoempresas')


@gasto_bp.route('/')
def gastoempresas():
    return render_template('gastoempresas.html')
