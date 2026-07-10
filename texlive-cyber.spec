%global tl_name cyber
%global tl_revision 46776

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	Annotate compliance with cybersecurity requirements
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cyber
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cyber.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cyber.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cyber.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package helps you write documents indicating your compliance
with cybersecurity requirements. It also helps you format your document
in a form suitable inside the U.S. Department of Defense, by attaching
distribution statements, destruction notices, organization logos, and
security labels to it.

