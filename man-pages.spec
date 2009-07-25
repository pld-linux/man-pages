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
Version:	3.22
Release:	1
License:	distributable
Group:		Documentation
%define		cs_version		0.16
%define		da_version		0.1.1
%define		de_version		0.4
%define		es_version		1.55
%define		es_extra_version	0.8a
%define		fi_version		0.2
%define		fr_version		2.39.0
%define		hu_version		20010119
%define		id_version		20011116
%define		it_version		2.34
%define		ja_version		20070615
%define		ko_version		20050219
%define		nl_version		0.13.3
%define		pl_version		20051105
%define		pt_version		1.39
%define		ro_version		0.2
#%%define	ru_version		0.98
%define		ru_asp_version		1.4
%define		tr_version		1.0.3
%define		zh_version		1.5
Source0:	http://www.kernel.org/pub/linux/docs/manpages/%{name}-%{version}.tar.gz
# Source0-md5:	409e7325188d8734a63c823fd58c7dce
Source1:	ftp://ftp.linux.cz/pub/localization/linux/czman/%{name}-cs-%{cs_version}.tar.gz
# Source1-md5:	e8036794c1762804f2e242cc5b52001e
# there is no LDP man page here, yet - but include it in sources for completeness
Source2:	http://www.sslug.dk/locale/man-sider/manpages-da-%{da_version}.tar.gz
# Source2-md5:	d12ba0481d824c28a8b7d6b73e20d7c0
Source3:	http://www.infodrom.org/projects/manpages-de/download/manpages-de-%{de_version}.tar.gz
# Source3-md5:	6a2a1cd24b0bd61c4ab384324e707a95
Source4:	http://www.ditec.um.es/~piernas/manpages-es/%{name}-es-%{es_version}.tar.bz2
# Source4-md5:	b71f701dcae827f2f5e4e848c66321fc
Source5:	http://www.ditec.um.es/~piernas/manpages-es/%{name}-es-extra-%{es_extra_version}.tar.gz
# Source5-md5:	5827f41f77658df17f550b7f8e831432
# extracted from http://www.ftp.funet.fi/index/sotlinux/bestlinux-2000R3/BL_2000_R3_FINAL/update/Finnish/man-pages-fi-0.2-1.src.rpm
# (despite archive filename it's 0.2 version)
Source6:	man-fi-0.1.tar.bz2
# Source6-md5:	bb266d3797cdf71bfbe1da190196f455
Source7:	http://manpagesfr.free.fr/download/man-pages-fr-%{fr_version}.tar.bz2
# Source7-md5:	7e9ecdd134703e8172107124f1f3fec4
#Source8:	http://download.uhulinux.hu/sources/man-pages-hu/man_hu_%{hu_version}.tar.gz (older)
Source8:	http://ftp.debian.org/debian/pool/main/m/manpages-hu/manpages-hu_%{hu_version}.orig.tar.gz
# Source8-md5:	742b682c5237a1e370b28f363826b2d5
# there is no LDP man page here, yet, but included for completeness
# based on http://nakula.rvs.uni-bielefeld.de/made/my_project/ManPage/ (dead now)
Source9:	http://www.mif.pg.gda.pl/homepages/ankry/man-pages/man-pages-from-www-id-%{id_version}.tar.gz
# Source9-md5:	34a69de42ec4ae8180b947f8777a3e7a
# available also as http://
Source10:	ftp://ftp.pluto.linux.it/pub/pluto/ildp/man/%{name}-it-%{it_version}.tar.gz
# Source10-md5:	259868d64ee589828b4cc43e8769507b
Source11:	http://www.linux.or.jp/JM/%{name}-ja-%{ja_version}.tar.gz
# Source11-md5:	d0079890039b10ef88f1e635ce59d859
Source12:	http://download.kldp.net/man/man-pages-ko/%{ko_version}/%{name}-ko-%{ko_version}.tar.gz
# Source12-md5:	e31dc6a51c02436371373dedaeeeacab
Source13:	ftp://ftp.nl.linux.org/pub/DOC-NL/manpages-nl/manpages-nl-%{nl_version}.tar.gz
# Source13-md5:	b37b0216a87db7583e88ba87031a0b4a
# currently at http://ptm.linux.pl/ (latest http://ptm.linux.pl/man-PL28-06-2007.tar.gz)
# there is also a fork at http://ptm.berlios.de/, but seems to be stalled just after it started
#Source14:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/PTM-snapshots/%{name}-pl-PTM-snapshot.%{pl_version}.tar.bz2
Source14:	%{name}-pl-PTM-snapshot.%{pl_version}.tar.bz2
# Source14-md5:	b9b5751fcde4c36022850d0e5a4757d3
Source15:	ftp://ftp.win.tue.nl/pub/home/aeb/linux-local/manpages/tr/%{name}-pt_BR-%{pt_version}.tgz
# Source15-md5:	3f8db6dd6a7884b595e70f624ac93735
# no LDP man pages yet
Source16:	http://www.rolix.org/man/arhiva/man-pages-ro-%{ro_version}.tar.gz
# Source16-md5:	ac5b2c970a31cb721e068ff80e5bd466
#Source17:	http://www.linuxshare.ru/projects/trans/manpages-ru-%{ru_version}.tar.bz2
# ASP-linux have more up-to-date manpages (but 0.98 contains some updated pages)
Source17:	http://www.mif.pg.gda.pl/homepages/ankry/man-pages/manpages-ru-asp-%{ru_asp_version}.tar.bz2
# Source17-md5:	fffb27648417c8dd551e2a4403eefc64
Source18:	http://dl.sourceforge.net/belgeler/man-pages-tr-%{tr_version}.tar.gz
# Source18-md5:	903c7b22a87961842dec8f4f1adeeaf3
Source19:	http://www.linux.org.ua/twiki/pub/Projects/ManUk/man-pages-uk_UA.alfa.tar.gz
# Source19-md5:	89576c5b51bb83c8bfa8bda794b96e21
#Source20:	http://cmpp.linuxforum.net/download/man-pages-zh_CN-%{zh_version}.tar.gz
Source20:	http://download.sf.linuxforum.net/cmpp/man-pages-zh_CN-%{zh_version}.tar.gz
# Source20-md5:	edfe517621579520cf7451088ab126ea
Source30:	http://www.kernel.org/pub/linux/docs/man-pages/man-pages-posix/man-pages-posix-2003-a.tar.bz2
# Source30-md5:	7c78aff03c0a6767ba483d34f19e4b09
Source50:	%{name}-extra.tar.bz2
# NoSource50-md5:	15d763c5221088dcb15ba8ae95f6d239
Source100:	%{name}-tars.list
Patch0:		%{name}-localtime.patch
Patch1:		%{name}-zh_fixes.patch
Patch2:		%{name}-misc.patch
Patch3:		%{name}-extra.patch
URL:		http://www.kernel.org/doc/man-pages/
BuildRequires:	sed >= 4.0
AutoReqProv:	no
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
Conflicts:	kbd < 1.12-9
Conflicts:	libcap < 1:1.10-5
BuildArch:	noarch
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
%setup -q -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a30
%patch0 -p1
%patch1 -p0

