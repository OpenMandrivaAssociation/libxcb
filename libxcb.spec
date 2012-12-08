Name: libxcb
Summary: X protocol C-language Binding Library
Version: 1.9
Release:  1
Group: System/X11
License: MIT
URL: http://xcb.freedesktop.org
Source0: http://xcb.freedesktop.org/dist/libxcb-%{version}.tar.bz2

# because of xcb-proto-1.5 (at least)
BuildRequires: x11-proto-devel >= 7.4-17mdv
BuildRequires: libxau-devel
BuildRequires: pkgconfig(xorg-macros) >= 1.0.1
BuildRequires: libpthread-stubs
BuildRequires: pkgconfig(libexslt)
BuildRequires: libxdmcp-devel
BuildRequires: doxygen
BuildRequires: python-celementtree
BuildRequires: graphviz
BuildRequires: pkgconfig(libxslt)
BuildRequires: xsltproc

%description
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

%define major 1
%define libxcb %mklibname xcb %major
%define libdev %mklibname xcb -d

%define compositemajor 0
%define damagemajor 0
%define dpmsmajor 0
%define dri2major 0
%define glxmajor 0
%define randrmajor 0
%define recordmajor 0
%define rendermajor 0
%define resmajor 0
%define screensavermajor 0
%define shapemajor 0
%define shmmajor 0
%define syncmajor 0
%define xeviemajor 0
%define xf86drimajor 0
%define xfixesmajor 0
%define xineramamajor 0
%define xprintmajor 0
%define xtestmajor 0
%define xvmajor 0
%define xvmcmajor 0

%define libxcb_composite   %mklibname xcb-composite   %compositemajor
%define libxcb_damage      %mklibname xcb-damage      %damagemajor
%define libxcb_dpms        %mklibname xcb-dpms        %dpmsmajor
%define libxcb_dri2        %mklibname xcb-dri2_       %dri2major
%define libxcb_glx         %mklibname xcb-glx         %glxmajor
%define libxcb_randr       %mklibname xcb-randr       %randrmajor
%define libxcb_record      %mklibname xcb-record      %recordmajor
%define libxcb_render      %mklibname xcb-render      %rendermajor
%define libxcb_res         %mklibname xcb-res         %resmajor
%define libxcb_screensaver %mklibname xcb-screensaver %screensavermajor
%define libxcb_shape       %mklibname xcb-shape       %shapemajor
%define libxcb_shm         %mklibname xcb-shm         %shmmajor
%define libxcb_sync        %mklibname xcb-sync        %syncmajor
%define libxcb_xevie       %mklibname xcb-xevie       %xeviemajor
%define libxcb_xf86dri     %mklibname xcb-xf86dri     %xf86drimajor
%define libxcb_xfixes      %mklibname xcb-xfixes      %xfixesmajor
%define libxcb_xinerama    %mklibname xcb-xinerama    %xineramamajor
%define libxcb_xprint      %mklibname xcb-xprint      %xprintmajor
%define libxcb_xtest       %mklibname xcb-xtest       %xtestmajor
%define libxcb_xv          %mklibname xcb-xv          %xvmajor
%define libxcb_xvmc        %mklibname xcb-xvmc        %xvmcmajor
# Need obsoletes
%define libxcb_util0       %mklibname xcb-util        0
%define libxcb_util1       %mklibname xcb-util        1
%define libxcb_randr1      %mklibname xcb-randr       1

#-----------------------------------------------------------

%package -n %{libxcb}
Summary: X protocol C-language Binding Library
Group: System/X11
Provides: %{name} = %{version}
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9
# Bug #53733: libxcb_randr1 was wrongly obsoleting old %{libxcb}s
Conflicts: %{libxcb_randr1} < 1.4
Obsoletes: %{libxcb_randr1} < 1.4

%description -n %{libxcb}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

%files -n %{libxcb}
%{_libdir}/libxcb.so.%{major}*

#-----------------------------------------------------------

