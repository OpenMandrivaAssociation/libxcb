# Workaround for 32bit gcc bug, but no harm done
# because we add -flto manually for the 64bit build
%global _disable_lto 1

# Workaround for ****ing libtool adding -L/usr/lib64
# while relinking during make install
%if %{cross_compiling}
%define prefer_gcc 1
%endif

%global optflags %{optflags} -O3

# libxcb is used by wine and steam
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

Summary:	X protocol C-language Binding Library
Name:		libxcb
Version:	1.16.1
Release:	1
Group:		System/X11
License:	MIT
Url:		http://xcb.freedesktop.org
Source0:	https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz
# This is stolen straight from the pthread-stubs source:
# http://cgit.freedesktop.org/xcb/pthread-stubs/blob/?id=6900598192bacf5fd9a34619b11328f746a5956d
# we don't need the library because glibc has working pthreads, but we need
# the pkgconfig file so libs that link against libxcb know this...
Source1:	pthread-stubs.pc.in
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(libexslt)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(xau)
BuildRequires:	pkgconfig(xcb-proto)
BuildRequires:	pkgconfig(xdmcp)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xkbcomp)
BuildRequires:	pkgconfig(xkbfile)
%if %{with compat32}
BuildRequires:	devel(libxslt)
BuildRequires:	devel(libexslt)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmcp)
%endif
%rename		libpthread-stubs

%description
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

%define major 1
%define libxcb %mklibname xcb %{major}
%define devname %mklibname xcb -d
%define lib32xcb libxcb%{major}
%define dev32name libxcb-devel

%define compositemajor 0
%define damagemajor 0
%define dbemajor 0
%define dpmsmajor 0
%define dri2major 0
%define dri3major 0
%define glxmajor 0
%define presentmajor 0
%define randrmajor 0
%define recordmajor 0
%define rendermajor 0
%define resmajor 0
%define screensavermajor 0
%define shapemajor 0
%define shmmajor 0
%define syncmajor 1
%define xeviemajor 0
%define xf86drimajor 0
%define xfixesmajor 0
%define xineramamajor 0
%define xinputmajor 0
%define xkbmajor 1
%define xprintmajor 0
%define xtestmajor 0
%define xvmajor 0
%define xvmcmajor 0

