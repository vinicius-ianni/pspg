# -*- mode: rpm-spec-mode; encoding: utf-8; -*-
# Pass '--without docs' to rpmbuild if you don't want the documentation to be build

Summary: 	pspg: a unix pager optimized for psql
Name: 		pspg
Version: 	0.7
Release: 	0%{?dist}
License: 	BSD
Group: 		Development/Tools
Vendor: 	Pavel Stehule <pavel.stehule@gmail.com>
URL: 		https://github.com/okbob/pspg
Source: 	https://github.com/okbob/pspg/releases/download/%{name}-%{version}/%{name}-%{version}.tgz
BuildRequires: 	ncurses-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: 	ncurses

%description
psps is a unix pager optimized for psql. It can freeze rows, freeze
columns, and lot of color themes are included.

%prep
%setup -q -n pspg

%build
%configure
CFLAGS="$RPM_OPT_FLAGS"
%{__make} %{_smp_mflags} \
	prefix=%{_prefix} \
	all

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
CFLAGS="$RPM_OPT_FLAGS"
%{__make} %{_smp_mflags} DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} bindir=%{_bindir} mandir=%{_mandir} \
	install

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*

%changelog
* Wed Sep 13 2017 Pavel Stehule <pavel.stehule@gmail.com>
- initial version

* Sat Nov 25 2017 Pavel Stehule <pavel.stehule@gmail.com>
- lot of fixes and new features