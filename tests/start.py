import os
# goto main directory:
os.system("cd $TRAVIS_WORKING_DIR")
# build and install package:
os.system("python3 setup.py sdist bdist_wheel")
os.system("cd $TRAVIS_WORKING_DIR/dist")
os.system("python3 -m pip install --upgrade area4-2.0.dev0.whl")
# run the tests:
os.system("cd $TRAVIS_WORKING_DIR/tests/")
os.system("python3 testmodule.py")
