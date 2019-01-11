Summary:	Python extension for emulating keypresses and getting current keyboard layout
Name:		python-virtkey
Version:	0.63.0
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		https://launchpad.net/virtkey
Source0:	http://launchpad.net/virtkey/0.63/0.63.0/+download/virtkey-%{version}.tar.gz
Patch0:		virtkey-gdk-pixbuf-headers.patch
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(xtst)

%description
Python-virtkey is a python extension for emulating keypresses and getting
current keyboard layout.

%prep
%setup -q 

%build
CFLAGS="%{optflags}" python2} setup.py build

%install
python setup.py install --root %{buildroot}


%files
#no documentation included in upstream tarball
%{py_platsitedir}/*
