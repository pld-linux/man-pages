#
# Conditional build:
# _with_tars         generate man-pages tars for other packages
#
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
Summary(uk):	���Ҧ��� ������� (man) � Linux Documentation Project
Name:		man-pages
Version:	1.56
Release:	4
License:	distributable
Group:		Documentation
%define		cs_version		0.16
%define		da_version		0.1.1
%define		de_version		0.4
%define		es_version		1.28
%define		es_extra_version	0.8a
%define		fi_version		0.1
%define		fr_version		0.9.7
%define		hu_version		2001_01_05
%define		id_version		20011116
%define		it_version		0.3.3
%define		ja_version		20030525
%define		ko_version		20010901
%define		nl_version		0.13.3
%define		pl_version		20020828
%define		pt_version		1.39
%define		ru_version		0.7
%define		uk_version		0.1.1 
%define		zh_version		0.3
Source0:	ftp://ftp.win.tue.nl/pub/home/aeb/linux-local/manpages/%{name}-%{version}.tar.gz
# Source0-md5: 191480045edc30c6443fd26e65c6395e
# Source1:	ftp://ftp.muni.cz/pub/linux/people/petr_kolar/localization/man-pages-cs/%{name}-cs-%{cs_version}.tar.gz
Source1:	ftp://ftp.linux.cz/pub/localization/linux/czman/%{name}-cs-%{cs_version}.tar.gz
# Source1-md5: e8036794c1762804f2e242cc5b52001e
# there is no LDP man page here, yet.
# Source2:	http://www.sslug.dk/locale/man-sider/manpages-da-%{da_version}.tar.gz
Source3:	http://www.infodrom.org/projects/manpages-de/download/manpages-de-%{de_version}.tar.gz
# Source3-md5: 6a2a1cd24b0bd61c4ab384324e707a95
Source4:	http://www.ditec.um.es/~piernas/manpages-es/%{name}-es-%{es_version}.tar.gz
# Source4-md5: b58b76cdd2b2174ba216fa30e5d83518
Source5:	http://www.ditec.um.es/~piernas/manpages-es/%{name}-es-extra-%{es_extra_version}.tar.gz
# Source5-md5: 5827f41f77658df17f550b7f8e831432
# extracted from http://developer.bestlinux.net/man-fi/usr/man/RPMS/%{name}-fi-%{fi_version}-4.src.rpm
Source6:	man-fi-%{fi_version}.tar.bz2
# Source6-md5: 	53dcf98b573c6e00c45eb91affca0a2e
# Source7:	ftp://ftp.lip6.fr/pub/linux/french/docs/man-fr-%{fr_version}.tar.gz
Source7:	http://perso.club-internet.fr/ccb/man/man-fr-%{fr_version}.tar.gz
# Source7-md5: aec50d6d7fbb9b7a096ae26ab4a3177f
Source8:	http://www.kde.hu/mlp/man/man_hu_%{hu_version}.tar.gz
# Source8-md5: 8b94f02287672c5a0601c1ad422a8e07
# there is no LDP man page here, yet.
# based on http://nakula.rvs.uni-bielefeld.de/made/my_project/ManPage/
# Source9:	man-pages-from-www-id-%{id_version}.tar.gz
# available also as http://
Source10:	ftp://ftp.pluto.linux.it/pub/pluto/ildp/man/%{name}-it-%{it_version}.tar.gz
# Source10-md5: dfacc75f081e7340094d88c7a04b5fab
Source11:	http://www.linux.or.jp/JM/%{name}-ja-%{ja_version}.tar.gz
# Source11-md5:	82e9882e75d038e9b416a386a059e692
# Source12:	ftp://metalab.unc.edu/pub/Linux/docs/LDP/man-pages/%{name}-ko-%{ko_version}.tar.gz
Source12:	http://download.kldp.net/man/%{name}-ko-%{ko_version}.tar.gz
# Source12-md5: e73c7999af103208e5497f939de764ca
Source13:	ftp://ftp.nl.linux.org/pub/DOC-NL/manpages-nl/manpages-nl-%{nl_version}.tar.gz
# Source13-md5: b37b0216a87db7583e88ba87031a0b4a
Source14:	%{name}-pl-PTM-snapshot.%{pl_version}.tar.bz2
# Source14-md5: 2ad83c91c1a568c1c5f40ba699077cd6
Source15:	ftp://ftp.win.tue.nl/pub/home/aeb/linux-local/manpages/tr/%{name}-%{pt_version}-pt_BR.tgz
# Source15-md5: 3f8db6dd6a7884b595e70f624ac93735
Source16:	http://alexm.here.ru/manpages-ru/download/manpages-ru-%{ru_version}.tar.gz
# Source16-md5: bfd5a8f20a12b994e19cfca0c4a21249
# from ASP Linux
Source17:	man-pages-uk-%{uk_version}.tar.bz2
# Source17-md5: a4f11eb6cdd2af4d57b967de868eb7fd
Source18:	http://cmpp.linuxforum.net/download/cman-%{zh_version}.tar.gz
# Source18-md5: 8c631fb761cd684ea3e41aef438d0b49
Source50:	%{name}-extra.tar.bz2
# Source50-md5: 967e10b6b691f53885ffa01695657f79
Source51:	mbox.5
Patch0:		%{name}-localtime.patch
BuildArch:	noarch
Autoreqprov:	false
Obsoletes:	man-pages-cs
Obsoletes:	man-pages-de
Obsoletes:	man-pages-es
Obsoletes:	man-pages-fi
Obsoletes:	man-pages-fr
Obsoletes:	man-pages-hu
Obsoletes:	manpages-hu
Obsoletes:	man-pages-it
Obsoletes:	man-pages-ja
Obsoletes:	man-pages-ko
Obsoletes:	man-pages-nl
Obsoletes:	man-pages-pl
Obsoletes:	man-pages-pt
Obsoletes:	man-pages-pt_BR
Obsoletes:	man-pages-ru
Obsoletes:	man-pages-ru-asp
Obsoletes:	man-pages-uk
Obsoletes:	man-pages-zh
Conflicts:	attr-devel < 2.2.0-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l uk
������� ��¦� ���Ҧ��� ������� (���������æ�) � Linux Documentation
Project (LDP). ���Ҧ��� ����Φ����Φ � ��˦ ���æ�: ���æ� 1, �������
����������� (Ԧ���� �����); ���æ� 2, ������Φ �������; ���æ� 3,
������� libc; ���æ� 4, ������ϧ (���������, hd, sd); ���æ� 5,
������� ���̦� �� ��������� (���������, wtmp, /etc/passwd, nfs);
���æ� 6, ���� (Ԧ���� �����); ���æ� 7, �����, ����������� � �.�.
(���������, nroff, ascii); ���æ� 8, �������� ��ͦΦ��������� (Ԧ����
�����).

