#!/usr/bin/env python3
import webbrowser
import sqlite3
import sys
import dearpygui.dearpygui as dpg
import database

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query_start = """
    CREATE TABLE IF NOT EXISTS service(
        name TEXT,
        amount REAL);
    """
    cursor.execute(query_start)


def add() -> None:
    user_service = dpg.get_value('__input_text')
    user_amount = dpg.get_value('__input_number')
    if user_service.isspace() or user_service == '':
        not_empty_err = """
The service name can only be a string! Wrong data not added!
        """
        return print(not_empty_err)
    if not user_amount.isdigit():
        not_digit_err = """
The amount can only be a number! Wrong data not added!
        """
        return print(not_digit_err)
    else:
        database.add_data(user_service, user_amount)


def read() -> None:
    database.read_data()


def exit() -> None:
    sys.exit()


def delete_all() -> None:
    database.delete_all()
    exit()


def delete_element() -> None:
    name_to_delete = dpg.get_value('element')
    database.delete_element(name_to_delete)


def open_github():
    github_link = "https://github.com/IvanIsak2000/finance_manager_app"
    webbrowser.open_new_tab(github_link)
    exit()


dpg.create_context()
dpg.create_viewport(title='Finance Manager', width=800, height=400)
with dpg.window(label='Menu', width=500, height=550, tag='Primary Window'):
    try:
        width, height, channels, data = dpg.load_image('background.png')
        with dpg.texture_registry():
            texture_id = dpg.add_static_texture(100, 100, data)
        dpg.add_image(texture_id)
    except TypeError:
        print('Failed to load background.png')
    with dpg.menu_bar():
        with dpg.menu(label='Add  '):
            dpg.add_text('Service name (only english):')
            user_service = (dpg.add_input_text(tag='__input_text'))
            dpg.add_text('Service amount (only english):')
            user_amount = (dpg.add_input_text(tag='__input_number'))
            dpg.add_button(label='Save?',
                           callback=add,
                           tag='__save')
        with dpg.tooltip('__input_text'):
            input_help_text = """
Enter service name.
For example: Foods
Only English is supported so far
            """
            dpg.add_text(input_help_text)
        with dpg.tooltip('__input_number'):
            input_help_text = """
Enter a service amount!
For example: 20
An error is given if you attempt entering 0 or non-digit characters
            """
            dpg.add_text(input_help_text)
        with dpg.tooltip('__save'):
            dpg.add_text('Click Save to save')
        with dpg.menu(label='  Read  '):
            dpg.add_menu_item(label='Open schedule ',
                              callback=database.read_data)
        with dpg.menu(label='  Delete  '):
            with dpg.menu(label='Delete all'):
                dpg.add_menu_item(label='Yes',
                                  callback=database.delete_all,
                                  tag='__delete')
            with dpg.menu(label='Delete element'):
                name_to_delete = (dpg.add_input_text(tag="element"))
                dpg.add_button(label='Delete', callback=database.delete_element)
            with dpg.tooltip('__delete'):
                dpg.add_text('If you press Yes - all data are delete!')
        with dpg.menu(label='  Exit  '):
            dpg.add_menu_item(label='Exit?', callback=exit)
        with dpg.menu(label='  GitHub  '):
            dpg.add_menu_item(label='Open', callback=open_github)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('Primary Window', True)
dpg.start_dearpygui()
