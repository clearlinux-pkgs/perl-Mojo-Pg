#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Mojo-Pg
Version  : 4.18
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/S/SR/SRI/Mojo-Pg-4.18.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SR/SRI/Mojo-Pg-4.18.tar.gz
Summary  : 'Mojolicious ♥ PostgreSQL'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Mojo-Pg-license = %{version}-%{release}
Requires: perl-Mojo-Pg-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(DBD::Pg)
BuildRequires : perl(DBI)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Mojo::Base)
BuildRequires : perl(Mojolicious)
BuildRequires : perl(Moo)
BuildRequires : perl(SQL::Abstract)
BuildRequires : perl(Sub::Quote)
BuildRequires : perl(Test::Deep)

%description
# Mojo::Pg [![Build Status](https://travis-ci.com/mojolicious/mojo-pg.svg?branch=master)](https://travis-ci.com/mojolicious/mojo-pg)

%package dev
Summary: dev components for the perl-Mojo-Pg package.
Group: Development
Provides: perl-Mojo-Pg-devel = %{version}-%{release}
Requires: perl-Mojo-Pg = %{version}-%{release}

%description dev
dev components for the perl-Mojo-Pg package.


%package license
Summary: license components for the perl-Mojo-Pg package.
Group: Default

%description license
license components for the perl-Mojo-Pg package.


%package perl
Summary: perl components for the perl-Mojo-Pg package.
Group: Default
Requires: perl-Mojo-Pg = %{version}-%{release}

%description perl
perl components for the perl-Mojo-Pg package.


%prep
%setup -q -n Mojo-Pg-4.18
cd %{_builddir}/Mojo-Pg-4.18

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Mojo-Pg
cp %{_builddir}/Mojo-Pg-4.18/LICENSE %{buildroot}/usr/share/package-licenses/perl-Mojo-Pg/2f8018a02043ed1a43f032379e036bb6b88265f2
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
/usr/share/package-licenses/perl-Mojo-Pg/2f8018a02043ed1a43f032379e036bb6b88265f2

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/Mojo/Pg.pm
/usr/lib/perl5/vendor_perl/5.30.2/Mojo/Pg/Database.pm
/usr/lib/perl5/vendor_perl/5.30.2/Mojo/Pg/Migrations.pm
/usr/lib/perl5/vendor_perl/5.30.2/Mojo/Pg/PubSub.pm
/usr/lib/perl5/vendor_perl/5.30.2/Mojo/Pg/Results.pm
/usr/lib/perl5/vendor_perl/5.30.2/Mojo/Pg/Transaction.pm
/usr/lib/perl5/vendor_perl/5.30.2/SQL/Abstract/Pg.pm
