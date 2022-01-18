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
@bp.route('/add', methods=['POST'])
def add():
    error = {"success": True, "error_message": ""}    
    product_name = request.form.get('product_name', '')
    # product_attribute = request.form.get('product_attribute', '')
    
    if not product_name:
        error["success"] = False
        error["error_message"] = "requires a product_name"
    else:
        db = get_db()
        product_row = db.execute(
            'SELECT product_id FROM product WHERE product_name = ?', (product_name,)
        ).fetchone()           
        
        if product_row:       
            db.execute(
                """
                UPDATE inventory
                SET quantity=quantity+1
                WHERE product_id=?;
                """,
                (product_row[0],)
            )        
            db.commit()
            db.execute(
                """
                INSERT INTO inventory(product_id, quantity)
                SELECT ?, ?
                WHERE (SELECT Changes() = 0);
                """,            
                (product_row[0], 1)
            )
            db.commit()
        else:    
            error['success'] = False
            error['error_message'] = "Product doesn't exist"
    return error


#returns all the available products in the inventory
@bp.route('/inventory')
def get_inventory():   
    rows = get_db().execute('SELECT * FROM inventory').fetchall() 
    return {"inventory": row_to_list(rows)}


#returns all products
@bp.route('/products')
def get_products():    
    rows = get_db().execute(
        """
            SELECT 
                product_name, product_description, added 
            FROM 
                product 
            ORDER BY 
                added
        """
    ).fetchall()
        
    return {"products": row_to_list(rows)}
        


@bp.route('/update', methods=['POST'])
def update_inventory():
    """
    be able to edit attributes to inventory items
    delete rows
    add products
    """
    pass

#returns list of data in row objects
def row_to_list(rows):
    data = []
    for row in rows:
        data.append(list(row))
    return data



    """
    product_id required 
    get attribute_id based on attribute not required 
    get product_id based on name 
    
    (t-shirt, "red") -> inventory
    (t-shirt)
    (t-shirt)
    (t-shirt, "red")
    ----------------------
    (t-shirt,"red") quantityt = 2
    (t-shirt) quantityt = 1
    
    if product_id 
        if attribute: 
            if already exists:
                inventory->increment quantity
            else:
                add new row in inventory
        else:
            if already exists:
                inventory -> increment quantity
            else: 
                add new row
        
    """