%package -n %{libdev}
Summary: Development files for %{name}
Group: Development/X11
Provides: xcb-devel = %{version}-%{release}
Obsoletes: %{_lib}xcb1-devel < %{EVRD}
Obsoletes: %{_lib}xcb-static-devel < %{EVRD}

Requires: %{libxcb} = %{version}
Requires: %{libxcb_composite} = %{version}
Requires: %{libxcb_damage} = %{version}
Requires: %{libxcb_dpms} = %{version}
Requires: %{libxcb_dri2} = %{version}
Requires: %{libxcb_glx} = %{version}
Requires: %{libxcb_randr} = %{version}
Requires: %{libxcb_record} = %{version}
Requires: %{libxcb_render} = %{version}
Requires: %{libxcb_res} = %{version}
Requires: %{libxcb_screensaver} = %{version}
Requires: %{libxcb_shape} = %{version}
Requires: %{libxcb_shm} = %{version}
Requires: %{libxcb_sync} = %{version}
Requires: %{libxcb_xevie} = %{version}
Requires: %{libxcb_xf86dri} = %{version}
Requires: %{libxcb_xfixes} = %{version}
Requires: %{libxcb_xinerama} = %{version}
Requires: %{libxcb_xprint} = %{version}
Requires: %{libxcb_xtest} = %{version}
Requires: %{libxcb_xv} = %{version}
Requires: %{libxcb_xvmc} = %{version}
# gw this isn't picked up by the automatic pkgconfig deps, but without it,
# pkg-config --libs xcb will fail
Requires: libpthread-stubs

%description -n %{libdev}
Development files for %{name}

