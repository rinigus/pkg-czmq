#!/bin/bash

set -e

VERSION=4.0.2

wget https://github.com/zeromq/czmq/releases/download/v$VERSION/czmq-$VERSION.tar.gz
tar xvf czmq-$VERSION.tar.gz

cd czmq-$VERSION

