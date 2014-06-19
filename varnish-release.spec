Name:           varnish-release
Version:        4.0
Release:        3%{?dist}

Summary:        Varnish %{version} package repository configuration

Group:          System Environment/Base
License:        BSD
URL:            http://www.varnish-software.com/installation/redhat

Source0:        varnish.repo
Source1:        RPM-GPG-KEY-VARNISH
Source2:        RPM-GPG-KEY-VARNISH-SOFTWARE

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch

%description
This package contains the varnish-cache.org repository
GPG key as well as configuration for yum.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .
install -pm 644 %{SOURCE2} .

%build

%install
rm -rf $RPM_BUILD_ROOT

# yum
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
sed 's/@@DIST@@/el%{rhel}/' %{SOURCE0} \
    > $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/$(basename "%{SOURCE0}")

install -Dpm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-VARNISH

install -Dpm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-VARNISH-SOFTWARE

install -Dpm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-VARNISH-SOFTWARE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#%doc GPL
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/RPM-GPG-KEY-VARNISH*

%changelog
* Wed Jun 18 2014 Lasse Karstensen <lkarsten@varnish-software.com> 4.0-2
- Install GPG keys.

* Fri May 09 2014 Lasse Karstensen <lkarsten@varnish-software.com> 4.0-1
- 4.0 release.

* Thu Jun 16 2011 Tollef Fog Heen <tfheen@varnish-software.com> 3.0-1
- 3.0 release

* Tue Sep 08 2010 Tollef Fog Heen <tfheen@varnish-software.com> 2.1-2
- Disable signatures as they seem to break RPM.

* Tue Sep 08 2010 Tollef Fog Heen <tfheen@varnish-software.com> 2.1-1
- Initial package
