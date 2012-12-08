Name:           python-virtkey
Version:        0.60.0
Release:        %mkrel 1
Summary:        Python extension for emulating keypresses and getting current keyboard layout

Group:          Development/Python
License:        GPLv2+
URL:            https://launchpad.net/virtkey
Source0:        http://launchpad.net/virtkey/trunk/0.50/+download/%{name}-%{version}.tar.gz
Patch0:         virtkey-gdk-pixbuf-headers.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel, libxtst-devel, gtk2-devel, glib2-devel

%description
Python-virtkey is a python extension for emulating keypresses and getting
current keyboard layout.

%prep
%setup -q 

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
#no documentation included in upstream tarball
%{python_sitearch}/*



%changelog
* Fri Jan 07 2011 Antoine Ginies <aginies@mandriva.com> 0.60.0-1mdv2011.0
+ Revision: 629471
- fix buildrequires, remove unwanted stuff
- fix group
- import python-virtkey

