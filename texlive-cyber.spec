Name:		texlive-cyber
Version:	46776
Release:	2
Summary:	Annotate compliance with cybersecurity requirements
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cyber
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cyber.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cyber.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cyber.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package helps you write documents indicating your
compliance with cybersecurity requirements. It also helps you
format your document in a form suitable inside the U.S.
Department of Defense, by attaching distribution statements,
destruction notices, organization logos, and security labels to
it.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/cyber
%{_texmfdistdir}/tex/latex/cyber
%doc %{_texmfdistdir}/doc/latex/cyber

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
