Summary:	Soundconverter for GNOME
Summary(pl.UTF-8):	Program do konwersji plików muzycznych dla GNOME'a
Name:		soundconverter
Version:	1.5.3
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://download.berlios.de/soundconverter/%{name}-%{version}.tar.gz
# Source0-md5:	e090893dcab72671d2e509d389b664d9
URL:		http://soundconverter.berlios.de/
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	python >= 1:2.4
BuildRequires:	python-gnome >= 2.12
BuildRequires:	python-pygtk-glade >= 2.12
BuildRequires:	python-pygtk-gtk >= 2.12
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires(post,postun):	hicolor-icon-theme
Requires:	python-gnome
Requires:	python-gnome-ui
Requires:	python-gstreamer
Requires:	python-pygtk-glade
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple sound converter application for the GNOME environment. It
reads anything the GStreamer library can read, and writes WAV, FLAC,
MP3, and Ogg Vorbis files.

%description -l pl.UTF-8
Prosty program do konwersji plików muzycznych dla GNOME'a. Czyta pliki
obsługiwane przez GStreamera i zapisuje w formatach: WAV, FLAC, MP3 i
Ogg Vorbis.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/*/*