%prep
#%setup -q -a1 -a3 -a4 -a5 -a6 -a7 -a10 -a11 -a13 -a14 -a15 -a16 -a17 -a18
%setup -q -a1 -a3 -a4 -a5 -a6 -a7 -a11 -a13 -a14 -a15 -a16 -a17 -a18
%patch0 -p1
rm -f cman/man*/*.html

mkdir hu it ko
tar xzf %{SOURCE8} -C hu
tar xzf %{SOURCE10} -C it
tar xzf %{SOURCE12} -C ko

%build
rm -f man1/{chgrp,chmod,chown,cp,dd,df,dircolors,du,install,diff}.1
rm -f man1/{ldd,ln,ls,mkdir,mkfifo,mknod,mv,rm,rmdir,time,touch,dir,vdir}.1
rm -f man1/COPYING
rm -f man2/{capget,capset}.2
find man3 -type f | grep -v 'intro\.3' | xargs rm -f
rm -f man4/{console,console_ioctl}.4
rm -f man5/{ftpusers,locale,nscd.conf,nsswitch.conf,passwd,tzfile}.5
rm -f man7/{ascii,charsets,iso*,koi8-r,latin*,locale,unicode,utf*}.7
rm -f man8/{ld.so,ldconfig,nscd,sync,tzselect,zdump,zic}.8

rm -f man*/README*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,2,3,4,5,6,7,8}

