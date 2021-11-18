from setuptools import setup
from setuptools import find_packages
from pip._internal.req import parse_requirements

install_reqs = [str(req.requirement) for req in parse_requirements('requirements.txt', session='hack')]

setup(
    name='zoom',
    version='1.0',
    packages=["zoom"],
    package_data={'': ['data/config.json']},
    include_package_data=True,
    url='https://github.com/viktorcvetanovic',
    author='vikitor',
    author_email='viktorcvetanovic@gmail.com',
    description='Zoom app starter',
    install_requires=install_reqs,
    entry_points={
        "console_scripts": ["zoom=zoom.__main__:main"]
    }
)