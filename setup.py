from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Enter AsyncAI models with API'

# Setting up
setup(
    name="AsyncAI",
    version=VERSION,
    author="AsyncAI",
    author_email="<asyncintellect@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'api', 'ai', 'datascience'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)