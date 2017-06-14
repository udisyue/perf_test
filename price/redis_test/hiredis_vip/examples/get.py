import os
import sys
reload(sys)
sys.path.append(".")

if __name__ == '__main__':
    cmd = "./get"
    print os.popen(cmd).read()
