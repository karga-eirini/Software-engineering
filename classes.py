class Admin:
    def __init__(self,username,idcode):
        self.username=username
        self.idcode=idcode

class User:
    def __init__(self,email,username,password,location):
        self.email=email
        self.username=username
        self.password=password
        self.location=location

class Store:
    def __init__(self,name,location,products,hours):
        self.name=name
        self.location=location
        self.products=products
        self.hours=hours

class Product:
    def __init__(self,product_code,category,description):
        self.product_code=product_code
        self.category=category
        self.description=description

class Order:
    def __init__(self,product,adress,tel_number,card_inf):
        self.product=product
        self.adress=adress
        self.tel_number=tel_number
        self.card_inf=card_inf

class UserComments:
    def __init__(self,user,store,description):
        self.user=user
        self.store=store
        self.description=description

class EntryRequest:
    def __init__(self,name,adress,tel_number,text):
        self.name=name
        self.adress=adress
        self.tel_number=tel_number
        self.text=text

class ExpensiveRate:
    def __init__(self,ratings,first_evaluation,store_id):
        self.ratings=ratings
        self.first_evaluation=first_evalutaton
        self.store_id=store_id
