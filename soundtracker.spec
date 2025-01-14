%define name soundtracker
%define version 0.6.8
%define release %mkrel 9

Summary: 	Sound modules editor/player
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Group: 		Sound
License: 	GPL
Url: 		https://www.soundtracker.org/
Source: 	http://soundtracker.org/dl/v0.6/%name-%version.tar.bz2
Patch0: 	soundtracker-0.6.8-remove-chown.patch.bz2
Patch1:		soundtracker-0.6.8-xdg.patch.bz2
Patch2:		soundtracker-0.6.8-autopoo_fixes.diff
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	SDL-devel
BuildRequires:	libgnome-devel
BuildRequires:  gdk-pixbuf-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libalsa-devel
BuildRequires:  libjack-devel
BuildRequires:  automake
BuildRequires:  gettext-devel

%description
Soundtracker is a module tracker for the X Window System similar to the DOS
program `FastTracker'. Soundtracker is based on the XM file format. The user
interface makes use of GTK+, and, optionally, GNOME.

%prep
%setup -q
%patch0 -p1 -b .chown
%patch1 -p1 -b .xdg
%patch2 -p0

%build
autoreconf -fi
#aclocal -I m4
#automake
#autoheader
#autoconf
%configure2_5x \
%ifarch %ix86
--enable-asm
%endif

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std MKINSTALLDIRS=`pwd`/mkinstalldirs
%find_lang %{name}
mv %buildroot%_datadir/gnome/apps/Multimedia %buildroot%_datadir/applications


%if %mdkversion < 200900
%post
%{update_menus}
%endif
 
%if %mdkversion < 200900
%postun
%{clean_menus}
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc ABOUT-NLS FAQ NEWS TODO README ChangeLog
%_bindir/soundtracker
%_datadir/applications/soundtracker.desktop
%_datadir/%name

