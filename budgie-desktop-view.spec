%define _disable_source_fetch 0
Name:           budgie-desktop-view
Version:        1.1.1
Release:        1%{?dist}
Summary:        The official Budgie desktop icons application / implementation.

License:        Apache 2.0
URL:            https://github.com/getsolus/budgie-desktop-view
Source0:        https://github.com/getsolus/budgie-desktop-view/releases/download/v1.1.1/budgie-desktop-view-v%{version}.tar.xz

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
%{_sysconfdir}/xdg/autostart/us.getsol.budgie-desktop-view-autostart.desktop
%{_bindir}/us.getsol.budgie-desktop-view
%{_datadir}/glib-2.0/schemas/us.getsol.budgie-desktop-view.gschema.xml
%{_datadir}/applications/us.getsol.budgie-desktop-view.desktop

%changelog
* Thu Sep 02 2021 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Release
