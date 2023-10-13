from setuptools import setup, find_packages

setup(
    name='vending_machine',
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=["fastapi", "pydantic", "requests",
                      "google-cloud", "google-cloud-resource-manager", "google-oauth", "redis", "uvicorn"],
    extras_require={
        "dev": []
    },
    description='',
    author='XCC',
    long_description_content_type='text/markdown',
)
