#
# Conditional build:
%bcond_without	static_libs # don't build static libraries
#
Summary:	Library to create and read several different archive formats
Summary(pl):	Biblioteka do tworzenia i odczytu ró¿nych formatów archiwów
Name:		libarchive
Version:	1.3.1
Release:	0.1
License:	BSD
Group:		Libraries
Source0:	http://people.freebsd.org/~kientzle/libarchive/src/%{name}-%{version}.tar.gz
# Source0-md5:	c618d26d680ace57fcd5f59cea3151c6
Patch0:		%{name}-CVE-2006-5680.patch
Patch1:		%{name}-man_progname.patch
URL:		http://people.freebsd.org/~kientzle/libarchive/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	e2fsprogs-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libarchive is a programming library that can create and read several
different streaming archive formats, including most popular TAR
variants and several CPIO formats. It can also write SHAR archives.

%description -l pl
Libarchive jest bibliotek± s³u¿ac± to tworzenia i odczytu wielu
ró¿nych strumieniowych formatów archiwów, w³±czaj±c w to popularne
odmiany TAR oraz wiele formatów CPIO. Biblioteka ta potrafi tak¿e
zapisywaæ archiwa SHAR.

%package devel
Summary:	Header files for libarchive library
Summary(pl):	Pliki nag³ówkowe biblioteki libarchive
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libarchive library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libarchive.

%package static
Summary:	Static libarchive library
Summary(pl):	Statyczna biblioteka libarchive
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libarchive library.

%description static -l pl
Statyczna biblioteka libarchive.

%package -n bsdtar
Summary:	bsdtar - tar(1) implementation based on libarchive
Summary(pl):	bsdtar - implementacja programu tar(1) oparta na libarchive
Group:		Applications/Archiving
Requires:	%{name} = %{version}-%{release}

%description -n bsdtar
bsdtar - tar(1) implementation based on libarchive.

%description -n bsdtar -l pl
bsdtar - implementacja programu tar(1), oparta na libarchive.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static=%{?with_static_libs:yes}%{!?with_static_libs:no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libarchive.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libarchive.so
%{_libdir}/libarchive.la
%{_includedir}/*.h
%{_mandir}/man3/*
%{_mandir}/man5/*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libarchive.a
%endif

%files -n bsdtar
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bsdtar
%{_mandir}/man1/bsdtar.1*
