#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-BatchJobs
Version  : 1.7
Release  : 4
URL      : https://cran.r-project.org/src/contrib/BatchJobs_1.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/BatchJobs_1.7.tar.gz
Summary  : Batch Computing with R
Group    : Development/Tools
License  : BSD-2-Clause
Requires: R-BBmisc
Requires: R-DBI
Requires: R-RSQLite
Requires: R-brew
Requires: R-data.table
Requires: R-sendmailR
Requires: R-stringi
BuildRequires : R-BBmisc
BuildRequires : R-DBI
BuildRequires : R-RSQLite
BuildRequires : R-brew
BuildRequires : R-data.table
BuildRequires : R-sendmailR
BuildRequires : R-stringi
BuildRequires : clr-R-helpers

%description
computing systems like PBS/Torque, LSF, SLURM and Sun Grid Engine.
    Multicore and SSH systems are also supported. For further details see the
    project web page.

%prep
%setup -q -c -n BatchJobs

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530441219

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530441219
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BatchJobs
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BatchJobs
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BatchJobs
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library BatchJobs|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/BatchJobs/CITATION
/usr/lib64/R/library/BatchJobs/DESCRIPTION
/usr/lib64/R/library/BatchJobs/INDEX
/usr/lib64/R/library/BatchJobs/LICENSE
/usr/lib64/R/library/BatchJobs/Meta/Rd.rds
/usr/lib64/R/library/BatchJobs/Meta/features.rds
/usr/lib64/R/library/BatchJobs/Meta/hsearch.rds
/usr/lib64/R/library/BatchJobs/Meta/links.rds
/usr/lib64/R/library/BatchJobs/Meta/nsInfo.rds
/usr/lib64/R/library/BatchJobs/Meta/package.rds
/usr/lib64/R/library/BatchJobs/NAMESPACE
/usr/lib64/R/library/BatchJobs/NEWS
/usr/lib64/R/library/BatchJobs/R/BatchJobs
/usr/lib64/R/library/BatchJobs/R/BatchJobs.rdb
/usr/lib64/R/library/BatchJobs/R/BatchJobs.rdx
/usr/lib64/R/library/BatchJobs/bin/linux-helper
/usr/lib64/R/library/BatchJobs/etc/BatchJobs_global_config.R
/usr/lib64/R/library/BatchJobs/help/AnIndex
/usr/lib64/R/library/BatchJobs/help/BatchJobs.rdb
/usr/lib64/R/library/BatchJobs/help/BatchJobs.rdx
/usr/lib64/R/library/BatchJobs/help/aliases.rds
/usr/lib64/R/library/BatchJobs/help/paths.rds
/usr/lib64/R/library/BatchJobs/html/00Index.html
/usr/lib64/R/library/BatchJobs/html/R.css
