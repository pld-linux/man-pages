Summary:	System manual pages from the Linux Documentation Project
Summary(de):	System-man-Seiten vom Linux Documentation Project
Summary(fr):	Pages man systХme du Projet de Documentation Linux
Summary(pl):	PodrЙczniki systemowe z Linux Documentation Project
Summary(ru):	Страницы руководства из Проекта Документации на Линукс.
Summary(tr):	Linux Belgeleme Projesinin sistem kЩlavuz sayfalarЩ
Name:		man-pages
Version:	1.35
Release:	4
License:	Distributable
Group:		Documentation
Group(de):	Dokumentation
Group(es):	DocumentaciСn
Group(pl):	Dokumentacja
Group(pt):	DocumentaГЦo
Group(ru):	Документация
%define		cs_version	0.14
%define		da_version	0.1.1
%define		de_version	0.3
%define		es_version	1.28
%define		fi_version	0.1
%define		fr_version	0.9
%define		hu_version	2001_01_05
%define		id_version	20010914
%define		it_version	0.3.0
%define		ja_version	20010815
%define		ko_version	20010605
%define		pl_version	20010913
%define		pt_version	1.39
%define		ru_version	0.7
%define		zh_version	0.1
Source0:	ftp://ftp.win.tue.nl/pub/linux-local/manpages/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.muni.cz/pub/linux/people/petr_kolar/localization/man-pages-cs/%{name}-cs-%{cs_version}.tar.gz
# there is no LDP man page here, yet.
#Source2:	http://www.sslug.dk/locale/man-sider/manpages-da-%{da_version}.tar.gz
Source3:	http://www.infodrom.ffis.de/projects/manpages-de/download/manpages-de-%{de_version}.tar.gz
Source4:	http://www.ditec.um.es/~piernas/manpages-es/%{name}-es-%{es_version}.tar.gz
Source5:	%{name}-from-rpm-fi-%{fi_version}.tar.gz
#Source5:	http://developer.bestlinux.net/man-fi/usr/man/RPMS/%{name}-fi-%{fi_version}-4.src.rpm
Source6:	ftp://ftp.lip6.fr/pub/linux/french/docs/man-fr-%{fr_version}.tar.gz
#Source6:	ftp://ftp.win.tue.nl/pub/home/aeb/linux-local/manpages/tr/%{name}-fr-%{fr_version}.tar.gz
Source7:	http://www.kde.hu/mlp/man/man_hu_%{hu_version}.tar.gz
# there is no LDP man page here, yet.
#Source8:	man-pages-from-www-id-%{id_version}.tar.gz
#Source8:	http://nakula.rvs.uni-bielefeld.de/made/my_project/ManPage/id-man.tar.bz2
Source9:	ftp://ftp.win.tue.nl/pub/home/aeb/linux-local/manpages/tr/%{name}-it-%{it_version}.tar.gz
Source10:	ftp://metalab.unc.edu/pub/Linux/docs/LDP/man-pages/%{name}-ja-%{ja_version}.tar.gz
#Source10:	http://www.linux.or.jp/JM/%{name}-ja-%{ja_version}.tar.bz2
Source11:	ftp://metalab.unc.edu/pub/Linux/docs/LDP/man-pages/%{name}-ko-%{ko_version}.tar.gz
Source12:	ftp://ftp.win.tue.nl/pub/home/aeb/linux-local/manpages/tr/%{name}-nl.tar.gz
Source13:	man-pages-pl-PTM-snapshot.%{pl_version}.tar.gz
Source14:	ftp://ftp.win.tue.nl/pub/home/aeb/linux-local/manpages/tr/%{name}-%{pt_version}-pt_BR.tgz
Source15:	http://alexm.here.ru/manpages-ru/download/manpages-ru-%{ru_version}.tar.gz
#Source16:	http://www.cmpp.net/download/cman-%{zh_version}.tar.gz
Patch0:		man-pages-iconv.patch
Patch1:		man-pages-ctype.patch
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
Eine groъe Sammlung von man-Seiten Эber Programmier-APIs,
Dateiformate, Protokolle, usw..

