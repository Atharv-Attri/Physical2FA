import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Physical2FA",  # Replace with your own username
    version="0.0.a7",
    author="Atharv2",
    author_email="atharv260107@gmail.com",
    description="Alpha version",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Atharv2/Physical2FA",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
