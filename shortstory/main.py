"""
------------------------------------------------------------------------
[program description]
Main function uses argparse to take arguments from user.
Take input file and output file to be parser argument.
And call the functions.
------------------------------------------------------------------------
Author: Jack Chen
Email:  jackchen4work@gmail.com
Cell:   519-616-7521
github: https://github.com/waterloostar
__updated__ = "2019-03-16"
------------------------------------------------------------------------
"""
import arrange
import argparse
def Main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-i","--input" ,help="Enter input file name")
    parser.add_argument("-o","--output", help="Enter output file name")
    args=parser.parse_args()
    print(args.input)
    if args.input and args.output:
        clean_contents=arrange.clean(args.input)
        parse_content=arrange.parse(clean_contents)
        arrange.sort(parse_content,args.output)
    else:
        pritn('please enter name of input file and output file, enter -h for help')
Main()
