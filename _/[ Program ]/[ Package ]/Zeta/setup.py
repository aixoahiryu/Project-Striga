from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Zeta Lockhart\'s framework'
LONG_DESCRIPTION = 'Framework for Zeta cross-platform parasitic desktop environment'

# Setting up
setup(
        name="Zeta", 
        version=VERSION,
        author="Zeta Lockhart",
        author_email="<aixoahiryu@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], 
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
        ]
)