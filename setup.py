"""
Setup script for Instagram Profile Analyzer
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="instagram-profile-analyzer",
    version="1.0.0",
    author="Anand",
    author_email="anand.developer@example.com",
    description="A powerful yet beginner-friendly Instagram profile analyzer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Anand0295/insta-profile-analyzer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Education",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    keywords="instagram, profile, analyzer, social-media, data-extraction, instaloader",
    project_urls={
        "Bug Reports": "https://github.com/Anand0295/insta-profile-analyzer/issues",
        "Source": "https://github.com/Anand0295/insta-profile-analyzer",
        "Documentation": "https://github.com/Anand0295/insta-profile-analyzer#readme",
    },
)