mv man-pages-posix-*/man*p .

mkdir ko
tar xzf %{SOURCE12} -C ko

find man-pages-tr-%{tr_version} -name '*.gz' | xargs gzip -d

# unify trees for easier processing
mv -f man-pages-%{pt_version}-pt_BR pt_BR
mv -f man-pages-cs-%{cs_version} cs
# replace symlinks by .so pointers
for l in `find cs -type l` ; do
	t=`readlink "$l"`
	rm -f "$l"
	echo ".so $t" > "$l"
done
mv -f manpages-da-%{da_version} da
install -d da/man1
mv -f da/*.1 da/man1
mv -f manpages-de-%{de_version} de
mv -f man-pages-es-%{es_version} es
# already in main es
rm -f man-pages-es-extra-%{es_extra_version}/man3/dl*.3
rm -f man-pages-es-extra-%{es_extra_version}/man5/{acct,host.conf,resolv.conf,resolver}.5
rm -f man-pages-es-extra-%{es_extra_version}/man8/ld.so.8
for f in 1 2 4 5 6 7 8 ; do
	mv -i man-pages-es-extra-%{es_extra_version}/man${f}/* es/man${f}
done
mv -f manpages-fi fi
mv -f man-pages-fr-%{fr_version} fr
mv -f manpages-hu-%{hu_version}.orig/usr/share/man/hu hu
mv -f man-pages-it-%{it_version} it
mv -f man-pages-ja-%{ja_version}/manual/LDP_man-pages ja
# duplicates of LDP man pages
rm -rf man-pages-ja-%{ja_version}/manual/{gnumaniak,ld.so,modutils/man2,glibc-linuxthreads/man3,netkit/{man3/{daemon,err,login}.3,man5/ftpusers.5},bind/{man5/resolver.5,man7/mailaddr.7},util-linux/man1/tailf.1}
# shadow manuals already in shadow package
rm -rf man-pages-ja-%{ja_version}/manual/shadow
# we have man not man-db
rm -rf man-pages-ja-%{ja_version}/manual/man-db
# dhcp 3 not dhcp2
rm -rf man-pages-ja-%{ja_version}/manual/dhcp2
# nfs-utils not nfs-server
rm -rf man-pages-ja-%{ja_version}/manual/nfs-server
# ypbind-mt not ypbind
rm -rf man-pages-ja-%{ja_version}/manual/ypbind
# we use: net-tools/hostname, util-linux/{kill,write}, SysVinit/{last,mesg,wall,halt,reboot,shutdown}, textutils/od, quota/rquotad
rm -f man-pages-ja-%{ja_version}/manual/{GNU_sh-utils/man1/hostname.1,procps/man1/kill.1,util-linux/man1/{last,mesg,od,wall}.1,netkit/man1/write.1,nfs-utils/man8/rquotad.8,util-linux/man8/{halt,reboot,shutdown}.8}
# following modutils changes
for f in man-pages-ja-%{ja_version}/manual/modutils/man8/{depmod,insmod,lsmod,modinfo,modprobe,rmmod} ; do
	mv -f ${f}.8 ${f}.modutils.8
done
# avoid filename conflict
mv -f man-pages-ja-%{ja_version}/manual/netkit/man8/ftpd.{8,8n}
for f in 1 3 4 5 6 7 8 ; do
	mv -i man-pages-ja-%{ja_version}/manual/*/man${f}/* ja/man${f}
done
mv -f manpages-nl-%{nl_version} nl
mv -f pl_PL pl
mv -f man-ro ro
mv -f manpages-ru-asp-%{ru_asp_version} ru
mv -f man-pages-tr-%{tr_version}/tr tr
mv -f man-pages-uk_UA.alfa uk
mv -f man-pages-zh_CN-%{zh_version}/src zh_CN
find zh_CN -name CVS -o -name '*.orig' -o -name '*~' | xargs rm -rf
# would go in big5 or gb18030, but not gb2312
rm -f zh_CN/man1/perltw.1
# would go in gb18030, but not gb2312
rm -f zh_CN/man8/{chat,printcap}.8

# these man-pages are in UTF-8
for f in zh_CN/man?/* ; do
	iconv -f UTF8 -t GB2312 $f > ${f}.tmp
	mv -f ${f}.tmp $f
done

mv -f cs/man8/at.1 cs/man1
# unify name
mv -f de/man7/{iso_8859_1,iso_8859-1}.7
mv -f es/man4/magic.4 es/man5/magic.5
mv -f es/man8/sync.8 es/man1/sync.1
mv -f fr/man8/sync.8 fr/man1/sync.1
mv -f hu/man1/gpm.1 hu/man8/gpm.8
# man1/sync.1 already exists
rm -f hu/man8/sync.8
# unify name + fix infinite loop
mv -f it/man7/{iso_8859-1,tmp}.7
mv -f it/man7/{iso_8859_1,iso_8859-1}.7
mv -f it/man7/{tmp,iso_8859_1}.7
# non-existing target
rm -f it/man7/latin.2
mv -f ja/man4/magic.4 ja/man5/magic.5
mv -f ja/man8/nslookup.8 ja/man1/nslookup.1
mv -f ja/man8/sync.8 ja/man1/sync.1
mv -f ko/man8/sync.8 ko/man1/sync.1
# filename typo?
mv -f pl/man5/{at_acces,at_access}.5
# man1/sync.1 already exists
rm -f pl/man8/sync.8
mv -f pt_BR/man8/sync.8 pt_BR/man1/sync.1
mv -f ru/man8/sync.8 ru/man1/sync.1
# man1/sync.1 already exists
rm -f zh_CN/man8/sync.8

%patch2 -p1

bzip2 -dc %{SOURCE50} | tar xf -
%patch3 -p0

# patching creates backups
find . '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -rf

# cleanup
rm -f man1/COPYING
rm -f man*/README*

