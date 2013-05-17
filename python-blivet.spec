# Versions of required components (done so we make sure the buildrequires
# match the requires versions of things).
%define dmver 1.02.17-6
%define pykickstartver 1.99.22
%define partedver 1.8.1
%define pypartedver 2.5-2
%define pythonpyblockver 0.45
%define e2fsver 1.41.0
%define pythoncryptsetupver 0.1.1
%define utillinuxver 2.15.1

%define module blivet
Summary:	A Python module for system storage configuration
Name:		python-blivet
Version:	0.14
Release:	1
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/python-blivet/%{module}-%{version}.tar.gz/30592cc8261fb936023b9d466dec68da/%{module}-%{version}.tar.gz
# Source0-md5:	30592cc8261fb936023b9d466dec68da
URL:		http://fedoraproject.org/wiki/blivet
BuildRequires:	gettext-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	btrfs-progs
Requires:	cryptsetup-luks
Requires:	device-mapper >= %{dmver}
Requires:	dosfstools
Requires:	e2fsprogs >= %{e2fsver}
Requires:	lvm2 >= 2.02.98-3
Requires:	mdadm
Requires:	multipath-tools
Requires:	parted >= %{partedver}
Requires:	python
Requires:	python-cryptsetup >= %{pythoncryptsetupver}
Requires:	python-parted >= %{pypartedver}
Requires:	python-pyblock >= %{pythonpyblockver}
Requires:	python-pykickstart >= %{pykickstartver}
Requires:	util-linux >= %{utillinuxver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The python-blivet package is a Python module for examining and
modifying storage configuration.

%prep
%setup -q -n %{module}-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# redo python install to get optimize=2
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

# unsupported locale
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ilo

%find_lang %{module}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{module}.lang
%defattr(644,root,root,755)
%doc README ChangeLog
%{py_sitescriptdir}/blivet
%{py_sitescriptdir}/blivet-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}
