#
# Conditional build:
%bcond_with	tars	# generate man-pages tars for other packages [not done yet]
#
Summary:	System manual pages from the Linux Documentation Project
Summary(de):	System-man-Seiten vom Linux Documentation Project
Summary(es):	P·ginas de manual, del Proyecto de DocumentaciÛn del Linux (LDP)
Summary(fi):	Suomenkieliset man-sivut
Summary(fr):	Pages man systËme du Projet de Documentation Linux
Summary(it):	Pagine di manuale
Summary(pl):	PodrÍczniki systemowe z Linux Documentation Project
Summary(pt):	P·ginas de manual, do Projeto de DocumentaÁ„o do Linux (LDP)
Summary(pt_BR):	P·ginas de manual, do Projeto de DocumentaÁ„o do Linux (LDP)
Summary(ru):	Û‘“¡Œ…√Ÿ “’Àœ◊œƒ”‘◊¡ …⁄ “œ≈À‘¡ ‰œÀ’Õ≈Œ‘¡√…… Œ¡ Ï…Œ’À”
Summary(tr):	Linux Belgeleme Projesinin sistem k˝lavuz sayfalar˝
Summary(uk):	Û‘œ“¶ŒÀ… Õ¡Œ’¡Ã’ (man) ⁄ Linux Documentation Project
Name:		man-pages
Version:	1.65
Release:	1
License:	distributable
Group:		Documentation
%define		cs_version		0.16
%define		da_version		0.1.1
%define		de_version		0.4
%define		es_version		1.28
%define		es_extra_version	0.8a
%define		fi_version		0.1
%define		fr_base_version		1.58
%define		fr_version		%{fr_base_version}.0
%define		hu_version		2001_01_05
%define		id_version		20011116
%define		it_version		0.3.4
%define		ja_version		20040115
%define		ko_version		20010901
%define		nl_version		0.13.3
%define		pl_version		20040119
%define		pt_version		1.39
%define		ru_version		0.7
%define		uk_version		0.1.1
%define		zh_version		1.4
Source0:	ftp://ftp.win.tue.nl/pub/home/aeb/linux-local/manpages/%{name}-%{version}.tar.gz
# Source0-md5:	b841b98513f57d0fb5aa279570a852df
#
# Source1:	ftp://ftp.muni.cz/pub/linux/people/petr_kolar/localization/man-pages-cs/%{name}-cs-%{cs_version}.tar.gz
Source1:	ftp://ftp.linux.cz/pub/localization/linux/czman/%{name}-cs-%{cs_version}.tar.gz
# Source1-md5:	e8036794c1762804f2e242cc5b52001e
#
# there is no LDP man page here, yet.
# Source2:	http://www.sslug.dk/locale/man-sider/manpages-da-%{da_version}.tar.gz
Source3:	http://www.infodrom.org/projects/manpages-de/download/manpages-de-%{de_version}.tar.gz
# Source3-md5:	6a2a1cd24b0bd61c4ab384324e707a95
Source4:	http://www.ditec.um.es/~piernas/manpages-es/%{name}-es-%{es_version}.tar.gz
# Source4-md5:	b58b76cdd2b2174ba216fa30e5d83518
Source5:	http://www.ditec.um.es/~piernas/manpages-es/%{name}-es-extra-%{es_extra_version}.tar.gz
# Source5-md5:	5827f41f77658df17f550b7f8e831432
# extracted from http://developer.bestlinux.net/man-fi/usr/man/RPMS/%{name}-fi-%{fi_version}-4.src.rpm
Source6:	http://www.mif.pg.gda.pl/homepages/ankry/man-pages/man-fi-%{fi_version}.tar.bz2
# Source6-md5:	53dcf98b573c6e00c45eb91affca0a2e
# Source7:	ftp://ftp.lip6.fr/pub/linux/french/docs/man-fr-%{fr_version}.tar.gz
Source7:	http://perso.club-internet.fr/ccb/man/man-fr-%{fr_version}.tar.bz2
# Source7-md5:	50c82c2114ccca1dcb691f4122b7b4ff
#Source8:	http://www.kde.hu/mlp/man/man_hu_%{hu_version}.tar.gz
Source8:	http://www.mif.pg.gda.pl/homepages/ankry/man-pages/man_hu_%{hu_version}.tar.gz
# Source8-md5:	8b94f02287672c5a0601c1ad422a8e07
#
# there is no LDP man page here, yet.
# based on http://nakula.rvs.uni-bielefeld.de/made/my_project/ManPage/
# Source9:	man-pages-from-www-id-%{id_version}.tar.gz
# available also as http://
Source10:	ftp://ftp.pluto.linux.it/pub/pluto/ildp/man/%{name}-it-%{it_version}.tar.gz
# Source10-md5:	4e072cafbd196654c925ff0a0dca2c8f
Source11:	http://www.linux.or.jp/JM/%{name}-ja-%{ja_version}.tar.gz
# Source11-md5:	6590d539e1da253c8cd6784041768414
#
# Source12:	ftp://metalab.unc.edu/pub/Linux/docs/LDP/man-pages/%{name}-ko-%{ko_version}.tar.gz
Source12:	http://download.kldp.net/man/%{name}-ko-%{ko_version}.tar.gz
# Source12-md5:	e73c7999af103208e5497f939de764ca
Source13:	ftp://ftp.nl.linux.org/pub/DOC-NL/manpages-nl/manpages-nl-%{nl_version}.tar.gz
# Source13-md5:	b37b0216a87db7583e88ba87031a0b4a
#Source14:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/PTM-snapshots/%{name}-pl-PTM-snapshot.%{pl_version}.tar.bz2
Source14:	%{name}-pl-PTM-snapshot.%{pl_version}.tar.bz2
# Source14-md5:	f2f4c62520c11d3cf909b571954fef0d
Source15:	ftp://ftp.win.tue.nl/pub/home/aeb/linux-local/manpages/tr/%{name}-%{pt_version}-pt_BR.tgz
# Source15-md5:	3f8db6dd6a7884b595e70f624ac93735
Source16:	http://alexm.here.ru/manpages-ru/download/manpages-ru-%{ru_version}.tar.gz
# Source16-md5:	bfd5a8f20a12b994e19cfca0c4a21249
#
# from ASP Linux
Source17:	http://www.mif.pg.gda.pl/homepages/ankry/man-pages/man-pages-uk-%{uk_version}.tar.bz2
# Source17-md5:	a4f11eb6cdd2af4d57b967de868eb7fd
Source18:	http://cmpp.linuxforum.net/download/man-pages-zh_CN-%{zh_version}.tar.gz
# Source18-md5:	2638da6c30a83b443064ca7353563a09
Source50:	%{name}-extra.tar.bz2
# Source50-md5:	967e10b6b691f53885ffa01695657f79
Source51:	mbox.5
Patch0:		%{name}-localtime.patch
Patch1:		%{name}-zh_fixes.patch
BuildArch:	noarch
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
Eine groﬂe Sammlung von man-Seiten ¸ber Programmier-APIs,
Dateiformate, Protokolle, usw..

