# Environment
- After conda is installed, to get the packages you need run
  - mac:
```
conda env create -f environment_mac.yml
```
  - ubuntu:
```
conda env create -f environment_ubuntu.yml
```
- after it's done, make sure to activate the conda env
```
conda activate pickapp
```

# Error handling (mac)
- I keep running in to an error where the miniconda gets moved to the end of the path
  - this means the python in my /usr/bin is foound which is python 2 and I should probably just delete it
- a quick fix is running:
`export PATH="/Users/scottwilster/miniconda3/envs/pickapp/bin:$PATH"`
  - only replace `scottwilster` with your username or the whole miniconda3 path to your conda