%files -n %{libdev}
%{_includedir}/xcb/*.h
%{_libdir}/libxcb*.so
%{_libdir}/pkgconfig/xcb*.pc

#-----------------------------------------------------------

%package doc
Summary: Documentation for %{name}
Group: Development/X11

%description doc
Documentation for %{name}

%files doc
%{_docdir}/libxcb
%{_mandir}/man3/*.xz

#-----------------------------------------------------------

%package -n %{libxcb_composite}
Summary: X protocol C-language Binding Library (composite extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_composite}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the composite extension.

%files -n %{libxcb_composite}
%{_libdir}/libxcb-composite.so.%{compositemajor}*

#-----------------------------------------------------------

%package -n %{libxcb_damage}
Summary: X protocol C-language Binding Library (damage extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_damage}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the damage extension.

%files -n %{libxcb_damage}
%{_libdir}/libxcb-damage.so.%{damagemajor}*

#-----------------------------------------------------------

%package -n %{libxcb_dpms}
Summary: X protocol C-language Binding Library (dpms extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_dpms}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the dpms extension.

%files -n %{libxcb_dpms}
%{_libdir}/libxcb-dpms.so.%{dpmsmajor}*

#-----------------------------------------------------------

%package -n %{libxcb_dri2}
Summary: X protocol C-language Binding Library (dri2 extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_dri2}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the dri2 extension.

%files -n %{libxcb_dri2}
%{_libdir}/libxcb-dri2.so.%{dri2major}*

#-----------------------------------------------------------

%package -n %{libxcb_glx}
Summary: X protocol C-language Binding Library (glx extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_glx}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the glx extension.

%files -n %{libxcb_glx}
%{_libdir}/libxcb-glx.so.%{glxmajor}*

#-----------------------------------------------------------

%package -n %{libxcb_randr}
Summary: X protocol C-language Binding Library (randr extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
# Bug #53733 explains why libxcb-randr0 obsoletes libxcb-randr1 < 1.4
Conflicts: %{libxcb_randr1} < 1.4
Obsoletes: %{libxcb_randr1} < 1.4
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_randr}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the randr extension.

%files -n %{libxcb_randr}
%{_libdir}/libxcb-randr.so.%{randrmajor}*

#-----------------------------------------------------------

%package -n %{libxcb_record}
Summary: X protocol C-language Binding Library (record extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_record}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the record extension.

%files -n %{libxcb_record}
%{_libdir}/libxcb-record.so.%{recordmajor}*

#-----------------------------------------------------------

%package -n %{libxcb_render}
Summary: X protocol C-language Binding Library (render extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_render}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the render extension.

%files -n %{libxcb_render}
%{_libdir}/libxcb-render.so.%{rendermajor}*

#-----------------------------------------------------------

%package -n %{libxcb_res}
Summary: X protocol C-language Binding Library (res extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_res}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the res extension.

%files -n %{libxcb_res}
%{_libdir}/libxcb-res.so.%{resmajor}*

#-----------------------------------------------------------

%package -n %{libxcb_screensaver}
Summary: X protocol C-language Binding Library (screensaver extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_screensaver}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the screensaver extension.

%files -n %{libxcb_screensaver}
%{_libdir}/libxcb-screensaver.so.%{screensavermajor}*

#-----------------------------------------------------------

%package -n %{libxcb_shape}
Summary: X protocol C-language Binding Library (shape extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_shape}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the shape extension.

%files -n %{libxcb_shape}
%{_libdir}/libxcb-shape.so.%{shapemajor}*

#-----------------------------------------------------------

%package -n %{libxcb_shm}
Summary: X protocol C-language Binding Library (shm extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_shm}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the shm extension.

%files -n %{libxcb_shm}
%{_libdir}/libxcb-shm.so.%{shmmajor}*

#-----------------------------------------------------------

%package -n %{libxcb_sync}
Summary: X protocol C-language Binding Library (sync extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_sync}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the sync extension.

%files -n %{libxcb_sync}
%{_libdir}/libxcb-sync.so.%{syncmajor}*

#-----------------------------------------------------------

%package -n %{libxcb_xevie}
Summary: X protocol C-language Binding Library (xevie extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_xevie}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the xevie extension.

%files -n %{libxcb_xevie}
%{_libdir}/libxcb-xevie.so.%{xeviemajor}*

#-----------------------------------------------------------

%package -n %{libxcb_xf86dri}
Summary: X protocol C-language Binding Library (xf86dri extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_xf86dri}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the xf86dri extension.

%files -n %{libxcb_xf86dri}
%{_libdir}/libxcb-xf86dri.so.%{xf86drimajor}*

#-----------------------------------------------------------

%package -n %{libxcb_xfixes}
Summary: X protocol C-language Binding Library (xfixes extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_xfixes}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the xfixes extension.

%files -n %{libxcb_xfixes}
%{_libdir}/libxcb-xfixes.so.%{xfixesmajor}*

#-----------------------------------------------------------

%package -n %{libxcb_xinerama}
Summary: X protocol C-language Binding Library (xinerama extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_xinerama}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the xinerama extension.

%files -n %{libxcb_xinerama}
%{_libdir}/libxcb-xinerama.so.%{xineramamajor}*

#-----------------------------------------------------------

%package -n %{libxcb_xprint}
Summary: X protocol C-language Binding Library (xprint extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_xprint}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the xprint extension.

%files -n %{libxcb_xprint}
%{_libdir}/libxcb-xprint.so.%{xprintmajor}*

#-----------------------------------------------------------

%package -n %{libxcb_xtest}
Summary: X protocol C-language Binding Library (xtest extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_xtest}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the xtest extension.

%files -n %{libxcb_xtest}
%{_libdir}/libxcb-xtest.so.%{xtestmajor}*

#-----------------------------------------------------------

%package -n %{libxcb_xv}
Summary: X protocol C-language Binding Library (xv extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_xv}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the xv extension.

%files -n %{libxcb_xv}
%{_libdir}/libxcb-xv.so.%{xvmajor}*

#-----------------------------------------------------------

%package -n %{libxcb_xvmc}
Summary: X protocol C-language Binding Library (xvmc extension)
Group: System/X11
Conflicts: %{libxcb} <= 1.3-1
Obsoletes: %{libxcb_util0} < 0.3.9
Obsoletes: %{libxcb_util1} < 0.3.9

%description -n %{libxcb_xvmc}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

This package provides bindings for the xvmc extension.

%files -n %{libxcb_xvmc}
%{_libdir}/libxcb-xvmc.so.%{xvmcmajor}*

#-----------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std
