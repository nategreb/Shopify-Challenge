from flask import (
    Blueprint, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api/v1')


#creates new product. Returns true or false if successful request
@bp.route('/create', methods=['POST'])
def create():
    product_name = request.form['product_name']
    product_description = request.form.get('product_description', '')
    db = get_db()
    
    product = db.execute(
        'SELECT * FROM product WHERE product_name = ?', (product_name,)
    ).fetchone()       

    #check if product exists 
    if not product:                
        db.execute(
            """
                INSERT INTO product (product_name, product_description)
                VALUES(?, ?)
            """,
            (product_name, product_description)
        )
        db.commit()
        return {"success": True, "error_message": ""}
    else:
        return {"success": False, "error_message":"Product already exists"}

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


@bp.route('/update', methods=['POST'])
def update_inventory():
    """
    be able to edit attributes to inventory items
    delete rows
    add products
    """
    pass
