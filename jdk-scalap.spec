Name     : jdk-scalap
Version  : 2.11.8
Release  : 1
URL      : http://repo1.maven.org/maven2/org/scala-lang/scalap/2.11.8/scalap-2.11.8.jar
Source0  : http://repo1.maven.org/maven2/org/scala-lang/scalap/2.11.8/scalap-2.11.8.jar
Source1  : http://repo1.maven.org/maven2/org/scala-lang/scalap/2.11.8/scalap-2.11.8.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: jdk-scalap-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-scalap package.
Group: Data

%description data
data components for the jdk-scalap package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/scalap.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/scalap.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/scalap.xml \
%{buildroot}/usr/share/maven-poms/scalap.pom \
%{buildroot}/usr/share/java/scalap.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/scalap.jar
/usr/share/maven-metadata/scalap.xml
/usr/share/maven-poms/scalap.pom
