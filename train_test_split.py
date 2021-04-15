import os
import splitfolders


base_dir = "Data"
for filename in os.listdir(base_dir):
        split_file = splitfolders.ratio(base_dir, output="output", seed=1337, ratio=(.8, .1, .1))