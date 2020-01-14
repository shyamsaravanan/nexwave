#Share the complete pacakage ie tar file
#Go to https://packaging.python.org/->tutorials->Packaging Python Projects-> Code for Creating setup.py COPY PASTE
#gIVE URL OF GITHUB
#Make file in release2 ie README.md and write anything\
#Terminal cd release2 then
# python setup.py sdist #create source in 2 directory
#This tar file we share under tar file
# Download this tar file how to install that
#write pip install Gautam-0.0.1.tar.gz in terminal


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Gautam", # Replace with your own username
    version="0.0.1",
    scripts=['searchprogram.py'],
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gautam-cloud/Nexwave",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)