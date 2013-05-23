from distutils.core import setup  
setup(name='finalseg',  
      version='0.13',
      description='Chinese Words Segementation Utilities',  
      author='Sun, Junyi & Linker Lin',
      author_email='linker.lin@me.com',
      url='https://github.com/linkerlin/finalseg',
      packages=['finalseg'],  
      package_dir={'finalseg':'finalseg'},
      package_data={'finalseg':['*.*']}
)  
