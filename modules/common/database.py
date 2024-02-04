import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'/Users/elena/OKorniichuk_qa_auto_2023' + r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_all_products(self):
        query = "SELECT id, name, description, quantity FROM products"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_all_customers(self):
        query = "SELECT * FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_all_orders(self):
        query = "SELECT * FROM orders"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_order_date_by_order_id(self, order_id):
        query = f"SELECT order_date FROM orders WHERE id = {order_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_order_with_correct_order_date_data_type(self, id, customer_id, product_id, order_date):
        query = f"INSERT OR REPLACE INTO orders (id, customer_id, product_id, order_date) \
                VALUES ({id}, {customer_id}, {product_id}, '{order_date}')"
        self.cursor.execute(query)
        self.connection.commit()
        record = self.cursor.fetchall()
        return record

    def get_products_by_quantity(self, quantity):
        query = f"SELECT id, name FROM products WHERE quantity <= {quantity}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_customer_by_city(self, city):
        query = f"SELECT * FROM customers WHERE city = '{city}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
        
    def update_customer_city_by_id(self, customer_id, city):
        query = f"UPDATE customers SET city = '{city}' WHERE id = {customer_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_customer_by_postal_code(self, postal_code):
        query = f"SELECT * FROM customers WHERE postalCode = '{postal_code}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_postal_code_by_customer_id(self, customer_id):
        query = f"SELECT postalCode FROM customers WHERE id = '{customer_id}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
        
    def update_customer_postal_code_by_id_1(self, customer_id, postal_code):
        query = f"UPDATE customers SET postalCode = '{postal_code}' WHERE id = {customer_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def update_customer_postal_code_by_id_2(self, customer_id, postal_code):
        query = f"UPDATE customers SET postalCode = '{postal_code}' WHERE id = {customer_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_more_detailed_orders(self):
        query = "SELECT orders.id, orders.order_date, customers.name, customers.city, \
                products.name, products.description \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    
    

    
    


