# NOTE: This is only designed for ubuntu and darwin (mac) for now.
#  I think we could use this if we wanted to expand:
#    https://stackoverflow.com/questions/714100/os-detecting-makefile

CONDA_ENV_NAME=pickapp
# Note that the extra activate is needed to ensure that the activate floats env to the front of PATH
CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate

ifeq ($(shell uname -s),Darwin)
	CONDA_YML="environment_mac.yml"
else ifeq ($shell uname -s,ubuntu)
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
    MY_ENV_DIR=$(ENV_DIR)/envs/$(CONDA_ENV_NAME)/
endif


# This dummy timestamp file will allow us to only refresh the environemnt if and when
# either of the environments are touched.
data/.create_env: environment_ubuntu.yml environment_mac.yml
	echo $(MY_ENV_DIR)
	echo $(ENV_DIR)
ifeq (True,$(HAS_CONDA))
# Check if the directory is there.
ifneq ($(wildcard $(MY_ENV_DIR)),)
	@echo ">>> Found $(CONDA_ENV_NAME) environment_mac in $(MY_ENV_DIR). Updating..."
	source $(ENV_DIR)/bin/activate && conda env update -n $(CONDA_ENV_NAME) --file $(CONDA_YML) --prune && source deactivate
else
	@echo ">>> Detected conda, but $(CONDA_ENV_NAME) is missing in $(ENV_DIR). Installing..."
	source $(ENV_DIR)/bin/activate && conda env create -f $(CONDA_YML) && source deactivate
endif
else
	@echo ">>> Install conda first."
	exit 1
endif

	touch $@


env: data/.create_env
	@echo ">>> conda environment $(CONDA_ENV_NAME) is ready to use. Run the following command:\n"
	@echo "conda activate $(CONDA_ENV_NAME)\n"
