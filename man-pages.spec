#
# Conditional build:
%bcond_with	tars	# generate man-pages tars for other packages [not done yet]
#
Summary:	System manual pages from the Linux Documentation Project
Summary(de.UTF-8):	System-man-Seiten vom Linux Documentation Project
Summary(es.UTF-8):	Páginas de manual, del Proyecto de Documentación del Linux (LDP)
Summary(fi.UTF-8):	Suomenkieliset man-sivut
Summary(fr.UTF-8):	Pages man système du Projet de Documentation Linux
Summary(it.UTF-8):	Pagine di manuale
Summary(pl.UTF-8):	Podręczniki systemowe z Linux Documentation Project
Summary(pt.UTF-8):	Páginas de manual, do Projeto de Documentação do Linux (LDP)
Summary(pt_BR.UTF-8):	Páginas de manual, do Projeto de Documentação do Linux (LDP)
Summary(ru.UTF-8):	Страницы руководства из Проекта Документации на Линукс
Summary(tr.UTF-8):	Linux Belgeleme Projesinin sistem kılavuz sayfaları
Summary(uk.UTF-8):	Сторінки мануалу (man) з Linux Documentation Project
Name:		man-pages
Version:	5.03
Release:	1
License:	distributable
Group:		Documentation
%define		cs_version		0.17.20080113
%define		da_version		0.1.2
%define		de_version		0.5
%define		es_version		1.55
%define		es_extra_version	0.8a
%define		fi_version		0.2
%define		fr_version		3.70-1
%define		hu_version		20010119
%define		id_version		20011116
%define		it_version		4.08
%define		ja_version		20191015
%define		ko_version		20050219
%define		nl_version		0.13.3
%define		pl_version		20051105
%define		pt_version		1.39
%define		ro_version		0.2
#%%define	ru_version		0.98
%define		ru_asp_version		1.4
%define		tr_version		1.0.5
%define		zh_version		1.5.2
%define		posix_version		2013-a
Source0:	https://www.kernel.org/pub/linux/docs/man-pages/%{name}-%{version}.tar.xz
# Source0-md5:	4a85d16759c883048a1d27c741dadf17
Source1:	ftp://ftp.linux.cz/pub/localization/linux/czman/%{name}-cs-%{cs_version}.tar.bz2
# Source1-md5:	a3df67d98ab63a0a360cd0794ec87e0e
# there is no LDP man page here, yet - but include it in sources for completeness
# http://www.sslug.dk/locale/man-sider/manpages-da-%{da_version}.tar.gz (404 as of Feb 2018)
Source2:	manpages-da-%{da_version}.tar.gz
# Source2-md5:	26cdd12ea7c62e595fc1a3a39bf53115
# TODO: new project at https://manpages-de-team.pages.debian.net/manpages-de/, current version is 2.12
Source3:	http://www.infodrom.org/projects/manpages-de/download/manpages-de-%{de_version}.tar.gz
# Source3-md5:	6686b1be6da01cdbb5ea7511ddcf61a0
Source4:	http://www.ditec.um.es/~piernas/manpages-es/%{name}-es-%{es_version}.tar.bz2
# Source4-md5:	b71f701dcae827f2f5e4e848c66321fc
Source5:	http://www.ditec.um.es/~piernas/manpages-es/%{name}-es-extra-%{es_extra_version}.tar.gz
# Source5-md5:	5827f41f77658df17f550b7f8e831432
# extracted from http://www.ftp.funet.fi/index/sotlinux/bestlinux-2000R3/BL_2000_R3_FINAL/update/Finnish/man-pages-fi-0.2-1.src.rpm
# (despite archive filename it's 0.2 version)
Source6:	man-fi-0.1.tar.bz2
# Source6-md5:	bb266d3797cdf71bfbe1da190196f455
#Source7Download: https://gitlab.com/perkamon/man-pages-fr/tags
# TODO: use https://gitlab.com/perkamon/man-pages-fr/-/archive/%{fr_version}/man-pages-fr-%{fr_version}.tar.bz2, then make dist-fr to get tarball - but 4.16 produces very few translations
Source7:	man-pages-fr-%{fr_version}.tar.xz
# Source7-md5:	66a6033fb2ed3641c35b1d53c0fe5deb
# there is also: http://manpagesfr.free.fr/download/man-pages-extras-fr-0.8.1.tar.bz2
# and: http://manpagesfr.free.fr/download/man-pages-sup-fr-20080606.tar.bz2
#Source8:	http://download.uhulinux.hu/sources/man-pages-hu/man_hu_%{hu_version}.tar.gz (older)
Source8:	http://ftp.debian.org/debian/pool/main/m/manpages-hu/manpages-hu_%{hu_version}.orig.tar.gz
# Source8-md5:	742b682c5237a1e370b28f363826b2d5
# there is no LDP man page here, yet, but included for completeness
# based on http://nakula.rvs.uni-bielefeld.de/made/my_project/ManPage/ (dead now)
Source9:	http://www.mif.pg.gda.pl/homepages/ankry/man-pages/%{name}-from-www-id-%{id_version}.tar.gz
# Source9-md5:	34a69de42ec4ae8180b947f8777a3e7a
# available also as http://
Source10:	ftp://ftp.pluto.linux.it/pub/pluto/ildp/man/%{name}-it-%{it_version}.tar.xz
# Source10-md5:	869cf8ff2aa5c11b8d15d1ba7a47f4fa
# note: man-pages-it-extra-0.5.0.tar.gz is also covered by the above version
#Source11Download: http://linuxjm.osdn.jp/download.html
Source11:	http://linuxjm.osdn.jp/%{name}-ja-%{ja_version}.tar.gz
# Source11-md5:	57969415701eb835a6437bbf1e464816
Source12:	http://download.kldp.net/man/man-pages-ko/%{ko_version}/%{name}-ko-%{ko_version}.tar.gz
# Source12-md5:	e31dc6a51c02436371373dedaeeeacab
# TODO: check 20051127 in Debian/Ubuntu?
Source13:	ftp://ftp.nl.linux.org/pub/DOC-NL/manpages-nl/manpages-nl-%{nl_version}.tar.gz
# Source13-md5:	b37b0216a87db7583e88ba87031a0b4a
# TODO: PTM has been overtaken by new project at http://manpages-pl.sourceforge.net/
# http://downloads.sourceforge.net/manpages-pl/manpages-pl-%{pl_version}.tar.bz2 with pl_version=0.7
Source14:	%{name}-pl-PTM-snapshot.%{pl_version}.tar.bz2
# Source14-md5:	b9b5751fcde4c36022850d0e5a4757d3
Source15:	http://www.win.tue.nl/~aeb/ftpdocs/linux-local/manpages/tr/%{name}-pt_BR-%{pt_version}.tgz
# Source15-md5:	3f8db6dd6a7884b595e70f624ac93735
# no LDP man pages yet
Source16:	http://www.rolix.org/man/arhiva/man-pages-ro-%{ro_version}.tar.gz
# Source16-md5:	ac5b2c970a31cb721e068ff80e5bd466
# TODO: new project at: https://sourceforge.net/projects/man-pages-ru/files/, latest version man-pages-ru_4.17-2385-2385-20181124.tar.bz2
#Source17:	http://linuxshare.ru/projects/trans/manpages-ru-%{ru_version}.tar.bz2
# ASP-linux have more up-to-date manpages (but 0.98 contains some updated pages)
Source17:	http://www.mif.pg.gda.pl/homepages/ankry/man-pages/manpages-ru-asp-%{ru_asp_version}.tar.bz2
# Source17-md5:	fffb27648417c8dd551e2a4403eefc64
Source18:	http://downloads.sourceforge.net/belgeler/man-pages-tr-%{tr_version}.tar.gz
# Source18-md5:	8f322a60c80e31c34ef8979edaf68aae
Source19:	http://www.linux.org.ua/twiki/pub/Projects/ManUk/man-pages-uk_UA.alfa.tar.gz
# Source19-md5:	89576c5b51bb83c8bfa8bda794b96e21
#Source20Download: https://github.com/lidaobing/manpages-zh/releases
# also newer git snapshot available at http://www.win.tue.nl/~aeb/ftpdocs/linux-local/manpages/tr/man-pages-zh-20141004.zip
Source20:	https://github.com/lidaobing/manpages-zh/archive/v%{zh_version}/manpages-zh-%{zh_version}.tar.gz
# Source20-md5:	1bbdc4f32272df0b95146518b27bf4be
Source30:	https://www.kernel.org/pub/linux/docs/man-pages/man-pages-posix/man-pages-posix-%{posix_version}.tar.xz
# Source30-md5:	825fde78e6fddd02426ecdd50e2cbe0d
Source50:	%{name}-links.list
Source100:	%{name}-tars.list
Patch0:		%{name}-zh_fixes.patch
Patch1:		%{name}-misc.patch
Patch2:		%{name}-extra.patch
Patch3:		%{name}-tr-bash.patch
Patch4:		%{name}-misc-localized.patch
Patch5:		%{name}-cs-bash.patch
Patch10:	%{name}-extra-files.patch
URL:		https://www.kernel.org/doc/man-pages/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	rpmbuild(macros) >= 1.566
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
# for man-pages-zh
BuildRequires:	zh-autoconvert
BuildRequires:	xz
# for man-pages-tr
BuildRequires:	zlib-devel
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
Obsoletes:	man-pages-ru-asp
Obsoletes:	man-pages-uk
Obsoletes:	man-pages-zh
Obsoletes:	manpages-hu
Conflicts:	attr-devel < 2.2.0-2
Conflicts:	kbd < 1.12-9
Conflicts:	keyutils < 1.5.10
Conflicts:	libcap < 1:1.10-5
Conflicts:	lirc < 0.9.3a-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
AutoReqProv:	no

