Summary: High-level C binding for ØMQ
Name: czmq
Version: 4.0.2
Release: 1%{?dist}
License: MPL
Group: Libraries/Network
URL: czmq.zeromq.org

#Source: https://github.com/zeromq/czmq/releases/download/v4.0.2/czmq-4.0.2.tar.gz
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc libzmq-devel
Requires: libzmq libtool

%description
High-level C binding for ØMQ

%package devel
Summary: CZMQ development headers
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This package provides headers for development


%package tools
Summary: CZMQ tools
Group: Libraries/Network
Requires: %{name} = %{version}

%description tools
The package provides command line tools to test basic operations of ZeroMQ

%prep
%setup -q -n %{name}-%{version}/czmq

%build
%{__make} clean || true

./autogen.sh

CFLAGS="$CFLAGS -fPIC"
CXXFLAGS="$CXXFLAGS -fPIC"
%configure --enable-static --with-docs=no

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%pre

%post -n czmq -p /sbin/ldconfig

%postun -n czmq -p /sbin/ldconfig

%files
%files
%defattr(-, root, root, 0755)
%{_libdir}/libczmq.so*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/czmq*.h
%{_includedir}/z*.h
%{_libdir}/libczmq.a
%{_libdir}/libczmq.la
%{_libdir}/pkgconfig/libczmq.pc
%{_datadir}/zproject/czmq

%files tools
%defattr(-, root, root, 0755)
%{_bindir}/zmakecert

%changelog
* Mon May 15 2017 rinigus <rinigus.git@gmail.com> - 4.2.2-1
- initial packaging release for SFOS
