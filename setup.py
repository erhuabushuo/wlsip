from setuptools import setup, find_packages


setup(
    name='wlsip',
    version='0.1',
    description='Itlong sip tester',
    author='Aidan He',
    author_email='erhuabushuo@gmail.com',
    url='https://github.com/erhuabushuo/wlsip',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    platforms='all',
    data_files=[
        ('xml', ['xml/register.xml']),
        ('xml', ['xml/uas.xml']),
        ('xml', ['xml/uac.xml']),
        ('xml', ['xml/ooc.xml']),
    ],
    install_requires=[
        'click',
        'ifaddr',
    ],
    classifiers=[
        'Development Status :: 3 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Communications',
        'Topic :: Internet'
    ],
    entry_points={
        'console_scripts': [
            'wlsip = scripts.wlsip_script:cli',
        ]
    },
    test_suite='nose.collector',
    tests_require=['nose'],
)