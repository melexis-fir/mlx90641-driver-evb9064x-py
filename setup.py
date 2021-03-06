from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="mlx90641-driver-evb9064x",
    install_requires=[
        'mlx90641-driver>=1.1.0',
        'pyserial>=3'
    ]
)
