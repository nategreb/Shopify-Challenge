from flask import (
    Blueprint, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')


#creates new product 
@bp.route('/create', methods=('POST'))
def create():
    """
    TODO create new product -- unless exists
    
    """
    pass


#adds item to inventory
@bp.route('/add', methods=('GET', 'POST'))
def add():
    """
    add to inventory if doesn't exist, else increment 
    """
    pass


#returns all the available products in the inventory
@bp.route('/inventory')
def get_inventory():
    pass


@bp.route('/update', methods=('POST'))
def update_inventory():
    """
    be able to edit attributes to inventory items
    delete rows
    add products
    """
    pass
