FROM python:3.5-alpine

RUN apk add --update curl make gcc g++ libstdc++ freetype-dev libpng-dev tk-dev libgfortran gfortran \
    && rm -rf /var/cache/apk/*

RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN pip install --upgrade pip

# Original:
# https://github.com/catholabs/docker-alpine
# https://github.com/drillan/docker-alpine-scipy
RUN mkdir -p /tmp/build \
    && cd /tmp/build/ \
    && curl -O http://www.netlib.org/blas/blas-3.6.0.tgz \
    && curl -O http://www.netlib.org/lapack/lapack-3.6.1.tgz \
    && tar xzf blas-3.6.0.tgz \
    && tar xzf lapack-3.6.1.tgz \
    && cd /tmp/build/BLAS-3.6.0/ \
    && gfortran -O3 -std=legacy -m64 -fno-second-underscore -fPIC -c *.f \
    && ar r libfblas.a *.o \
    && ranlib libfblas.a \
    && mv libfblas.a /tmp/build/. \
    && cd /tmp/build/lapack-3.6.1/ \
    && sed -e "s/frecursive/fPIC/g" -e "s/ \.\.\// /g" -e "s/^CBLASLIB/\#CBLASLIB/g" make.inc.example > make.inc \
    && make lapacklib \
    && make clean \
    && mv liblapack.a /tmp/build/. \
    && cd / \
    && export BLAS=/tmp/build/libfblas.a \
    && export LAPACK=/tmp/build/liblapack.a

ENV BLAS=/tmp/build/libfblas.a
ENV LAPACK=/tmp/build/liblapack.a

RUN pip install cython numpy

RUN pip install scipy pandas matplotlib boto3 seaborn statsmodels \
    && rm -rf /tmp/build

ENTRYPOINT ["python", "/opt/project/main.py"]