- section 1: Benutzerbefehle (nur intro)
- section 2: Systemaufrufe
- section 3: libc-Aufrufe (nur intro)
- section 4: Ger‰te (z.B. hd, sd)
- section 5: Dateiformate und Protokolle (z.B. wtmp, /etc/passwd, nfs)
- section 6: Spiele (nur intro)
- section 7: Konventionen, Makro-Pakete, usw. (z.B. nroff, ascii)
- section 8: Systemverwaltung (nur intro)

%description -l es
Una larga colecciÛn de p·ginas de manuales cubriendo programaciÛn
APIs, formatos de archivos, protocolos, etc.

- seciÛn 1: comandos de usuario (solamente introducciÛn)
- seciÛn 2: llamadas de sistema
- seciÛn 3: llamadas libc (solamente introducciÛn)
- seciÛn 4: dispositivos (ej.: hd, sd)
- seciÛn 5: formatos de archivos y protocolos (ej: wtmp, /etc/passwd,
  nfs)
- seciÛn 6: juegos (solamente introducciÛn)
- seciÛn 7: convenciones, paquetes de macros, etc. (ej: nroff, ascii)
- seciÛn 8: administraciÛn de sistema (solamente introducciÛn)

%description -l fi
Kokoelma man-sivujen k‰‰nnˆksi‰ suomenkielelle. Sivuja on mukana
yhteens‰ 211 kpl ja ne on paketoitu 14.11.1999 menness‰ valmiina
olleista sivuista. Sivut ovat osista 1 (komennot) ja 2 (pelit).

%description -l fr
Une large collection de pages de manuel du Project de Documentation
Linux (LDP), traduites en FranÁais. Les pages de manuel sont
organisÈes en differentes sections :

- section 1: Commandes utilisateur (intro seulement)
- section 2: Appels systËme
- section 3: Appels de la Libc (intro seulement)
- section 4: PÈriphÈriques (par ex. hd, sd)
- section 5: Formats de fichiers et de protocoles (par ex. wtmp,
  /etc/passwd, nfs)
- section 6: Jeux (intro seulement)
- section 7: Conventions, macro packages, etc. (par ex. nroff, ascii)
- section 8: Administration systËme (intro seulement)

%description -l it
Traduzioni italiane delle pagine di manuale per Linux: questo
pacchetto include non solo quelle dell'LDP, ma anche traduzioni di
altre pagine di uso comune. ATTENZIONE: alcune pagine sono obsolete!

