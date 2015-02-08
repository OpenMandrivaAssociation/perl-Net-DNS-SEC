%define	upstream_name	 Net-DNS-SEC
%define upstream_version 0.21_11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	DNSSEC support for Net::DNS perl module
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:  perl(Test::Pod)
BuildRequires: perl(Crypt::OpenSSL::Bignum) >= 0.30.0
BuildRequires: perl(Crypt::OpenSSL::DSA) >= 0.100.0
BuildRequires: perl(Crypt::OpenSSL::RSA) >= 0.190.0
BuildRequires: perl(Digest::BubbleBabble) >= 0.10.0
BuildRequires: perl(Digest::SHA) >= 5.230.0
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename)
BuildRequires: perl(MIME::Base32)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Math::BigInt)
BuildRequires: perl(Net::DNS) >= 0.640.0
BuildRequires: perl(Test::More) >= 0.470.0
BuildRequires: perl(Time::Local)


BuildArch:	noarch

%description
This perl modules implements DNSSEC extensions as described in
rfc 2535, 2931. With it, you can use DS, SIG, KEY and NXT record.

It extends perl-Net-DNS to manipulate these records.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%files
%doc Changes README TODO
%doc demo/
%{perl_vendorlib}/*
%{_mandir}/man3/*




