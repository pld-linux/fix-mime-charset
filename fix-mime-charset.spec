Summary:	Fix incorrect charset information in Content-Type MIME headers of e-mail messages
Summary(pl):	Poprawianie niepoprawnych informacji o kodowaniu w nag��wkach pocztowych MIME
Summary(ru):	���������� ������������ ���������� � MIME-���������� e-mail ���������
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
Fix-mime-charset automatycznie wykrywa u�yte kodowanie znak�w w
wiadomo�ciach pocztowych i modyfikuje odpowiednio nag��wek
Content-Type. Mo�e by� wykorzystany jako filtr pocztowy w listach
mailowych, gdzie u�ytkownicy cz�sto nieprawid�owo ustawiaj� w
nag��wkach u�ywane przez siebie kodowanie. Szybko i skutecznie
przetwarza wiadomo�ci, ignoruje za��czniki i poprawnie interpretuje
kodowanie podczas transferu. Nie zmienia nic poza nag��wkiem
Content-Type.

%description -l ru
Fix-mime-charset ������������� ���������� ��������� ��������� ���������
� �������� ��������������� ������� ���� Content-Type � ���������. �����
�������������� ��� ������ ��������� � ������� ��������, ��� ������������
����� ����������� ��������� ��������� ����� ���������. ���������
������������ ��������� ������ � ���������, ��������� �������� �
��������� �������������� transfer-encodings.
����� ���� Content-Type ������ �� ����������.

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
