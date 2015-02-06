%define		_class		File
%define		_subclass	IMC
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.5.0
Release:	2
Summary:	Create and parse Internet Mail Consortium-style files
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/File_IMC/
Source0:	http://download.pear.php.net/package/File_IMC-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Allows you to programmatically create a vCard or vCalendar, and fetch
the text.

IMPORTANT: The array structure has changed slightly from
Contact_Vcard_Parse. See the example output for the new structure.
Also different from Contact_Vcard is the use of a factory pattern.
Again, see the examples. 

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3-13mdv2012.0
+ Revision: 741976
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3-12
+ Revision: 679322
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-11mdv2011.0
+ Revision: 613659
- the mass rebuild of 2010.1 packages

* Mon Dec 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3-10mdv2010.1
+ Revision: 478669
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.3-9mdv2010.0
+ Revision: 441071
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3-8mdv2009.0
+ Revision: 236839
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.3-7mdv2008.1
+ Revision: 136404
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3-7mdv2007.0
+ Revision: 81582
- Import php-pear-File_IMC

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3-1mdk
- initial Mandriva package (PLD import)


