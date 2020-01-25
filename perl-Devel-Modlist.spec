%define		pdir	Devel
%define		pnam	Modlist
Summary:	Devel::Modlist - collect module use information
Summary(pl.UTF-8):	Devel::Modlist - gromadzenie informacji o używanych modułach
Name:		perl-Devel-Modlist
Version:	0.801
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f636cc3580d0129c89421226034d7738
URL:		http://search.cpan.org/dist/Devel-Modlist/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Devel::Modlist utility is provided as a means by which to get a
quick run-down on which libraries and modules are being utilized by a
given script.

%description -l pl.UTF-8
Narzędzie Devel::Modlist służy jako środek do szybkiego pobierania
informacji o tym, które biblioteki i moduły są wykorzystywane przez
zadany skrypt.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Devel/Modlist.pm
%{_mandir}/man3/*
