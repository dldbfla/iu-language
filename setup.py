from setuptools import setup, find_packages

setup(
    name='iulove',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'iulove=iulove.main:main'
        ]
    },
    author="iyulim",
    author_email="iyulim210@gmail.com",
    description="아이유는 사랑",
    long_description=open("../README.md", "r", encoding="UTF-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dldbfla/iu-language",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