# languages of packaged man pages
# note: pt_BR is omitted here, these manuals are packaged as pt
%define	man_langs	cs da de es fi fr hu id it ja ko nl pl pt ru tr uk zh_CN zh_TW

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

%description -l de.UTF-8
Eine große Sammlung von man-Seiten über Programmier-APIs,
Dateiformate, Protokolle, usw..

- section 1: Benutzerbefehle (nur intro)
- section 2: Systemaufrufe
- section 3: libc-Aufrufe (nur intro)
- section 4: Geräte (z.B. hd, sd)
- section 5: Dateiformate und Protokolle (z.B. wtmp, /etc/passwd, nfs)
- section 6: Spiele (nur intro)
- section 7: Konventionen, Makro-Pakete, usw. (z.B. nroff, ascii)
- section 8: Systemverwaltung (nur intro)

%description -l es.UTF-8
Una larga colección de páginas de manuales cubriendo programación
APIs, formatos de archivos, protocolos, etc.

- seción 1: comandos de usuario (solamente introducción)
- seción 2: llamadas de sistema
- seción 3: llamadas libc (solamente introducción)
- seción 4: dispositivos (ej.: hd, sd)
- seción 5: formatos de archivos y protocolos (ej: wtmp, /etc/passwd,
  nfs)
- seción 6: juegos (solamente introducción)
- seción 7: convenciones, paquetes de macros, etc. (ej: nroff, ascii)
- seción 8: administración de sistema (solamente introducción)

