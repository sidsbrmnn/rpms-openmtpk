Name:           openmtpk
Version:        0.9.4
Release:        %autorelease
Summary:        General-purpose Math Package

License:        GPL-3.0-or-later
URL:            https://akielaries.github.io/openMTPK/
Source:         https://github.com/akielaries/openMTPK/archive/v%{version}/openMTPK-%{version}.tar.gz
Patch1:         use-system-gtest.patch
Patch2:         enable-shared-library.patch
Patch3:         fix-version.patch

BuildRequires:  gcc-c++ swig cmake gtest-devel
# Requires:

%description
openMTPK is an open-source (intended) mathematics package written in C++ with
a primary focus on Numbery Theory and Cryptographic algorithms, Linear Algebra,
and Machine/Deep learning concepts as well as a range of language API's.
openMTPK aims to provide options for pre-built functions, models, etc. along
with modularity for user freedom.

%package devel
Summary:        Development files for openMTPK
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use openMTPK. This package is not required for running
applications that use openMTPK.

%prep
%autosetup -p1 -n openMTPK-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%{_libdir}/libopenMTPK.so.%{version}

%doc README.md
%license LICENSE

%files devel
%{_includedir}/openMTPK/arithmetic.hpp
%{_includedir}/openMTPK/calculus/analysis.hpp
%{_includedir}/openMTPK/calculus/deriv.hpp
%{_includedir}/openMTPK/linalg.hpp
%{_includedir}/openMTPK/linalg/matrix.hpp
%{_includedir}/openMTPK/linalg/tensors.hpp
%{_includedir}/openMTPK/linalg/vectors.hpp
%{_includedir}/openMTPK/ml.hpp
%{_includedir}/openMTPK/ml/activators.hpp
%{_includedir}/openMTPK/ml/bayes_clf.hpp
%{_includedir}/openMTPK/ml/bayes_net.hpp
%{_includedir}/openMTPK/ml/encoder.hpp
%{_includedir}/openMTPK/ml/encoder_var.hpp
%{_includedir}/openMTPK/ml/k-foldCV.hpp
%{_includedir}/openMTPK/ml/knn.hpp
%{_includedir}/openMTPK/ml/kohonen_net.hpp
%{_includedir}/openMTPK/ml/linreg.hpp
%{_includedir}/openMTPK/ml/logreg.hpp
%{_includedir}/openMTPK/ml/mlp_net.hpp
%{_includedir}/openMTPK/ml/naive_net.hpp
%{_includedir}/openMTPK/ml/nn.hpp
%{_includedir}/openMTPK/ml/optimizers.hpp
%{_includedir}/openMTPK/ml/regularizers.hpp
%{_includedir}/openMTPK/ml/statistics.hpp
%{_includedir}/openMTPK/ml/svc.hpp
%{_includedir}/openMTPK/ml/trainers.hpp
%{_includedir}/openMTPK/nt.hpp
%{_includedir}/openMTPK/nt/cipher.hpp
%{_includedir}/openMTPK/nt/primes.hpp
%{_includedir}/openMTPK/nt/rc4.hpp
%{_includedir}/openMTPK/nt/rc5.hpp
%{_includedir}/openMTPK/utils.hpp

%{_libdir}/libopenMTPK.so

%{_datadir}/openMTPK/cmake/openMTPKConfig-release.cmake
%{_datadir}/openMTPK/cmake/openMTPKConfig.cmake

%doc README.md
%license LICENSE

%changelog
%autochangelog
