from distutils.core import setup
import py2exe 
setup(
    console=['splitFile.py'] ,
    name="splitfile",
    version="1.0",
    description="splits the input file into as many files as pairs of lines there are",
    author="Yankeevic",
    url="http://www.nourlyet.com",
    author_email="yankeevic@gmail.com",
    #data_files=[("", ["redstring.png", "redstring_interface.glade"])],
    #py_modules=["redstring"],
    options = { 'py2exe': {
            'compressed':0,
            'bundle_files':0}})

