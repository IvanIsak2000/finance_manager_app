import webbrowser
import sqlite3
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import dearpygui.dearpygui as dpg

from app.delete_element import delete_element_in_sql
from app.delete_all import delete_all_in_sql
from app.read import read_data_in_sql
from app.add import add_data_in_sql




# the database will always be created at the beginning if it does not exist
with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query_start = ''' CREATE TABLE IF NOT EXISTS service(
        name TEXT,
        amount REAL) '''

    cursor.execute(query_start)


def add(user_service, user_amount):
    user_service = dpg.get_value('__input_text')
    user_amount = dpg.get_value('__input_number')

    if user_service.isspace() or user_service == '':
        return print(
            'The service name can only be a string! Wrong data not added!')

    if user_amount.isspace() or user_amount == '':
        return print(
            'The amount can only be a number! Wrong data not added! ')

    else:
        add_data_in_sql(user_service, user_amount)


def read():
    read_data_in_sql()


def delete_all():
    delete_all_in_sql()


def delete_element(name_to_delete):
    name_to_delete = dpg.get_value('element')
    delete_element_in_sql(name_to_delete)


def exit_from_program():
    sys.exit()


def open_github():
    webbrowser.open_new_tab(
        'https://github.com/IvanIsak2000/finance_manager_app')
    sys.exit()


dpg.create_context()
dpg.create_viewport(title='Finance Manager', width=800, height=400)
with dpg.window(label='Menu', width=500, height=550, tag='Primary Window'):

    try:
        width, height, channels, data = dpg.load_image('background.png')

        with dpg.texture_registry():
            texture_id = dpg.add_static_texture(100, 100, data)

        dpg.add_image(texture_id)

    except BaseException:
        print('Failed to load background.png')
        pass

    with dpg.menu_bar():

        with dpg.menu(label='Add  '):  # ADD FUNCTION

            dpg.add_text('Servise name(only english):')
            user_service = (dpg.add_input_text(tag='__input_text'))

            dpg.add_text('Service amount(only english):')
            user_amount = (dpg.add_input_text(tag='__input_number'))

            user_service = dpg.get_value('__input_text')
            user_amount = dpg.get_value('__input_number')

            dpg.add_button(label='Save?', callback=add, tag='__save')

        with dpg.tooltip('__input_text'):
            dpg.add_text(
                '''Enter service name\nFor example:foods\nSo far only supports English''')
        with dpg.tooltip('__input_number'):
            dpg.add_text(
                '''Enter a service amount!\nFor example:20\nIf you enter zero or other characters other than numbers, it will give an error!''')
        with dpg.tooltip('__save'):
            dpg.add_text('Click Save to save')

        with dpg.menu(label='  Read  '):  # READ FUNCTION
            dpg.add_menu_item(label='Open schedule ', callback=read)

        with dpg.menu(label='  Delete  '):  # DELETE FUNCTION
            with dpg.menu(label='Delete all'):
                dpg.add_menu_item(
                    label='Yes',
                    callback=delete_all,
                    tag='__delete')

            with dpg.menu(label='Delete element'):
                name_to_delete = (dpg.add_input_text(tag="element"))

                dpg.add_button(label='Delete', callback=delete_element)

            with dpg.tooltip('__delete'):
                dpg.add_text('If you press Yes - all data are delete!')

        with dpg.menu(label='  Exit  '):  # EXIT FUNCTION
            dpg.add_menu_item(label='Exit?', callback=exit_from_program)

        with dpg.menu(label='  GitHub  '):
            dpg.add_menu_item(label='Open', callback=open_github)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('Primary Window', True)
dpg.start_dearpygui()
