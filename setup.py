from setuptools import setup

with open('README.md') as file_readme:
      readme = file_readme.read()
setup(name='frcdatapy',
      version='0.1',
      description='API wrapper for the offical FRC (FIRST Robotics Competition) API',
      long_description=readme ,
      url='https://github.com/isiah-lloyd/frcdatapy',
      author='Isiah Lloyd',
      author_email='lloyd@isiah.me',
      license='MIT',
      classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English', 
            'Topic :: Software Development'
      ],
      packages=['frcdatapy'],
	  install_requires=[
          'requests',
      ],
      zip_safe=True)