- section 1 = Benutzerbefehle (nur intro)
- section 2 = Systemaufrufe
- section 3 = libc-Aufrufe
- section 4 = GerДte (z.B. hd, sd)
- section 5 = Dateiformate und Protokolle (z.B. wtmp, /etc/passwd,
  nfs)
- section 6 = Spiele (nur intro)
- section 7 = Konventionen, Makro-Pakete, usw. (z.B. nroff, ascii)
- section 8 = Systemverwaltung (nur intro)

%description -l fr
Un large ensemble de pages de man couvrant la programmation des APIs,
les formats de fichiers, les protocoles, etc.

- section 1 = commandes utilisateur (intro seulement)
- section 2 = appels systХme
- section 3 = appels libc
- section 4 = pИriphИriques (e.g., hd, sd)
- section 5 = formats de fichiers et protocoles (e.g., wtmp,
  /etc/passwd, nfs)
- section 6 = jeux (intro seulement)
- section 7 = conventions, paquetages, etc. (e.g., nroff, ascii)
- section 8 = administration systХme (intro seulement)

%description -l pl
Pakiet ten zawiera du©╠ kolekcjЙ podrЙcznikСw ekranowych (man pages),
opisuj╠cych format plikСw, protokoЁy itp.

- sekcja 1 = komendy u©ytkownikСw (tylko wstЙp)
- sekcja 2 = wywoЁania systemowe
- sekcja 3 = wywoЁania bibliotek
- sekcja 4 = urz╠dzenia (np., hd, sd)
- sekcja 5 = format plikСw i protokoЁy (np., wtmp, /etc/passwd, nfs)
- sekcja 6 = gry (tylko wstЙp)
- sekcja 7 = konwencje, makro-pakiety, itp. (np., nroff, ascii)
- sekcja 8 = administracja systemu (tylko wstЙp)

%description(ru)
Небольшая коллекция страниц руководства из Проекта Документации на Линукс.
Страницы руководства организованы следующим образом:

- секция 1, команд пользователя (только введение)
- секция 2, системные вызовы
- секция 3, функции библиотеки языка C
- секция 4, устройства (например, hd, sd)
- секция 4, форматы файлов и протоколы (например, wtmp, /etc/passwd, nfs)
- секция 6, игры (только введение)
- секция 7, соглашения, макро-пакеты, и т. п. (например, nroff, ascii)
- секция 8, утилиты администратора (только введение)

%description -l tr
Programlama arayЭzlerini, dosya formatlarЩnЩ, protokolleri vs.
kapsayan, geniЧ bir kЩlavuz sayfalarЩ derlemesi.

%prep
%setup -q -a7 -c -T -n %{name}-hu-%{hu_version}
%setup -q -a11 -c -T -n %{name}-ko-%{ko_version}
%setup -q -a1 -a3 -a4 -a5 -a6 -a9 -a10 -a12 -a13 -a14 -a15
%patch0 -p1
%patch1 -p1

%build
rm -f man1/{chgrp,chmod,chown,cp,dd,df,dircolors,du,install,diff}.1
rm -f man1/{ln,ls,mkdir,mkfifo,mknod,mv,rm,rmdir,time,touch,dir,vdir}.1
rm -f man1/COPYING
rm -f man2/{capget,capset}.2 
rm -f man4/console.4
rm -f man5/passwd.5
rm -f man8/sync.8

rm -f man*/README*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,2,3,4,5,6,7,8}

for n in man{1,2,3,4,5,6,7,8}/*; do
	install $n $RPM_BUILD_ROOT%{_mandir}/$n
done

# rm -f $RPM_BUILD_ROOT%{_mandir}/man*/README*

