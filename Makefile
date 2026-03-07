.PHONY: all

OUTDIR ?= _output
CLAW = $(VIRTUAL_ENV)/src/clawpack
PYTHON = $(VIRTUAL_ENV)/bin/python

simulation:
	cp config.yaml numerical_simulation/config.yaml
	cd numerical_simulation ; make simulation OUTDIR=$(OUTDIR)

clawpack:
	echo "export CLAW=$(CLAW)" >> $(VIRTUAL_ENV)/bin/activate
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install meson-python ninja pkgconfig scipy matplotlib
	$(PYTHON) -m pip install --no-build-isolation -e git+https://github.com/clawpack/clawpack.git@v5.12.0#egg=clawpack