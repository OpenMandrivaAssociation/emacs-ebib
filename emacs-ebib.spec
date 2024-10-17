%define tarname	ebib
%define name	emacs-%{tarname}
%define version 1.7.2
%define release 2

Summary:	BibTeX database manager for Emacs
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
License:	BSD
Group:		Editors
Url:		https://ebib.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Provides:	%{tarname} = %{version}-%{release}
Requires:	emacs 
BuildRequires:	emacs 

%description
Ebib is a BibTeX database manager that runs in GNU Emacs and
XEmacs. With Ebib, you can create and manage .bib-files, all within
Emacs. It supports @string and @preamble definitions, multi-line field
values, searching, and integration with Emacs' (La)TeX mode.

%prep
%setup -q -n %{tarname}-%{version}

%build
emacs -batch -f batch-byte-compile ebib.el
cp -p info/*.info .
lzma -z *.info

%install
%__rm -rf %{buildroot}
%__install -d -m 755 %{buildroot}%{_datadir}/emacs/site-lisp
%__install -d -m 755 %{buildroot}%{_infodir}
%__install -d -m 755 %{buildroot}%{_sysconfdir}/emacs/site-start.d
%__install -m 644 ebib.el* %{buildroot}%{_datadir}/emacs/site-lisp
%__install -m 644 ebib-manual.info* %{buildroot}%{_infodir}
ln -s %{_infodir}/ebib-manual.info.lzma %{buildroot}%{_infodir}/ebib.info.lzma
%__cat <<EOF > %{buildroot}%{_sysconfdir}/emacs/site-start.d/ebib.el
(autoload 'ebib "ebib" "Ebib, a BibTeX database manager" t)
EOF
%__chmod 644 %{buildroot}%{_sysconfdir}/emacs/site-start.d/ebib.el

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README doc/html/*
%_sysconfdir/emacs/site-start.d/ebib.*
%_datadir/emacs/site-lisp/ebib*
%_infodir/*



%changelog
* Wed Feb 04 2009 Lev Givon <lev@mandriva.org> 1.7.2-1mdv2009.1
+ Revision: 337547
- Update to 1.7.2.

* Tue Jul 08 2008 Lev Givon <lev@mandriva.org> 1.5.2-1mdv2009.0
+ Revision: 232643
- import emacs-ebib


