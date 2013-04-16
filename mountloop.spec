Summary: Allow users to mount files via loopback
Name: mountloop
Version: 0.15.4
Release: 6
URL: http://www.mandriva.com/
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: System/Base
Requires: ssh-askpass, drakxtools, perl-MDK-Common, mount >= 2.11r-2mdk
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libx11-devel

%description
Allow users to mount encrypted loopback filesystems.

%prep
%setup -q

%build
%make CFLAGS="%optflags %ldflags"

%install
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=DrakLoop
Comment=Create encrypted folder
Exec=drakloop
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-System-FileTools;System;
EOF

mkdir -p %{buildroot}%_iconsdir %{buildroot}%_miconsdir %{buildroot}%_liconsdir
install -m 644 mountloop-20.png %{buildroot}%_iconsdir/%name.png
install -m 644 mountloop-32.png %{buildroot}%_miconsdir/%name.png
install -m 644 mountloop-48.png %{buildroot}%_liconsdir/%name.png

%{find_lang} drakloop

%clean

%files -f drakloop.lang
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


%changelog
* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 0.15.4-5mdv2011.0
+ Revision: 636097
- tighten BR

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.15.4-4mdv2011.0
+ Revision: 620394
- the mass rebuild of 2010.0 packages

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.15.4-3mdv2010.0
+ Revision: 436175
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.15.4-2mdv2008.1
+ Revision: 153211
- rebuild
- drop old menu
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Oct 03 2007 Thierry Vignaud <tv@mandriva.org> 0.15.4-1mdv2008.0
+ Revision: 95096
- updated translation
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Fri Mar 09 2007 Olivier Blin <oblin@mandriva.com> 0.15.3-2mdv2007.1
+ Revision: 138745
- add xdg menu
- update url
- Import mountloop

* Mon Nov 07 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.15.3-1mdk
- use the right bugzilla URL (#19561)
- don't use anymore the https protocol

* Mon Jun 06 2005 Frederic Lepied <flepied@mandriva.com> 0.15.2-1mdk
- translation updates

* Sun Mar 13 2005 Frederic Lepied <flepied@mandrakesoft.com> 0.15.1-1mdk
- translation updates

* Mon Feb 28 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.15-1mdk
- reuse MDK::Common
- fix wrong values filled in config file (#14023)

* Mon Feb 21 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.14-1mdk
- translation updates
- fix large file support (fredl, #12015)

* Fri Feb 04 2005 Frederic Lepied <flepied@mandrakesoft.com> 0.13-1mdk
- drakloop: o removed file column.
            o added support for on boot feature. Force to mount
	    relatively from $HOME.
- mountloop.sh: mount from $HOME.  wait even if nothing has been
  mounted to be able to unmount automatically directories mounted
  interactivelly later by drakloop.
- po updates

* Mon Oct 04 2004 Robert Vojta <robert.vojta@mandrake.org> 0.12.5-4mdk
- et, fi, fr, he, hu, sv, uk, zh_CN, da .po updates

* Sat Oct 02 2004 Robert Vojta <robert.vojta@mandrake.org> 0.12.5-3mdk
- po updates

* Fri Oct 01 2004 Robert Vojta <robert.vojta@mandrake.org> 0.12.5-2mdk
- untranslated string marked for translation
- po updates

* Tue Sep 28 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.12.5-1mdk
- po updates

* Thu Sep 09 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.12.4-1mdk
- drakloop:
  o log explanations
  o fix encoding issues with messages from the 'drakloop' domain (#11268)

* Wed Sep 01 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.12.3-1mdk
- po updates

* Thu Jul 29 2004 Robert Vojta <robert.vojta@mandrake.org> 0.12.2-1mdk
- buttons ordering fix
- new possibility to remove encrypted folder (unmounted only)

* Thu Jul 29 2004 Robert Vojta <robert.vojta@mandrake.org> 0.12.1-2mdk
- do not use output() for pipes, it doesn't work (due to ">$f")

* Thu Jul 29 2004 Robert Vojta <robert.vojta@mandrake.org> 0.12.1-1mdk
- about dialog added
- perl_checker warnings removed (Titi)
- more use of MDK::Common things like cat_, output (Titi)
- remove created directory if any of the later steps fails (during new
  encrypted folder creation)

* Thu Jul 29 2004 Robert Vojta <robert.vojta@mandrake.org> 0.12.0-1mdk
- new user interface
- possibility to add new directory, mount and unmount directories

* Fri Jul 16 2004 Robert Vojta <robert.vojta@mandrake.org> 0.11.6-1mdk
- localization added (few translations)
- default minimum password length is 3 characters
- higher security level means longer password requirement (maximum 8 chars)

* Thu Mar 25 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.11.5-1mdk
- use new path for ssh-askpass
- modprobe aes and cryptoloop

