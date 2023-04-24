from setuptools import setup

readme = ""
with open("README.rst") as f:
    readme = f.read()
setup(
    name="expressipy",
    version="1.0",
    author="ExHiraku",
    license="MIT",
    requires=["aiohttp"],
    packages=["expressipy"],
    python_requires=">=3.7",
    description="Add emotion to your python applications.",
    long_description=readme,
    long_description_content_type="text/x-rst",
)
