#
# Copyright (C) 2013 Judge Maygarden (wtfpl.jmaygarden@safersignup.com)
#
#        DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.
#

import argparse
from ftltools import profile

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dump FTL profile data.')
    parser.add_argument('file', nargs=1, help='FTL profile (prof.sav) file')
    args = parser.parse_args()
    with open(args.file[0], 'rb') as fin:
        data = profile.parse(fin)
        print profile.to_txt(data)

