'''
Given a version, such as 1.23.45, various portions of it can be increased.

By default the least significant portion of the version is increased by one.

The -m option will increase the middle portion.

The -M option will increase the most significant portion.


Examples:

python bumpversion.py 1.23.45
1.23.46

python bumpversion.py -m 1.23.45
1.24.0

python bumpversion.py -M 1.23.45
2.0.0


Versions can also be piped into the tool and output to stdout:

echo 1.23.45 | python bumpversion.py
1.23.46

echo 1.23.45 | python bumpversion.py -m
1.24.0

echo 1.23.45 | python bumpversion.py -M
2.0.0

'''

import sys
import os

def main(args):
    version = ''
    bumpindex = 2
    if len(args) > 0:
        thisarg = args[0]
        if thisarg == '-h' or thisarg == '--help':
            print("Usage: python {} [-m | -M] M.m.x\n       echo M.m.x | python {} [-m | -M]\n\n-m    bump minor version\n-M    bump major version".format(os.path.basename(__file__),os.path.basename(__file__)))
            return
        if thisarg == '-m':
            bumpindex = 1
        elif thisarg == '-M':
            bumpindex = 0
        else:
            version = thisarg.strip()
        if len(args) > 1:
            version = args[1]
    if len(version) == 0:
        try:
            for line in sys.stdin:
                version = line.strip()
        except KeyboardInterrupt:
            pass

    try:
        versions = list(map(int,version.split('.')))[:bumpindex+1]
        versions.extend([0,0])
        versions[bumpindex] += 1
        newversion = '.'.join(map(str,versions[:3]))
        print('{}'.format(newversion))
    except:
        print('Invalid version')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
