import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
import os

setup(
    name='mpls.ethics',
    version='0.0.1',
    description="Individual and group reports for the CPA PCP Pretest product",
    long_description=open("README.txt").read() + "\n" +
        open(os.path.join("doc", "HISTORY.txt")).read(),
    classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Education",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: English",
        "Topic :: Education :: Computer Aided Instruction (CAI)",
        "Topic :: Education :: Testing",
    ],
    keywords='Minneapolis ethics training',
    author='John Trammell',
    author_email='johntrammell@gmail.com',
    url='http://www.johntrammell.com/',
    license='GPL',
    packages=['app.met'],
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools',],
    dependency_links = [],
    entry_points=""
)

