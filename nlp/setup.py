from setuptools import setup, find_packages

with open(file="README.md", mode="r") as fh:
    long_description = fh.read()

setup(
    name='py-challenge',
    author='Florida Hoxha',
    author_email='flhoxha33@gmail.com',
    version='0.0.1',
    description='Easy challanges',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Lori-ml/NLP-Challenges-',
    install_requires=[
        'sklearn==0.22.1',
        'pandas==1.1.0',
        'numpy==1.19.5',
        'seaborn==0.10.0',
        'matplotlib==3.1.3',
        'wmi==1.5.1',
        'urllib.request==3.7'
    ],
    packages=find_packages(
        include=['pyopt']
    ),
    classifiers=[
        'License :: OSI Approved :: No License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>3.7'
)