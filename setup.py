from setuptools import setup, find_packages


with open('README.md') as readme_file:
    readme = readme_file.read()


setup_requirements = ['pytest-runner', ]
test_requirements = ['pytest>=3', ]
requirements = [
    'argh',
    'jupyter',
    'matplotlib==3.3.1',
    'numpy==1.19.0',
    'pandas==1.1.1',
    'scikit-learn==0.23'
]


COMMANDS = [
    'greet = eleven.cli:greet',
]


setup(
    author="Todd Young",
    author_email='young.todd.mk@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Data Science 511!",
    entry_points={'console_scripts': COMMANDS},
    install_requires=requirements,
    license="BSD license",
    long_description=readme,
    include_package_data=True,
    keywords='eleven',
    name='eleven',
    packages=find_packages(include=['eleven', 'eleven.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/yngtodd/eleven',
    version='0.1.0',
    zip_safe=False,
)