for n in man{1,2,3,4,5,6,7,8}/*; do
	if head -1 $n| grep '^\.so' >/dev/null 2>&1 ; then
		sed 's,\.so man./,.so ,' < $n > $n.
		mv $n. $n
	fi
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
install -d $RPM_BUILD_ROOT%{_mandir}/uk/man{1,2,3,4,5,6,7,8}
install -d $RPM_BUILD_ROOT%{_mandir}/zh_CN/man{1,2,3,4,5,6,7,8}
install -d $RPM_BUILD_ROOT%{_mandir}/zh_TW/man{1,2,3,4,5,6,7,8}
for n in man{1,2,3,4,5,6,7,8}/*; do
	if [ -f %{name}-cs-%{cs_version}/$n ]; then
		install %{name}-cs-%{cs_version}/$n $RPM_BUILD_ROOT%{_mandir}/cs/$n
	fi
	if [ -f manpages-de-%{de_version}/$n ]; then
		install manpages-de-%{de_version}/$n $RPM_BUILD_ROOT%{_mandir}/de/$n
	fi
	if [ -f %{name}-es-%{es_version}/$n ]; then
		install %{name}-es-%{es_version}/$n $RPM_BUILD_ROOT%{_mandir}/es/$n
	elif [ -f %{name}-es-extra-%{es_extra_version}/$n ]; then
		install %{name}-es-extra-%{es_extra_version}/$n $RPM_BUILD_ROOT%{_mandir}/es/$n
	fi
	if [ -f manpages-fi/$n ]; then
		install manpages-fi/$n $RPM_BUILD_ROOT%{_mandir}/fi/$n
	fi
#	if [ -f man-fr-%{fr_version}/$n ]; then
#		install man-fr-%{fr_version}/$n $RPM_BUILD_ROOT%{_mandir}/fr/$n
	if [ -f man-fr/$n ]; then
		install man-fr/$n $RPM_BUILD_ROOT%{_mandir}/fr/$n
	fi
	if [ -f hu/$n ]; then
		install hu/$n $RPM_BUILD_ROOT%{_mandir}/hu/$n
	fi
#	if [ -f %{name}-it-%{it_version}/$n ]; then
#		install %{name}-it-%{it_version}/$n $RPM_BUILD_ROOT%{_mandir}/it/$n
	if [ -f it/$n ]; then
		install it/$n $RPM_BUILD_ROOT%{_mandir}/it/$n
	fi
	if [ -f %{name}-ja-%{ja_version}/manual/LDP_man-pages/$n ]; then
		install %{name}-ja-%{ja_version}/manual/LDP_man-pages/$n $RPM_BUILD_ROOT%{_mandir}/ja/$n
	fi
	if [ -f ko/$n ]; then
		install ko/$n $RPM_BUILD_ROOT%{_mandir}/ko/$n
	fi
	if [ -f manpages-nl-%{nl_version}/$n ]; then
		install manpages-nl-%{nl_version}/$n $RPM_BUILD_ROOT%{_mandir}/nl/$n
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
	if [ -f %{name}-uk-%{uk_version}/$n ]; then
		install %{name}-uk-%{uk_version}/$n $RPM_BUILD_ROOT%{_mandir}/uk/$n
	fi
	if [ -f cman/$n ]; then
		install cman/$n $RPM_BUILD_ROOT%{_mandir}/zh_CN/$n
#               Doesn't work. Bad encoding ?
#		iconv -f GB2312 -t Big5 cman/$n > $RPM_BUILD_ROOT%{_mandir}/zh_TW/$n
	fi
done
bzip2 -dc %{SOURCE50} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

install %{SOURCE51} $RPM_BUILD_ROOT%{_mandir}/man5/mbox.5

for k in $RPM_BUILD_ROOT%{_mandir}/{cs,de,es,fi,fr,hu,it,ja,ko,nl,pl,pt,pt_BR,ru,uk,zh_CN,zh_TW} ; do
	for n in $k/man{1,2,3,4,5,6,7,8}/*; do
		if head -1 $n| grep '^\.so' >/dev/null 2>&1 ; then
			sed 's,\.so man./,.so ,' < $n > $n.
			mv $n. $n
		fi
	done
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
%lang(uk) %{_mandir}/uk/man*/*
%lang(zh_CN) %{_mandir}/zh_CN/man*/*
#%lang(zh_TW) %{_mandir}/zh_TW/man*/*