%define libxcb_composite   %mklibname xcb-composite   %{compositemajor}
%define libxcb_damage      %mklibname xcb-damage      %{damagemajor}
%define libxcb_dbe         %mklibname xcb-dbe         %{dbemajor}
%define libxcb_dpms        %mklibname xcb-dpms        %{dpmsmajor}
%define libxcb_dri2        %mklibname xcb-dri2_       %{dri2major}
%define libxcb_dri3        %mklibname xcb-dri3_       %{dri3major}
%define libxcb_glx         %mklibname xcb-glx         %{glxmajor}
%define libxcb_present     %mklibname xcb-present     %{presentmajor}
%define libxcb_randr       %mklibname xcb-randr       %{randrmajor}
%define libxcb_record      %mklibname xcb-record      %{recordmajor}
%define libxcb_render      %mklibname xcb-render      %{rendermajor}
%define libxcb_res         %mklibname xcb-res         %{resmajor}
%define libxcb_screensaver %mklibname xcb-screensaver %{screensavermajor}
%define libxcb_shape       %mklibname xcb-shape       %{shapemajor}
%define libxcb_shm         %mklibname xcb-shm         %{shmmajor}
%define libxcb_sync        %mklibname xcb-sync        %{syncmajor}
%define libxcb_xevie       %mklibname xcb-xevie       %{xeviemajor}
%define libxcb_xf86dri     %mklibname xcb-xf86dri     %{xf86drimajor}
%define libxcb_xfixes      %mklibname xcb-xfixes      %{xfixesmajor}
%define libxcb_xinerama    %mklibname xcb-xinerama    %{xineramamajor}
%define libxcb_xinput      %mklibname xcb-xinput      %{xinputmajor}
%define libxcb_xkb         %mklibname xcb-xkb         %{xkbmajor}
%define libxcb_xprint      %mklibname xcb-xprint      %{xprintmajor}
%define libxcb_xtest       %mklibname xcb-xtest       %{xtestmajor}
%define libxcb_xv          %mklibname xcb-xv          %{xvmajor}
%define libxcb_xvmc        %mklibname xcb-xvmc        %{xvmcmajor}
# Need obsoletes
%define libxcb_util0       %mklibname xcb-util        0
%define libxcb_util1       %mklibname xcb-util        1
%define libxcb_randr1      %mklibname xcb-randr       1
# 32-bit
%define lib32xcb_composite   libxcb-composite%{compositemajor}
%define lib32xcb_damage      libxcb-damage%{damagemajor}
%define lib32xcb_dbe         libxcb-dbe%{dbemajor}
%define lib32xcb_dpms        libxcb-dpms%{dpmsmajor}
%define lib32xcb_dri2        libxcb-dri2_%{dri2major}
%define lib32xcb_dri3        libxcb-dri3_%{dri3major}
%define lib32xcb_glx         libxcb-glx%{glxmajor}
%define lib32xcb_present     libxcb-present%{presentmajor}
%define lib32xcb_randr       libxcb-randr%{randrmajor}
%define lib32xcb_record      libxcb-record%{recordmajor}
%define lib32xcb_render      libxcb-render%{rendermajor}
%define lib32xcb_res         libxcb-res%{resmajor}
%define lib32xcb_screensaver libxcb-screensaver%{screensavermajor}
%define lib32xcb_shape       libxcb-shape%{shapemajor}
%define lib32xcb_shm         libxcb-shm%{shmmajor}
%define lib32xcb_sync        libxcb-sync%{syncmajor}
%define lib32xcb_xevie       libxcb-xevie%{xeviemajor}
%define lib32xcb_xf86dri     libxcb-xf86dri%{xf86drimajor}
%define lib32xcb_xfixes      libxcb-xfixes%{xfixesmajor}
%define lib32xcb_xinerama    libxcb-xinerama%{xineramamajor}
%define lib32xcb_xinput      libxcb-xinput%{xinputmajor}
%define lib32xcb_xkb         libxcb-xkb%{xkbmajor}
%define lib32xcb_xprint      libxcb-xprint%{xprintmajor}
%define lib32xcb_xtest       libxcb-xtest%{xtestmajor}
%define lib32xcb_xv          libxcb-xv%{xvmajor}
%define lib32xcb_xvmc        libxcb-xvmc%{xvmcmajor}

%package -n %{libxcb}
Summary:	X protocol C-language Binding Library
Group:		System/X11
Provides:	%{name} = %{version}

%description -n %{libxcb}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

