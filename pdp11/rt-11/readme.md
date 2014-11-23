# Installing RT-11 5.3 on SIMH

Original: http://gunkies.org/wiki/Installing_RT-11_5.3_on_SIMH

The installation manuals for RT-11 on bitsavers can be a bit scary and
longwinding, but installing RT-11 can be done quickly in emulation nowadays.

## Pre install

* Get an empty RL02 disk image where your installation will live.

```
wget --no-check-certificate https://dl.dropboxusercontent.com/u/16445500/simh/rt-11/rl02.dsk.gz
gunzip rl02.dsk.gz
cp rl02.dsk rl0.dsk
```

* Get the Mentec software kit distributed as RL02 image.

```
wget --no-check-certificate https://dl.dropboxusercontent.com/u/16445500/simh/rt-11/rtv53swre.tar.Z
uncompress rtv53swre.tar.Z
tar -xvf rtv53swre.tar
cp Disks/rtv53_rl.dsk rl1.dsk
```

* To get text out of your installation without having to set up KERMIT provide
an entry point for simh to print to

```
touch lpt.txt
```

* In case something goes wrong beyond this point you should be able to restart
quickly with

```
cp Disks/rtv53_rl.dsk rl1.dsk; cp rl02.dsk rl0.dsk
```
