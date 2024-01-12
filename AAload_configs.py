import argparse
import yaml
from pprint import pprint

# list of system and user configs to load 
CONFIG_PATHS = ['system_config.yml', 'user_config.yml']

# parse  the job config file from command line 
parser = argparse.ArgumentParser()
parser.add_argument('job_config', type=str)
args = parser.parse_args()

# add analysis config to list of paths to load 
paths_to_load = CONFIG_PATHS + [args.job_config]

# initialize an empty dictionary to hold the final configuration
config = {}

for path in paths_to_load:
    print('Loading ' + path)
    with open(path, 'r') as f:
        this_config = yaml.safe_load(f)
        
    config.update(this_config) #use update to overwrite configuration update
    print(config)
    

print(config)