%files -n %{libxcb}
%{_libdir}/libxcb.so.%{major}*

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Provides:	xcb-devel = %{EVRD}
Requires:	%{libxcb} = %{EVRD}
Requires:	%{libxcb_composite} = %{EVRD}
Requires:	%{libxcb_damage} = %{EVRD}
Requires:	%{libxcb_dbe} = %{EVRD}
Requires:	%{libxcb_dpms} = %{EVRD}
Requires:	%{libxcb_dri2} = %{EVRD}
Requires:	%{libxcb_dri3} = %{EVRD}
Requires:	%{libxcb_glx} = %{EVRD}
Requires:	%{libxcb_present} = %{EVRD}
Requires:	%{libxcb_randr} = %{EVRD}
Requires:	%{libxcb_record} = %{EVRD}
Requires:	%{libxcb_render} = %{EVRD}
Requires:	%{libxcb_res} = %{EVRD}
Requires:	%{libxcb_screensaver} = %{EVRD}
Requires:	%{libxcb_shape} = %{EVRD}
Requires:	%{libxcb_shm} = %{EVRD}
Requires:	%{libxcb_sync} = %{EVRD}
Requires:	%{libxcb_xevie} = %{EVRD}
Requires:	%{libxcb_xf86dri} = %{EVRD}
Requires:	%{libxcb_xfixes} = %{EVRD}
Requires:	%{libxcb_xinerama} = %{EVRD}
Requires:	%{libxcb_xprint} = %{EVRD}
Requires:	%{libxcb_xtest} = %{EVRD}
Requires:	%{libxcb_xv} = %{EVRD}
Requires:	%{libxcb_xvmc} = %{EVRD}
Requires:	%{libxcb_xinput} = %{EVRD}
Requires:	%{libxcb_xkb} = %{EVRD}
%rename 	libpthread-stubs-devel

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%{_includedir}/xcb/*.h
%{_libdir}/libxcb*.so
%{_libdir}/pkgconfig/*.pc
%doc %{_mandir}/man3/*.*

%package -n %{libxcb_composite}
Summary:	X protocol C-language Binding Library (composite extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_composite}
This package provides bindings for the composite extension.

%files -n %{libxcb_composite}
%{_libdir}/libxcb-composite.so.%{compositemajor}*

%package -n %{libxcb_damage}
Summary:	X protocol C-language Binding Library (damage extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_damage}
This package provides bindings for the damage extension.

%files -n %{libxcb_damage}
%{_libdir}/libxcb-damage.so.%{damagemajor}*

%package -n %{libxcb_dbe}
Summary:	X protocol C-language Binding Library (dbe extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_dbe}
This package provides bindings for the dbe extension.

%files -n %{libxcb_dbe}
%{_libdir}/libxcb-dbe.so.%{dbemajor}*

%package -n %{libxcb_dpms}
Summary:	X protocol C-language Binding Library (dpms extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_dpms}
This package provides bindings for the dpms extension.

%files -n %{libxcb_dpms}
%{_libdir}/libxcb-dpms.so.%{dpmsmajor}*

%package -n %{libxcb_dri2}
Summary:	X protocol C-language Binding Library (dri2 extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_dri2}
This package provides bindings for the dri2 extension.

%files -n %{libxcb_dri2}
%{_libdir}/libxcb-dri2.so.%{dri2major}*

%package -n %{libxcb_dri3}
Summary:	X protocol C-language Binding Library (dri3 extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_dri3}
This package provides bindings for the dri3 extension.

%files -n %{libxcb_dri3}
%{_libdir}/libxcb-dri3.so.%{dri2major}*

%package -n %{libxcb_glx}
Summary:	X protocol C-language Binding Library (glx extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_glx}
This package provides bindings for the glx extension.

%files -n %{libxcb_glx}
%{_libdir}/libxcb-glx.so.%{glxmajor}*

%package -n %{libxcb_present}
Summary:	X protocol C-language Binding Library (present extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_present}
This package provides bindings for the present extension.

%files -n %{libxcb_present}
%{_libdir}/libxcb-present.so.%{presentmajor}*

%package -n %{libxcb_randr}
Summary:	X protocol C-language Binding Library (randr extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1
# Bug #53733 explains why libxcb-randr0 obsoletes libxcb-randr1 < 1.4
Conflicts:	%{libxcb_randr1} < 1.4

%description -n %{libxcb_randr}
This package provides bindings for the randr extension.

%files -n %{libxcb_randr}
%{_libdir}/libxcb-randr.so.%{randrmajor}*

%package -n %{libxcb_record}
Summary:	X protocol C-language Binding Library (record extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_record}
This package provides bindings for the record extension.

%files -n %{libxcb_record}
%{_libdir}/libxcb-record.so.%{recordmajor}*

%package -n %{libxcb_render}
Summary:	X protocol C-language Binding Library (render extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_render}
This package provides bindings for the render extension.

%files -n %{libxcb_render}
%{_libdir}/libxcb-render.so.%{rendermajor}*

%package -n %{libxcb_res}
Summary:	X protocol C-language Binding Library (res extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_res}
This package provides bindings for the res extension.

%files -n %{libxcb_res}
%{_libdir}/libxcb-res.so.%{resmajor}*

%package -n %{libxcb_screensaver}
Summary:	X protocol C-language Binding Library (screensaver extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_screensaver}
This package provides bindings for the screensaver extension.

%files -n %{libxcb_screensaver}
%{_libdir}/libxcb-screensaver.so.%{screensavermajor}*

%package -n %{libxcb_shape}
Summary:	X protocol C-language Binding Library (shape extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_shape}
This package provides bindings for the shape extension.

%files -n %{libxcb_shape}
%{_libdir}/libxcb-shape.so.%{shapemajor}*

%package -n %{libxcb_shm}
Summary:	X protocol C-language Binding Library (shm extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_shm}
This package provides bindings for the shm extension.

%files -n %{libxcb_shm}
%{_libdir}/libxcb-shm.so.%{shmmajor}*

%package -n %{libxcb_sync}
Summary:	X protocol C-language Binding Library (sync extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_sync}
This package provides bindings for the sync extension.

%files -n %{libxcb_sync}
%{_libdir}/libxcb-sync.so.%{syncmajor}*

%package -n %{libxcb_xevie}
Summary:	X protocol C-language Binding Library (xevie extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_xevie}
This package provides bindings for the xevie extension.

%files -n %{libxcb_xevie}
%{_libdir}/libxcb-xevie.so.%{xeviemajor}*

%package -n %{libxcb_xf86dri}
Summary:	X protocol C-language Binding Library (xf86dri extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_xf86dri}
This package provides bindings for the xf86dri extension.

%files -n %{libxcb_xf86dri}
%{_libdir}/libxcb-xf86dri.so.%{xf86drimajor}*

%package -n %{libxcb_xfixes}
Summary:	X protocol C-language Binding Library (xfixes extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_xfixes}
This package provides bindings for the xfixes extension.

%files -n %{libxcb_xfixes}
%{_libdir}/libxcb-xfixes.so.%{xfixesmajor}*

%package -n %{libxcb_xinerama}
Summary:	X protocol C-language Binding Library (xinerama extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_xinerama}
This package provides bindings for the xinerama extension.

%files -n %{libxcb_xinerama}
%{_libdir}/libxcb-xinerama.so.%{xineramamajor}*

%package -n %{libxcb_xinput}
Summary:	X protocol C-language Binding Library (xinput extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_xinput}
This package provides bindings for the xinput extension.

%files -n %{libxcb_xinput}
%{_libdir}/libxcb-xinput.so.%{xinputmajor}*

%package -n %{libxcb_xkb}
Summary:	X protocol C-language Binding Library (XKB extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_xkb}
This package provides bindings for the XKB extension.

%files -n %{libxcb_xkb}
%{_libdir}/libxcb-xkb.so.%{xkbmajor}*

%package -n %{libxcb_xprint}
Summary:	X protocol C-language Binding Library (xprint extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_xprint}
This package provides bindings for the xprint extension.

%files -n %{libxcb_xprint}
%{_libdir}/libxcb-xprint.so.%{xprintmajor}*

%package -n %{libxcb_xtest}
Summary:	X protocol C-language Binding Library (xtest extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_xtest}
This package provides bindings for the xtest extension.

%files -n %{libxcb_xtest}
%{_libdir}/libxcb-xtest.so.%{xtestmajor}*

%package -n %{libxcb_xv}
Summary:	X protocol C-language Binding Library (xv extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_xv}
This package provides bindings for the xv extension.

%files -n %{libxcb_xv}
%{_libdir}/libxcb-xv.so.%{xvmajor}*

%package -n %{libxcb_xvmc}
Summary:	X protocol C-language Binding Library (xvmc extension)
Group:		System/X11
Conflicts:	%{libxcb} <= 1.3-1

%description -n %{libxcb_xvmc}
This package provides bindings for the xvmc extension.

%files -n %{libxcb_xvmc}
%{_libdir}/libxcb-xvmc.so.%{xvmcmajor}*

%if %{with compat32}
%package -n %{lib32xcb}
Summary:	X protocol C-language Binding Library (32-bit)
Group:		System/X11

%description -n %{lib32xcb}
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

%files -n %{lib32xcb}
%{_prefix}/lib/libxcb.so.%{major}*

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{lib32xcb} = %{EVRD}
Requires:	%{lib32xcb_composite} = %{EVRD}
Requires:	%{lib32xcb_damage} = %{EVRD}
Requires:	%{lib32xcb_dbe} = %{EVRD}
Requires:	%{lib32xcb_dpms} = %{EVRD}
Requires:	%{lib32xcb_dri2} = %{EVRD}
Requires:	%{lib32xcb_dri3} = %{EVRD}
Requires:	%{lib32xcb_glx} = %{EVRD}
Requires:	%{lib32xcb_present} = %{EVRD}
Requires:	%{lib32xcb_randr} = %{EVRD}
Requires:	%{lib32xcb_record} = %{EVRD}
Requires:	%{lib32xcb_render} = %{EVRD}
Requires:	%{lib32xcb_res} = %{EVRD}
Requires:	%{lib32xcb_screensaver} = %{EVRD}
Requires:	%{lib32xcb_shape} = %{EVRD}
Requires:	%{lib32xcb_shm} = %{EVRD}
Requires:	%{lib32xcb_sync} = %{EVRD}
Requires:	%{lib32xcb_xevie} = %{EVRD}
Requires:	%{lib32xcb_xf86dri} = %{EVRD}
Requires:	%{lib32xcb_xfixes} = %{EVRD}
Requires:	%{lib32xcb_xinerama} = %{EVRD}
Requires:	%{lib32xcb_xprint} = %{EVRD}
Requires:	%{lib32xcb_xtest} = %{EVRD}
Requires:	%{lib32xcb_xv} = %{EVRD}
Requires:	%{lib32xcb_xvmc} = %{EVRD}
Requires:	%{lib32xcb_xinput} = %{EVRD}
Requires:	%{lib32xcb_xkb} = %{EVRD}

%description -n %{dev32name}
Development files for %{name}.

%files -n %{dev32name}
%{_prefix}/lib/libxcb*.so
%{_prefix}/lib/pkgconfig/*.pc

%package -n %{lib32xcb_composite}
Summary:	X protocol C-language Binding Library (composite extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_composite}
This package provides bindings for the composite extension.

%files -n %{lib32xcb_composite}
%{_prefix}/lib/libxcb-composite.so.%{compositemajor}*

%package -n %{lib32xcb_damage}
Summary:	X protocol C-language Binding Library (damage extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_damage}
This package provides bindings for the damage extension.

%files -n %{lib32xcb_damage}
%{_prefix}/lib/libxcb-damage.so.%{damagemajor}*

%package -n %{lib32xcb_dbe}
Summary:	X protocol C-language Binding Library (dbe extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_dbe}
This package provides bindings for the dbe extension.

%files -n %{lib32xcb_dbe}
%{_prefix}/lib/libxcb-dbe.so.%{dbemajor}*

%package -n %{lib32xcb_dpms}
Summary:	X protocol C-language Binding Library (dpms extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_dpms}
This package provides bindings for the dpms extension.

%files -n %{lib32xcb_dpms}
%{_prefix}/lib/libxcb-dpms.so.%{dpmsmajor}*

%package -n %{lib32xcb_dri2}
Summary:	X protocol C-language Binding Library (dri2 extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_dri2}
This package provides bindings for the dri2 extension.

%files -n %{lib32xcb_dri2}
%{_prefix}/lib/libxcb-dri2.so.%{dri2major}*

%package -n %{lib32xcb_dri3}
Summary:	X protocol C-language Binding Library (dri3 extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_dri3}
This package provides bindings for the dri3 extension.

%files -n %{lib32xcb_dri3}
%{_prefix}/lib/libxcb-dri3.so.%{dri2major}*

%package -n %{lib32xcb_glx}
Summary:	X protocol C-language Binding Library (glx extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_glx}
This package provides bindings for the glx extension.

%files -n %{lib32xcb_glx}
%{_prefix}/lib/libxcb-glx.so.%{glxmajor}*

%package -n %{lib32xcb_present}
Summary:	X protocol C-language Binding Library (present extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_present}
This package provides bindings for the present extension.

%files -n %{lib32xcb_present}
%{_prefix}/lib/libxcb-present.so.%{presentmajor}*

%package -n %{lib32xcb_randr}
Summary:	X protocol C-language Binding Library (randr extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_randr}
This package provides bindings for the randr extension.

%files -n %{lib32xcb_randr}
%{_prefix}/lib/libxcb-randr.so.%{randrmajor}*

%package -n %{lib32xcb_record}
Summary:	X protocol C-language Binding Library (record extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_record}
This package provides bindings for the record extension.

%files -n %{lib32xcb_record}
%{_prefix}/lib/libxcb-record.so.%{recordmajor}*

%package -n %{lib32xcb_render}
Summary:	X protocol C-language Binding Library (render extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_render}
This package provides bindings for the render extension.

%files -n %{lib32xcb_render}
%{_prefix}/lib/libxcb-render.so.%{rendermajor}*

%package -n %{lib32xcb_res}
Summary:	X protocol C-language Binding Library (res extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_res}
This package provides bindings for the res extension.

%files -n %{lib32xcb_res}
%{_prefix}/lib/libxcb-res.so.%{resmajor}*

%package -n %{lib32xcb_screensaver}
Summary:	X protocol C-language Binding Library (screensaver extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_screensaver}
This package provides bindings for the screensaver extension.

%files -n %{lib32xcb_screensaver}
%{_prefix}/lib/libxcb-screensaver.so.%{screensavermajor}*

%package -n %{lib32xcb_shape}
Summary:	X protocol C-language Binding Library (shape extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_shape}
This package provides bindings for the shape extension.

%files -n %{lib32xcb_shape}
%{_prefix}/lib/libxcb-shape.so.%{shapemajor}*

%package -n %{lib32xcb_shm}
Summary:	X protocol C-language Binding Library (shm extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_shm}
This package provides bindings for the shm extension.

%files -n %{lib32xcb_shm}
%{_prefix}/lib/libxcb-shm.so.%{shmmajor}*

%package -n %{lib32xcb_sync}
Summary:	X protocol C-language Binding Library (sync extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_sync}
This package provides bindings for the sync extension.

%files -n %{lib32xcb_sync}
%{_prefix}/lib/libxcb-sync.so.%{syncmajor}*

%package -n %{lib32xcb_xevie}
Summary:	X protocol C-language Binding Library (xevie extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_xevie}
This package provides bindings for the xevie extension.

%files -n %{lib32xcb_xevie}
%{_prefix}/lib/libxcb-xevie.so.%{xeviemajor}*

%package -n %{lib32xcb_xf86dri}
Summary:	X protocol C-language Binding Library (xf86dri extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_xf86dri}
This package provides bindings for the xf86dri extension.

%files -n %{lib32xcb_xf86dri}
%{_prefix}/lib/libxcb-xf86dri.so.%{xf86drimajor}*

%package -n %{lib32xcb_xfixes}
Summary:	X protocol C-language Binding Library (xfixes extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_xfixes}
This package provides bindings for the xfixes extension.

%files -n %{lib32xcb_xfixes}
%{_prefix}/lib/libxcb-xfixes.so.%{xfixesmajor}*

%package -n %{lib32xcb_xinerama}
Summary:	X protocol C-language Binding Library (xinerama extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_xinerama}
This package provides bindings for the xinerama extension.

%files -n %{lib32xcb_xinerama}
%{_prefix}/lib/libxcb-xinerama.so.%{xineramamajor}*

%package -n %{lib32xcb_xinput}
Summary:	X protocol C-language Binding Library (xinput extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_xinput}
This package provides bindings for the xinput extension.

%files -n %{lib32xcb_xinput}
%{_prefix}/lib/libxcb-xinput.so.%{xinputmajor}*

%package -n %{lib32xcb_xkb}
Summary:	X protocol C-language Binding Library (XKB extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_xkb}
This package provides bindings for the XKB extension.

%files -n %{lib32xcb_xkb}
%{_prefix}/lib/libxcb-xkb.so.%{xkbmajor}*

%package -n %{lib32xcb_xprint}
Summary:	X protocol C-language Binding Library (xprint extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_xprint}
This package provides bindings for the xprint extension.

%files -n %{lib32xcb_xprint}
%{_prefix}/lib/libxcb-xprint.so.%{xprintmajor}*

%package -n %{lib32xcb_xtest}
Summary:	X protocol C-language Binding Library (xtest extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_xtest}
This package provides bindings for the xtest extension.

%files -n %{lib32xcb_xtest}
%{_prefix}/lib/libxcb-xtest.so.%{xtestmajor}*

%package -n %{lib32xcb_xv}
Summary:	X protocol C-language Binding Library (xv extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_xv}
This package provides bindings for the xv extension.

%files -n %{lib32xcb_xv}
%{_prefix}/lib/libxcb-xv.so.%{xvmajor}*

%package -n %{lib32xcb_xvmc}
Summary:	X protocol C-language Binding Library (xvmc extension) (32-bit)
Group:		System/X11

%description -n %{lib32xcb_xvmc}
This package provides bindings for the xvmc extension.

%files -n %{lib32xcb_xvmc}
%{_prefix}/lib/libxcb-xvmc.so.%{xvmcmajor}*
%endif

%prep
%autosetup -p1

sed -i 's/pthread-stubs //' configure.ac
# autoreconf -f needed to expunge rpaths
autoreconf -v -f --install

export CONFIGURE_TOP="$(pwd)"

%if %{with compat32}
mkdir build32
cd build32
%configure32 \
	--enable-xinput \
	--enable-dri3 \
	--enable-xevie \
	--enable-xprint \
	--with-queue-size=32768

# Remove rpath from libtool (extra insurance if autoreconf is ever dropped)
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

cd ..
%endif

mkdir build
cd build
CFLAGS="%{optflags} -flto" \
LDFLAGS="%{build_ldflags} -flto" \
%configure \
	--enable-xinput \
	--enable-dri3 \
	--enable-xevie \
	--enable-xprint \
	--with-queue-size=32768

# Remove rpath from libtool (extra insurance if autoreconf is ever dropped)
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

cd ..

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
sed 's,@libdir@,%{_prefix}/lib,;s,@prefix@,%{_prefix},;s,@exec_prefix@,%{_exec_prefix},' %{SOURCE1} > %{buildroot}%{_prefix}/lib/pkgconfig/pthread-stubs.pc
%endif
%make_install -C build
sed 's,@libdir@,%{_libdir},;s,@prefix@,%{_prefix},;s,@exec_prefix@,%{_exec_prefix},' %{SOURCE1} > %{buildroot}%{_libdir}/pkgconfig/pthread-stubs.pc

# (tpg) get rid of it, as it takes lot of place
rm -rf %{buildroot}%{_docdir}/libxcb
