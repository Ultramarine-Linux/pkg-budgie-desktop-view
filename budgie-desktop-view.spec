%define _disable_source_fetch 0
Name:           budgie-desktop-view
Version:        1.2
Release:        2%{?dist}
Summary:        The official Budgie desktop icons application / implementation.

License:        Apache 2.0
URL:            https://github.com/BuddiesOfBudgie/budgie-desktop-view
Source0:        https://github.com/BuddiesOfBudgie/budgie-desktop-view/releases/download/v%{version}/budgie-desktop-view-v%{version}.tar.xz

BuildRequires:  meson intltool glib2-devel gtk3-devel vala
Requires:       budgie-desktop

%description


%prep
%autosetup


%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT
%meson_install

%check
%meson_test

%files
%license LICENSE.md
%doc README.md
%{_sysconfdir}/xdg/autostart/org.buddiesofbudgie.budgie-desktop-view-autostart.desktop
%{_bindir}/org.buddiesofbudgie.budgie-desktop-view
%{_datadir}/glib-2.0/schemas/org.buddiesofbudgie.budgie-desktop-view.gschema.xml
%{_datadir}/applications/org.buddiesofbudgie.budgie-desktop-view.desktop

%changelog
* Tue Jan 11 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Update source path to Buddies of Budgie

* Thu Sep 02 2021 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Release
