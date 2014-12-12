from setuptools import setup

setup(name='frcpy',
      version='0.1',
      description='API wrapper for the offical FRC (FIRST Robotics Competition) API',
      url='N/A',
      author='Isiah Lloyd',
      author_email='lloyd@isiah.me',
      license='MIT',
      packages=['frcpy'],
	  install_requires=[
          'requests',
      ],
      zip_safe=False)