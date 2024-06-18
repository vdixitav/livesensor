from setuptools import setup, find_packages

def get_requirements() -> list[str]:
    requirements_list: list[str] = []
    return requirements_list

setup(
    name='sensor',
    version='0.0.1',
    author='Dixitha',
    author_email='vishwasraodixita@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),  # This will include the requirements obtained from get_requirements()
)
