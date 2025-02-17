import setuptools

setuptools.setup(
    name="streamlit-file-browser",
    version="2.3.7",
    author="",
    author_email="",
    description="",
    long_description="",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "pandas",
        "filetype",
        "wcmatch",
        "streamlit-molstar",
        "streamlit-antd",
        "streamlit >= 0.63",
    ],
)
