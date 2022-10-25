#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-blivet
Version  : 3.6.0
Release  : 33
URL      : https://files.pythonhosted.org/packages/a0/85/62a513a64d757284d4d6568901d5667292aa80bcbc9743623f985265f076/blivet-3.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/a0/85/62a513a64d757284d4d6568901d5667292aa80bcbc9743623f985265f076/blivet-3.6.0.tar.gz
Summary  : Python module for system storage configuration
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0+ LGPL-2.1
Requires: pypi-blivet-data = %{version}-%{release}
Requires: pypi-blivet-libexec = %{version}-%{release}
Requires: pypi-blivet-license = %{version}-%{release}
Requires: pypi-blivet-python = %{version}-%{release}
Requires: pypi-blivet-python3 = %{version}-%{release}
Requires: pypi-blivet-services = %{version}-%{release}
Requires: pygobject
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pyudev)
BuildRequires : pypi(six)

%description
The python-blivet package is a python module for examining and modifying
storage configuration.

%package data
Summary: data components for the pypi-blivet package.
Group: Data

%description data
data components for the pypi-blivet package.


%package libexec
Summary: libexec components for the pypi-blivet package.
Group: Default
Requires: pypi-blivet-license = %{version}-%{release}

%description libexec
libexec components for the pypi-blivet package.


%package license
Summary: license components for the pypi-blivet package.
Group: Default

%description license
license components for the pypi-blivet package.


%package python
Summary: python components for the pypi-blivet package.
Group: Default
Requires: pypi-blivet-python3 = %{version}-%{release}

%description python
python components for the pypi-blivet package.


%package python3
Summary: python3 components for the pypi-blivet package.
Group: Default
Requires: python3-core
Provides: pypi(blivet)
Requires: pypi(pyudev)
Requires: pypi(six)

%description python3
python3 components for the pypi-blivet package.


%package services
Summary: services components for the pypi-blivet package.
Group: Systemd services

%description services
services components for the pypi-blivet package.


%prep
%setup -q -n blivet-3.6.0
cd %{_builddir}/blivet-3.6.0
pushd ..
cp -a blivet-3.6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663687287
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-blivet
cp %{_builddir}/blivet-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-blivet/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/blivet-%{version}/COPYING.LESSER %{buildroot}/usr/share/package-licenses/pypi-blivet/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/com.redhat.Blivet0.service

%files libexec
%defattr(-,root,root,-)
/usr/libexec/blivetd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-blivet/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/pypi-blivet/4cc77b90af91e615a64ae04893fdffa7939db84c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/blivet.service
