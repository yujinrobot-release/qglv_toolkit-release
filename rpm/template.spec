Name:           ros-indigo-qglv-pcl
Version:        0.1.3
Release:        0%{?dist}
Summary:        ROS qglv_pcl package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       pcl
Requires:       pcl-devel
Requires:       pcl-tools
Requires:       ros-indigo-ecl-build
Requires:       ros-indigo-qglv-opengl
BuildRequires:  pcl-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-ecl-build
BuildRequires:  ros-indigo-qglv-opengl

%description
OpenGL, PCL, ...

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
* Wed Oct 28 2015 Daniel Stonier <stonier@yujinrobot.com> - 0.1.3-0
- Autogenerated by Bloom

* Tue Oct 27 2015 Daniel Stonier <stonier@yujinrobot.com> - 0.1.2-0
- Autogenerated by Bloom

* Tue Oct 20 2015 Daniel Stonier <stonier@yujinrobot.com> - 0.1.1-0
- Autogenerated by Bloom

