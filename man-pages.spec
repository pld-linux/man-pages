Summary:	System manual pages from the Linux Documentation Project
Summary(de):	System-man-Seiten vom Linux Documentation Project
Summary(es):	P�ginas de manual, del Proyecto de Documentaci�n del Linux (LDP)
Summary(fi):	Suomenkieliset man-sivut
Summary(fr):	Pages man syst�me du Projet de Documentation Linux
Summary(it):	Pagine di manuale
Summary(pl):	Podr�czniki systemowe z Linux Documentation Project
Summary(pt):	P�ginas de manual, do Projeto de Documenta��o do Linux (LDP)
Summary(pt_BR):	P�ginas de manual, do Projeto de Documenta��o do Linux (LDP)
Summary(ru):	�������� ����������� �� ������� ������������ �� ������
Summary(tr):	Linux Belgeleme Projesinin sistem k�lavuz sayfalar�
Name:		man-pages
Version:	1.40
Release:	4
License:	Distributable
Group:		Documentation
Group(de):	Dokumentation
Group(es):	Documentaci�n
Group(pl):	Dokumentacja
Group(pt):	Documenta��o
Group(pt_BR):	Documenta��o
Group(ru):	������������
%define		cs_version	0.14
%define		da_version	0.1.1
%define		de_version	0.3
%define		es_version	1.28
%define		fi_version	0.1
%define		fr_version	0.9
%define		hu_version	2001_01_05
%define		id_version	20010914
%define		it_version	0.3.0
%define		ja_version	20011015
%define		ko_version	20010605
%define		pl_version	20011004
%define		pt_version	1.39
%define		ru_version	0.7
%define		zh_version	0.1
Source0:	ftp://ftp.win.tue.nl/pub/linux-local/manpages/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.muni.cz/pub/linux/people/petr_kolar/localization/man-pages-cs/%{name}-cs-%{cs_version}.tar.gz
# there is no LDP man page here, yet.
#Source2:	http://www.sslug.dk/locale/man-sider/manpages-da-%{da_version}.tar.gz
Source3:	http://www.infodrom.ffis.de/projects/manpages-de/download/manpages-de-%{de_version}.tar.gz
Source4:	http://www.ditec.um.es/~piernas/manpages-es/%{name}-es-%{es_version}.tar.gz
Source5:	man-fi-%{fi_version}.tar.bz2
#Source5:	http://developer.bestlinux.net/man-fi/usr/man/RPMS/%{name}-fi-%{fi_version}-4.src.rpm
Source6:	ftp://ftp.lip6.fr/pub/linux/french/docs/man-fr-%{fr_version}.tar.gz
#Source6:	ftp://ftp.win.tue.nl/pub/home/aeb/linux-local/manpages/tr/%{name}-fr-%{fr_version}.tar.gz
Source7:	http://www.kde.hu/mlp/man/man_hu_%{hu_version}.tar.gz
# there is no LDP man page here, yet.
#Source8:	man-pages-from-www-id-%{id_version}.tar.gz
#Source8:	http://nakula.rvs.uni-bielefeld.de/made/my_project/ManPage/id-man.tar.bz2
Source9:	ftp://ftp.win.tue.nl/pub/home/aeb/linux-local/manpages/tr/%{name}-it-%{it_version}.tar.gz
Source10:	ftp://metalab.unc.edu/pub/Linux/docs/LDP/man-pages/%{name}-ja-%{ja_version}.tar.gz
#Source10:	http://www.linux.or.jp/JM/%{name}-ja-%{ja_version}.tar.gz
Source11:	ftp://metalab.unc.edu/pub/Linux/docs/LDP/man-pages/%{name}-ko-%{ko_version}.tar.gz
Source12:	ftp://ftp.win.tue.nl/pub/home/aeb/linux-local/manpages/tr/%{name}-nl.tar.gz
Source13:	%{name}-pl-PTM-snapshot.%{pl_version}.tar.bz2
Source14:	ftp://ftp.win.tue.nl/pub/home/aeb/linux-local/manpages/tr/%{name}-%{pt_version}-pt_BR.tgz
Source15:	http://alexm.here.ru/manpages-ru/download/manpages-ru-%{ru_version}.tar.gz
#Source16:	http://www.cmpp.net/download/cman-%{zh_version}.tar.gz
Patch0:		%{name}-iconv.patch
Patch1:		%{name}-ctype.patch
Patch2:		%{name}-localtime.patch
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Autoreqprov:	false
Obsoletes:	man-pages-cs
Obsoletes:	man-pages-de
Obsoletes:	man-pages-es
Obsoletes:	man-pages-fi
Obsoletes:	man-pages-fr
Obsoletes:	man-pages-hu
Obsoletes:	man-pages-it
Obsoletes:	man-pages-ja
Obsoletes:	man-pages-ko
Obsoletes:	man-pages-nl
Obsoletes:	man-pages-pl
Obsoletes:	man-pages-pt
Obsoletes:	man-pages-pt_BR
Obsoletes:	man-pages-ru

