class Admin:
    def __init__(self,username,idcode,password):
        self.username=username
        self.idcode=idcode
        self.password=password
    
    def applies(self,EntryRequest):
        self.EntryRequest=EntryRequest

    def delete_store(self,Store):
        self.Store=Store

    def add_store(self,Store):
        self.Store=Store

    def check_if_exists(self,id):
        self.Store.id=id


class User:
    def __init__(self,email,username,password,location,favorite):
        self.email=email
        self.username=username
        self.password=password
        self.location=location
        self.favorite=favorite

    def Createprofile(self,email,username,password):
        self.User.email=email
        self.User.username=username
        self.User.password=password
    
    def UpdateList(self,favorite,id):
        self.User.favorite=favorite
        self.Store.id=id

    def Search_by_category(self,category,id):
        self.Store.category=category
        self.Store.id=id

    def Search_by_name(self,name):
        self.Store.name=name

    def List_os_shops(self,category,id):
        self.Store.category=category
        self.Store.id=id

    def changeof(self,email,username,password,location):
        self.User.email=email
        self.User.username=username
        self.User.password=password
        self.User.location=location
        

class Store:
    def __init__(self,id,name,location,adress,schedule,category,evaluations):
        self.id=id
        self.name=name
        self.location=location
        self.adress=adress
        self.schedule=schedule
        self.category=category
        self.evaluations=evaluations

    def add_product(self,Product,Store):
        self.Product=Product
        self.Store=Store
        

class Product:
    def __init__(self,id,category,description,price,stock):
        self.id=id
        self.category=category
        self.description=description
        self.price=price
        self.stock=stock


class Order:
    def __init__(self,products,adress,phone_Number,transaction,totalPrice):
        self.products=products
        self.adress=adress
        self.phone_Number=phone_Number
        self.transaction=transaction
        self.totalPrice=totalPrice
    
    

class StoreProposal:
    def __init__(self,store,description):
        self.store=store
        self.description=description

class StoreExperience:
    def __init__(self,store,description,stars):
        self.store=store
        self.description=description
        self.stars=stars
    
    def check_criterial(self,StoreExperience):
        self.StoreExperience=StoreExperience
    
    def post_evaluation(self,evaluations,StoreExpirience):
        self.StoreExperience=StoreExperience
        self.Store.evaluations=evaluations
    
    def change_evaluation(self,StoreExpirience):
        self.StoreExperience=StoreExperience

class EntryRequest:
    def __init__(self,name,adress,phone_number,details,questions,validation_documents):
        self.name=name
        self.adress=adress
        self.phone_number=phone_number
        self.detail=details
        self.questions=questions
        self.validation_documents=validation_documents

class Location:
    def __init__(self,adress,cityid,coordinations,postcode):
        self.adress=adress
        self.cityid=cityid
        self.coordinations=coordinations
        self.postcode=postcode

    def GetStores(self,Store,location):
        self.User.location=location
        self.Store.location=location
        self.Store=Store

class ExpensiveRate:
    def __init__(self,id,rating,estimation):
        self.ratings=rating
        self.id=id
        self.estimation=estimation

class News:
    def __init__(self,text,title,news_id,news_kind,publish_date):
        self.text=text
        self.title=title
        self.news_id=news_id
        self.news_kind=news_kind
        self.publish_date=publish_date

class Quiz:
    def __init__(self,questions,anwsers):
        self.questions=questions
        self.anwsers=anwsers

class Coupon:
    def __init__(self,id,price_tag,coupon_comment):
        self.id=id
        self.price_tag=price_tag
        self.coupon_comment=coupon_comment

class Ad:
    def __init__(self,id,text,format):
        self.id=id
        self.text=text
        self.format=format

    def addad(self,id):
        self.Ad.id=id
