import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'lunabotics'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'model'),
            glob('model/*')),
        (os.path.join('share', package_name, 'parameters'),
            glob('parameters/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='emma',
    maintainer_email='emma@todo.todo',
    description='Lunabotics robot description and ROS 2 simulation bringup',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