%description -l fi.UTF-8
Kokoelma man-sivujen käännöksiä suomenkielelle. Sivuja on mukana
yhteensä 211 kpl ja ne on paketoitu 14.11.1999 mennessä valmiina
olleista sivuista. Sivut ovat osista 1 (komennot) ja 2 (pelit).

%description -l fr.UTF-8
Une large collection de pages de manuel du Project de Documentation
Linux (LDP), traduites en Français. Les pages de manuel sont
organisées en differentes sections :

- section 1: Commandes utilisateur (intro seulement)
- section 2: Appels système
- section 3: Appels de la Libc (intro seulement)
- section 4: Périphériques (par ex. hd, sd)
- section 5: Formats de fichiers et de protocoles (par ex. wtmp,
  /etc/passwd, nfs)
- section 6: Jeux (intro seulement)
- section 7: Conventions, macro packages, etc. (par ex. nroff, ascii)
- section 8: Administration système (intro seulement)

%description -l it.UTF-8
Traduzioni italiane delle pagine di manuale per Linux: questo
pacchetto include non solo quelle dell'LDP, ma anche traduzioni di
altre pagine di uso comune. ATTENZIONE: alcune pagine sono obsolete!

%description -l pl.UTF-8
Pakiet ten zawiera dużą kolekcję podręczników ekranowych (man pages),
opisujących format plików, protokoły itp.

- sekcja 1: polecenia użytkowników (tylko wstęp)
- sekcja 2: wywołania systemowe
- sekcja 3: wywołania bibliotek (tylko wstęp)
- sekcja 4: urządzenia (np., hd, sd)
- sekcja 5: format plików i protokoły (np., wtmp, /etc/passwd, nfs)
- sekcja 6: gry (tylko wstęp)
- sekcja 7: konwencje, makro-pakiety, itp. (np., nroff, ascii)
- sekcja 8: administracja systemu (tylko wstęp)

