from setuptools import setup, find_packages
setup(
    name = "smpp.pdu",
    version = "0.1",
    author = "Roger Hoover",
    author_email = "roger.hoover@gmail.com",
    description = "SMPP PDU parsing library",
    license = 'GPL',
    packages = find_packages(),
    py_modules=["smpp.pdu"],
    include_package_data = True,
    zip_safe = False,   
    install_requires = [
        'enum',
    ],
    test_suite = 'smpp.pdu.tests',
)

