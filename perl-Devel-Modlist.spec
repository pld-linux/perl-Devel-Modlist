%include	/usr/lib/rpm/macros.perl
Summary:	Devel-Modlist perl module
Summary(pl):	Modu³ perla Devel-Modlist
Name:		perl-Devel-Modlist
Version:	0.4
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Devel/Devel-Modlist-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel-Modlist - Perl extension to collect module use information.

%description -l pl
Modu³ perla Devel-Modlist.

%prep
%setup -q -n Devel-Modlist-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Devel/Modlist.pm
%{_mandir}/man3/*
