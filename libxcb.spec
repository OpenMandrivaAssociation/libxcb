%define libxcb %mklibname xcb 1
%define libdev %mklibname xcb -d
%define libdevst %mklibname xcb -d -s

Name: libxcb
Summary: X protocol C-language Binding Library
Version: 1.1.91
Release: %mkrel 1
Group: System/X11
License: MIT
URL: http://xcb.freedesktop.org
Source0: http://xcb.freedesktop.org/dist/libxcb-%{version}.tar.bz2
Patch0: libxcb-1.1-sloppy-lock-on-by-default.patch
BuildRoot: %{_tmppath}/%{name}-root

# because of xcb-proto-1.1 (at least)
BuildRequires: x11-proto-devel >= 7.3-2mdv

BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: libpthread-stubs
BuildRequires: libxslt-proc
BuildRequires: libxdmcp-devel
BuildRequires: doxygen
BuildRequires: python-celementtree

%description
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

#-----------------------------------------------------------

%package -n %{libxcb}
Summary: X protocol C-language Binding Library
Group: System/X11
Provides: %{name} = %{version}

%description -n %{libxcb}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

#-----------------------------------------------------------

%package -n %{libdev}
Summary: Development files for %{name}
Group: Development/X11
Requires: x11-proto-devel >= 1.2.0
Provides: xcb-devel = %{version}-%{release}
Obsoletes: %{libxcb}-devel
Requires: %{libxcb} = %{version}
# gw this isn't picked up by the automatic pkgconfig deps, but without it,
# pkg-config --libs xcb will fail
Requires: libpthread-stubs


%description -n %{libdev}
Development files for %{name}

%files -n %{libdev}
%defattr(-,root,root)
%{_includedir}/xcb/*.h
%{_libdir}/libxcb*.la
%{_libdir}/libxcb*.so
%{_libdir}/pkgconfig/xcb*.pc
%{_docdir}/libxcb/*

#-----------------------------------------------------------

%package -n %{libdevst}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libdev} = %{version}
Obsoletes: %{libxcb}-static-devel

%description -n %{libdevst}
Static development files for %{name}

%files -n %{libdevst}
%defattr(-,root,root)
%{_libdir}/libxcb*.a

#-----------------------------------------------------------

%prep
%setup -q -n libxcb-%{version}
%patch0 -p0 -b .sloppy

%build
%configure

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libxcb} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libxcb} -p /sbin/ldconfig
%endif

%files -n %{libxcb}
%defattr(-,root,root)
%{_libdir}/libxcb-composite.so.0
%{_libdir}/libxcb-composite.so.0.0.0
%{_libdir}/libxcb-damage.so.0
%{_libdir}/libxcb-damage.so.0.0.0
%{_libdir}/libxcb-dpms.so.0
%{_libdir}/libxcb-dpms.so.0.0.0
%{_libdir}/libxcb-glx.so.0
%{_libdir}/libxcb-glx.so.0.0.0
%{_libdir}/libxcb-randr.so.0
%{_libdir}/libxcb-randr.so.0.0.0
%{_libdir}/libxcb-record.so.0
%{_libdir}/libxcb-record.so.0.0.0
%{_libdir}/libxcb-render.so.0
%{_libdir}/libxcb-render.so.0.0.0
%{_libdir}/libxcb-res.so.0
%{_libdir}/libxcb-res.so.0.0.0
%{_libdir}/libxcb-screensaver.so.0
%{_libdir}/libxcb-screensaver.so.0.0.0
%{_libdir}/libxcb-shape.so.0
%{_libdir}/libxcb-shape.so.0.0.0
%{_libdir}/libxcb-shm.so.0
%{_libdir}/libxcb-shm.so.0.0.0
%{_libdir}/libxcb-sync.so.0
%{_libdir}/libxcb-sync.so.0.0.0
%{_libdir}/libxcb-xevie.so.0
%{_libdir}/libxcb-xevie.so.0.0.0
%{_libdir}/libxcb-xf86dri.so.0
%{_libdir}/libxcb-xf86dri.so.0.0.0
%{_libdir}/libxcb-xfixes.so.0
%{_libdir}/libxcb-xfixes.so.0.0.0
%{_libdir}/libxcb-xinerama.so.0
%{_libdir}/libxcb-xinerama.so.0.0.0
%{_libdir}/libxcb-xlib.so.0
%{_libdir}/libxcb-xlib.so.0.0.0
%{_libdir}/libxcb-xprint.so.0
%{_libdir}/libxcb-xprint.so.0.0.0
%{_libdir}/libxcb-xtest.so.0
%{_libdir}/libxcb-xtest.so.0.0.0
%{_libdir}/libxcb-xv.so.0
%{_libdir}/libxcb-xv.so.0.0.0
%{_libdir}/libxcb-xvmc.so.0
%{_libdir}/libxcb-xvmc.so.0.0.0
%{_libdir}/libxcb.so.1
%{_libdir}/libxcb.so.1.0.0

