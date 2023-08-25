from sqlite3 import connect
import matplotlib as plt
import numpy as np


def read_data():
    try:
        with connect("database.db") as db:
            cursor = db.cursor()
            query = """SELECT * FROM service"""
            cursor.execute(query)
            output = []
            for name, amount in cursor:
                new_list = [name, str(amount)]
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
            index = np.arange(len(keys))
            values1 = values
            plt.bar(index, values1)
            plt.xticks(index + 0.4, keys)
            plt.title("Statistics", fontsize=20, color="black")
            plt.xlabel("service name", fontsize=15, color="red")
            plt.ylabel("dollars", fontsize=15, color="green")
            plt.show()
    except Exception as e:
        print(e)
