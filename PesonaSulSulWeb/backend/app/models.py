from . import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Admin(db.Model):
    __tablename__ = 'admin'
    admin_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120), nullable=False)

class RiwayatTransaksi(db.Model):
    __tablename__ = 'riwayat_transaksi'
    riwayat_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

class Wisata(db.Model):
    __tablename__ = 'wisata'
    wisata_id = db.Column(db.Integer, primary_key=True)
    tempat_wisata = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Komentar(db.Model):
    __tablename__ = 'komentar'
    comment_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    wisata_id = db.Column(db.Integer, db.ForeignKey('wisata.wisata_id'), nullable=False)
