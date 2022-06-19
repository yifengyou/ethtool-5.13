Name:		ethtool
Epoch:		2
Version:	5.13
Release:	1%{?dist}
Summary:	Settings tool for Ethernet NICs
License:	GPLv2
Group:		Applications/System
URL:		https://www.kernel.org/pub/software/network/%{name}/
Source0:	https://www.kernel.org/pub/software/network/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	libmnl-devel
Conflicts:	filesystem < 3

%description
This utility allows querying and changing settings such as speed,
port, auto-negotiation, PCI locations and checksum offload on many
network devices, especially of Ethernet devices.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} INSTALL='install -p' install

%files
%license COPYING LICENSE
%doc AUTHORS ChangeLog* NEWS README
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*
%{_datadir}/bash-completion/completions/ethtool

%changelog
* Thu Nov 18 2021 Ivan Vecera <ivecera@redhat.com> - 2:5.13-1
- Updated to upstream v5.13

* Thu Jun 03 2021 Ivan Vecera <ivecera@redhat.com> - 2:5.8-7
- Added support for lanes

* Thu Mar 11 2021 Ivan Vecera <ivecera@redhat.com> - 2:5.8-6
- Added support for pause frame statistics

* Thu Nov 12 2020 Ivan Vecera <ivecera@redhat.com> - 2:5.8-5
- Fixed a regression

* Fri Nov 06 2020 Ivan Vecera <ivecera@redhat.com> - 2:5.8-4
- Added support for extended link state reporting

* Fri Sep 25 2020 Ivan Vecera <ivecera@redhat.com> - 2:5.8-3
- Fixed memory leak

* Thu Sep 24 2020 Ivan Vecera <ivecera@redhat.com> - 2:5.8-2
- Add post-5.8 bugfixes

