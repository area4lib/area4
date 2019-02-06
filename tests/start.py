import os

# get working directory:
dir = os.getenv("TRAVIS_BUILD_DIR")

# goto main directory:
os.system("{0} {1}".format("cd", dir))

print("now in working directory")
# install package:

os.system("{0} {1}{2}".format("cd", dir, "/dist/"))
print("changed to dist directory")
