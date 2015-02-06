%define	upstream_name	 Net-DNS-SEC
%define upstream_version 0.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	DNSSEC support for Net::DNS perl module
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Crypt::OpenSSL::Bignum)
BuildRequires:	perl(Crypt::OpenSSL::DSA)
BuildRequires:	perl(Crypt::OpenSSL::RSA) >= 0.170.0
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(Digest::BubbleBabble)
BuildRequires:	perl(Net::DNS)
BuildRequires:	perl(MIME::Base32)

BuildArch:	noarch

%description
This perl modules implements DNSSEC extensions as described in
rfc 2535, 2931. With it, you can use DS, SIG, KEY and NXT record.

It extends perl-Net-DNS to manipulate these records.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
rm -f t/14-misc.t
chmod 755 demo/{key2ds,make-signed-keyset}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README demo
%{perl_vendorlib}/Net
%{_mandir}/man?/*


%changelog
* Fri Mar 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.1
+ Revision: 518486
- update to 0.16

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.150.0-1mdv2010.0
+ Revision: 401624
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 15 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.15-2mdv2010.0
+ Revision: 375938
- rebuild

* Sun Mar 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2009.1
+ Revision: 355282
- update to new version 0.15

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.14-3mdv2009.1
+ Revision: 140692
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.14-3mdv2008.0
+ Revision: 25291
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.14-2mdk
- Fix SPEC according to Perl Policy

* Wed Mar 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdk
- New release 0.14

* Wed Dec 14 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdk
- new version
- %%mkrel
- spec cleanup
- rpmbuildupdate aware
- fix buildrequires
- drop test 14-misc, doesn't work now
- fix demo scripts perms

* Mon Jul 04 2005 Oden Eriksson <oeriksson@mandriva.com> 0.12-2mdk
- rebuild

* Mon Jun 14 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.12-1mdk
- 0.12

* Sun Apr 18 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.11-1mdk
- 0.11
- disable test

* Sat Apr 10 2004 Michael Scherer <misc@mandrake.org> 0.10-5mdk 
- rebuild for new perl
- [DIRM]
- better description

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.10-4mdk
- rebuild for new perl
- don't use PREFIX
- %%module macro
- use %%makeinstall_std macro

* Fri Jul 18 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.10-3mdk
- buildrequires
- don't require perl modules, rpm will figure out those dependencies by
  itself now

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.10-2mdk
- rebuild for new auto{prov,req}

