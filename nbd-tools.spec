Summary:	Tools for using the Network Block Device
Summary(pl):	Narzêdzia do u¿ywania Network Block Device
Name:		nbd-tools
Version:	1.3
License:	GPL
Release:	2
Group:		Applications/System
Source0:	http://atrey.karlin.mff.cuni.cz/~pavel/nbd/nbd.14.tar.gz
Source1:	http://www.image.dk/~ehcorry/linux/nbd.swap-patch.123-erik-2.2.13pre17
Source2:	nbd.README
Patch0:		ndb-debug.patch
URL:		http://atrey.karlin.mff.cuni.cz/~pavel/nbd/nbd.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nbd-tools are the tools needed to export a network block device and to
use a network block device. There are no README files or man pages,
but the programs have a usage-message, and you can read the source of
the nbd kernel module. The nbd module is part of the 2.2 kernels and
higher.

If you have a kernel patched for it, you can use the network block
device to swap over the net, which is particularly useful for diskless
workstations.

%description -l pl
nbd-tools to narzêdzia potrzebne do wyeksportowania i u¿ywania
sieciowego urz±dzenia blokowego (Network Block Device). Modu³ do nbd
jest w j±drze 2.2 i pó¼niejszych.

Je¿eli masz kernel z odpowiedni± ³at±, mo¿esz u¿ywaæ sieciowego
urz±dzenia blokowego do swapowania przez sieæ - jest to przydatne w
przypadku stacji bezdyskowych.

%prep
%setup -q -n nbd
%patch0 -p0
cp -f %{SOURCE1} .
cp -f %{SOURCE2} .

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,%{_sbindir}}

install nbd-client $RPM_BUILD_ROOT/sbin/
install nbd-server $RPM_BUILD_ROOT%{_sbindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc nbd.README nbd.swap-patch.123-erik-2.2.13pre17 nbd.20.diff nbd.swap-patch.23
%attr(755,root,root) /sbin/nbd-client
%attr(755,root,root) %{_sbindir}/nbd-server
