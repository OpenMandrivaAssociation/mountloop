Summary: Allow users to mount files via loopback
Name: mountloop
Version: 0.15.4
Release: %mkrel 2
URL: http://www.mandriva.com/
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: System/Base
Requires: ssh-askpass, drakxtools, perl-MDK-Common, mount >= 2.11r-2mdk
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: X11-devel
Prefix: %{_prefix}

%description
Allow users to mount encrypted loopback filesystems.

%prep
%setup -q

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=DrakLoop
Comment=Create encrypted folder
Exec=drakloop
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-System-FileTools;System;
EOF

mkdir -p $RPM_BUILD_ROOT%_iconsdir $RPM_BUILD_ROOT%_miconsdir $RPM_BUILD_ROOT%_liconsdir
install -m 644 mountloop-20.png $RPM_BUILD_ROOT%_iconsdir/%name.png
install -m 644 mountloop-32.png $RPM_BUILD_ROOT%_miconsdir/%name.png
install -m 644 mountloop-48.png $RPM_BUILD_ROOT%_liconsdir/%name.png

%{find_lang} drakloop

%clean
rm -rf $RPM_BUILD_ROOT

%files -f drakloop.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%attr(4755,root,root) %{_bindir}/encsetup
%attr(4755,root,root) %{_bindir}/mountloop
%attr(4755,root,root) %{_bindir}/umountloop
%{_bindir}/drakloop
/etc/X11/xinit.d/*
/usr/X11R6/bin/*
%{_datadir}/applications/mandriva-%{name}.desktop
%_iconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/%name.png

%post

%if %mdkversion < 200900
%update_menus
%endif

%postun

%if %mdkversion < 200900
%clean_menus
%endif


