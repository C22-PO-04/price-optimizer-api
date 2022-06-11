import os
from flask import request
from app.model.user import User
from app import response, app, db
from app.controller.VoucherController import transform_voucher

def index(page):
    try:
        offset = (int(page) - 1) * 10
        users = User.query.offset(offset).limit(10).all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest([], message=e)

def transform(users):
    data = []
    for i in users:
        data.append(singleTransform(i))
    return data

def singleTransform(user):
    data = {
        'id': user.id,
        'name': user.name,
        'voucher': transform_voucher(user.voucher)
    }
    return data

def show(id):
    try:
        user = User.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], 'user not found')

        data = singleTransform(user)
        return response.ok(data, "")
    except Exception as e:
        print(e)

'''
def assignVoucher(id_voucher):
    try:
        
    except Exception as e:
        print(e)
'''