# Environment
- There is a makefile set up now that can handle the conda environment install / update
`make env`
  - this will tell you to run the `conda activate pickapp` commands
  - unfortunately, I am having a tricky time doing this without make making this the base env


# Error handling (mac)
- I keep running in to an error where the miniconda gets moved to the end of the path
  - this means the python in my /usr/bin is foound which is python 2 and I should probably just delete it
- a quick fix is running:
`export PATH="/Users/scottwilster/miniconda3/envs/pickapp/bin:$PATH"`
  - only replace `scottwilster` with your username or the whole miniconda3 path to your conda
