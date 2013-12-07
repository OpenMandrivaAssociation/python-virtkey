Summary:	Python extension for emulating keypresses and getting current keyboard layout
Name:		python-virtkey
Version:	0.60.0
Release:	3
Group:		Development/Python
License:	GPLv2+
Url:		https://launchpad.net/virtkey
Source0:	http://launchpad.net/virtkey/trunk/0.50/+download/%{name}-%{version}.tar.gz
Patch0:		virtkey-gdk-pixbuf-headers.patch
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(xtst)

%description
Python-virtkey is a python extension for emulating keypresses and getting
current keyboard layout.

%prep
%setup -q 

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__python} setup.py install --root %{buildroot}


%files
#no documentation included in upstream tarball
%{python_sitearch}/*

