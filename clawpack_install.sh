export CLAW=$VIRTUAL_ENV/claw/src/clawpack
echo "export CLAW=$CLAW" >> $VIRTUAL_ENV/bin/activate
source $VIRTUAL_ENV/bin/activate

pip install --upgrade pip
pip install meson-python ninja pkgconfig scipy matplotlib
pip install --no-build-isolation -e git+https://github.com/clawpack/clawpack.git@v5.12.0#egg=clawpack