for n in man{1,2,3,4,5,6,7,8,0p,1p,3p}/* */man{1,2,3,4,5,6,7,8,9}/* ; do
	x=`echo $n | sed -e 's,^.*man\([^/]\)/.*,\1,'`
	if head -n 1 $n| grep "^\.so man$x/" >/dev/null 2>&1 ; then
		sed -i -e 's,\.so man./,.so ,' $n
	fi
done

ln -sf pt_BR pt

# these belong to coreutils (sync is man1 BTW)
rm -f man1/{chgrp,chmod,chown,cp,dd,df,dircolors,du,install,diff}.1
rm -f man1/{ln,ls,mkdir,mkfifo,mknod,mv,rm,rmdir,touch,dir,vdir}.1
rm -f man8/sync.8
# time
rm -f man1/time.1
# ftp servers
rm -f man5/ftpusers.5

%if %{with tars}
package=NONE
while read line ; do
	if echo $line | grep -q '^\[.\+\]$' ; then
		package=`echo $line | sed -e 's/^\[//;s/\]$//;'`
	else
		if [ -f "$line" ]; then
			echo "$line" >> ${package}-man.list
		fi
		# omit pt_BR here, package them as pt
		for l in cs da de es fi fr hu id it ja ko nl pl pt ru tr uk zh_CN ; do
			if [ -f "$l/$line" ]; then
				echo "$l/$line" >> ${package}-man.list
			fi
		done
	fi
done < %{SOURCE100}
for l in *-man.list ; do
	t=`basename $l .list`
	if [ -f README.${t}-pages ]; then
		echo "README.${t}-pages" >> "$l"
	fi
	tar cjf %{_sourcedir}/${t}-pages.tar.bz2 --files-from "$l"
	grep '^man' "$l" | xargs rm -f
done
%else
# glibc
find man3 -type f | grep -v 'intro\.3' | xargs rm -f
rm -f man1/ldd.1
rm -f man1/rpcgen.1
rm -f man5/{locale,nscd.conf,nsswitch.conf,tzfile}.5
rm -f man7/{ascii,charsets,iso*,koi8-r,latin*,locale,unicode,utf*}.7
rm -f man8/{ld.so,ldconfig,nscd,tzselect,zdump,zic}.8
rm -f */man1/ldd.1 */man8/sln.8 */man1/iconv.1
rm -f {ja,ru}/man1/rpcgen.1
%endif

