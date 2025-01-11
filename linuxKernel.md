# Linux Kernel

## What is `alldefconfig` and `savedefconfig`

This patch set introduce "alldefconfig".
alldefconfig create a configuration with all values set
to default values.
This can be usefull when we check if we do have a sane
set of default values. Rhe config can be inspected
using menuconfig.

The patches also introduce "savedefconfig" which
reads the current configuration and save it
as a minimal configuration.
