%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Modlist
Summary:	Devel::Modlist perl module
Summary(pl):	Modu³ perla Devel::Modlist
Name:		perl-Devel-Modlist
Version:	0.5
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6b60fecb7a20c4c52023535ca3745867
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::Modlist - Perl extension to collect module use information.

%description -l pl
Modu³ perla Devel::Modlist.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Devel/Modlist.pm
%{_mandir}/man3/*