%description -l pt.UTF-8
Uma larga coleção de páginas de manuais cobrindo programação APIs,
formatos de arquivos, protocolos, etc.

- seção 1: comandos de usuário (somente introdução)
- seção 2: chamadas de sistema
- seção 3: chamadas libc (somente introdução)
- seção 4: dispositivos (ex.: hd, sd)
- seção 5: formatos de arquivos e protocolos (ex: wtmp, /etc/passwd,
  nfs)
- seção 6: jogos (somente introdução)
- seção 7: convenções, pacotes de macros, etc. (ex: nroff, ascii)
- seção 8: administração de sistema (somente introdução)

%description -l pt_BR.UTF-8
Uma larga coleção de páginas de manuais cobrindo programação APIs,
formatos de arquivos, protocolos, etc.

- seção 1: comandos de usuário (somente introdução)
- seção 2: chamadas de sistema
- seção 3: chamadas libc (somente introdução)
- seção 4: dispositivos (ex.: hd, sd)
- seção 5: formatos de arquivos e protocolos (ex: wtmp, /etc/passwd,
  nfs)
- seção 6: jogos (somente introdução)
- seção 7: convenções, pacotes de macros, etc. (ex: nroff, ascii)
- seção 8: administração de sistema (somente introdução)

%description -l ru.UTF-8
Небольшая коллекция страниц руководства из Проекта Документации на
Линукс. Страницы руководства организованы следующим образом:

- секция 1: команд пользователя (только введение)
- секция 2: системные вызовы
- секция 3: функции библиотеки языка C (только введение)
- секция 4: устройства (например, hd, sd)
- секция 5: форматы файлов и протоколы (например, wtmp, /etc/passwd,
  nfs)
- секция 6: игры (только введение)
- секция 7: соглашения, макро-пакеты, и т. п. (например, nroff, ascii)
- секция 8: утилиты администратора (только введение)

%description -l tr.UTF-8
Programlama arayüzlerini, dosya formatlarını, protokolleri vs.
kapsayan, geniş bir kılavuz sayfaları derlemesi.

%description -l uk.UTF-8
Великий набір сторінок мануалу (документації) з Linux Documentation
Project (LDP). Сторінки організовані у такі секції: Секція 1, команди
користувача (тільки вступ); Секція 2, системні виклики; Секція 3,
виклики libc; Секція 4, пристрої (наприклад, hd, sd); Секція 5,
формати файлів та протоколи (наприклад, wtmp, /etc/passwd, nfs);
Секція 6, ігри (тільки вступ); Секція 7, угоди, макропакети і т.і.
(наприклад, nroff, ascii); Секція 8, системне адміністрування (тільки
вступ).

%package posix
Summary:	POSIX manual pages from the Linux Documentation Project
Summary(de.UTF-8):	POSIX-man-Seiten vom Linux Documentation Project
Summary(pl.UTF-8):	Podręczniki systemowe z Linux Documentation Project dotyczące POSIX
Group:		Documentation

%description posix
Part of POSIX 1003.1-2003 in man pages format.

%description posix -l pl.UTF-8
Fragmenty POSIX 1003.1-2003 w postaci stron podręcznika systemowego.

%prep
%setup -q -c -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a30
%patch0 -p1 -d manpages-zh-%{zh_version}
%patch3 -p1 -d man-pages-tr-%{tr_version}
%patch5 -p1 -d man-pages-cs-%{cs_version}
# man-pages-extra
%patch10 -p0
%patch2 -p0 -d man-pages-extra
install -d man-pages-extra/C
%{__mv} man-pages-extra/man* man-pages-extra/C

# prepare somehow unified source trees
install -d src
%{__mv} man-pages-%{version} src/C
%{__mv} man-pages-posix-%{posix_version}/man*p src/C
%{__mv} man-pages-cs-%{cs_version} src/cs
%{__mv} manpages-da-%{da_version} src/da
%{__mv} manpages-de-%{de_version} src/de
%{__mv} man-pages-es-%{es_version} src/es
%{__mv} manpages-fi src/fi
%{__mv} fr src/fr
%{__mv} manpages-hu-%{hu_version}.orig/usr/share/man/hu src/hu
install -d src/id/man{1,8}
%{__mv} man-pages-it-%{it_version} src/it
%{__mv} man-pages-ja-%{ja_version} src/ja
install -d src/ko
tar xzf %{SOURCE12} -C src/ko
%{__mv} manpages-nl-%{nl_version} src/nl
%{__mv} pl_PL src/pl
%{__mv} man-pages-%{pt_version}-pt_BR src/pt_BR
%{__mv} man-ro src/ro
%{__mv} manpages-ru-asp-%{ru_asp_version} src/ru
%{__mv} man-pages-tr-%{tr_version} src/tr
%{__mv} man-pages-uk_UA.alfa src/uk
%{__mv} manpages-zh-%{zh_version} src/zh

