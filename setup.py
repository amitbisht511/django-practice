from setuptools import find_packages, setup

setup(
    name="A Test Project",
    author="Amit Bisht",
    author_email="amitb@clavax.us",
    description="Description about test project",
    version="1.0",
    # package_dir={"": "src"},
    packages=find_packages(),
    scripts=["src/manage.py"],
    install_requires=[
        "django",
        "django-environ",
        "django-extensions",
        "django-allauth",
        "mysqlclient",
    ],
)
