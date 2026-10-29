import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/emma/Downloads/lunabotics-challenge-2027-software/ros2/install_modular/lunabotics_sim'
