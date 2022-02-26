Name:		python_cmake_module
Version:	0.8.1
Release:	1
Summary:	This is ROS2 foxy python_cmake_module Package
License:	Public Domain and Apache-2.0 and BSD and MIT and BSL-1.0 and LGPL-2.1-only and MPL-2.0 and GPL-3.0-only and GPL-2.0-or-later and MPL-1.1 and IJG and Zlib and OFL-1.1
URL:		https://github.com/ros2/python_cmake_module.git
Source0:	https://github.com/ros2/python_cmake_module/archive/refs/tags/0.8.1.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-pytest
BuildRequires:	asio-devel
BuildRequires:	tinyxml2-devel
BuildRequires:	git

%description
This is ROS2 foxy python_cmake_module Package.

%prep
%setup

%install
cd 3rdparty/ 

cd empy-3.3.4/
python3 setup.py install --user
cd ..

cd six-1.15.0/
python3 setup.py install --user
cd ..

cd setuptools_scm-4.1.2/
python3 setup.py install --user
cd ..

cd python-dateutil-2.8.1/
python3 setup.py install --user
cd ..

cd pyparsing-2.4.7/
python3 setup.py install --user
cd ..

cd docutils-0.16/
python3 setup.py install --user
cd ..

cd catkin_pkg-0.4.22/
python3 setup.py install --user
cd ..

#ros2

cd distlib-0.3.3/
python3 setup.py install --user
cd ..

cd attrs-21.2.0
python3 setup.py install --user
cd ..

cd more-itertools-5.0.0
python3 setup.py install --user
cd ..

cd zipp-1.0.0
python3 setup.py install --user
cd ..

cd wheel-0.33.0
python3 setup.py install --user
cd ..

cd toml-0.10.2
python3 setup.py install --user
cd ..

cd importlib_metadata-3.8.0
python3 setup.py install --user
cd ..

cd py-1.11.0
python3 setup.py install --user
cd ..

cd packaging-21.3
python3 setup.py install --user
cd ..

cd iniconfig-1.1.1
python3 setup.py install --user
cd ..

cd pluggy-1.0.0
python3 setup.py install --user
cd ..

cd typing_extensions-3.7.4
python3 setup.py install --user
cd ..

cd pytest-6.2.5
python3 setup.py install --user
cd ..

cd coverage-5.4
python3 setup.py install --user
cd ..

cd pytest-cov-3.0.0
python3 setup.py install --user
cd ..

cd pytest-repeat-0.9.1
python3 setup.py install --user
cd ..

cd pytest-rerunfailures-10.2
python3 setup.py install --user
cd ..

cd pytest-runner-5.3.1
python3 setup.py install --user
cd ..

cd PyYAML-6.0
python3 setup.py install --user
cd ..

cd setuptools-50.0.0
python3 setup.py install --user
cd ..

cd argcomplete-1.11.1
python3 setup.py install --user
cd ..

cd notify2-0.3.1
python3 setup.py install --user
cd ..

cd ..

# for colcon build tools
cd build_tools
./colcon/colcon-core/bin/colcon build --paths colcon/* --merge-install
source install/local_setup.sh
cd ..

# for workspace
cd workspace
colcon build --merge-install

####
# 对install内部的变量名称进行替换
#
####
SRC_PATH=$PWD/install
DST_PATH=/opt/ros/foxy
sed -i "s:${SRC_PATH}:${DST_PATH}:g"  `grep -rIln "${SRC_PATH}" install/*`

####
# install
#
####
mkdir -p %{buildroot}/opt/ros/foxy/
cp -r install/* %{buildroot}/opt/ros/foxy/

###for debug
#mkdir -p %{buildroot}/opt/ros/foxy/log
#cp -r log/ %{buildroot}/opt/ros/foxy/log

%files
%defattr(-,root,root)
/opt/ros/foxy/*

%changelog
* Thu 11-30-2021 openEuler Buildteam <hanhaomin008@126.com>
- Package init
* Thu 01-05-2022 openEuler Buildteam <ximonaxi@126.com>
- Package update
