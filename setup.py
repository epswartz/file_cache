from distutils.core import setup


VERSION="0.0.1"

setup(
    name = 'file_cache',
    version = VERSION,
    packages = ['file_cache'],
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'Decorator to cache on disk',
    author = 'Ethan Swartzentruber',
    author_email = 'eswartzen@gmail.com',
    url = 'https://github.com/epswartz/file_cache',
    download_url=f'https://github.com/epswartz/block_distortion/archive/{VERSION}.zip',
    keywords = ['cache', 'disk', 'decorator'],
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta', # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.9',
)
