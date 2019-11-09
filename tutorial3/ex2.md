####1
  Look into [this short explanation on how memory works](../extras/brief_on_memory.md)    
####2. For linux you can try `sudo dmidecode --type 17 | less`, it will give you info about your pc memory.
Probably you will see line like that: `Speed: 2400 MT/s` where `MT/s` means Mega Transfers per second.
Since each transfer carry 64 bits of information (Memory bus width) we can estimate that in this case
`2.4*64 = 153.6 Gb/s = 19.2 GB/s`

####3. `sudo hdparm -Tt /dev/YOUR_DISK_DEVICE` - simple linux benchmark to check your disk speed (also memory speed) 
