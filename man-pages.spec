Summary:	System manual pages from the Linux Documentation Project
Summary(de):	System-man-Seiten vom Linux Documentation Project
Summary(fr):	Pages man syst�me du Projet de Documentation Linux
Summary(pl):	Podr�czniki systemowe z Linux Documentation Project
Summary(tr):	Linux Belgeleme Projesinin sistem k�lavuz sayfalar�
Name:		man-pages
Version:	1.23
Release:	1
Copyright:	distributable
Group:		Documentation
Source:		ftp://ftp.win.tue.nl/pub/linux/docs/manpages/%{name}-%{version}.tar.bz2
BuildArch:	noarch
Buildroot:	/tmp/%{name}-%{version}-root
Autoreqprov:	false

%description
A large collection of man pages covering programming APIs, file
formats, protocols, etc.

    Section 1 = user commands (intro only)
    Section 4 = devices (e.g., hd, sd)
    Section 5 = file formats and protocols (e.g., wtmp, /etc/passwd, nfs)
    Section 6 = games (intro only)
    Section 7 = conventions, macro packages, etc. (e.g., nroff, ascii)
    Section 8 = system administration (intro only)

%description -l de
Eine gro�e Sammlung von man-Seiten �ber Programmier-APIs,
Dateiformate, Protokolle, usw..

    Section 1 = Benutzerbefehle (nur intro)
    Section 4 = Ger�te (z.B. hd, sd)
    Section 5 = Dateiformate und Protokolle (z.B. wtmp, /etc/passwd, nfs)
    Section 6 = Spiele (nur intro)
    Section 7 = Konventionen, Makro-Pakete, usw. (z.B. nroff, ascii)
    Section 8 = Systemverwaltung (nur intro)

%description -l fr
Un large ensemble de pages de man couvrant la programmation des APIs,
les formats de fichiers, les protocoles, etc.

    Section 1 = commandes utilisateur (intro seulement)
    Section 4 = p�riph�riques (e.g., hd, sd)
    Section 5 = formats de fichiers et protocoles (e.g., wtmp, /etc/passwd, nfs)
    Section 6 = jeux (intro seulement)
    Section 7 = conventions, paquetages, etc. (e.g., nroff, ascii)
    Section 8 = administration syst�me (intro seulement)

%description -l pl
Pakiet ten zawiera du�� kolekcj� podr�cznik�w ekranowych (man pages),
opisuj�cych format plik�w, protoko�y itp.

    Section 1 = komendy u�ytkownik�w (tylko wst�p)
    Section 4 = urz�dzenia (np., hd, sd)
    Section 5 = format plik�w i protoko�y (np., wtmp, /etc/passwd, nfs)
    Section 6 = gry (tylko wst�p)
    Section 7 = konwencje, makro-pakiety, etc. (np., nroff, ascii)
    Section 8 = administracja systemu (tylko wst�p)

%description -l tr
Programlama aray�zlerini, dosya formatlar�n�, protokolleri vs. kapsayan,
geni� bir k�lavuz sayfalar� derlemesi.

%prep
%setup -q

%build
rm -fv man1/{chgrp,chmod,chown,cp,dd,df,dircolors,du,install}.1
rm -fv man1/{ln,ls,mkdir,mkfifo,mknod,mv,rm,rmdir,touch}.1
rm -fv man4/console.4
rm -fv man5/exports.5
rm -fv man5/nfs.5
rm -fv man5/fstab.5
rm -fv man5/lilo.conf.5
rm -fv man3/strcasecmp.3
rm -fv man1/lilo.conf.5
rm -fv man8/lilo.8

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/man/man{1,4,5,6,7,8}
for n in man{1,4,5,6,7,8}/*; do
	install $n $RPM_BUILD_ROOT/usr/man/$n
done

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(644,root,root) /usr/man/man*/*

%changelog
* Tue Mar 30 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.23-1]
- man pages level 2 moved to kernel-headers,
- removed lilo.conf(5),
- man pages level 3 moved to glibc-devel package,
- removed man group from man pages.

* Fri Dec  6 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.22-2]
- removed lilo(5), lilo.conf(8) man pages (will be in lilo package),
- %defattr changed to %attr.

* Sun Nov 29 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.22-1]
- added gzipping man pages,
- changed base Source url.

* Fri Sep 04 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [1.19-2]
- added pl translation,
- removed strcasecmp.3 (conflict with inn-1.5.1-devel).

* Tue Jun 30 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
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
