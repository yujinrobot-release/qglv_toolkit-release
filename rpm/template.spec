Name:           ros-indigo-qglv-gallery
Version:        0.1.4
Release:        0%{?dist}
Summary:        ROS qglv_gallery package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       freeglut-devel
Requires:       libQGLViewer
Requires:       libXi-devel
Requires:       libXmu-devel
Requires:       mesa-libGL-devel
Requires:       mesa-libGLU-devel
BuildRequires:  freeglut-devel
BuildRequires:  libQGLViewer-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  ros-indigo-catkin

%description
Example programs from qglviewer.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Nov 02 2015 Daniel Stonier <stonier@yujinrobot.com> - 0.1.4-0
- Autogenerated by Bloom

* Wed Oct 28 2015 Daniel Stonier <stonier@yujinrobot.com> - 0.1.3-1
- Autogenerated by Bloom

* Wed Oct 28 2015 Daniel Stonier <stonier@yujinrobot.com> - 0.1.3-0
- Autogenerated by Bloom

* Tue Oct 27 2015 Daniel Stonier <stonier@yujinrobot.com> - 0.1.2-0
- Autogenerated by Bloom

* Tue Oct 20 2015 Daniel Stonier <stonier@yujinrobot.com> - 0.1.1-0
- Autogenerated by Bloom

