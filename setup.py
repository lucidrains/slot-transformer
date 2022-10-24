from setuptools import setup, find_packages

setup(
  name = 'slot-transformer',
  packages = find_packages(exclude=[]),
  version = '0.0.1',
  license='MIT',
  description = 'Slot Transformer for reasoning in images and video',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/lucidrains/slot-transformer',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'attention mechanism',
    'slot attention',
    'reasoning'
  ],
  install_requires=[
    'einops>=0.4',
    'torch>=1.6',
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
