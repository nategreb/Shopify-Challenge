DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS attribute;
DROP TABLE IF EXISTS size;

CREATE TABLE inventory (
    inventory_id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    attribute_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    FOREIGN KEY (attribute_id) REFERENCES attribute(attribute_id)    
);

CREATE TABLE product (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,      
    item_description TEXT,
    added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE attribute (
    attribute_id INTEGER PRIMARY KEY,
    attribute VARCHAR(255) NOT NULL,
);

-- CREATE TABLE size (
--     size_id INTEGER PRIMARY KEY,
--     item_size VARCHAR(10) NOT NULL
-- );

-- Nosql might be better ... since attributes are dynamic