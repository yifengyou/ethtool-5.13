#!/bin/bash

if ! which gcc ; then
	echo "gcc not found!"
	exit 1
fi

start_time=`date`
./configure --build=x86_64-redhat-linux-gnu --host=x86_64-redhat-linux-gnu \
	--program-prefix= --disable-dependency-tracking --prefix=/usr \
	--exec-prefix=/usr --bindir=/usr/bin --sbindir=/usr/sbin \
	--sysconfdir=/etc --datadir=/usr/share --includedir=/usr/include \
	--libdir=/usr/lib64 --libexecdir=/usr/libexec --localstatedir=/var \
	--sharedstatedir=/var/lib --mandir=/usr/share/man --infodir=/usr/share/info
make -j`nproc`
ret=$?
end_time=`date`

echo "All done![${ret}]"
echo "  ${start_time}"
echo "  ${end_time}"
