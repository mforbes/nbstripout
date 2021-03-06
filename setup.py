from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup_requires = [
    'pytest-runner'
]

tests_require = [
    'cram',
    'flake8'
]

setup(name='nbstripout',
      version='0.2.1',
      author='Min RK',
      author_email='benjaminrk@gmail.com',

      # 0.1 branch
      # maintainer='Florian Rathgeber',
      # maintainer_email='florian.rathgeber@gmail.com',
      # url='https://github.com/kynan/nbstripout',

      # 0.2 branch
      maintainer='Michael McNeil Forbes',
      maintainer_email='michael.forbes+python@gmail.com',
      url='https://github.com/mforbes/nbstripout',

      license="License :: OSI Approved :: MIT License",

      description='Strips outputs from Jupyter and IPython notebooks',
      long_description=long_description,
      py_modules=['pytest_cram', 'nbstripout'],
      entry_points={
          'console_scripts': [
              'nbstripout = nbstripout:main'
          ],
          'pytest11': [
              'pytest_cram = pytest_cram',
          ]
      },

      setup_requires=setup_requires,
      tests_require=tests_require,

      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Other Environment",
          "Framework :: IPython",
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Topic :: Software Development :: Version Control",
      ])
