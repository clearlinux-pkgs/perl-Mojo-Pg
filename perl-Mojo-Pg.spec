#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Mojo-Pg
Version  : 4.13
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/S/SR/SRI/Mojo-Pg-4.13.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SR/SRI/Mojo-Pg-4.13.tar.gz
Summary  : Mojolicious ♥ PostgreSQL
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Mojo-Pg-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(DBD::Pg)
BuildRequires : perl(DBI)
BuildRequires : perl(Mojo::Base)
BuildRequires : perl(Mojolicious)
BuildRequires : perl(SQL::Abstract)

%description
# Mojo::Pg [![Build Status](https://travis-ci.com/mojolicious/mojo-pg.svg?branch=master)](https://travis-ci.com/mojolicious/mojo-pg)

%package dev
Summary: dev components for the perl-Mojo-Pg package.
Group: Development
Provides: perl-Mojo-Pg-devel = %{version}-%{release}

%description dev
dev components for the perl-Mojo-Pg package.


%package license
Summary: license components for the perl-Mojo-Pg package.
Group: Default

%description license
license components for the perl-Mojo-Pg package.


%prep
%setup -q -n Mojo-Pg-4.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Mojo-Pg
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Mojo-Pg/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/Pg.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/Pg/Database.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/Pg/Migrations.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/Pg/PubSub.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/Pg/Results.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/Pg/Transaction.pm
/usr/lib/perl5/vendor_perl/5.28.2/SQL/Abstract/Pg.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Mojo::Pg.3
/usr/share/man/man3/Mojo::Pg::Database.3
/usr/share/man/man3/Mojo::Pg::Migrations.3
/usr/share/man/man3/Mojo::Pg::PubSub.3
/usr/share/man/man3/Mojo::Pg::Results.3
/usr/share/man/man3/Mojo::Pg::Transaction.3
/usr/share/man/man3/SQL::Abstract::Pg.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Mojo-Pg/LICENSE
