class Cart():
    def __init__(self):
        self.cart_items = []
        pass

    def add_item(item_id):
        pass

    def remove_item(ited_id):
        pass

    def total_price():
        pass
    
    def empty_cart():
        pass

    def get_cart_contents():
        pass


class Customer_Details():
    def __init__(self, _firstname, _lastname, _phone, _email, _pickup_time):
        self.firstname = _firstname
        self.lastname = _lastname
        self.phone = _phone
        self.email = _email
        self.pickup_time = _pickup_time

        
class Card_Details():
    def __init__(self, _card_number, _expiry, _cvc):
        self.card_number = _card_number
        self.expiry = _expiry
        self.cvc = _cvc

    def is_valid():
        pass


class Completed_Order():
    def __init__(self, _cart, _customer_details):
        self.cart = _cart
        self.customer_details = _customer_details
    