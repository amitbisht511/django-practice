from setuptools import setup, find_packages

setup(
    name="A Test Project",
    author="Amit Bisht",
    author_email="amitb@clavax.us",
    description="Description about test project",
    version="1.0",
    # package_dir={"": "src"},
    packages=find_packages(),
    scripts=["src/manage.py"],
    install_requires=["django", "black", "isort", "flake8", "django-environ"],
)
