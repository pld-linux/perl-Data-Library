#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Data
%define		pnam	Library
Summary:	Data::Library - virtual class for repository support classes
Summary(pl.UTF-8):	Data::Library - klasa wirtualna dla klas usług magazynowych
Name:		perl-Data-Library
Version:	0.2
Release:	1
# same as perl (but for Data::Library is unknown)
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3d849a67a8d0273458043c5378c8bca9
URL:		http://search.cpan.org/dist/Data-Library/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Virtual
BuildRequires:	perl-Log-Channel
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Library Perl module provides a general repository service.
Specifics are implemented in subclasses.

%description -l pl.UTF-8
Moduł Perla Data::Library udostępnia ogólną usługę magazynową.
Szczegóły są zaimplementowane w podklasach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Data/Library.pm
%{perl_vendorlib}/Data/Library
%{_mandir}/man3/*
