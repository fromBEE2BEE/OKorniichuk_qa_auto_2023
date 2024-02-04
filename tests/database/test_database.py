import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()
    print(users)

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')
    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)
    assert water_qnt[0][0] == 25

@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)
    assert water_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)
    assert len(qnt) == 0

@pytest.mark.database
def test_get_all_products():
    db = Database()
    products = db.get_all_products()
    print(products)


@pytest.mark.database
def test_get_all_customers():
    db = Database()
    customers = db.get_all_customers()
    print(customers)

@pytest.mark.database
def test_get_all_orders():
    db = Database()
    orders = db.get_all_orders()
    print(orders)


@pytest.mark.database
def test_get_order_date_by_order_id():
    db = Database()
    order_date = db.get_order_date_by_order_id(1)
    assert order_date [0][0] == '12:22:23'

@pytest.mark.database
def test_insert_order_with_correct_order_date_data_type_1():
    db = Database()
    db.insert_order_with_correct_order_date_data_type(2, 2, 3, '2023-12-13 11:55:48 PM')
    order_date = db.get_order_date_by_order_id(2)
    assert order_date [0][0] == '2023-12-13 11:55:48 PM'

@pytest.mark.database
def test_insert_order_with_correct_order_date_data_type_2():
    db = Database()
    db.insert_order_with_correct_order_date_data_type(3, 2, 3, '14/12/2023')
    order_date = db.get_order_date_by_order_id(3)
    assert order_date [0][0] == '14/12/2023'

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 3

    # Check struture of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'чай чорний'
    assert orders[0][3] == 'Akbar'

    assert orders[1][0] == 2
    assert orders[1][1] == 'Stepan'
    assert orders[1][2] == 'молоко'
    assert orders[1][3] == 'натуральне незбиране'

    assert orders[2][0] == 3
    assert orders[2][1] == 'Stepan'
    assert orders[2][2] == 'молоко'
    assert orders[2][3] == 'натуральне незбиране'

@pytest.mark.database
def test_get_products_by_quantity():
    db = Database()
    products = db.get_products_by_quantity(10)
    print(products)

@pytest.mark.database
def test_get_customer_by_city():
    db = Database()
    customers = db.get_customer_by_city('Kyiv')
    print(customers)

@pytest.mark.database
def test_update_customer_city_by_id():
    db = Database()
    db.update_customer_city_by_id(2, 'Dnipro')
    customer = db.get_customer_by_city('Dnipro')
    print(customer)

@pytest.mark.database
def test_get_customer_by_postal_code():
    db = Database()
    customers = db.get_customer_by_postal_code('3127')
    print(customers)

@pytest.mark.database
def test_get_postal_code_by_customer_id():
    db = Database()
    postal_code = db.get_postal_code_by_customer_id(1)
    print(postal_code)

@pytest.mark.database
def test_update_customer_postal_code_by_id_1():
    db = Database()
    db.update_customer_postal_code_by_id_1(2, '1234567891011')
    customer = db.get_customer_by_postal_code('1234567891011')
    postal_code = db.get_postal_code_by_customer_id(2)
    assert 13 <= 10
    
@pytest.mark.database
def test_update_customer_postal_code_by_id_2():
    db = Database()
    db.update_customer_postal_code_by_id_2(1, Null)
    postal_code = db.get_postal_code_by_customer_id(1)
    
@pytest.mark.database
def test_more_detailed_orders():
    db = Database()
    orders = db.get_more_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 3

    # Check struture of data
    assert orders[0][0] == 1
    assert orders[0][1] == '12:22:23'
    assert orders[0][2] == 'Sergii'
    assert orders[0][3] == 'Kyiv'
    assert orders[0][4] == 'чай чорний'
    assert orders[0][5] == 'Akbar'
    
    assert orders[1][0] == 2
    assert orders[1][1] == '2023-12-13 11:55:48 PM'
    assert orders[1][2] == 'Stepan'
    assert orders[1][3] == 'Dnipro'
    assert orders[1][4] == 'молоко'
    assert orders[1][5] == 'натуральне незбиране'

    assert orders[2][0] == 3
    assert orders[2][1] == '14/12/2023'
    assert orders[2][2] == 'Stepan'
    assert orders[2][3] == 'Dnipro'
    assert orders[2][4] == 'молоко'
    assert orders[2][5] == 'натуральне незбиране'
    

    
