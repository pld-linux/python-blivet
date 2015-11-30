%define module blivet
Summary:	A Python module for system storage configuration
Name:		python-blivet
Version:	0.14
Release:	3
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/python-blivet/%{module}-%{version}.tar.gz/30592cc8261fb936023b9d466dec68da/%{module}-%{version}.tar.gz
# Source0-md5:	30592cc8261fb936023b9d466dec68da
Patch0:		lvm-lvmetad.patch
URL:		http://fedoraproject.org/wiki/blivet
BuildRequires:	gettext-tools
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	btrfs-progs
Requires:	cryptsetup-luks
Requires:	device-mapper >= 1.02.17-6
Requires:	dosfstools
Requires:	e2fsprogs >= 1.41.0
Requires:	lvm2 >= 2.02.98-3
Requires:	mdadm
Requires:	multipath-tools >= 0.4.9-10
Requires:	parted >= 1.8.1
Requires:	python
Requires:	python-cryptsetup >= 0.1.1
Requires:	python-parted >= 2.5-2
Requires:	python-pyblock >= 0.45
Requires:	python-pykickstart >= 1.99.22
Requires:	util-linux >= 2.22.2-6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The python-blivet package is a Python module for examining and
modifying storage configuration.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# redo python install to get optimize=2
%py_install

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
