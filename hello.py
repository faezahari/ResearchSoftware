import argparse #a library that stores the parsed command-line argument 

#Creating a parser: 
parser = argparse.ArgumentParser(description='Say Hello')
#Adding arguments
parser.add_argument('name')
parser.add_argument('-r', type=int, default=1) #optional argument and expected to be integer 
#Parsing arguments 
args = parser.parse_args()

# Loop to repeat the greeting
for _ in range(args.r):
    print('Hello ' + args.name + '!')