%description -l pl
Pakiet ten zawiera duø± kolekcjÍ podrÍcznikÛw ekranowych (man pages),
opisuj±cych format plikÛw, protoko≥y itp.

- sekcja 1: komendy uøytkownikÛw (tylko wstÍp)
- sekcja 2: wywo≥ania systemowe
- sekcja 3: wywo≥ania bibliotek (tylko wstÍp)
- sekcja 4: urz±dzenia (np., hd, sd)
- sekcja 5: format plikÛw i protoko≥y (np., wtmp, /etc/passwd, nfs)
- sekcja 6: gry (tylko wstÍp)
- sekcja 7: konwencje, makro-pakiety, itp. (np., nroff, ascii)
- sekcja 8: administracja systemu (tylko wstÍp)

%description -l pt
Uma larga coleÁ„o de p·ginas de manuais cobrindo programaÁ„o APIs,
formatos de arquivos, protocolos, etc.

- seÁ„o 1: comandos de usu·rio (somente introduÁ„o)
- seÁ„o 2: chamadas de sistema
- seÁ„o 3: chamadas libc (somente introduÁ„o)
- seÁ„o 4: dispositivos (ex.: hd, sd)
- seÁ„o 5: formatos de arquivos e protocolos (ex: wtmp, /etc/passwd,
  nfs)
- seÁ„o 6: jogos (somente introduÁ„o)
- seÁ„o 7: convenÁıes, pacotes de macros, etc. (ex: nroff, ascii)
- seÁ„o 8: administraÁ„o de sistema (somente introduÁ„o)

%description -l pt_BR
Uma larga coleÁ„o de p·ginas de manuais cobrindo programaÁ„o APIs,
formatos de arquivos, protocolos, etc.

- seÁ„o 1: comandos de usu·rio (somente introduÁ„o)
- seÁ„o 2: chamadas de sistema
- seÁ„o 3: chamadas libc (somente introduÁ„o)
- seÁ„o 4: dispositivos (ex.: hd, sd)
- seÁ„o 5: formatos de arquivos e protocolos (ex: wtmp, /etc/passwd,
  nfs)
- seÁ„o 6: jogos (somente introduÁ„o)
- seÁ„o 7: convenÁıes, pacotes de macros, etc. (ex: nroff, ascii)
- seÁ„o 8: administraÁ„o de sistema (somente introduÁ„o)

%description -l ru
Ó≈¬œÃÿ€¡— ÀœÃÃ≈À√…— ”‘“¡Œ…√ “’Àœ◊œƒ”‘◊¡ …⁄ “œ≈À‘¡ ‰œÀ’Õ≈Œ‘¡√…… Œ¡
Ï…Œ’À”. Û‘“¡Œ…√Ÿ “’Àœ◊œƒ”‘◊¡ œ“«¡Œ…⁄œ◊¡ŒŸ ”Ã≈ƒ’¿›…Õ œ¬“¡⁄œÕ:

- ”≈À√…— 1: ÀœÕ¡Œƒ –œÃÿ⁄œ◊¡‘≈Ã— (‘œÃÿÀœ ◊◊≈ƒ≈Œ…≈)
- ”≈À√…— 2: ”…”‘≈ÕŒŸ≈ ◊Ÿ⁄œ◊Ÿ
- ”≈À√…— 3: ∆’ŒÀ√…… ¬…¬Ã…œ‘≈À… —⁄ŸÀ¡ C (‘œÃÿÀœ ◊◊≈ƒ≈Œ…≈)
- ”≈À√…— 4: ’”‘“œ ”‘◊¡ (Œ¡–“…Õ≈“, hd, sd)
- ”≈À√…— 5: ∆œ“Õ¡‘Ÿ ∆¡ Ãœ◊ … –“œ‘œÀœÃŸ (Œ¡–“…Õ≈“, wtmp, /etc/passwd,
  nfs)
- ”≈À√…— 6: …«“Ÿ (‘œÃÿÀœ ◊◊≈ƒ≈Œ…≈)
- ”≈À√…— 7: ”œ«Ã¡€≈Œ…—, Õ¡À“œ-–¡À≈‘Ÿ, … ‘. –. (Œ¡–“…Õ≈“, nroff, ascii)
- ”≈À√…— 8: ’‘…Ã…‘Ÿ ¡ƒÕ…Œ…”‘“¡‘œ“¡ (‘œÃÿÀœ ◊◊≈ƒ≈Œ…≈)

%description -l tr
Programlama aray¸zlerini, dosya formatlar˝n˝, protokolleri vs.
kapsayan, geni˛ bir k˝lavuz sayfalar˝ derlemesi.

