from distutils.core import setup
setup(
  name = 'prsa',
  packages = ['prsa'], # this must be the same as the name above
  version = '0.21',
  description = 'Public Encryption Command Line Utility',
  author = 'Ridwan M. Sharif',
  author_email = 'ridwanmsharif@hotmail.com',
  url = 'https://github.com/ridwanmsharif/rsa', # use the URL to the github repo
  #download_url = 'https://github.com/peterldowns/mypackage/tarball/0.1', # I'll explain this in a second
  keywords = ['encryption','rsa','public encryption','cryptography'], # arbitrary keywords
  classifiers = [],
  scripts=['scripts/prsa'],
)
