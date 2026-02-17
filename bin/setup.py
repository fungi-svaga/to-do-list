#!/usr/bin/python3

from setuptools import setup, find_packages

setup(
    name='todo-list-package',
    version='1.0.0',
    packages=find_packages("."),
    scripts=["run.py"],
    url='',
    license='MIT',
    author='Зевакин Ростислав Андреевич',
    author_email='rost.zerar@mail.ru',
    description='Пакет для управления задачами (to-do list) с поддержкой приоритетов и дат',
    include_package_data=True,
    install_requires=[],
)