%global plugin_name discord

%global commit0 2ca7b3cb82abac229f5d2f0a33d798dba8023eb0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20171010

Name: purple-%{plugin_name}
Version: 0
Release: 13.%{date}git%{shortcommit0}%{?dist}
Summary: Discord plugin for libpurple

License: GPLv3+
URL: https://github.com/EionRobb/purple-discord
Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(purple)
BuildRequires: gettext-devel
BuildRequires: gcc

%package -n pidgin-%{plugin_name}
Summary: Adds pixmaps, icons and smileys for Discord protocol
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: pidgin

%description
Adds support for Discord to Pidgin, Adium, Finch and other libpurple
based messengers.

%description -n pidgin-%{plugin_name}
Adds pixmaps, icons and smileys for Discord protocol implemented by
purple-discord.

%prep
%autosetup -n %{name}-%{commit0}

# fix W: wrong-file-end-of-line-encoding
sed -i -e "s,\r,," README.md

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_libdir}/purple-2/lib%{plugin_name}.so

%files -n pidgin-%{plugin_name}
%{_datadir}/pixmaps/pidgin/protocols/*/%{plugin_name}.png

%changelog
* Wed Nov 08 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-13.20171010git2ca7b3c
- Updated to latest snapshot.

* Sat Sep 09 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-12.20170904gitcb53020
- Updated to latest snapshot.

* Tue Aug 29 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-11.20170829git9115bd2
- Updated to latest snapshot.

* Mon Aug 28 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-10.20170823git4397461
- Updated to latest snapshot.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20170608git5263aff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20170608git5263aff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-7.20170608git5263aff
- Updated to latest snapshot.

* Thu May 25 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-6.20170525gitec1292a
- Updated to latest snapshot.

* Thu May 25 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-5.20170521gitfe92ea6
- Updated to latest snapshot.

* Sat May 06 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-4.20170501git28b1aa4
- Updated to latest snapshot.

* Thu Apr 27 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-3.20170427gitd879f18
- Updated to latest snapshot.

* Wed Apr 26 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-2.20170426gitcca7860
- Updated to latest snapshot.

* Thu Apr 20 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20170420git5c2b3ee
- First SPEC release.
