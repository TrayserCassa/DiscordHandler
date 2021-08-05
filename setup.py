import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="discord_handler",
    version="0.0.3",
    author="Traysercassa",
    author_email="",
    description="A small discord handler for the logging module using webtokens",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/traysercassa/DiscordHandler",
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Logging"
    ],
    python_requires='>=3',
)
