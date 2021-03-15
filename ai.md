# ai
## Jetson
* https://developer.nvidia.com/embedded/learn/jetson-ai-certification-programs#course_outline
* https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#troubleshooting
* https://github.com/NVIDIA/jetson-gpio
* https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit#:~:text=Setup%20Steps,on%20a%20non-conductive%20surface.&text=Connect%20your%20other%20computer%20to%20the%20developer%20kit's%20Micro-USB%20port.&text=Allow%201%20minute%20for%20the%20developer%20kit%20to%20boot.

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
## cuda and java
### Good Read
* https://stackoverflow.com/questions/22866901/using-java-with-nvidia-gpus-cuda
