# ai
## Jetson
* https://developer.nvidia.com/embedded/learn/jetson-ai-certification-programs#course_outline
* https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#troubleshooting
* https://github.com/NVIDIA/jetson-gpio
* [jetson nano](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit#:~:text=Setup%20Steps,on%20a%20non-conductive%20surface.&text=Connect%20your%20other%20computer%20to%20the%20developer%20kit's%20Micro-USB%20port.&text=Allow%201%20minute%20for%20the%20developer%20kit%20to%20boot)
### L4T U
> L4T Ubuntu is a version of Linux based on nvidia's linux for tegra project
### jetpack version
```
sudo apt-cache show nvidia-jetpack
```
* https://forums.developer.nvidia.com/t/how-to-check-the-jetpack-version/69549/9
#### jetpack 5 download
* https://developer.download.nvidia.com/embedded/L4T/r32_Release_v5.1/r32_Release_v5.1/Jeston_Nano_2GB/jetson-nano-2gb-jp451-sd-card-image.zip

### course link
* https://courses.nvidia.com/courses/course-v1:DLI+S-RX-02+V2/
* https://ngc.nvidia.com/catalog/containers/nvidia:dli:dli-nano-ai
* 192.168.55.1:8888
```
sudo docker run --runtime nvidia -it --rm --network host --volume ~/nvdli-data:/nvdli-nano/data --device /dev/video0 nvcr.io/nvidia/dli/dli-nano-ai:v2.0.1-r32.5.0
sudo docker run --runtime nvidia -it --rm --network host --volume ~/nvdli-data:/nvdli-nano/data --device /dev/video0 nvcr.io/nvidia/dli/dli-nano-ai:v2.0.1-r32.4.4
192.168.55.1:8888
dlinano
```
#### no cuda found issue
```
cd /usr/local/cuda/samples/1_Utilities/deviceQuery
sudo make
./deviceQuery
```
* https://forums.developer.nvidia.com/t/pytorch-found-no-nvidia-driver-on-your-system-jetson-nano/169477/12
### gpio
* https://maker.pro/nvidia-jetson/tutorial/how-to-use-gpio-pins-on-jetson-nano-developer-kit
### jetbot
* https://jetbot.org/master/
- - - 
## Coral ai
## python
* https://jupyter.org/

### Jetson Nano commands
```
git clone --recursive https://github.com/dusty-nv/jetson-inference
cd jetson-inference
docker/run.sh

cd jetson-inference/tools
./download-models.sh
nvgstcapture-1.0 --camsrc=0 --cap-dev-node=0
```
---
## cuda
### cuda c
*https://smist08.wordpress.com/2019/04/03/playing-with-cuda-on-my-nvidia-jetson-nano/
### cuda and java
#### Good Read
* https://stackoverflow.com/questions/22866901/using-java-with-nvidia-gpus-cuda

## tensorrt
> SDK for deep learning inference from Nvidia

> It can run from embedded to data centers 

### Ref.

* https://developer.nvidia.com/tensorrt
* https://developer.nvidia.com/blog/speeding-up-deep-learning-inference-using-tensorrt/


### deep learning traninng and inference
> Training - process of creating model

> Inference - process of using tranined model to make a prediction
## PyTorch
> PyTorch is an open source machine learning library
> PyTorch is needed only for transfer learning
> PyTorch is needed for training the model
---
## jetson nano getting started
1. Docker container
2. Compiling locally

### 1. Docker setup(Usually slow)

### 2. Compiling locally steps
#### Model download
```
$ cd jetson-inference/tools
$ ./download-models.sh
```
#### Ref.
* https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md

---
## Disabling the Desktop GUI
This will freeup 800MB of RAM. 
> Stop the desktop
```
sudo init 3  
```
> Restart the desktop
```
sudo init 5
```
To persist the setting
```
$ sudo systemctl set-default multi-user.target     # disable desktop on boot
$ sudo systemctl set-default graphical.target      # enable desktop on boot
```
* https://github.com/dusty-nv/jetson-inference/blob/master/docs/pytorch-transfer-learning.md#disabling-the-desktop-gui

---
#### cuda deviceQuery output
```

 CUDA Device Query (Runtime API) version (CUDART static linking)

Detected 1 CUDA Capable device(s)

Device 0: "NVIDIA Tegra X1"
  CUDA Driver Version / Runtime Version          10.2 / 10.2
  CUDA Capability Major/Minor version number:    5.3
  Total amount of global memory:                 1972 MBytes (2067648512 bytes)
  ( 1) Multiprocessors, (128) CUDA Cores/MP:     128 CUDA Cores
  GPU Max Clock rate:                            922 MHz (0.92 GHz)
  Memory Clock rate:                             13 Mhz
  Memory Bus Width:                              64-bit
  L2 Cache Size:                                 262144 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(65536), 2D=(65536, 65536), 3D=(4096, 4096, 4096)
  Maximum Layered 1D Texture Size, (num) layers  1D=(16384), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(16384, 16384), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total number of registers available per block: 32768
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 1 copy engine(s)
  Run time limit on kernels:                     Yes
  Integrated GPU sharing Host Memory:            Yes
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Disabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Compute Preemption:            No
  Supports Cooperative Kernel Launch:            No
  Supports MultiDevice Co-op Kernel Launch:      No
  Device PCI Domain ID / Bus ID / location ID:   0 / 0 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 10.2, CUDA Runtime Version = 10.2, NumDevs = 1
Result = PASS

```
