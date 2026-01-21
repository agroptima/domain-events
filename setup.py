from setuptools import setup

from domain_events import get_version

setup(
    name="domain-events",
    version=get_version(),
    license="GPLv3",
    author="Isagri S.L.U.",
    author_email="devs.es@groupeisagri.com",
    description="A lightweight library with an implementation of Pub-Sub.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/agroptima/domain-events",
    download_url="https://github.com/agroptima/domain-events/releases",
    keywords=["python", "ddd"],
    packages=["domain_events"],
    install_requires=["pytz"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
)
