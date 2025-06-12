from setuptools import setup, find_packages

setup(
    name='trumpy',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    author='Harupyon716',
    author_email='rrubypyon@gmail.com',
    description='トランプカードの実装および, 複数のデモゲームを内包.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.*',
)