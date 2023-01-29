
def install_libs():
    import os
    import sys
    try:

        import dearpygui.dearpygui as dpg
        import matplotlib.pyplot as plt
        import numpy as np
        print("All libraries are there!")

    except BaseException:

        os.system("pip install dearpygui")
        os.system("pip install matplotlib")
        os.system("pip install numpy")

        os.system("cls")
        print("Required libraries installed! All done!")
