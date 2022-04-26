import os
import json
from app import db, models
from datetime import datetime

def load_fixtures(file_path):
    # функция чтения файла
    content = []
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = json.load(file)

    return content

def migrate_user_roles(fixture_path):
    # функция загрузки роли пользователя
    fixture_content = load_fixtures(fixture_path)
    for role in fixture_content:
        if db.session.query(models.UserRole).filter(models.UserRole.id == role['id']).first() is None:
            new_role = models.UserRole(**role)
            db.session.add(new_role)
    db.session.commit()


def migrate_users(fixture_path):
    # функция загрузки данных пользователя
    fixture_content = load_fixtures(fixture_path)
    for user in fixture_content:
        if db.session.query(models.User).filter(models.User.id == user['id']).first() is None:
            new_user = models.User(**user)
            db.session.add(new_user)
    db.session.commit()


def migrate_orders(fixture_path):
    # функция загрузки заказов
    fixture_content = load_fixtures(fixture_path)
    for order in fixture_content:
        # перевод даты в нужный формат
        for field_name, field_value in order.items():
            if isinstance(field_value, str) and field_value.count('/') == 2:
                order[field_name] = datetime.strptime(field_value, '%m/%d/%Y')

        if db.session.query(models.Order).filter(models.Order.id == order['id']).first() is None:
            new_order = models.Order(**order)
            db.session.add(new_order)
    db.session.commit()


def migrate_offers(fixture_path):
    # функция загрузки откликов на заказы
    fixture_content = load_fixtures(fixture_path)
    for offer in fixture_content:
        if db.session.query(models.Offer).filter(models.Offer.id == offer['id']).first() is None:
            new_offer = models.Offer(**offer)
            db.session.add(new_offer)
    db.session.commit()
