## Acquire.py

Primary purpose of this function, produce DataFrames from fitbit CSVs
How to use:
1. Make sure all your CSVs are in a folder
1. Make sure to not change the name of any of the CSVs
1. import acquire
1. acquire.acquire_fitbit("name of folder with CSVs")

acquire_fitbit returns 3 DataFrames in a list:
1. Food Data
1. Activity Data
1. Food Log Data
