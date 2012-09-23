%bcond_without	tests

%include	/usr/lib/rpm/macros.perl

Summary:	GNU autoconf - source configuration tools
Name:		autoconf
Version:	2.69
Release:	2
License:	GPL
Group:		Development/Building
# stable releases:
Source0:	ftp://ftp.gnu.org/gnu/autoconf/%{name}-%{version}.tar.xz
# Source0-md5:	50f97f4159805e374639a73e2636f22e
Patch0:		%{name}-AC_EGREP.patch
Patch1:		%{name}-cxxcpp-warnonly.patch
URL:		http://www.gnu.org/software/autoconf/
BuildRequires:	m4
BuildRequires:	rpm-perlprov
BuildRequires:	texinfo
Requires:	awk
Requires:	coreutils
Requires:	diffutils
%requires_eq	m4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		%{_datadir}

%description
GNU's Autoconf is a tool for configuring source code and Makefiles.
Using Autoconf, programmers can create portable and configurable
packages, since the person building the package is allowed to specify
various configuration options.

You should install Autoconf if you are developing software and you'd
like to use it to create shell scripts which will configure your
source code packages.

Note that the Autoconf package is not required for the end user who
may be configuring software with an Autoconf-generated script;
Autoconf is only required for the generation of the scripts, not their
use.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--host=%{_host}	\
	--build=%{_host}
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \

%if %{with tests}
%check
%{__make} -j1 check
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog ChangeLog.2 NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_libdir}/autoconf
%{_infodir}/*.info*
%{_mandir}/man1/*

