Summary:	System manual pages from the Linux Documentation Project
Summary(de):	System-man-Seiten vom Linux Documentation Project
Summary(fr):	Pages man système du Projet de Documentation Linux
Summary(pl):	Podrêczniki systemowe z Linux Documentation Project
Summary(tr):	Linux Belgeleme Projesinin sistem kýlavuz sayfalarý
Name:		man-pages
Version:	1.29
Release:	1
Copyright:	distributable
Group:		Documentation
Group(pl):	Dokumentacja
Source:		ftp://ftp.us.kernel.org/pub/linux/docs/manpages/%{name}-%{version}.tar.bz2
BuildArch:	noarch
Buildroot:	/tmp/%{name}-%{version}-root
Autoreqprov:	false

%description
A large collection of man pages covering programming APIs, file
formats, protocols, etc.

    Section 1 = user commands (intro only)
    Section 2 = system calls
    Section 3 = libc calls
    Section 4 = devices (e.g., hd, sd)
    Section 5 = file formats and protocols (e.g., wtmp, /etc/passwd, nfs)
    Section 6 = games (intro only)
    Section 7 = conventions, macro packages, etc. (e.g., nroff, ascii)
    Section 8 = system administration (intro only)

%description -l de
Eine große Sammlung von man-Seiten über Programmier-APIs,
Dateiformate, Protokolle, usw..

    Section 1 = Benutzerbefehle (nur intro)
    Section 2 = Systemaufrufe
    Section 3 = libc-Aufrufe
    Section 4 = Geräte (z.B. hd, sd)
    Section 5 = Dateiformate und Protokolle (z.B. wtmp, /etc/passwd, nfs)
    Section 6 = Spiele (nur intro)
    Section 7 = Konventionen, Makro-Pakete, usw. (z.B. nroff, ascii)
    Section 8 = Systemverwaltung (nur intro)

%description -l fr
Un large ensemble de pages de man couvrant la programmation des APIs,
les formats de fichiers, les protocoles, etc.

    Section 1 = commandes utilisateur (intro seulement)
    Section 2 = appels système
    Section 3 = appels libc
    Section 4 = périphériques (e.g., hd, sd)
    Section 5 = formats de fichiers et protocoles (e.g., wtmp, /etc/passwd, nfs)
    Section 6 = jeux (intro seulement)
    Section 7 = conventions, paquetages, etc. (e.g., nroff, ascii)
    Section 8 = administration système (intro seulement)

%description -l pl
Pakiet ten zawiera du¿± kolekcjê podrêczników ekranowych (man pages),
opisuj±cych format plików, protoko³y itp.

    Section 1 = komendy u¿ytkowników (tylko wstêp)
    Section 2 = wywo³ania systemowe
    Section 3 = wywo³ania bibliotek
    Section 4 = urz±dzenia (np., hd, sd)
    Section 5 = format plików i protoko³y (np., wtmp, /etc/passwd, nfs)
    Section 6 = gry (tylko wstêp)
    Section 7 = konwencje, makro-pakiety, etc. (np., nroff, ascii)
    Section 8 = administracja systemu (tylko wstêp)

%description -l tr
Programlama arayüzlerini, dosya formatlarýný, protokolleri vs. kapsayan,
geniþ bir kýlavuz sayfalarý derlemesi.

%prep
%setup -q

%build
rm -fv man1/{chgrp,chmod,chown,cp,dd,df,dircolors,du,install,diff}.1
rm -fv man1/{ln,ls,mkdir,mkfifo,mknod,mv,rm,rmdir,touch,dir,vdir}.1
rm -fv man2/{modules,quotactl,get_kernel_syms,capget,capset}.2 
rm -fv man2/{create,delete,init,query}_module.2
rm -fv man3/{resolver,getnetent,strcasecmp}.3
rm -fv man4/console.4
rm -fv man5/{exports,lilo.conf,nfs,fstab,passwd}.5
rm -fv man8/lilo.8

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man{1,2,3,4,5,6,7,8}
for n in man{1,2,3,4,5,6,7,8}/*; do
	install $n $RPM_BUILD_ROOT%{_mandir}/$n
done

rm -f $RPM_BUILD_ROOT%{_mandir}/man*/README*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_mandir}/man*/*
