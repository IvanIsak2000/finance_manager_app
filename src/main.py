#!/usr/bin/env python3

import webbrowser
import sys
import dearpygui.dearpygui as dpg
import database
import logging
from sqlalchemy import create_engine, Column, String, REAL
from sqlalchemy.ext.declarative import declarative_base


logging.basicConfig(filename='finance_manager_app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s'
                    )
logger = logging.getLogger(__name__)


def log(error: str) -> None:
    logger.error(error)
    return print(error)





def add_in_db() -> None:
    user_service = dpg.get_value('user_service_name')
    user_amount = dpg.get_value('user_service_amount')

    if service_and_amount_is_valid(user_service, user_amount):
        try:
            database.add_data(user_service, user_amount)
            logger.info('Data was added')
        except Exception as e:
            log(e)
    else:
        logger.info(f'Data don`t added : `{user_service}` `{user_amount}` ')
        return print('''
ERROR! Verifier that the entered data matches the condition:
service: text greater than 0 characters
amount: number''')


def service_and_amount_is_valid(user_service: str, user_amount: str) -> bool:
    service_is_valid = False
    amount_is_valid = False

    if len(user_service) > 0:
        if not user_service.isspace():
            service_is_valid = True

    if user_amount.isdigit():
        amount_is_valid = True
    return service_is_valid is True and amount_is_valid is True


def read() -> None:
    database.read_data()


def exit() -> None:
    sys.exit()


def delete_all() -> None:
    database.delete_all()


def delete_element() -> None:
    name_to_delete = dpg.get_value('element')
    database.delete_element(name_to_delete)


def open_github():
    webbrowser.open_new_tab("https://github.com/IvanIsak2000/finance_manager_app")
    sys.exit()


dpg.create_context()
dpg.create_viewport(title='Finance Manager', width=800, height=400)
with dpg.window(label='Menu', width=500, height=550, tag='Primary Window'):
    width, height, channels, data = dpg.load_image('background.png')

    with dpg.texture_registry():
        try:
            texture_id = dpg.add_static_texture(100, 100, data)
        except NameError:
            logger.info('no background')
            print('Background don`t found!')
    dpg.add_image(texture_id)

    with dpg.menu_bar():
        with dpg.menu(label='Add  '):
            dpg.add_text('Service name (only english):')
            dpg.add_input_text(tag='user_service_name')
            user_service = dpg.get_value('user_service_name')

            dpg.add_text('Service amount (only english):')
            dpg.add_input_text(tag='user_service_amount')
            user_amount = dpg.get_value('user_service_amount')
            dpg.add_button(label='Save?',
                           callback=add_in_db,
                           tag='save_button')
        with dpg.tooltip('user_service_name'):
            input_help_text = """
Enter service name.
For example: Foods
Only English is supported so far
            """
            dpg.add_text(input_help_text)
        with dpg.tooltip('user_service_amount'):
            input_help_text = """
Enter a service amount!
For example: 20
An error is given if you attempt entering 0 or non-digit characters
            """
            dpg.add_text(input_help_text)
        with dpg.tooltip('save_button'):
            dpg.add_text('Click Save to save')

        with dpg.menu(label='  Read  '):
            dpg.add_menu_item(label='Open schedule ',
                              callback=database.read_data)

        with dpg.menu(label='  Delete  '):
            with dpg.menu(label='Delete all'):
                dpg.add_menu_item(label='Yes',
                                  callback=delete_all,
                                  tag='__delete')
            with dpg.menu(label='Delete element'):
                name_to_delete = (dpg.add_input_text(tag="element"))
                dpg.add_button(label='Delete', callback=delete_element)
            with dpg.tooltip('__delete'):
                dpg.add_text('If you press Yes - all data are delete!')

        with dpg.menu(label='  Exit  '):
            dpg.add_menu_item(label='Exit?', callback=exit)

        with dpg.menu(label='  GitHub  '):
            dpg.add_menu_item(label='Open', callback=open_github)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('Primary Window', True)
try:
    dpg.start_dearpygui()
except KeyboardInterrupt:
    print('Goodbye!')
    exit()
