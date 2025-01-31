%global debug_package %{nil}

Name:           vulkan-volk
Version:        1.3.277.0
Release:        %autorelease
Summary:        Meta loader for Vulkan API

License:        MIT
URL:            https://github.com/zeux/volk
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  vulkan-headers

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
Requires:       vulkan-headers
Conflicts:      volk-devel

%description    devel
%{summary}

%prep
%autosetup -n %{name}-%{version}/upstream

%build
%cmake3 -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
        -DVOLK_INSTALL:BOOL=ON
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE.md
%doc README.md
%dir %{_libdir}/cmake/volk
%{_includedir}/volk.h
%{_includedir}/volk.c
%{_libdir}/cmake/volk/*.cmake
%{_libdir}/libvolk.a
