# How to get around using virtual environment.
- most python packages git ignore virtual environments
  - this means we will need to keep track of which packages are necessary so anyone can run this repo when your venv/ folder is not in it
- I am using conda to handle my packages (tehe)
- I copied all the packages you have in your `venv/lib/python3.8/site-packages`:
```
conda install asgiref django pip pypandoc pytz setuptools sqlparse wheel
```
- **NOTE**: pkg_resources is in setuptools, which is why it doesn't have an .egg-info folder
- **NOTE**: I learne this from errors, but these three packages have to be pip installed, not conda:
`sly publisher aggregate`
  - to do this, I will create then environment_ubuntu.yml file:
```
conda env export > environment_ubuntu.yml
```
  - then add them to the pip section of the environment_ubuntu.yml file and run ubuntu:
```
conda env update -n pickapp --file environment_ubuntu.yml --prune
```
- and on mac:
```
conda env update -n pickapp --file environment_mac.yml --prune
```
  - I had to `conda install nbconvert` for publisher
  - I had to `conda install numpy pandas matplotlib scipy seaborn` for aggregate
    - python is dogshit without numpy and pandas anyway
    - fun fact: all the fedora nerds run `import seaborn as sns` because [this](https://stackoverflow.com/questions/41499857/seaborn-why-import-as-sns) and I think it's stupid