%description
A large collection of man pages covering programming APIs, file
formats, protocols, etc.

- section 1: user commands (intro only)
- section 2: system calls
- section 3: libc calls (intro only)
- section 4: devices (e.g., hd, sd)
- section 5: file formats and protocols (e.g., wtmp, /etc/passwd, nfs)
- section 6: games (intro only)
- section 7: conventions, macro packages, etc. (e.g., nroff, ascii)
- section 8: system administration (intro only)

%description -l de
Eine gro�e Sammlung von man-Seiten �ber Programmier-APIs,
Dateiformate, Protokolle, usw..

- section 1: Benutzerbefehle (nur intro)
- section 2: Systemaufrufe
- section 3: libc-Aufrufe (nur intro)
- section 4: Ger�te (z.B. hd, sd)
- section 5: Dateiformate und Protokolle (z.B. wtmp, /etc/passwd, nfs)
- section 6: Spiele (nur intro)
- section 7: Konventionen, Makro-Pakete, usw. (z.B. nroff, ascii)
- section 8: Systemverwaltung (nur intro)

%description -l es
Una larga colecci�n de p�ginas de manuales cubriendo programaci�n
APIs, formatos de archivos, protocolos, etc.

- seci�n 1: comandos de usuario (solamente introducci�n)
- seci�n 2: llamadas de sistema
- seci�n 3: llamadas libc (solamente introducci�n)
- seci�n 4: dispositivos (ej.: hd, sd)
- seci�n 5: formatos de archivos y protocolos (ej: wtmp, /etc/passwd,
  nfs)
- seci�n 6: juegos (solamente introducci�n)
- seci�n 7: convenciones, paquetes de macros, etc. (ej: nroff, ascii)
- seci�n 8: administraci�n de sistema (solamente introducci�n)
- seci�n 9: kernel

%description -l fi
Kokoelma man-sivujen k��nn�ksi� suomenkielelle. Sivuja on mukana
yhteens� 211 kpl ja ne on paketoitu 14.11.1999 menness� valmiina
olleista sivuista. Sivut ovat osista 1 (komennot) ja 2 (pelit).

%description -l fr
Une large collection de pages de manuel du Project de Documentation
Linux (LDP), traduites en Fran�ais. Les pages de manuel sont
organis�es en differentes sections :

- section 1: Commandes utilisateur (intro seulement)
- section 2: Appels syst�me
- section 3: Appels de la Libc (intro seulement)
- section 4: P�riph�riques (par ex. hd, sd)
- section 5: Formats de fichiers et de protocoles (par ex. wtmp,
  /etc/passwd, nfs)
- section 6: Jeux (intro seulement)
- section 7: Conventions, macro packages, etc. (par ex. nroff, ascii)
- section 8: Administration syst�me (intro seulement)
- section 9: Routines du noyau

%description -l it
Traduzioni italiane delle pagine di manuale per Linux: questo
pacchetto include non solo quelle dell'LDP, ma anche traduzioni di
altre pagine di uso comune. ATTENZIONE: alcune pagine sono obsolete!

%description -l pl
Pakiet ten zawiera du�� kolekcj� podr�cznik�w ekranowych (man pages),
opisuj�cych format plik�w, protoko�y itp.

- sekcja 1: komendy u�ytkownik�w (tylko wst�p)
- sekcja 2: wywo�ania systemowe
- sekcja 3: wywo�ania bibliotek (tylko wst�p)
- sekcja 4: urz�dzenia (np., hd, sd)
- sekcja 5: format plik�w i protoko�y (np., wtmp, /etc/passwd, nfs)
- sekcja 6: gry (tylko wst�p)
- sekcja 7: konwencje, makro-pakiety, itp. (np., nroff, ascii)
- sekcja 8: administracja systemu (tylko wst�p)

%description -l pt
Uma larga cole��o de p�ginas de manuais cobrindo programa��o APIs,
formatos de arquivos, protocolos, etc.

- se��o 1: comandos de usu�rio (somente introdu��o)
- se��o 2: chamadas de sistema
- se��o 3: chamadas libc (somente introdu��o)
- se��o 4: dispositivos (ex.: hd, sd)
- se��o 5: formatos de arquivos e protocolos (ex: wtmp, /etc/passwd,
  nfs)
- se��o 6: jogos (somente introdu��o)
- se��o 7: conven��es, pacotes de macros, etc. (ex: nroff, ascii)
- se��o 8: administra��o de sistema (somente introdu��o)
- se��o 9: kernel

%description -l pt_BR
Uma larga cole��o de p�ginas de manuais cobrindo programa��o APIs,
formatos de arquivos, protocolos, etc.

- se��o 1: comandos de usu�rio (somente introdu��o)
- se��o 2: chamadas de sistema
- se��o 3: chamadas libc (somente introdu��o)
- se��o 4: dispositivos (ex.: hd, sd)
- se��o 5: formatos de arquivos e protocolos (ex: wtmp, /etc/passwd,
  nfs)
