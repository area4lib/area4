import os
# get working directory:
dir = os.getenv("TRAVIS_BUILD_DIR")
# goto main directory:
os.system("cd", dir)
print("now in working directory")
# build and install package:
os.system("python3 setup.py sdist bdist_wheel")
print("built package")
os.system("cd", "dir" + "/dist/")
print("changed to dist directory")
os.system("python3 -m pip install --upgrade area4-2.0.dev0.whl")
print("installed")
# run the tests:
os.system("cd", dir + "/tests/")
print("time to run tests")
os.system("python3 testmodule.py")
