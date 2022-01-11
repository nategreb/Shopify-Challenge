DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS attribute;

CREATE TABLE inventory (
    inventory_id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    attribute_id INTEGER,
    product_price DECIMAL(10,2),
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    FOREIGN KEY (attribute_id) REFERENCES attribute(attribute_id)    
);

CREATE TABLE product (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,      
    product_description TEXT,
    added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE attribute (
    attribute_id INTEGER PRIMARY KEY,
    attribute VARCHAR(255) NOT NULL
);

-- Nosql might be better ... since attributes are dynamic