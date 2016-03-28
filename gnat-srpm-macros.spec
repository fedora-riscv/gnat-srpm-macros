Name:           gnat-srpm-macros
Version:        4
Release:        1%{?dist}
Summary:        RPM macros needed when source packages that need GNAT are built
Summary(sv):    RPM-makron som behövs när källkodspaket som behöver GNAT byggs

Group:          Development/Libraries
License:        MIT
URL:            http://pkgs.fedoraproject.org/cgit/gnat-srpm-macros.git
Source1:        macros.gnat-srpm
BuildArch:      noarch


%description
This package contains RPM macros that need to be available when source RPM
packages that need the GNAT tools are built. It is a standalone package in
order to have as few dependencies as possible.

%description -l sv
Det här paketet innehåller RPM-makron som behöver finnas tillgängliga när käll-
RPM-paket som behöver GNAT-verktygen byggs. Det är ett fristående paket för att
bero av så få andra paket som möjligt.


%global RPM_macro_dir %{_rpmconfigdir}/macros.d


%prep
# nothing to do


%build
# nothing to do


%install
mkdir -p %{buildroot}/%{RPM_macro_dir}
install -p -m 0644 -t %{buildroot}/%{RPM_macro_dir} %{SOURCE1}


%files
%{RPM_macro_dir}/*


%changelog
* Mon Mar 28 2016 Björn Persson <Bjorn@Rombobjörn.se> - 4-1
- GPRbuild is available on s390x and ppc64le.
- ia64, ppc and alpha are inactive.

* Tue Mar 22 2016 Björn Persson <Bjorn@Rombobjörn.se> - 3-1
- GNAT has been bootstrapped on s390x and ppc64le.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 25 2015 Björn Persson <bjorn@rombobjörn.se> - 2-1
- Added ARM to GPRbuild_arches, as GPRbuild now works on ARM.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Sep 14 2014 Björn Persson <bjorn@rombobjörn.se> - 1-1
- Separated GNAT_arches from redhat-rpm-config.
- Introduced GPRbuild_arches, excluding ARM.
- Added ppc64p7 to synchronize with the GCC package.
