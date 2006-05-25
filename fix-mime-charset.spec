Summary:	Fix incorrect charset information in Content-Type MIME headers of e-mail messages
Summary(pl):	Poprawianie niepoprawnych informacji o kodowaniu w nagЁСwkach pocztowych MIME
Summary(ru):	Исправляет некорректную информацию в MIME-заголовках e-mail сообщений
Name:		fix-mime-charset
Version:	0.5.3
Release:	1
License:	GPL v2+
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/fix-mime-chr/%{name}-%{version}.tar.gz
# Source0-md5:	c8f97db0170c78b092f3d9b7d0311120
URL:		http://fix-mime-chr.sourceforge.net/
BuildRequires:	enca-devel >= 0.99.4
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fix-mime-charset automatically detects character sets of email message
and modifies the Content-Type header appropriately. It can be used as
mail filter in mailing lists where users often set the charset of their
messages incorrectly. It processes messages fast and accurately,
ignoring attachments, and correctly interprets transfer-encodings.
None but the Content-Type header is changed.

%description -l pl
Fix-mime-charset automatycznie wykrywa u©yte kodowanie znakСw w
wiadomo╤ciach pocztowych i modyfikuje odpowiednio nagЁСwek
Content-Type. Mo©e byФ wykorzystany jako filtr pocztowy w listach
mailowych, gdzie u©ytkownicy czЙsto nieprawidЁowo ustawiaj╠ w
nagЁСwkach u©ywane przez siebie kodowanie. Szybko i skutecznie
przetwarza wiadomo╤ci, ignoruje zaЁ╠czniki i poprawnie interpretuje
kodowanie podczas transferu. Nie zmienia nic poza nagЁСwkiem
Content-Type.

%description -l ru
Fix-mime-charset автоматически определяет кодировку почтового сообщения
и изменяет соответствующим образом поле Content-Type в заголовке. Может
использоваться как фильтр сообщений в списках рассылки, где пользователи
часто неправильно указывают кодировки своих сообщений. Программа
обрабатывает сообщения быстро и аккуратно, игнорируя вложения и
корректно интерпретирует transfer-encodings.
Кроме поля Content-Type ничего не изменяется.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%lang(ru) %doc README.koi8r
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
