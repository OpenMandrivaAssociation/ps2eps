%define name	ps2eps
%define version 1.64
%define release %mkrel 5

Name: 	 	%{name}
Summary: 	Converts standard PostScript documents to EPS
Version: 	%{version}
Release: 	%{release}

Source:		http://www.telematik.informatik.uni-karlsruhe.de/~bless/%{name}-%{version}.tar.bz2
URL:		http://www.telematik.informatik.uni-karlsruhe.de/~bless/ps2eps.html
License:	GPL
Group:		Publishing
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Ps2eps is a tool (written in Perl) to produce Encapsulated PostScript Files
(EPS/EPSF) from usual one-paged Postscript documents. It calculates correct
Bounding Boxes for those EPS files and filters some special postscript
command sequences that can produce erroneous results on printers. EPS files
are often needed for including (scalable) graphics of high quality into
TeX/LaTeX (or even Word) documents.

%prep
%setup -q -n %name

%build
cd src/C
gcc $RPM_OPT_FLAGS -o bbox bbox.c
chmod 755 bbox
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_bindir
cp bin/%name %buildroot/%_bindir
cp src/C/bbox %buildroot/%_bindir
mkdir -p %buildroot/%_mandir/man1
cp doc/man/man1/* %buildroot/%_mandir/man1/
bzip2 %buildroot/%_mandir/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc *.txt doc/html doc/pdf
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.64-5mdv2010.0
+ Revision: 430810
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.64-4mdv2009.0
+ Revision: 259334
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.64-3mdv2009.0
+ Revision: 247234
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.64-1mdv2008.1
+ Revision: 140737
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jun 14 2007 Austin Acton <austin@mandriva.org> 1.64-1mdv2008.0
+ Revision: 39763
- new version
- mkrel
- Import ps2eps



* Thu Aug 25 2005 Austin Acton <austin@mandriva.org> 1.58-1mdk
- New release 1.58

* Mon Jan 17 2005 Austin Acton <austin@mandrake.org> 1.54-1mdk
- initial package
