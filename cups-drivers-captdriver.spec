%define filter_name captdriver

%define snapshot 20231218
%define commit 711d4a56c57e2dde5cfbb166f036192a5913413c
%define shortcommit %(c=%{commit}; echo ${c:0:7})

Summary:	Cups filter for Canon CAPT printers
Name:		cups-drivers-%{filter_name}
Version:	0.1.4
Release:	%{?snapshot:0.%{snapshot}git.}1
License:	GPLv3+
Group:		System/Printing
# Also: https://github.com/agalakhov/captdriver
Url:		https://github.com/mounaiban/captdriver
Source0:	https://github.com/mounaiban/captdriver/archive/%{?snapshot:%{commit}/}captdriver-%{?snapshot:%{commit}}%{?!snapshot:%{version}}.%{?snapshot:zip}%{?!snapshot:tar.gz}

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
%{_prefix}/lib/cups/filter/rastertocapt
%{_datadir}/cups/model/%{filter_name}/*ppd

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{?snapshot:%{filter_name}-%{commit}}%{?!snapshot:captdriver-%{version}}

%build
autoreconf -fiv
%configure
%make_build all
ppdc src/*.drv

%install
#make_install

# filter
install -dm 0755 %{buildroot}%{_prefix}/lib/cups/filter/
install -pm 0755 src/rastertocapt %{buildroot}%{_prefix}/lib/cups/filter/

# PPD files
install -dm 0755 %{buildroot}%{_datadir}/cups/model/%{filter_name}/
install -pm 644 ppd/*.ppd %{buildroot}%{_datadir}/cups/model/%{filter_name}/

