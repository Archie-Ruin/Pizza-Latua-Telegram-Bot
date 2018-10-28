# -*- coding: utf-8 -*-

from enum import Enum


def product(product_):
    title = product_['title']
    comp = product_['comp']
    price = product_['price']
    return '<b>{}</b>\n\n' \
           '{}\n\n' \
           '<b>Цена: {} руб.</b>'.format(title, comp, price)


class Messages(Enum):
    WELCOME = 'Добро пожаловать, {}. \n' \
              'Мы рады приветсвовать вас в нашем боте для доставки еды. \nВ случае ' \
              'возникновения вопросов, звониите по номеру \n+99 999 999 99 99 '

    DELIVERY = '<b>Условия и описание доставки:</b>\n' \
               'Отдел доставки работает ежедневно с nn:nn до nn:nn'

    CONTACTS = '🏴 Здесь будут контакты'

    NEWS = '📢 Здесь будут новости'
