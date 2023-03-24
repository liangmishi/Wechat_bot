from setuptools import setup, find_packages

setup(
    name='Wechat Assistant',
    version='0.1',
    author='SIBAO',
    author_email='490347176@qq.com',
    description='这是一个微信AI聊天助手脚本',
    packages=find_packages(),
    install_requires=[
        'pyautogui',
        'pyperclip',
    ],
)