# extra so links (via man-pages-extra)
while read LINE ; do
	if echo "$LINE" | grep -q '^#' ; then
		continue
	fi
	set -- $LINE
	install -d man-pages-extra/${1}/$(dirname $2)
	if [ -f man-pages-extra/${1}/${2} ]; then
		echo "man-pages-extra/${1}/${2} already exists!"
		exit 1
	fi
	echo ".so $3" >>man-pages-extra/${1}/${2}
	# special case for zh
	if [ "$1" = "zh_CN" ]; then
		zhmandir="src/zh/src/$(dirname "$2")"
		makefile="$zhmandir/manpages"
		if [ ! -f "$zhmandir/.init.mark" ]; then
			# allow continuation in next line
			%{__sed} -i -e 's/\(\.[1-8]\)$/\1 \\/' "$makefile"
			touch "$zhmandir/.init.mark"
		fi
		printf " %s" "$(basename "$2")" >> "$makefile"
	fi
done < %{SOURCE50}

# unify trees for easier processing (where possible)

# da: add man1 subdir
install -d src/da/man1
%{__mv} src/da/*.1 src/da/man1

# es: merge in "extra" pages
# skip pages already in main es
%{__rm} man-pages-es-extra-%{es_extra_version}/man3/dl*.3
%{__rm} man-pages-es-extra-%{es_extra_version}/man5/{acct,host.conf,resolv.conf,resolver}.5
%{__rm} man-pages-es-extra-%{es_extra_version}/man8/ld.so.8
for f in 1 2 4 5 6 7 8 ; do
	mv -i man-pages-es-extra-%{es_extra_version}/man${f}/* src/es/man${f}
done

# it: merge per-package trees
%{__mv} src/it/man-pages/man? src/it
for f in 1 4 5 8 9 ; do
	mv -i src/it/*/man${f}/* src/it/man${f}
done

# ja: merge per-package trees
%{__mv} src/ja/manual/LDP_man-pages/man* src/ja
# duplicates of LDP man pages
%{__rm} -r src/ja/manual/{gnumaniak,ld.so,modutils/man2,glibc-linuxthreads/man3,man/man1/{apropos,man,whatis}.1,netkit/{man3/{daemon,err,login}.3,man5/ftpusers.5},bind/{man5/resolver.5,man7/mailaddr.7}}
# shadow manuals already in shadow package
%{__rm} -r src/ja/manual/shadow
# dhcp 3 not dhcp2
%{__rm} -r src/ja/manual/dhcp2
# nfs-utils not nfs-server
%{__rm} -r src/ja/manual/nfs-server
# ypbind-mt not ypbind
%{__rm} -r src/ja/manual/ypbind
# we use: net-tools/hostname, util-linux/{kill,last,lastb,write}, SysVinit/{mesg,wall,halt,reboot,shutdown}, textutils/od, quota/rquotad
%{__rm} src/ja/manual/{GNU_sh-utils/man1/hostname.1,SysVinit/man1/{last,lastb}.1,procps/man1/kill.1,util-linux/man1/{mesg,wall}.1,netkit/man1/write.1,nfs-utils/man8/rquotad.8}
# following modutils changes
for f in src/ja/manual/modutils/man8/{depmod,insmod,lsmod,modinfo,modprobe,rmmod} ; do
	%{__mv} ${f}.8 ${f}.modutils.8
done
# avoid filename conflict
%{__mv} src/ja/manual/netkit/man8/ftpd.{8,8n}
# remove files existing in main man-pages tarball
# note: (should we keep those from main tarball or ja tarball?)
%{__rm} src/ja/manual/GNU_fileutils/man1/{chgrp,chmod,chown,cp,dd,df,du,install,ln,ls,mkdir,mkfifo,mknod,mv,rm,rmdir,touch}.1
%{__rm} src/ja/manual/GNU_sh-utils/man1/{basename,chroot,date,dirname,echo,env,expr,false,groups,hostid,id,logname,nice,nohup,pathchk,printenv,printf,pwd,sleep,stty,su,tee,test,true,tty,uname,users,who,whoami,yes}.1
%{__rm} src/ja/manual/GNU_textutils/man1/{cat,cksum,comm,csplit,cut,expand,fmt,fold,head,join,md5sum,nl,od,paste,pr,sort,split,sum,tac,tail,tr,unexpand,uniq,wc}.1
%{__rm} src/ja/manual/lpr-linux/man1/{lpq,lpr,lprm}.1
%{__rm} src/ja/manual/net-tools/man1/hostname.1
%{__rm} src/ja/manual/netatalk/man1/timeout.1
%{__rm} src/ja/manual/procps/man1/uptime.1
%{__rm} src/ja/manual/util-linux/man1/kill.1
%{__rm} src/ja/manual/bind/man7/hostname.7
%{__rm} src/ja/manual/cups/man8/lpc.8
for f in 1 3 4 5 6 7 8 ; do
	mv -i src/ja/manual/*/man${f}/* src/ja/man${f}
done

# zh_CN: cleanup must be done after build (in build stage)

# individual man pages fixes

# unify name
%{__mv} src/de/man7/{iso_8859_1,iso_8859-1}.7
%{__mv} src/es/man4/magic.4 src/es/man5/magic.5
%{__mv} src/es/man8/sync.8 src/es/man1/sync.1
%{__mv} src/hu/man1/gpm.1 src/hu/man8/gpm.8
# man1/sync.1 already exists
%{__rm} src/hu/man8/sync.8
%undos src/it/man7/{iso-8859-2,iso_8859_2}.7
%{__mv} src/ja/man4/magic.4 src/ja/man5/magic.5
%{__mv} src/ja/man8/nslookup.8 src/ja/man1/nslookup.1
%{__mv} src/ko/man8/sync.8 src/ko/man1/sync.1
# filename typo?
%{__mv} src/pl/man5/{at_acces,at_access}.5
# man1/sync.1 already exists
%{__rm} src/pl/man8/sync.8
%{__mv} src/pt_BR/man8/sync.8 src/pt_BR/man1/sync.1
%{__mv} src/ru/man8/sync.8 src/ru/man1/sync.1
# zh: handler later (after build)

%patch1 -p1 -d src/C
%patch4 -p1 -d src

# patching creates backups
find . '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -rf

# merge our "extra" tarball

# apply man-pages-extra, preventing overwriting of already existing man pages
for d in man-pages-extra/C/man* ; do
	mv -i $d/*.* src/C/${d#man-pages-extra/C/}
done
# note: cs and zh_CN are omitted here and processed in separate special pass
for d in man-pages-extra/{de,es,fi,fr,hu,id,it,ja,ko,nl,pl,pt_BR,ru}/man* ; do
	mv -i $d/*.* src/${d#man-pages-extra/}
done
for d in man-pages-extra/zh_CN/man* ; do
	mv -i $d/*.* src/zh/src/${d#man-pages-extra/zh_CN/}
done

ln -sf pt_BR src/pt

# remove man pages existing in other packages

# time
%{__rm} src/C/man1/time.1
# ftp servers
%{__rm} src/C/man5/ftpusers.5

%build
# some man-pages require build step

# cs: prepare man pages and apply extra
LANG=en_GB.UTF-8 \
%{__make} -C src/cs latest
%{__mv} src/cs/latest/man* src/cs
rmdir src/cs/latest
for d in man-pages-extra/cs/man* ; do
	mv -i $d/*.* src/${d#man-pages-extra/}
done

# tr: make man pages from XML (note: compiles some utility)
%{__make} -C src/tr/source
find src/tr/tr -name '*.gz' | xargs gzip -d
%{__mv} src/tr/tr/man* src/tr

# zh: prepare zh_CN and zh_TW
cd src/zh
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}
cd ../..
for l in zh_CN zh_TW ; do
install -d src/${l}
for d in man{1,2,3,4,5,6,7,8,n} ; do
ln -snf ../zh/src/${d}/${l} src/${l}/${d}
done
done
# zh_*: man1/sync.1 already exists
%{__rm} src/zh_CN/man8/sync.8
%{__rm} src/zh_TW/man8/sync.8

# per-package lists / tarballs production
package=NONE
while read line ; do
	if echo $line | grep -q '^\[.\+\]$' ; then
		package=`echo $line | sed -e 's/^\[//;s/\]$//;'`
	elif ! echo $line | grep -q '^#' ; then
		if [ -f "src/C/$line" ]; then
			echo "$line" >> ${package}-man.list
		fi
		for l in %{man_langs} ; do
			if [ -f "src/$l/$line" ]; then
				echo "$l/$line" >> ${package}-man.list
			fi
		done
	fi
done < %{SOURCE100}
%if %{with tars}
rm -rf tarsrc tar
install -d tarsrc tar
cd tarsrc
ln -snf ../src/[!C]* ../src/C/man* ../man-pages-extra/README.*-pages .
cd ..
for l in *-man.list ; do
	t=`basename $l .list`
	if [ -f tarsrc/README.${t}-pages ]; then
		echo "README.${t}-pages" >> "$l"
	fi
	tar chJf tar/${t}-pages.tar.xz -C tarsrc --files-from "$l"
done
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,2,3,4,5,6,7,8,0p,1p,3p}

# install C man pages
for n in src/C/man{1,2,3,4,5,6,7,8,0p,1p,3p}/*; do
	bn=${n#src/C/}
	install -m644 $n $RPM_BUILD_ROOT%{_mandir}/$bn
done
# drop man pages packaged separately
grep '^man' glibc-man.list | sed -e "s,^,$RPM_BUILD_ROOT%{_mandir}/," | xargs -r %{__rm}
# rpcbind, formerly glibc
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man8/rpcinfo.8
# gawk
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/{gawk,igawk}.1
# libaio
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/{aio_init,lio_listio}.3
# shadow (but not pwdutils!); shadow(5) is missing in pwdutils too
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man5/passwd.5

# install localized man pages, only for installed C man pages
for l in %{man_langs} ; do
	install -d $RPM_BUILD_ROOT%{_mandir}/$l/man{1,2,3,4,5,6,7,8}
	for n in $RPM_BUILD_ROOT%{_mandir}/man{1,2,3,4,5,6,7,8}/*; do
		bn=$(basename $(dirname $n))/$(basename $n)
		if [ -f src/$l/$bn ]; then
			install -m644 src/$l/$bn $RPM_BUILD_ROOT%{_mandir}/$l/$bn
		fi
	done
done

# files with just .so links pointing to non-existing man pages
# modules.2
%{__rm} $RPM_BUILD_ROOT%{_mandir}/de/man2/{create_module,delete_module,get_kernel_syms,init_module}.2
# obsolete.2
%{__rm} $RPM_BUILD_ROOT%{_mandir}/{cs,de,es,ko,nl,pl,pt,ru}/man2/{oldfstat,oldlstat,oldolduname,oldstat,olduname}.2
# undocumented.7 (exists in es, but not installed because it's not in C manuals)
%{__rm} $RPM_BUILD_ROOT%{_mandir}/es/man5/networks.5
# clock_getres.3 (packaged in glibc, but these links exist only in fr manuals, not C)
%{__rm} $RPM_BUILD_ROOT%{_mandir}/fr/man2/{clock_getres,clock_gettime,clock_settime}.2
# undocumented.7
%{__rm} $RPM_BUILD_ROOT%{_mandir}/ru/man5/networks.5
# statfs.2
%{__rm} $RPM_BUILD_ROOT%{_mandir}/pl/man2/fstatfs.2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_mandir}/man1/*.1*
%{_mandir}/man2/*.2*
%{_mandir}/man3/*.3*
%{_mandir}/man4/*.4*
%{_mandir}/man5/*.5*
%{_mandir}/man6/*.6*
%{_mandir}/man7/*.7*
%{_mandir}/man8/*.8*
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
# packaged as plain pt for now
#%lang(pt_BR) %{_mandir}/pt_BR/man*/*
%lang(ru) %{_mandir}/ru/man*/*
%lang(tr) %{_mandir}/tr/man*/*
%lang(uk) %{_mandir}/uk/man*/*
%lang(zh_CN) %{_mandir}/zh_CN/man*/*
%lang(zh_TW) %{_mandir}/zh_TW/man*/*

%files posix
%defattr(644,root,root,755)
%dir %{_mandir}/man0p
%{_mandir}/man0p/*.0p*
%dir %{_mandir}/man1p
%{_mandir}/man1p/*.1p*
%dir %{_mandir}/man3p
%{_mandir}/man3p/*.3p*
