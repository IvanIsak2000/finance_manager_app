def read_data_in_sql():  # open and read all data
    import sqlite3
    import dearpygui.dearpygui as dpg
    import matplotlib.pyplot as plt
    import numpy as np

    output = " NO TABLE,PLEASE REBOOT PROGRAMM !"
    try:
        with sqlite3.connect('database.db') as db:
            cursor = db.cursor()
            query = ''' SELECT * FROM service '''
            cursor.execute(query)
            output = []
            for name, amount in cursor:
                new_list = []
                new_list.append(name)
                new_list.append(str(amount))
                output.append(new_list)

            result = []
            for element in output:
                result += element
            dictionary = dict([(k, float(v))
                              for k, v in zip(result[::2], result[1::2])])
            dictionary = dict(
                sorted(
                    dictionary.items(),
                    key=lambda item: item[1]))

            values = list((dictionary.values()))
            keys = list(dictionary.keys())

            index = np.arange(len(keys))  # column count

            values1 = values
            plt.bar(index, values1)
            plt.xticks(index + 0.4, keys)
            plt.title('Statistics', fontsize=20, color='black')  # title

            plt.xlabel('service name', fontsize=15, color='red')  # x-axis name

            plt.ylabel('dollars', fontsize=15, color='green')  # y-axis name

            plt.show()

    except:
        pass
        print(f'NO DATA OR ERROR!!!  Your data: {output}')
