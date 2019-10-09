import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, REAL, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///shop.db', echo=True)

metadata = MetaData()
users_table = Table('users', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('first_name', String),
                    Column('last_name', String),
                    Column('email', String),
                    Column('password', String)
                    )

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s', '%s')>" % (self.first_name, self.last_name, self.email, self.password)


product_table = Table('product', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('name', String),
                      Column('description', String),
                      Column('price', REAL),
                      Column('color', String)
                      )


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(REAL)
    color = Column(String)

    def __init__(self, name, description, price, color):
        self.name = name
        self.description = description
        self.price = price
        self.color = color

    def __repr__(self):
        return "<Product('%s','%s', '%r', '%s')>" % (self.name, self.description, self.price, self.color)


category_table = Table('category', metadata,
                       Column('id', Integer, primary_key=True),
                       Column('name', String),
                       Column('description', String),
                       )


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Product('%s','%s')>" % (self.name, self.description)


category_product_table = Table('category_product', metadata,
                               Column('id', Integer, primary_key=True),
                               Column('product_id', Integer, ForeignKey('product.id')),
                               Column('category_id', Integer, ForeignKey('category.id')),
                               )


class CategoryProduct(Base):
    __tablename__ = 'category_product'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    category_id = Column(Integer, ForeignKey('category.id'))

    def __init__(self, product_id, category_id):
        self.product_id = product_id
        self.category_id = category_id

    def __repr__(self):
        return "<Product('%d','%d')>" % (self.product_id, self.category_id)


basket_table = Table('basket', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('creation_date', Date),
                     Column('checkout_date', Date),
                     Column('total_price', REAL),
                     Column('user_id', Integer, ForeignKey('user.id')),
                     Column('status', Boolean),
                     Column('delivery_address', String),
                     )


class Basket(Base):
    __tablename__ = 'basket'
    id = Column(Integer, primary_key=True)
    creation_date = Column(Date)
    checkout_date = Column(Date)
    total_price = Column(REAL)
    user_id = Column(Integer, ForeignKey('user.id'))
    status = Column(Boolean)
    delivery_address = Column(String)

    def __init__(self, creation_date, checkout_date, total_price, user_id, status, delivery_address):
        self.creation_date = creation_date
        self.checkout_date = checkout_date
        self.total_price = total_price
        self.user_id = user_id
        self.status = status
        self.delivery_address = delivery_address

    def __repr__(self):
        return "<Product('%s','%s, %r, %d, %b, %s')>" % (self.creation_date,
                                                         self.checkout_date,
                                                         self.total_price,
                                                         self.user_id,
                                                         self.status,
                                                         self.delivery_address)


basket_product_table = Table('basket_product', metadata,
                             Column('id', Integer, primary_key=True),
                             Column('product_id', Integer, ForeignKey('product.id')),
                             Column('category_id', Integer, ForeignKey('basket.id')),
                             Column('quantity', Integer, ),
                             Column('price', REAL),
                             )


class BasketProduct(Base):
    __tablename__ = 'basket_product'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    basket_id = Column(Integer, ForeignKey('basket.id'))
    quantity = Column(Integer)
    price = Column(REAL)

    def __init__(self, product_id, basket_id, quantity, price):
        self.product_id = product_id
        self.basket_id = basket_id
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return "<Product('%d','%d, %d, %r')>" % (self.product_id, self.basket_id, self.quantity, self.price)


# Создание таблицы
Base.metadata.create_all(engine)
