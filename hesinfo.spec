Name: hesinfo
Version: 3.1.0
Release: 8%{?dist}
Source: ftp://athena-dist.mit.edu/pub/ATHENA/hesiod/hesinfo-%{version}.tar.gz
Summary: Command-line Hesiod client
Group: Applications/Internet
License: MIT
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: hesiod-devel >= 3.1.0

%description
Hesiod is a system which uses existing DNS functionality to provide access
to databases of information that changes infrequently.  It is often used to
distribute information kept in the /etc/passwd, /etc/group, and /etc/printcap
files, among others.  The hesinfo package contains the hesinfo client program,
which can be used to query Hesiod.

%changelog
* Fri Feb 19 2010 Nalin Dahyabhai <nalin@redhat.com> 3.1.0-8
- override permissions on files in %{_bindir} (#225883)

* Wed Jan 13 2010 Nalin Dahyabhai <nalin@redhat.com> 3.1.0-7
- drop unnecessary %%post/%%postun
- tweak default payload file attributes (guidelines)
- tweak summary (guidelines)

* Tue Oct 13 2009 Nalin Dahyabhai <nalin@redhat.com>
- add a disttag

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.1.0-3
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Nalin Dahyabhai <nalin@redhat.com> - 3.1.0-2
- rebuild
- verified that license tag is correct

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.1.0-1.1
- rebuild

* Thu Mar 30 2006 Nalin Dahyabhai <nalin@redhat.com> - 3.1.0-1
- split off from hesiod package, following upstream

%prep
%setup -q

%build
%configure 
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README NEWS
%attr(0755,root,root) %{_bindir}/*
%{_mandir}/man1/*
