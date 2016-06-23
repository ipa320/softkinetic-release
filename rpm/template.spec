Name:           ros-indigo-softkinetic-camera
Version:        0.6.2
Release:        0%{?dist}
Summary:        ROS softkinetic_camera package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-camera-info-manager
Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-pcl-ros
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-camera-info-manager
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-pcl-ros
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs

%description
Softkinetic cameras drivers, including filters.

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Thu Jun 23 2016 Felipe Garcia Lopez <flg@ipa.fhg.de> - 0.6.2-0
- Autogenerated by Bloom

* Tue Jun 21 2016 Felipe Garcia Lopez <flg@ipa.fhg.de> - 0.6.1-0
- Autogenerated by Bloom

