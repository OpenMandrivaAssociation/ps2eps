%define name	ps2eps
%define version 1.64
%define release %mkrel 3

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
