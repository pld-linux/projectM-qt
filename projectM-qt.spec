Summary:	GUI to enhance the projectM user and preset writer experience
Summary(pl.UTF-8):	GUI ułatwiające pracę użytkownikom projectM i twórcom ustawień
Name:		projectM-qt
Version:	2.0.1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/projectm/%{name}-%{version}-Source.tar.gz
# Source0-md5:	b8551e148633d2e2ddb5c5efa859a4c3
URL:		http://projectm.sourceforge.net/
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	QtOpenGL-devel >= 4
BuildRequires:	QtXml-devel >= 4
BuildRequires:	cmake >= 2.4.0
BuildRequires:	libprojectM-devel >= 1:2.0.1
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
projectM-qt is a GUI designed to enhance the projectM user and preset
writer experience.

%description -l pl.UTF-8
projectM-qt to GUI zaprojektowane w celu ułatwienia pracy użytkownikom
projectM oraz piszącym ustawienia. 

%package devel
Summary:	Header files for projectM-qt library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki projectM-qt
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	QtCore-devel >= 4
Requires:	QtGui-devel >= 4
Requires:	QtOpenGL-devel >= 4
Requires:	QtXml-devel >= 4
Requires:	libprojectM-devel >= 1:2.0.1

%description devel
Header files for projectM-qt library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki projectM-qt.

%prep
%setup -q -n %{name}-%{version}-Source

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ReadMe
%attr(755,root,root) %{_libdir}/libprojectM-qt.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libprojectM-qt.so.1
%{_pixmapsdir}/prjm16-transparent.svg

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libprojectM-qt.so
%{_includedir}/libprojectM-qt
%{_pkgconfigdir}/libprojectM-qt.pc
