%define major 1
%define libname %mklibname wpebackend-fdo %{major}
%define devname %mklibname wpebackend-fdo -d


Name:           wpebackend-fdo
Version:        1.12.0
Release:        1
Summary:        A WPE backend designed for Linux desktop systems
Group:		System/Libraries
License:        BSD
URL:            https://github.com/Igalia/%{name}
Source0:	https://github.com/Igalia/WPEBackend-fdo/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  mesa-common-devel
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(wpe-1.0)
BuildRequires:  wayland-devel
BuildRequires:  glib2.0-devel

%description
A WPE backend designed for Linux desktop systems.

%package -n %{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries
License:	LGPLv2+

%description -n %{libname}
Libraries for %{name}.

%package   -n	%{devname}
Summary:	Development files for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
The %{devname} package contains libraries, build data, and header
files for developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake
%make_build

%install
%make_install -C build

%files -n %{libname}
%license COPYING
%doc NEWS
%{_libdir}/libWPEBackend-fdo-1.0.so.%{major}*

%files -n %{devname}
%{_includedir}/wpe-fdo-1.0
%{_libdir}/pkgconfig/wpebackend-fdo-1.0.pc
%{_libdir}/libWPEBackend-fdo-1.0.so
