Summary: 	Tools for using the Network Block Device
Name: 		nbd-tools
Version: 	1.3
Copyright: 	GPL
Release:	1
Group: 		Utilities/System
Group(pl):	Narzêdzia/System
Packager:	Erik Corry <erik@arbat.com>
Source0:	http://atrey.karlin.mff.cuni.cz/~pavel/nbd/nbd.14.tar.gz
Source1:	http://www.image.dk/~ehcorry/linux/nbd.swap-patch.123-erik-2.2.13pre17
Source2:	nbd.README
Patch0:		ndb-debug.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nbd-tools are the tools needed to export a network block device
and to use a network block device.  There are no README files
or man pages, but the programs have a usage-message, and you
can read the source of the nbd kernel module.  The nbd module is
part of the 2.2 kernels and higher.

If you have a kernel patched for it, you can use the network block
device to swap over the net, which is particularly useful for
diskless workstations.

The nbd home page is on http://atrey.karlin.mff.cuni.cz/~pavel/nbd/nbd.html

%prep
%setup -q -n nbd
%patch0 -p0 -b .debug
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
%configure
%{__make}

%install
install -d $RPM_BUILD_ROOT/sbin
install -d $RPM_BUILD_ROOT/usr/sbin
install nbd-client $RPM_BUILD_ROOT/sbin/
install nbd-server $RPM_BUILD_ROOT/usr/sbin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root)
%doc nbd.README nbd.swap-patch.123-erik-2.2.13pre17 nbd.20.diff nbd.swap-patch.23
/sbin/nbd-client
/usr/sbin/nbd-server

%post
umask 177
if [ ! -b /dev/nb0 ]; then
    minor=0
    while [ "$minor" -ne 128 ]; do
	mknod "/dev/nb$minor" b 43 $minor
	minor=$(($minor + 1))
    done
fi
