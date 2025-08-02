from flask import Blueprint, render_template

compra_bp = Blueprint('compraempresas', __name__, url_prefix='/compraempresas')


@compra_bp.route('/')
def compraempresas():
    return render_template('compraempresas.html')
