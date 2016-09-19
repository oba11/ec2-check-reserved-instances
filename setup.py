try:
  from setuptools import setup
except:
  from distutils.core import setup

setup(name='ec2-check-reserved-instances',
      version='0.2',
      py_modules=[],
      install_requires=[
        'boto3'
      ],
      packages=[ 
        'lib'
      ],
      entry_points={
        'console_scripts': [
          'ec2-check-reserved-instances = lib.ec2_check_reserved_instances:main'
        ]
      }
)