# shadow (but not pwdutils!); shadow(5) is missing in pwdutils too
rm -f man5/passwd.5

# rpcbind, formerly glibc
rm -f man8/rpcinfo.8

rm -f man1/{i,}gawk.1
rm -f man1/{i,}gawk.1
rm -f {it,ja,pl}/man1/{i,}gawk.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,2,3,4,5,6,7,8,0p,1p,3p}

for n in man{1,2,3,4,5,6,7,8,0p,1p,3p}/*; do
	install $n $RPM_BUILD_ROOT%{_mandir}/$n
done

# omit pt_BR here, package them as pt
for l in cs da de es fi fr hu id it ja ko nl pl pt ru tr uk zh_CN ; do
	install -d $RPM_BUILD_ROOT%{_mandir}/$l/man{1,2,3,4,5,6,7,8}
	for n in man{1,2,3,4,5,6,7,8}/*; do
		if [ -f $l/$n ]; then
			install $l/$n $RPM_BUILD_ROOT%{_mandir}/$l/$n
		fi
	done
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_mandir}/man?/*
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
#%lang(pt_BR) %{_mandir}/pt_BR/man*/*
%lang(ru) %{_mandir}/ru/man*/*
%lang(tr) %{_mandir}/tr/man*/*
%lang(uk) %{_mandir}/uk/man*/*
%lang(zh_CN) %{_mandir}/zh_CN/man*/*

%files posix
%defattr(644,root,root,755)
%dir %{_mandir}/man?p
%{_mandir}/man?p/*
