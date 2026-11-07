##  Home Assistant 2026 

# Additional Implementation Notes

This integration requires System Monitor to be installed as an Integration, and each entity monitored to be specifically enabled in the configuration of System Monitor.

Changes to the System Monitor mean that some entities listed in the source code of the original implementation no longer work (at all).  
Some entities have been renamed, some have been removed entirely, some are dependant upon how your Home Assistant is implemented, the original example code
points to network interfaces that are implementation dependent.  For example network interfaces - enp3s0 is not present in my Proxmox hosted HomeAsisstant, but enp0s18 is.

  - Network throughput has been removed entirely as an entity in System Monitor (at least under a container deployment).
  - Processor temperature doesn't apply in a container.

# Making ha2munin work for you

Fork the repository and add/change the entities you want to monitor in ha2munin.py, then pull your fork into Home Assistant, follow the revised configuration and installation notes in the README.

# Post Home Assistant Upgrade 

The library must be reinstalled after every upgrade from the Advanced Terminal using 

  - pip install homeassistant

It should be possible to make ha2munin reinstall homeassistant, but I haven't figured that out yet.
