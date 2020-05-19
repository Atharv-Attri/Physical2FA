import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Physical2FA",  # Replace with your own username
    version="1.0.1",
    author="Atharv2",
    author_email="atharv260107@gmail.com",
    description="Encryption using 2 Factor Authentication through an external drive.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Atharv2/Physical2FA",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Win32 (MS Windows)",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: Microsoft :: Windows :: Windows 8",
        "Operating System :: Microsoft :: Windows :: Windows 8.1",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Topic :: Security :: Cryptography",
        "Topic :: Security",
    ],
    python_requires='>=3.0',
)
