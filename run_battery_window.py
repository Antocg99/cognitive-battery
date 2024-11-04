#https://github.com/sho-87/cognitive-battery.git
from __future__ import division, print_function
import os
import sys
import argparse
from PyQt5 import QtWidgets
from interface import  battery_window

def main(data_save_path):
    # Get application directory
    base_dir = os.path.dirname(os.path.realpath(__file__))
    project_dir = os.path.join(base_dir, 'cognitive-battery')

    # Initialize application
    app = QtWidgets.QApplication(sys.argv)
    screen_resolution = app.primaryScreen().availableGeometry() 

    # Create project manager window
    try:
        project_manager = battery_window.BatteryWindow(base_dir, project_dir, screen_resolution.width(), screen_resolution.height(), data_save_path)

        project_manager.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Error intializing the application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Run Congitive Battery Window')
    parser.add_argument(
        '--data_save_path',
        type=str,
        default='/Users/antoniocangelosi/Documents/GitHub/eye_gaze_cognitive_test/data',
        help = 'Path to save data')
    args = parser.parse_args()
    main(args.data_save_path)
