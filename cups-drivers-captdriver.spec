%define filter_name captdriver

%define snapshot 20220921
%define commit 50aa43b947fabee2967fa6757517fb30c197ecb3
%define shortcommit %(c=%{commit}; echo ${c:0:7})

Summary:	Cups filter for Canon CAPT printers
Name:		cups-drivers-%{filter_name}
Version:	0.1.3
Release:	%{?snapshot:0.%{snapshot}git.}1
License:	GPLv3+
Group:		System/Printing
Url:		https://github.com/agalakhov/captdriver
Source0:	https://github.com/agalakhov/%{filter_name}/archive/%{?snapshot:%{commit}/}captdriver-%{?snapshot:%{commit}}%{?!snapshot:%{version}}.%{?snapshot:zip}%{?!snapshot:tar.gz}

BuildRequires:	cups
BuildRequires:	cups-common
BuildRequires:	cups-devel

%description
This is a driver for Canon CAPT3-based printers (LBP-***) based on several
reverse engineering attempts.

This is currently in an early alpha stage. Use at your own risk.

Actually it supports the following models:
  * LBP2900 (works)
  * LBP3000 (experimental)
  * LBP3010/LBP3018/LBP3050 (works)

%files
%license COPYING
%doc AUTHORS README SPECS NEWS ChangeLog
%{_libdir}/cups/filter/rastertocapt
%{_datadir}/cups/model/%{filter_name}/*ppd

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{?snapshot:%{filter_name}-%{commit}}%{?!snapshot:captdriver-%{version}}

%build
autoreconf -fiv
%configure
%make_build all ppd

%install
#make_install

# filter
install -dm 0755 %{buildroot}%{_libdir}/cups/filter/
install -pm 0755 src/rastertocapt %{buildroot}%{_libdir}/cups/filter/

# PPD files
install -dm 0755 %{buildroot}%{_datadir}/cups/model/%{filter_name}/
install -pm 644 ppd/*.ppd %{buildroot}%{_datadir}/cups/model/%{filter_name}/

