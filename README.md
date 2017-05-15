# pkg-zmq
RPM packaging of CZMQ for Sailfish

To get the sources, run `download.sh`

To build and install:

```
export SFARCH=armv7hl
mb2 -t SailfishOS-$SFARCH -s ../rpm/czmq.spec build
sb2 -t SailfishOS-$SFARCH -m sdk-install -R rpm -i <INSERT-PATH>/czmq*$SFARCH.rpm
```

