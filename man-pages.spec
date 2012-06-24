Summary:	System manual pages from the Linux Documentation Project
Summary(de):	System-man-Seiten vom Linux Documentation Project
Summary(fr):	Pages man syst�me du Projet de Documentation Linux
Summary(pl):	Podr�czniki systemowe z Linux Documentation Project
Summary(tr):	Linux Belgeleme Projesinin sistem k�lavuz sayfalar�
Name:		man-pages
Version:	1.33
Release:	1
License:	Distributable
Group:		Documentation
Group(de):	Dokumentation
Group(pl):	Dokumentacja
Source0:	ftp://ftp.us.kernel.org/pub/linux/docs/manpages/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Autoreqprov:	false
Obsoletes:	man-pages-pl

%description
A large collection of man pages covering programming APIs, file
formats, protocols, etc.

- section 1 = user commands (intro only)
- section 2 = system calls
- section 3 = libc calls
- section 4 = devices (e.g., hd, sd)
- section 5 = file formats and protocols (e.g., wtmp, /etc/passwd,
  nfs)
- section 6 = games (intro only)
- section 7 = conventions, macro packages, etc. (e.g., nroff, ascii)
- section 8 = system administration (intro only)

%description -l de
Eine gro�e Sammlung von man-Seiten �ber Programmier-APIs,
Dateiformate, Protokolle, usw..

- section 1 = Benutzerbefehle (nur intro)
- section 2 = Systemaufrufe
- section 3 = libc-Aufrufe
- section 4 = Ger�te (z.B. hd, sd)
- section 5 = Dateiformate und Protokolle (z.B. wtmp, /etc/passwd,
  nfs)
- section 6 = Spiele (nur intro)
- section 7 = Konventionen, Makro-Pakete, usw. (z.B. nroff, ascii)
- section 8 = Systemverwaltung (nur intro)

%description -l fr
Un large ensemble de pages de man couvrant la programmation des APIs,
les formats de fichiers, les protocoles, etc.

- section 1 = commandes utilisateur (intro seulement)
- section 2 = appels syst�me
- section 3 = appels libc
- section 4 = p�riph�riques (e.g., hd, sd)
- section 5 = formats de fichiers et protocoles (e.g., wtmp,
  /etc/passwd, nfs)
- section 6 = jeux (intro seulement)
- section 7 = conventions, paquetages, etc. (e.g., nroff, ascii)
- section 8 = administration syst�me (intro seulement)

%description -l pl
Pakiet ten zawiera du�� kolekcj� podr�cznik�w ekranowych (man pages),
opisuj�cych format plik�w, protoko�y itp.

- sekcja 1 = komendy u�ytkownik�w (tylko wst�p)
- sekcja 2 = wywo�ania systemowe
- sekcja 3 = wywo�ania bibliotek
- sekcja 4 = urz�dzenia (np., hd, sd)
- sekcja 5 = format plik�w i protoko�y (np., wtmp, /etc/passwd, nfs)
- sekcja 6 = gry (tylko wst�p)
- sekcja 7 = konwencje, makro-pakiety, etc. (np., nroff, ascii)
- sekcja 8 = administracja systemu (tylko wst�p)

%description -l tr
Programlama aray�zlerini, dosya formatlar�n�, protokolleri vs.
kapsayan, geni� bir k�lavuz sayfalar� derlemesi.

%prep
%setup -q

%build
rm -f man1/{chgrp,chmod,chown,cp,dd,df,dircolors,du,install,diff}.1
rm -f man1/{ln,ls,mkdir,mkfifo,mknod,mv,rm,rmdir,touch,dir,vdir}.1
rm -f man1/COPYING
rm -f man2/{modules,quotactl,get_kernel_syms,capget,capset}.2 
rm -f man2/{create,delete,init,query}_module.2
rm -f man3/{resolver,getnetent,strcasecmp}.3
rm -f man4/console.4
rm -f man5/{exports,lilo.conf,nfs,fstab,passwd}.5
rm -f man8/lilo.8

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,2,3,4,5,6,7,8}

for n in man{1,2,3,4,5,6,7,8}/*; do
	install $n $RPM_BUILD_ROOT%{_mandir}/$n
done

rm -f $RPM_BUILD_ROOT%{_mandir}/man*/README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_mandir}/man*/*