%description -l uk
˜≈Ã…À…  Œ¡¬¶“ ”‘œ“¶ŒœÀ Õ¡Œ’¡Ã’ (ƒœÀ’Õ≈Œ‘¡√¶ß) ⁄ Linux Documentation
Project (LDP). Û‘œ“¶ŒÀ… œ“«¡Œ¶⁄œ◊¡Œ¶ ’ ‘¡À¶ ”≈À√¶ß: Û≈À√¶— 1, ÀœÕ¡Œƒ…
Àœ“…”‘’◊¡ﬁ¡ (‘¶ÃÿÀ… ◊”‘’–); Û≈À√¶— 2, ”…”‘≈ÕŒ¶ ◊…ÀÃ…À…; Û≈À√¶— 3,
◊…ÀÃ…À… libc; Û≈À√¶— 4, –“…”‘“œß (Œ¡–“…ÀÃ¡ƒ, hd, sd); Û≈À√¶— 5,
∆œ“Õ¡‘… ∆¡ Ã¶◊ ‘¡ –“œ‘œÀœÃ… (Œ¡–“…ÀÃ¡ƒ, wtmp, /etc/passwd, nfs);
Û≈À√¶— 6, ¶«“… (‘¶ÃÿÀ… ◊”‘’–); Û≈À√¶— 7, ’«œƒ…, Õ¡À“œ–¡À≈‘… ¶ ‘.¶.
(Œ¡–“…ÀÃ¡ƒ, nroff, ascii); Û≈À√¶— 8, ”…”‘≈ÕŒ≈ ¡ƒÕ¶Œ¶”‘“’◊¡ŒŒ— (‘¶ÃÿÀ…
◊”‘’–).

%package posix
Summary:	POSIX manual pages from the Linux Documentation Project
Summary(de):	POSIX-man-Seiten vom Linux Documentation Project
Summary(pl):	PodrÍczniki systemowe z Linux Documentation Project dotycz±ce POSIX
Group:		Documentation

%description posix
Part of POSIX 1003.1-2003 in man pages format.

%description posix -l pl
Fragmenty POSIX 1003.1-2003 w postaci stron podrÍcznika systemowego.

%prep
#%setup -q -a1 -a3 -a4 -a5 -a6 -a7 -a10 -a11 -a13 -a14 -a15 -a16 -a17 -a18
%setup -q -a1 -a3 -a4 -a5 -a6 -a7 -a11 -a13 -a14 -a15 -a16 -a17 -a18
%patch0 -p1
%patch1 -p0
#rm -f cman/man*/*.html

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
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,2,3,4,5,6,7,8,0p,1p,3p}

for n in man{1,2,3,4,5,6,7,8,0p,1p,3p}/*; do
	if head -n 1 $n| grep '^\.so' >/dev/null 2>&1 ; then
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
	if [ -f man-fr-%{fr_base_version}/$n ]; then
		install man-fr-%{fr_base_version}/$n $RPM_BUILD_ROOT%{_mandir}/fr/$n
#	if [ -f man-fr/$n ]; then
#		install man-fr/$n $RPM_BUILD_ROOT%{_mandir}/fr/$n
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
#	if [ -f cman/$n ]; then
#		install cman/$n $RPM_BUILD_ROOT%{_mandir}/zh_CN/$n
	if [ -f man-pages-zh_CN-%{zh_version}/src/$n ]; then
		# these man-pages are in UTF-8
		iconv -f UTF8 -t GB2312 man-pages-zh_CN-%{zh_version}/src/$n > $RPM_BUILD_ROOT%{_mandir}/zh_CN/$n
#		install man-pages-zh_CN-%{zh_version}/src/$n $RPM_BUILD_ROOT%{_mandir}/zh_CN/$n
#               Doesn't work. Bad encoding ?
#		iconv -f GB2312 -t Big5 cman/$n > $RPM_BUILD_ROOT%{_mandir}/zh_TW/$n
	fi
done
bzip2 -dc %{SOURCE50} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

install %{SOURCE51} $RPM_BUILD_ROOT%{_mandir}/man5/mbox.5

for k in $RPM_BUILD_ROOT%{_mandir}/{cs,de,es,fi,fr,hu,it,ja,ko,nl,pl,pt,pt_BR,ru,uk,zh_CN,zh_TW} ; do
	for n in $k/man{1,2,3,4,5,6,7,8}/*; do
		if head -n 1 $n| grep '^\.so' >/dev/null 2>&1 ; then
			sed 's,\.so man./,.so ,' < $n > $n.
			mv $n. $n
		fi
	done
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_mandir}/man*p
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
%lang(pt_BR) %{_mandir}/pt_BR/man*/*
%lang(ru) %{_mandir}/ru/man*/*
%lang(uk) %{_mandir}/uk/man*/*
%lang(zh_CN) %{_mandir}/zh_CN/man*/*
#%lang(zh_TW) %{_mandir}/zh_TW/man*/*

%files posix
%defattr(644,root,root,755)
%dir %{_mandir}/man?p
%{_mandir}/man?p/*
