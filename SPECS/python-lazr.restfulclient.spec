%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

#python major version
%{expand: %%define pyver %(%{__python} -c 'import sys;print(sys.version[0:3])')}

Name:		python-lazr.restfulclient
Version:	0.11.2
Release:	1.ius%{?dist}
Summary:	A programmable client library	

Group:		Applicatons/System
License:	GPLv3
URL:		https://launchpad.net/lazr.restfulclient	
Source0:	http://launchpad.net/lazr.restfulclient/trunk/0.11.2/+download/lazr.restfulclient-%{version}.tar.gz
Patch0:		remove_install_requires.diff

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

BuildRequires:	python, python-setuptools
Requires:	python
Requires:	python-httplib2, python-lazr.authentication, python-oauth
Requires:	python-wadllib >= 1.1.4
Requires:	python-wsgi_intercept

%description
A programmable client library that takes advantage of ithe commonalities among 
lazr.restful web services to provide added functionality on top of wadllib.

%prep
%setup -q -n lazr.restfulclient-%{version}
%patch0 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 \
		    --skip-build \
	     --root %{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc PKG-INFO README.txt HACKING.txt COPYING.txt 
%{python_sitelib}/lazr.restfulclient-%{version}-py%{pyver}.egg-info/
%{python_sitelib}/lazr.restfulclient-%{version}-py%{pyver}-nspkg.pth/
%{python_sitelib}/lazr/restfulclient/


%changelog
* Fri Jun 10 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.11.2-1.ius
- Initial spec
