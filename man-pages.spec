Summary:     System manual pages from the Linux Documentation Project
Summary(de): System-man-Seiten vom Linux Documentation Project
Summary(fr): Pages man système du Projet de Documentation Linux
Summary(pl): Podrêczniki systemowe z Linux Documentation Project
Summary(tr): Linux Belgeleme Projesinin sistem kýlavuz sayfalarý
Name:        man-pages
Version:     1.22
Release:     1
Copyright:   distributable
Group:       Documentation
Source:      ftp://ftp.win.tue.nl/pub/linux/man/%{name}-%{version}.tar.gz
BuildArchitectures: noarch
Buildroot:   /tmp/%{name}-%{version}-root
Autoreqprov: false

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
rm -fv man1/{chgrp,chmod,chown,cp,dd,df,dircolors,du,install}.1
rm -fv man1/{ln,ls,mkdir,mkfifo,mknod,mv,rm,rmdir,touch}.1
rm -fv man2/{modules,quotactl,get_kernel_syms}.2 
rm -fv man2/{create,delete,init,query}_module.2
rm -fv man3/resolver.3
rm -fv man3/getnetent.3
rm -fv man3/gethostbyname.3
rm -fv man4/console.4
rm -fv man5/exports.5
rm -fv man5/nfs.5
rm -fv man5/fstab.5
rm -fv man3/strcasecmp.3

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/man/man{1,2,3,4,5,6,7,8}
for n in man?/*; do
	install $n $RPM_BUILD_ROOT/usr/man/$n
done

gzip -9nf $RPM_BUILD_ROOT/usr/man/man{1,2,3,4,5,6,7,8}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, man)
/usr/man/man*/*

%changelog
* Sun Nov 29 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.22-1]
- added gziping man pages,
- changed base Source url.

* Fri Sep 04 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.19-2]
- added pl translation,
- removed strcasecmp.3 (conflict with inn-1.5.1-devel).

* Tue Jun 30 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.19-1]
- removed gethostbyname.3 (conflict with bind-8.1.2)

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- get rid of the modutils man pages
- updated to 1.19

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Erik Troan <ewt@redhat.com>
- updated to 1.18

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- updated to 1.17
- moved build root to /var

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
