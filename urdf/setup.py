from setuptools import setup
import os
from glob import glob

package_name = 'simple_urdf_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        # Install package.xml
        ('share/ament_index/resource_index/packages', ['package.xml']),
        ('share/' + package_name, ['package.xml']),
        # Install launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        # Install URDF files
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jenifa',
    maintainer_email='jenifa@example.com',
    description='Simple 2-link robotic arm URDF project',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'move_arm = simple_urdf_robot.move_arm:main',
        ],
    },
)
