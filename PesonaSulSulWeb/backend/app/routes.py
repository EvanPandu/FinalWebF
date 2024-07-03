from unittest import main

from flask import request, jsonify, flash, redirect, url_for
from . import db, photos

from .models import User, Admin, RiwayatTransaksi, Wisata, Komentar
from datetime import datetime

from ..run import app

# Method to get all admins
@app.route('/admins', methods=['GET'])
def get_admins():
    admins = Admin.query.all()
    return jsonify([{'admin_id': admin.admin_id, 'username': admin.username} for admin in admins])

# Method to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'user_id': user.user_id, 'username': user.username} for user in users])


@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    role = data['role']

    if role == 'Admin':
        user = Admin.query.filter_by(username=username).first()
    else:
        user = User.query.filter_by(username=username).first()

    if user and user.password == password:
        return jsonify({'success': True, 'user': user.to_dict()})
    return jsonify({'success': False})


@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    role = data['role']

    if role == 'Admin':
        new_user = Admin(username=username, password=password)
        db.session.add(new_user)
    else:
        new_user = User(username=username, password=password)
        db.session.add(new_user)

    db.session.commit()
    return jsonify({'success': True, 'user': new_user.to_dict()})


# Method to add new wisata
@app.route('/admin/wisata/add', methods=['POST'])
def add_wisata():
    tempat_wisata = request.form['tempat_wisata']
    description = request.form['description']
    price = request.form['price']
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        image_path = f"uploads/{filename}"
        new_wisata = Wisata(tempat_wisata=tempat_wisata, image=image_path, description=description, price=price)
        db.session.add(new_wisata)
        db.session.commit()
        return jsonify({'message': 'Wisata added successfully!'})

# Method to edit wisata
@app.route('/admin/wisata/edit/<int:id>', methods=['POST'])
def edit_wisata(id):
    wisata = Wisata.query.get_or_404(id)
    wisata.tempat_wisata = request.form['tempat_wisata']
    wisata.description = request.form['description']
    wisata.price = request.form['price']
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        wisata.image = f"uploads/{filename}"
    db.session.commit()
    return jsonify({'message': 'Wisata updated successfully!'})

# Method to delete wisata
@app.route('/admin/wisata/delete/<int:id>', methods=['DELETE'])
def delete_wisata(id):
    wisata = Wisata.query.get_or_404(id)
    db.session.delete(wisata)
    db.session.commit()
    return jsonify({'message': 'Wisata deleted successfully!'})

# Method to add new komentar
@app.route('/wisata/<int:id>/komentar', methods=['POST'])
def add_komentar(id):
    name = request.form['name']
    comment = request.form['comment']
    new_komentar = Komentar(name=name, comment=comment, wisata_id=id)
    db.session.add(new_komentar)
    db.session.commit()
    return jsonify({'message': 'Komentar added successfully!'})

# Method to get all comments by wisata_id
@app.route('/wisata/<int:id>/komentar', methods=['GET'])
def get_komentar(id):
    comments = Komentar.query.filter_by(wisata_id=id).all()
    return jsonify([{'comment_id': comment.comment_id, 'name': comment.name, 'comment': comment.comment} for comment in comments])

# Method to get all data for a specific wisata
@app.route('/wisata/<int:id>', methods=['GET'])
def get_wisata(id):
    wisata = Wisata.query.get_or_404(id)
    return jsonify({'wisata_id': wisata.wisata_id, 'tempat_wisata': wisata.tempat_wisata, 'image': wisata.image, 'description': wisata.description, 'price': wisata.price})

# Method to get all transactions by user_id
@app.route('/riwayat_transaksi/<int:user_id>', methods=['GET'])
def get_riwayat_transaksi_by_user_id(user_id):
    transaksi = RiwayatTransaksi.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'riwayat_id': t.riwayat_id,
        'name': t.name,
        'quantity': t.quantity,
        'total_price': t.total_price,
        'date': t.date,
        'user_id': t.user_id
    } for t in transaksi])
