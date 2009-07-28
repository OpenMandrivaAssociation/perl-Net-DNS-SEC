%define	upstream_name	 Net-DNS-SEC
%define upstream_version 0.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	DNSSEC support for Net::DNS perl module
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-Crypt-OpenSSL-RSA >= 0.17
BuildRequires:	perl(Crypt::OpenSSL::DSA)
BuildRequires:	perl(Crypt::OpenSSL::Bignum)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(Digest::BubbleBabble)
BuildRequires:	perl(Net::DNS)
BuildRequires:	perl(MIME::Base32)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This perl modules implements DNSSEC extensions as described in
rfc 2535, 2931. With it, you can use DS, SIG, KEY and NXT record.

It extends perl-Net-DNS to manipulate these records.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
      
