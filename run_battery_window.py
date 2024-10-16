from __future__ import division, print_function
#https://github.com/sho-87/cognitive-battery.git
import os
import sys

from PyQt5 import QtWidgets

from interface import  battery_window

if __name__ == "__main__":
    # Get application directory
    base_dir = os.path.dirname(os.path.realpath(__file__))

    # Create project manager window
    app = QtWidgets.QApplication(sys.argv)
    screen_resolution = app.desktop().screenGeometry()
    project_dir = os.path.join(base_dir, 'cognitive-battery')

    project_manager = battery_window.BatteryWindow(
        base_dir, project_dir, screen_resolution.width(), screen_resolution.height()
    )
    project_manager.show()

    sys.exit(app.exec_())
