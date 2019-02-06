import os
# goto main directory:
os.system("cd $TRAVIS_WORKING_DIR")
# build and install package:
os.system("python3 setup.py sdist bdist_wheel")
os.system("cd $TRAVIS_WORKING_DIR/dist")
os.system("python3 -m pip install --upgrade .")
# run the tests:
os.system("cd $TRAVIS_WORKING_DIR/tests/")
os.system("python3 testmodule.py")
