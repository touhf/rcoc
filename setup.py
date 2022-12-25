from distutils.core import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
  name = 'rcoc',
  packages = ['rcoc'],
  version = 'v1.0.1',
  license='MIT',
  description = 'RCOC - Random Country Or City name generator',
  author = 'touhf',
  author_email = 'tobytubar@gmail.com',
  url = 'https://github.com/touhf/rcoc',
  long_description=long_description,
  long_description_content_type="text/markdown",
  download_url = 'https://github.com/touhf/rcoc/archive/refs/tags/v1.0.1.tar.gz',
  keywords = ['country', 'city', 'generator'],
  install_requires=[],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)