install -d $RPM_BUILD_ROOT%{_mandir}/cs/man{1,2,3,4,5,6,7,8}
install -d $RPM_BUILD_ROOT%{_mandir}/de/man{1,2,3,4,5,6,7,8}
install -d $RPM_BUILD_ROOT%{_mandir}/es/man{1,2,3,4,5,6,7,8}
install -d $RPM_BUILD_ROOT%{_mandir}/fi/man{1,2,3,4,5,6,7,8}
install -d $RPM_BUILD_ROOT%{_mandir}/fr/man{1,2,3,4,5,6,7,8}
install -d $RPM_BUILD_ROOT%{_mandir}/hu/man{1,2,3,4,5,6,7,8}
install -d $RPM_BUILD_ROOT%{_mandir}/it/man{1,2,3,4,5,6,7,8}
install -d $RPM_BUILD_ROOT%{_mandir}/ja/man{1,2,3,4,5,6,7,8}
install -d $RPM_BUILD_ROOT%{_mandir}/ko/man{1,2,3,4,5,6,7,8}
install -d $RPM_BUILD_ROOT%{_mandir}/nl/man{1,2,3,4,5,6,7,8}
install -d $RPM_BUILD_ROOT%{_mandir}/pl/man{1,2,3,4,5,6,7,8}
install -d $RPM_BUILD_ROOT%{_mandir}/pt/man{1,2,3,4,5,6,7,8}
install -d $RPM_BUILD_ROOT%{_mandir}/ru/man{1,2,3,4,5,6,7,8}
for n in man{1,2,3,4,5,6,7,8}/*; do
	if [ -f %{name}-cs-%{cs_version}/$n ]; then
		install %{name}-cs-%{cs_version}/$n $RPM_BUILD_ROOT%{_mandir}/cs/$n
	fi
	if [ -f %{name}-de-%{de_version}/$n ]; then
		install %{name}-de-%{de_version}/$n $RPM_BUILD_ROOT%{_mandir}/de/$n
	fi
	if [ -f %{name}-es-%{es_version}/$n ]; then
		install %{name}-es-%{es_version}/$n $RPM_BUILD_ROOT%{_mandir}/es/$n
	fi
	# fi/man?/* are bziped
	if [ -f fi/$n.bz2 ]; then
		bunzip2 fi/$n.bz2
		install fi/$n $RPM_BUILD_ROOT%{_mandir}/fi/$n
	fi
	if [ -f man-fr-%{fr_version}/$n ]; then
		install man-fr-%{fr_version}/$n $RPM_BUILD_ROOT%{_mandir}/fr/$n
	fi
	if [ -f ../%{name}-hu-%{hu_version}/$n ]; then
		install ../%{name}-hu-%{hu_version}/$n $RPM_BUILD_ROOT%{_mandir}/hu/$n
	fi
	if [ -f %{name}-it-%{it_version}/$n ]; then
		install %{name}-it-%{it_version}/$n $RPM_BUILD_ROOT%{_mandir}/it/$n
	fi
	if [ -f %{name}-ja-%{ja_version}/manual/LDP_man-pages/$n ]; then
		install %{name}-ja-%{ja_version}/manual/LDP_man-pages/$n $RPM_BUILD_ROOT%{_mandir}/ja/$n
	fi
	if [ -f ../%{name}-ko-%{ko_version}/$n ]; then
		install ../%{name}-ko-%{ko_version}/$n $RPM_BUILD_ROOT%{_mandir}/ko/$n
	fi
	if [ -f nl/$n ]; then
		install nl/$n $RPM_BUILD_ROOT%{_mandir}/nl/$n
	fi
	if [ -f pl_PL/$n ]; then
		install pl_PL/$n $RPM_BUILD_ROOT%{_mandir}/pl/$n
	fi
	if [ -f %{name}-%{pt_version}-pt_BR/$n ]; then
		install %{name}-%{pt_version}-pt_BR/$n $RPM_BUILD_ROOT%{_mandir}/pt/$n
	fi
	if [ -f manpages-ru-%{ru_version}/$n ]; then
		install manpages-ru-%{ru_version}/$n $RPM_BUILD_ROOT%{_mandir}/ru/$n
	fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_mandir}/man*/*
%lang(cs) %{_mandir}/cs/man*/*
%lang(de) %{_mandir}/de/man*/*
%lang(es) %{_mandir}/es/man*/*
%lang(fi) %{_mandir}/fi/man*/*
%lang(fr) %{_mandir}/fr/man*/*
%lang(hu) %{_mandir}/hu/man*/*
%lang(it) %{_mandir}/it/man*/*
%lang(ja) %{_mandir}/ja/man*/*
%lang(ko) %{_mandir}/ko/man*/*
%lang(nl) %{_mandir}/nl/man*/*
%lang(pl) %{_mandir}/pl/man*/*
%lang(pt) %{_mandir}/pt/man*/*
%lang(ru) %{_mandir}/ru/man*/*