- se��o 6: jogos (somente introdu��o)
- se��o 7: conven��es, pacotes de macros, etc. (ex: nroff, ascii)
- se��o 8: administra��o de sistema (somente introdu��o)
- se��o 9: kernel

%description -l ru
��������� ��������� ������� ����������� �� ������� ������������ ��
������. �������� ����������� ������������ ��������� �������:

- ������ 1: ������ ������������ (������ ��������)
- ������ 2: ��������� ������
- ������ 3: ������� ���������� ����� C (������ ��������)
- ������ 4: ���������� (��������, hd, sd)
- ������ 5: ������� ������ � ��������� (��������, wtmp, /etc/passwd,
  nfs)
- ������ 6: ���� (������ ��������)
- ������ 7: ����������, �����-������, � �. �. (��������, nroff, ascii)
- ������ 8: ������� �������������� (������ ��������)

%description -l tr
Programlama aray�zlerini, dosya formatlar�n�, protokolleri vs.
kapsayan, geni� bir k�lavuz sayfalar� derlemesi.

%prep
%setup -q -a1 -a3 -a4 -a5 -a6 -a9 -a10 -a12 -a13 -a14 -a15
%patch0 -p1
%patch1 -p1
%patch2 -p1

mkdir hu ko
tar xzf %{SOURCE7} -C hu
tar xzf %{SOURCE11} -C ko

%build
rm -f man1/{chgrp,chmod,chown,cp,dd,df,dircolors,du,install,diff}.1
rm -f man1/{ln,ls,mkdir,mkfifo,mknod,mv,rm,rmdir,time,touch,dir,vdir}.1
rm -f man1/COPYING
rm -f man2/{capget,capset}.2 
find man3 -type f | grep -v 'intro\.3' | xargs rm -f
rm -f man4/console.4
rm -f man5/{locale,nsswitch.conf,passwd,tzfile}.5
rm -f man7/{ascii,charsets,iso*,koi8-r,latin*,locale,unicode,utf*}.7
rm -f man8/{sync,tzselect,zdump,zic,ldconfig}.8

rm -f man*/README*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,2,3,4,5,6,7,8}

for n in man{1,2,3,4,5,6,7,8}/*; do
	install $n $RPM_BUILD_ROOT%{_mandir}/$n
done

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
install -d $RPM_BUILD_ROOT%{_mandir}/pt_BR/man{1,2,3,4,5,6,7,8}
install -d $RPM_BUILD_ROOT%{_mandir}/ru/man{1,2,3,4,5,6,7,8}
for n in man{1,2,3,4,5,6,7,8}/*; do
	if [ -f %{name}-cs-%{cs_version}/$n ]; then
		install %{name}-cs-%{cs_version}/$n $RPM_BUILD_ROOT%{_mandir}/cs/$n
	fi
	if [ -f manpages-de-%{de_version}/$n ]; then
		install manpages-de-%{de_version}/$n $RPM_BUILD_ROOT%{_mandir}/de/$n
	fi
	if [ -f %{name}-es-%{es_version}/$n ]; then
		install %{name}-es-%{es_version}/$n $RPM_BUILD_ROOT%{_mandir}/es/$n
	fi
	if [ -f manpages-fi/$n ]; then
		install manpages-fi/$n $RPM_BUILD_ROOT%{_mandir}/fi/$n
	fi
	if [ -f man-fr-%{fr_version}/$n ]; then
		install man-fr-%{fr_version}/$n $RPM_BUILD_ROOT%{_mandir}/fr/$n
	fi
	if [ -f hu/$n ]; then
		install hu/$n $RPM_BUILD_ROOT%{_mandir}/hu/$n
	fi
	if [ -f %{name}-it-%{it_version}/$n ]; then
		install %{name}-it-%{it_version}/$n $RPM_BUILD_ROOT%{_mandir}/it/$n
	fi
	if [ -f %{name}-ja-%{ja_version}/manual/LDP_man-pages/$n ]; then
		install %{name}-ja-%{ja_version}/manual/LDP_man-pages/$n $RPM_BUILD_ROOT%{_mandir}/ja/$n
	fi
	if [ -f ko/$n ]; then
		install ko/$n $RPM_BUILD_ROOT%{_mandir}/ko/$n
	fi
	if [ -f nl/$n ]; then
		install nl/$n $RPM_BUILD_ROOT%{_mandir}/nl/$n
	fi
	if [ -f pl_PL/$n ]; then
		install pl_PL/$n $RPM_BUILD_ROOT%{_mandir}/pl/$n
	fi
	if [ -f %{name}-%{pt_version}-pt_BR/$n ]; then
		install %{name}-%{pt_version}-pt_BR/$n $RPM_BUILD_ROOT%{_mandir}/pt_BR/$n
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
%lang(pt_BR) %{_mandir}/pt_BR/man*/*
%lang(ru) %{_mandir}/ru/man*/*
