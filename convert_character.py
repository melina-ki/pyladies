import argparse

parser=argparse.ArgumentParser(prog='convert_character', description='This program converts defined characters of an input file to defined characters, and writes the output into an output file. Default: o to 0.')
parser.add_argument('input_file', help='Define input file', type=str)
parser.add_argument('output_file', help='Define output file', type=str)
parser.add_argument('-v','--verbose',help='increase output verbosity', action='store_true')
parser.add_argument('-o','--original_character',help='Character to be replaced',default="o", type=str)
parser.add_argument('-R', '--replacement_character',help='Character to replace original character',default="0",type=str)

args=parser.parse_args()

def convert_character(input_file, output_file, verbose, original_character, replacement_character):
        file_to_convert=open(input_file, encoding='utf-8')
        converted_file=open(output_file, mode='r+', encoding='utf-8') #mode=read and write, else its not going to be able to print it at the end!

        for line in file_to_convert:
                converted_file.write(line.replace(original_character,replacement_character))

#this tells Python to start reading the file from the beginning, else  it is stuck at the end.
#I wanted to print the output file to check if it worked, and just doing print(converted_file.read()) wouldnt work, so after searching I found this solution..

        converted_file.seek(0) 
        print(converted_file.read())
        file_to_convert.close()
        converted_file.close()
        if verbose:
                print("{} has been replaced with {} in the input file".format(original_character,replacement_character))

convert_character(args.input_file, args.output_file, args.verbose, args.original_character, args.replacement_character)

