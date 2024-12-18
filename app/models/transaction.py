from datetime import datetime
from app.extensions import db

class PurchaseOrder(db.Model):
    __tablename__ = 'purchase_order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    delivery_date = db.Column(db.Date)
    status = db.Column(db.String(20), nullable=False)
    total_amount = db.Column(db.Numeric(10, 2))

    def __repr__(self):
        return f'<PurchaseOrder {self.id}>'

class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Item {self.name}>'

class PurchaseOrderItem(db.Model):
    __tablename__ = 'purchase_order_item'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    purchase_order_id = db.Column(db.Integer, db.ForeignKey('purchase_order.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    def __repr__(self):
        return f'<PurchaseOrderItem {self.id}>'


class Invoice(db.Model):
    __tablename__ = 'invoice'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    invoice_date = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.Date)
    status = db.Column(db.String(20), nullable=False)
    total_amount = db.Column(db.Numeric(10, 2))

    def __repr__(self):
        return f'<Invoice {self.id}>'

class Payment(db.Model):
    __tablename__ = 'payment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    payment_method = db.Column(db.String(50))
    excess_amount = db.Column(db.Numeric(10, 2), default=0)

    def __repr__(self):
        return f'<Payment {self.id}>'

class InvoicePayment(db.Model):
    __tablename__ = 'invoice_payment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    payment_id = db.Column(db.Integer, db.ForeignKey('payment.id'), nullable=False)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), nullable=False)
    amount_applied = db.Column(db.Numeric(10, 2), nullable=False)

    def __repr__(self):
        return f'<InvoicePayment {self.id}>'

class Inventory(db.Model):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id', name='fk_inventory_item_id'), nullable=False)

    def __repr__(self):
        return f'<Inventory {self.item_id}>'
    

class InvoiceItem(db.Model):
    __tablename__ = 'invoice_item'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    def __repr__(self):
        return f'<InvoiceItem {self.id}>'

