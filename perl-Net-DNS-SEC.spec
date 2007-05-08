%define	module	Net-DNS-SEC
%define name	perl-%{module}
%define version	0.14
%define release	%mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	DNSSEC support for Net::DNS perl module
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-Crypt-OpenSSL-RSA >= 0.17
BuildRequires:	perl(Crypt::OpenSSL::DSA)
BuildRequires:	perl(Crypt::OpenSSL::Bignum)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(Digest::BubbleBabble)
BuildRequires:	perl(Net::DNS)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This perl modules implements DNSSEC extensions as described in
rfc 2535, 2931. With it, you can use DS, SIG, KEY and NXT record.

It extends perl-Net-DNS to manipulate these records.

%prep
%setup -q -n %{module}-%{version} 
rm -f t/14-misc.t
chmod 755 demo/{key2ds,make-signed-keyset}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc README demo
%{perl_vendorlib}/Net
%{_mandir}/man?/*
      
