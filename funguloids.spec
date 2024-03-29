# TODO:
# - docs need to be included in package
# - patches propably need love too
#
Summary:	Those Funny Funguloids - a nice little piece of entertainment
Summary(pl.UTF-8):	Those Funny Funguliods - przyjemny, mały przedmiot rozrywki
Name:		funguloids
Version:	1.06
Release:	0.1
License:	zlib/libpng
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/funguloids/%{name}-linux-%{version}.tar.bz2
# Source0-md5:	45ef7a0da156d7b65627a674fcfb12f0
Source1:	%{name}.desktop
Patch0:		%{name}-lua51.patch
Patch1:		%{name}-path.patch
URL:		http://funguloids.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freealut-devel
BuildRequires:	libmad-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	lua51-devel
BuildRequires:	ogre-devel
BuildRequires:	ois-devel >= 1.0-0.RC1
# EA becouse it requires ogre with cg plugin which has EA
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Those Funny Funguloids!" is a nice little piece of entertainment. You
collect mushrooms, bring them back to your home base and profit!
That's the basic idea in a nutshell. It has smooth, appealing 3D
graphics and nice atmospheric sound effects.

Go ahead and try it out - it has sounds too!

%description -l pl.UTF-8
"Those Funny Funguloids!" (te zabawne Funguloidy) to przyjemny, mały
przedmiot rozrywki. Gracz zbiera grzyby i przynosi je do domu. Taka
jest podstawowa idea gry w pigułce. Ma płynną, przyciągającą grafikę
3D i miłe, atmosferyczne efekty dźwiękowe.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-lua=%{_includedir}/lua51

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}
mv -f $RPM_BUILD_ROOT%{_prefix}/games/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/games/%{name}
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop
