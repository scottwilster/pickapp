# NOTE: This is only designed for ubuntu and darwin (mac) for now.
#  I think we could use this if we wanted to expand:
#    https://stackoverflow.com/questions/714100/os-detecting-makefile

CONDA_ENV_NAME=pickapp

ifeq ($(shell uname -s), Darwin)
	CONDA_YML="environment_mac.yml"
else ifeq ($shell uname -s, ubuntu)
	CONDA_YML="environment_ubuntu.yml"
else
	@echo "Error, only designed for Darwin & ubuntu currently"
	exit 0
endif

# Check for existing conda env.
ifeq (,$(shell which conda))
    HAS_CONDA=False
else
    HAS_CONDA=True
    ENV_DIR=$(shell conda info --base)
    MY_ENV_DIR=$(ENV_DIR)/envs/$(CONDA_ENV_NAME)
    # CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate
endif

test:
	echo $(HAS_CONDA)
	echo $(ENV_DIR)
	echo $(MY_ENV_DIR)
#	echo $(CONDA_ACTIVATE)

# environment:
# ifeq (True,$(HAS_CONDA))
# ifneq ("$(wildcard $(MY_ENV_DIR))","") # check if the directory is there
# 	@echo ">>> Found $(CONDA_ENV_NAME) environment in $(MY_ENV_DIR). Skipping installation..."
# else
# 	@echo ">>> Detected conda, but $(CONDA_ENV_NAME) is missing in $(ENV_DIR). Installing ..."
# 	conda env create -f $(CONDA_YML) -n $(CONDA_ENV_NAME)
# endif
# else
# 	@echo ">>> Install conda first."
# 	exit
# endif


# This dummy timestamp file will allow us to only refresh the environemnt if and when
# either of the environments are touched.
data/.create_env: environment_ubuntu.yml environment_mac.yml
	echo $(shell uname)
	echo $(CONDA_YML)

	touch $@

env: data/.create_env
	make data/.create_env
