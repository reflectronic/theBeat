Name:           thebeat-blueprint
Version:        3.0.0
Release:        1%{?dist}
Summary:        Music Player

License:        GPLv3+
URL:            https://github.com/vicr123/thebeat
Source0:        https://github.com/vicr123/theBeat/archive/v%{version}.tar.gz

%if 0%{?fedora} == 32
BuildRequires:  make qt5-devel qt5-qtmultimedia-devel the-libs-blueprint-devel phonon-qt5-devel taglib-devel libcdio-paranoia-devel libcdio-paranoia-devel libmusicbrainz5-devel
Requires:       qt5 qt5-qtmultimedia the-libs-blueprint phonon-qt5 taglib libmusicbrainz5
%endif

%if 0%{?fedora} >= 33
BuildRequires:  make qt5-qtbase-devel qt5-qtmultimedia-devel qt5-qtx11extras-devel the-libs-blueprint-devel phonon-qt5-devel taglib-devel qt5-linguist libcdio-paranoia-devel libcdio-paranoia-devel libmusicbrainz5-devel
Requires:       qt5-qtbase qt5-qtx11extras qt5-qtmultimedia the-libs-blueprint phonon-qt5 taglib libmusicbrainz5
%endif

%define debug_package %{nil}
%define _unpackaged_files_terminate_build 0

%description
Music Player

%prep
%setup

%build
mkdir build
cd build
qmake-qt5 ../theBeat.pro CONFIG+=blueprint
make

%install
rm -rf $RPM_BUILD_ROOT
#%make_install
cd build
make install INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%{_bindir}/thebeat
%{_libdir}/thebeat/*
%{_libdir}/libthebeat.so*
%{_datadir}/applications/com.vicr123.thebeat_blueprint.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.vicr123.thebeat_blueprint.svg
%{_datadir}/thebeat/*



%changelog
* Sun May  3 2020 Victor Tran
- 
