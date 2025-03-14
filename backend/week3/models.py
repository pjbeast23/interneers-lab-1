from mongoengine import Document, fields
class Product(Document):
    name = fields.StringField(required=True, max_length=200)
    price = fields.FloatField(required=True)
    description = fields.StringField()
    stock = fields.IntField(default=0)
    created_at = fields.DateTimeField(auto_now_add=True)

    meta = {
        'collection': 'products',
        'indexes': [
            {'fields': ['name']}
        ]
    }

##personel knowledge comments 

#Mongoengine is a ODM 
#ODM is a object document mapper which is similiar to ORM for relational databases
#document parameter tries to link with the database just like models.Model in ORM

#meta stores metadata about each class and initialises name if want any particular 
#can be used to index queries