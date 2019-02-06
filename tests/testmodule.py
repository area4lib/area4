try:
    import area4
except ImportError:
    raise Exception("Can't run tests because the package could not be imported.")

if not __name__ == "__main__":
    raise Exception("This module must be run directly!")

rawDividers: str
with open("$TRAVIS_BUILD_DIR/area4/dividers.txt", "r") as fh:
    rawDividers = fh.readlines()

d = Area4Instance()

for i in range(len(rawDividers)):
    if i < 1:
        i = 1
    if rawDividers[i] == d.divider(i):
        print("Divider", i, "should work.")
    else:
        print("Divider", i, "is broken!")
        raise ValueError("Broken divider detected!")
