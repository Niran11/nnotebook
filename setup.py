from setuptools import setup

setup(name='nnotebook',
      version='0.1',
      description='Simple app for taking notes',
      url='https://github.com/Niran11/nnotebook',
      python_requires='>=3.7',
      packages=['nnotebook','nnotebook/actions'],
      entry_points={
          'console_scripts': [
              'note = nnotebook.__main__:main'
          ]
      },
)
