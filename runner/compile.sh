#!/bin/bash
#
# compile.sh
# Copyright (C) 2020 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD 3-Clause license.
#

export MAKEFLAGS='-j16'
version='5.5.2'

cd config
configs=$(ls -1 config_* | sed 's#^config_\(.\+\)#\1#')
cd ..

mkdir -p compiled

for c in $configs; do
	if ls -1 compiled | grep $c >/dev/null; then
		continue
	fi

	cp config/config_$c linux/config

	cd linux
	makepkg -sf
	cp linux-$version*.pkg.tar.zst ../compiled/linux-$version-$c.pkg.tar.zst
	cd ..
done
