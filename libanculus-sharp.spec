%define name libanculus-sharp
%define version 0.3.1
%define release %mkrel 5

Summary: Reusable utility library written in C#
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch: libanculus-sharp-0.3.1-libdir.patch
License: MIT
Group: Development/Other
Url: http://code.google.com/p/libanculus-sharp/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: monodoc
BuildRequires: gtk-sharp2
BuildArch: noarch

%description
Anculus means servant in Latin, and that is exactly what the library does. It
serves and helps you to easily and quickly write new applications.
libanculus-sharp contains all the building blocks that you need to develop a
good C# application.
Features:
* XML Configuration files (primitive types, strings, serializable objects,
  lists, arrays, ...)
* Sorting algorithms (quicksort)
* String Search algorithms (Boyer-Moore, Aho-Corasick)
* Translation support (Managed Gettext)
* Logging (Console, Colored Console, File)
* Gui thread dispatching (Gtk-sharp, System.Windows.Forms)
* Collections (sorted list) 

%package doc
Summary:	Development documentation for %name
Group:		Development/Other
Requires(post):		mono-tools >= 1.1.9
Requires(postun):	mono-tools >= 1.1.9

%description doc
This package contains the API documentation for %name in
Monodoc format.

%prep
%setup -q
%patch -p1
sh autogen.sh

%build
%configure2_5x --libdir=%_prefix/lib
%make

%install
rm -rf %{buildroot}
%makeinstall pkgconfigdir=%buildroot%_datadir/pkgconfig monodocdir=%buildroot%_prefix/lib/monodoc/sources monodoc_DATA="libanculus-sharp.zip libanculus-sharp.tree libanculus-sharp.sources"
rm -fr %buildroot%_prefix/lib*/libanculus-sharp

%clean
rm -rf %{buildroot}

%post doc
%_bindir/monodoc --make-index > /dev/null

%postun doc
if [ "$1" = "0" -a -x %_bindir/monodoc ]; then %_bindir/monodoc --make-index > /dev/null
fi

%files
%defattr(-,root,root)
%doc AUTHORS
%_prefix/lib/mono/libanculus-sharp
%_prefix/lib/mono/gac/Anculus.Core/
%_prefix/lib/mono/gac/Anculus.Core.Extended/
%_prefix/lib/mono/gac/Anculus.Gui/
%_datadir/pkgconfig/*.pc

%files doc
%defattr(-,root,root)
%_prefix/lib/monodoc/sources/libanculus-sharp*


