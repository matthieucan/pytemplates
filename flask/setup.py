import os

from setuptools import setup, find_packages

deps = []
with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    for line in f:
        deps.append(line.strip())

setup(
    name="myproject",
    version="0.1",
    packages=find_packages(),
    install_requires=deps,
    package_data={'': ['web/static/css/*', 'web/static/js/*',
                       'web/static/img/*', 'web/templates/*']},
    author="AUTHOR",
    author_email="EMAIL@EXAMPLE.ORG",
    description="DESCRIPTION",
    license="LICENSE",
    keywords="K E Y W O R D S",
    url="http://EXAMPLE.ORG/URL/",
)
