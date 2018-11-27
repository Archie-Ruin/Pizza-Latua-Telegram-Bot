# -*- coding: utf-8 -*-

from enum import Enum

import db
import product


def product_data(product):
    title = product['title']
    price = product['price']

    if not product['comp']:
        output = '<b>{}</b>\n\n' \
                 '<b>Цена: {} руб.</b>'.format(title, price)
    else:
        comp = product['comp']
        output = '<b>{}</b>\n\n' \
                 '{}\n\n' \
                 '<b>Цена: {} руб.</b>'.format(title, comp, price)
    return output


def pizza_data(info):
    title = info['title']
    price = info['price']
    gram = info['gram']

    weights = product.get_pizza_weight_by_title(title)
    prices = ''
    for w in weights:
        prices = prices + str(w['text'] + ' - ' + str(int(price) + int(w['price'])) + ' руб.\n')

    if not info['comp']:
        output = '<b>{}</b>\n\n' \
                 '<b>{}</b>'.format(title, prices.replace('Диаметр ', 'Ø='))
    else:
        comp = info['comp']
        output = '<b>{}</b>\n\n' \
                 '{}\n\n' \
                 '<b>{}</b>'.format(title, comp, prices.replace('Диаметр ', 'Ø='))
    return output


def basket(chat_id):
    db.delete_empty_orders(chat_id)
    orders = db.get_orders_by_chat_id(chat_id)
    sum = 0
    output = '<b>📥 Корзина:</b>\n\n'

    for o in orders:
        try:
            output = output + o[3] + ' — ' + str(o[2]) + ' шт. \n(' + o[7] + ') = ' + str(o[5] * o[2]) + ' руб.' + '\n\n'
        except:
            output = output + o[3] + ' — ' + str(o[2]) + ' шт. = ' + str(o[5] * o[2]) + ' руб.' + '\n\n'

    for o in orders:
        sum = sum + o[5] * o[2]

    output = output + '<b>Общая сумма: ' + str(sum) + ' руб.</b>'

    if sum == 0:
        output = 'Минимальная сумма заказа должна быть больше чем 0 руб.'

    return output


class Messages(Enum):
    WELCOME = 'Добро пожаловать, {}. \n' \
              'Мы рады приветсвовать вас в нашем боте для доставки еды. \nВ случае ' \
              'возникновения вопросов, звониите по номеру \n8 (3532) 579-779 '

    DELIVERY = '✅ <b>Быстрая доставка 30-60 минут</b>\n' \
               '✅ Мы контролируем скорость за счёт запасных курьеров\n' \
               '✅ Бесплатная доставка при заказе от 500 рублей'

    CONTACTS = '📌 Наш адрес: Оренбург ул. Салмышская, 58\n' \
               '📱 Наш телефон: 8 (3532) 579-779'

    INFO = 'Пицца… Сколько в этом слове всего вкусного: свежее мясо, курица, ' \
           'морепродукты, изумительный соус, грибы, ананасы, домашние помидорчики ' \
           'и еще много ваших любимых ингредиентов!\n\nМы делаем свою пиццу только из ' \
           'натуральных продуктов, которая прямо из печи попадает к вам на стол. ' \
           'Именно в этом наш главный секрет, с которым мы делимся с вами, нашими любимыми гостями! \n\n' \
           'А вы уже решили, какую пиццу будете заказывать сегодня в La Tua?'
