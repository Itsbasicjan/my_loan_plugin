import setuptools

PLUGIN_NAME = "my_loan_plugin"

setuptools.setup(
    name=PLUGIN_NAME,
    version="1.0.0",
    author="Jan Schüler",
    author_email="",
    description="A plugin to manage item loans in InvenTree",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "inventree_plugins": [
            # The key must match your plugin class path:
            "MyLoanPlugin = my_loan_plugin.plugin:MyLoanPlugin"
        ]
    },
    install_requires=[
        # List any extra dependencies your plugin needs
    ],
    python_requires=">=3.7",
)