* Tue Sep 15 2020 Ivan Vecera <ivecera@redhat.com> - 2:5.8-1
- Update to 5.8 (#1878826)

* Thu May 16 2019 Ivan Vecera <ivecera@redhat.com> - 2:5.0-2
- Added support for 200Gbps (50Gbps/lane) link mode 

* Wed Mar 13 2019 Ivan Vecera <ivecera@redhat.com> - 2:5.0-1
- Update to 5.0 (#1688299)

* Sat Apr 14 2018 Robert Scheck <robert@fedoraproject.org> - 2:4.16-1
- Update to 4.16 (#1567447)

* Sun Feb 18 2018 Robert Scheck <robert@fedoraproject.org> - 2:4.15-1
- Update to 4.15 (#1541183)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 04 2017 Robert Scheck <robert@fedoraproject.org> - 2:4.13-1
- Update to 4.13 (#1507171)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Fri Jul 28 2017 Robert Scheck <robert@fedoraproject.org> - 2:4.11-1
- Update to 4.11 (#1435843)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Robert Scheck <robert@fedoraproject.org> - 2:4.8-1
- Update to 4.8 (#1317497)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 09 2015 Jaromir Capik <jcapik@redhat.com> - 2:4.2-1
- Updating to 4.2 (#1270250)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 01 2015 Jaromir Capik <jcapik@redhat.com> - 2:4.0-1
- Update to 4.0 (#1226742)

* Thu Jan 29 2015 Jaromir Capik <jcapik@redhat.com> - 2:3.18-1
- Update to 3.18 (#1175150)

* Tue Sep 23 2014 Jaromir Capik <jcapik@redhat.com> - 2:3.16-1
- Update to 3.16 (#1144992)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 05 2014 Jaromir Capik <jcapik@redhat.com> - 2:3.15-1
- Update to 3.15 (#1124044)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Jaromir Capik <jcapik@redhat.com> - 2:3.14-1
- Update to 3.14 (#1089943)

* Thu Jan 30 2014 Jaromir Capik <jcapik@redhat.com> - 2:3.13-1
- Update to 3.13 (#1059565)

* Mon Nov 18 2013 Jaromir Capik <jcapik@redhat.com> - 2:3.12-1
- Update to 3.12 (#1030854)

* Fri Sep 13 2013 Jaromir Capik <jcapik@redhat.com> - 2:3.11-1
- Update to 3.11 (#1007738)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 04 2013 Jaromir Capik <jcapik@redhat.com> - 2:3.10-1
- Update to 3.10 (#981357)

* Thu May 02 2013 Jaromir Capik <jcapik@redhat.com> - 2:3.9-1
- Update to 3.9 (#958467)

* Mon Mar 04 2013 Jaromir Capik <jcapik@redhat.com> - 2:3.8-1
- Update to 3.8 (#916922)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 17 2012 Jaromir Capik <jcapik@redhat.com> - 2:3.7-1
- Update to 3.7 (#887463)

* Tue Oct 23 2012 Jaromir Capik <jcapik@redhat.com> 2:3.6-1
- Update to 3.6 (#863774)

* Tue Sep 25 2012 Jaromir Capik <jcapik@redhat.com> 2:3.5-1
- Update to 3.5 (#840741)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Jaromir Capik <jcapik@redhat.com> 2:3.4.1-1
- Update to 3.4.1 (#830263)

* Wed Jan 25 2012 Harald Hoyer <harald@redhat.com> 2:3.2-2
- install everything in /usr
  https://fedoraproject.org/wiki/Features/UsrMove

* Fri Jan 13 2012 Jaromir Capik <jcapik@redhat.com> 2:3.2-1
- Update to 3.2 (#781357)
- Minor spec file changes according to the latest guidelines

* Fri Dec 23 2011 Robert Scheck <robert@fedoraproject.org> 2:3.1-1
- Upgrade to 3.1 (#728480)

* Sun Jul 17 2011 Robert Scheck <robert@fedoraproject.org> 2:2.6.39-1
- Upgrade to 2.6.39 (#710400)

* Mon Mar 21 2011 Robert Scheck <robert@fedoraproject.org> 2:2.6.38-1
- Upgrade to 2.6.38 (#667594)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:2.6.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 31 2010 Robert Scheck <robert@fedoraproject.org> 2:2.6.36-1
- Upgrade to 2.6.36 (#623094)

* Wed Jul 14 2010 Jeff Garzik <jgarzik@redhat.com> 2:2.6.34-1
- Update to release 2.6.34.

* Thu Feb  4 2010 Jeff Garzik <jgarzik@redhat.com> 2.6.33-0.1
- update to version 2.6.33-pre1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-7.20090323git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 18 2009 Robert Scheck <robert@fedoraproject.org> 6-6.20090323git
- Upgrade to GIT 20090323

* Thu Jul 16 2009 Jeff Garzik <jgarzik@redhat.com> 6-5.20090306git
- minor specfile cleanups

* Sat Mar 07 2009 Robert Scheck <robert@fedoraproject.org> 6-4.20090306git
- Upgrade to GIT 20090306

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 6-3.20090115git
- Rebuild for gcc 4.4 and rpm 4.6

* Sat Jan 17 2009 Robert Scheck <robert@fedoraproject.org> 6-2.20090115git
- Changes to match with Fedora Packaging Guidelines (#225735)
- Upgrade to GIT 20090115 (#225735, #477498)
- Removed bogus stated need of DEVNAME in -h/--help (#472038)
- Removed completely needless INSTALL file from %%doc (#472034)

* Wed Mar 12 2008 Tom "spot" Callaway <tcallawa@redhat.com> 6-1
- Upgrade to ethtool version 6

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5-2
- Autorebuild for GCC 4.3

* Thu Dec 14 2006 Jay Fenlason <fenlason@redhat.com> 5-1
- Upgrade to ethtool version 5 to close
  bz#184985: RFE: 10gigE support
  bz#204840: "buffer overflow detected" when devname's length >=16 of ethtool
  Resolves: #184985, #204840

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3-1.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Mar  3 2005 Jeff Garzik <jgarzik@pobox.com>
- Update to version 3.
- Use %%buildroot macro, rather than RPM_BUILD_ROOT env var,
  as recommended by RPM packaging guidelines.

* Sun Feb 27 2005 Florian La Roche <laroche@redhat.com>
- Copyright: -> License

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Sep  5 2003 Bill Nottingham <notting@redhat.com> 1.8-2
- remove bogus check for devices starting with ethXX, this time applying
  the patch

* Thu Jul 24 2003 Bill Nottingham <notting@redhat.com> 1.8-1
- update to 1.8
- remove bogus check for devices starting with ethXX

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Feb  8 2003 Bill Nottingham <notting@redhat.com> 1.6-5
- move to /sbin

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 12 2002 Tim Powers <timp@redhat.com> 1.6-3
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jun 20 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.6

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Mar  4 2002 Bill Nottingham <notting@redhat.com> 1.5-1
- 1.5

* Thu Feb 21 2002 Bill Nottingham <notting@redhat.com>
- rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Dec  4 2001 Bill Nottingham <notting@redhat.com>
- update to 1.4

* Fri Aug  3 2001 Bill Nottingham <notting@redhat.com>
- return of ethtool! (#50475)

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Matt Wilson <msw@redhat.com>
- rebuilt for next release
- use FHS man path

* Tue Feb 22 2000 Bill Nottingham <notting@redhat.com>
- handle compressed manpages

* Wed Apr 14 1999 Bill Nottingham <notting@redhat.com>
- run through with new s/d

* Tue Apr 13 1999 Jakub Jelinek <jj@ultra.linux.cz>
- initial package.
