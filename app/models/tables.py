from app import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)

    #Login
    email=db.Column(db.String,unique=True,nullable=False)
    password=db.Column(db.String,nullable=False)

    #info
    name=db.Column(db.String)
    cpf = db.Column(db.String)
    gender = db.Column(db.String)
    birtday = db.Column(db.Date)

    def __repr__(self):
        return "<id: %r User %r>" %(self.id,self.email)

class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)

    #info
    title=db.Column(db.String,nullable=True)
    author=db.Column(db.String,nullable=True)#create an specific table
    publisher=db.Column(db.String,nullable=True)#create an specific tab le
    genter=db.Column(db.String,nullable=True)#create an specific table
    isbn=db.Column(db.String)

    def __repr__(self):
        return "<id: %r Book %r>" %(self.id,self.title)

class Borrow(db.Model):
    id = db.Column(db.Integer,primary_key=True)

    id_lender=db.Column(db.Integer,nullable=False)
    id_borrowe=db.Column(db.Integer,nullable=False)
    id_book=db.Column(db.Integer,nullable=False)
    final_date=db.Column(db.Date,nullable=False)
