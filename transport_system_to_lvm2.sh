перенос системы на lvm2

1. создание на диске файловой системы lvm
2. pvcreate /dev/sdb1
pvdisplay
3. vgcreate archi-volume /dev/sdb1
4. vgdisplay
lvcreate -L 1G --name home archi-volume
lvcreate -L 100M --name boot archi-volume
lvcreate -l100%FREE --name root archi-volume
lvdisplay
mkfs.ext4 /dev/archi-volume/home
mkfs.ext4 /dev/archi-volume/boot
mkfs.ext4 /dev/archi-volume/root
rsync --exclude=/dev --exclude=/proc --exclude=/sys -uvroght / /mnt/root/
