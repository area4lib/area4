import os
# get working directory:
dir = os.getenv("TRAVIS_BUILD_DIR")
# goto main directory:
os.system("{0} {1}".format("cd", dir))
print("now in working directory")
# build and install package:
os.system("python3 setup.py sdist bdist_wheel")
print("built package")
os.system("{0} {1}{2}".format("cd", dir, "/dist/"))
print("changed to dist directory")
os.system("{0} {1}/dist/{2}".format("python3 -m pip install --upgrade", dir, "area4-2.0.dev0.whl"))
print("installed")
# run the tests:
print("time to run tests")
