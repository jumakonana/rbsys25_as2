from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'rbsys25_as2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jumakonana',
    maintainer_email='s24C1079LG@s.chibakoudai.jp',
    description='a package counting elapsed times',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'pub_etime = rbsys25_as2.pub_etime:main',
            'sub_etime = rbsys25_as2.sub_etime:main', 
        ],
    },
)
