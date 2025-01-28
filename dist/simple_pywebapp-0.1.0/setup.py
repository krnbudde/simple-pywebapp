from setuptools import setup, find_packages

setup(
    name="simple-pywebapp",
    version="0.1.0",
    description="A simple FastAPI application",
    author="kiran",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "mangum",
        "pydantic",
        "httpx"
    ],
    extras_require={
        "dev": ["pytest"]
    },
    python_requires=">=3.7",
)