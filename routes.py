from app import models, db
from flask import current_app as app, jsonify, abort

'''
Создайте представление для пользователей, которое обрабатывало бы GET-запросы получения всех пользователей 
/users и одного пользователя по идентификатору /users/1.
'''
@app.route('/users', methods=['GET'])
def get_users():
    users = db.session.query(models.User).all()
    return jsonify([user.serialize() for user in users])

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = db.session.query(models.User).filter(models.User.id == user_id).first()

    if user is None:
        abort(404)
    return jsonify(user.serialize())

'''
Создайте представление для заказов, которое обрабатывало бы GET-запросы получения всех заказов 
/orders и заказа по идентификатору /orders/1.
'''
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = db.session.query(models.Order).all()
    return jsonify([order.serialize() for order in orders])

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = db.session.query(models.Order).filter(models.Order.id == order_id).first()

    if order is None:
        abort(404)
    return jsonify(order.serialize())

'''
Создайте представление для предложений, которое обрабатывало бы GET-запросы получения всех предложений 
/offers и предложения по идентификатору /offers/<id>
'''
@app.route('/offers', methods=['GET'])
def get_offers():
    offers = db.session.query(models.Offer).all()
    return jsonify([offer.serialize() for offer in offers])

@app.route('/offers/<int:offer_id>', methods=['GET'])
def get_offer(offer_id):
    offer = db.session.query(models.Offer).filter(models.Offer.id == offer_id).first()

    if offer is None:
        abort(404)
    return jsonify(offer.serialize())

'''
Реализуйте создание пользователя user посредством метода POST на URL /users  для users.
Реализуйте обновление пользователя user посредством метода PUT на URL /users/<id>  для users. 
В Body будет приходить JSON со всеми полями для обновление заказа.
Реализуйте удаление пользователя user посредством метода DELETE на URL /users/<id> для users.
'''
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    db.session.add(models.User(**data))
    db.session.commit()
    return {}

@app.route('/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    data = request.json
    user = db.session.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        abort(404)
    db.session.query(models.User).filter().update(data)
    db.session.commit()
    return {}

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = db.session.query(models.User).filter(models.User.id == user_id).delete()
    if result == 0:
        abort(404)
    db.session.commit()
    return {}

'''
тоже для orders
'''

@app.route('/orders', methods=['POST'])
def create_user():
    data = request.json
    db.session.add(models.Order(**data))
    db.session.commit()
    return {}

@app.route('/orders/<int:order_id>', methods=['PUT'])
def edit_user(order_id):
    data = request.json
    order = db.session.query(models.Order).filter(models.Order.id == order_id).first()
    if order is None:
        abort(404)
    db.session.query(models.Order).filter().update(data)
    db.session.commit()
    return {}

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_user(order_id):
    result = db.session.query(models.Order).filter(models.Order.id == order_id).delete()
    if result == 0:
        abort(404)
    db.session.commit()
    return {}

'''
тоже для offers
'''

@app.route('/offers', methods=['POST'])
def create_user():
    data = request.json
    db.session.add(models.Offer(**data))
    db.session.commit()
    return {}

@app.route('/offers/<int:offer_id>', methods=['PUT'])
def edit_user(offer_id):
    data = request.json
    offer = db.session.query(models.Offer).filter(models.Offer.id == offer_id).first()
    if offer is None:
        abort(404)
    db.session.query(models.Offer).filter().update(data)
    db.session.commit()
    return {}

@app.route('/offers/<int:offer_id>', methods=['DELETE'])
def delete_user(offer_id):
    result = db.session.query(models.Offer).filter(models.Offer.id == offer_id).delete()
    if result == 0:
        abort(404)
    db.session.commit()
    return {}
