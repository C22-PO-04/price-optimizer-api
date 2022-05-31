from app import db
from datetime import datetime
from app.model.user import User
from app.model.product import Product

class Voucher(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(230), nullable=False)
    discount_percent = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    def __repr__(self):
        return '<Voucher {}>'.format(self.name)

