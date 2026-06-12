# ai

## Terminology

### GPT 

- Generative Pre-trained Transformer

### PEFT (Parameter-Efficient Fine-Tuning)

  - Parameter Efficient Fine Tuning is a library for efficiently adapting large pretrained models such as pre-trained policies (e.g., SmolVLA, π₀, …) to new tasks without training all of the model’s parameters while yielding comparable performance.

### Quantization

  - It converts high-precision numbers, such as 32-bit floating-point numbers (FP32), into lower-precision integers, like 8-bit or 4-bit integers (INT8) or (INT4)

### GPU

- CUDA Cores
  - CUDA cores are the general-purpose processing units inside an NVIDIA GPU. They execute many operations in parallel.
- Tensor Cores
  - are specialized hardware units designed specifically for matrix multiplication and accumulation, which are the core operations used in deep learning.
  - FP16
  - BF16 BF16 &rarr; (Brain Floating Point) Developed for AI workloads.
  - TF32 &rarr; TF32 (TensorFloat-32) - NVIDIA format used internally on newer GPUs.
  - INT8
  - INT4 (on newer GPUs)

```text
More Precision  <-----------------> Less Precision
FP32 → FP16 → INT8 → INT4
 ↑        ↑       ↑       ↑
More      Faster  Smaller Smallest
Accurate
```
- TOPS
  - Trillion Operations per second
  - Trillion Floating Point Operations per second
  - 

### Huggingface

- transformers
- accelerate
- bitsandbytes

###  ReLU (Rectified Linear Unit)
- Formula: max(0, x)
  - It's the simplest activation function — it passes positive values through unchanged, and kills negative values (outputs 0).
**ReLU (Rectified Linear Unit)** is one of the most commonly used **activation functions** in neural networks.
It is defined as:

$f(x)=max(0,x)$

This means:
* If the input is positive → output the same value.
* If the input is negative → output 0.

 ### LoRA (Low-Rank Adaptation) 
 
 * LoRA adapter is a small, lightweight file used to modify or fine-tune a large, pre-trained Artificial Intelligence model.

### Quantize f16 → Q4_K_M
This actually compresses the weights. Each weight value goes from 16 bits → ~4 bits.

#### What a weight looks like

```text
float16:  0.3421875   (stored as 16 bits = 2 bytes per number)
Q4_K_M:  "bucket 11"  (stored as ~4 bits = 0.5 bytes per number)
```
### safetensors

safetensors is HuggingFace's file format — model weights stored as raw float16 or float32 numbers in separate files (one per layer or shard). It's designed for training and fine-tuning in Python/PyTorch.

```text
qwen-base/
  model.safetensors     ← PyTorch tensors, float16
  config.json           ← architecture config
  tokenizer.json        ← tokenizer
  tokenizer_config.json

         convert_hf_to_gguf.py
                  ↓
qwen-linux-f16.gguf     ← single file, same float16 weights + everything bundled
```

### What's inside a GGUF file?

A GGUF file contains:

1. **Model weights** (the learned parameters)
2. **Model architecture information**
3. **Tokenizer vocabulary**
4. **Metadata** (model name, context size, etc.)


#### GGUF

* stands for **GPT-Generated Unified Format**.
* It is a file format used to store AI models in a way that tools like llama.cpp can load efficiently.
* — everything bundled into a single binary file: weights + tokenizer + architecture metadata. It's designed for efficient inference, especially on CPU.

### MoE (Mixture of Experts)

Mixture of Experts is a model architecture technique where not all parameters are used for every input.

#### Core idea

Instead of one big neural network, you have:
* multiple “expert” sub-networks
* a router (gating network) that decides which experts to use

### RLHF (Reinforcement Learning from Human Feedback)

Reinforcement Learning from Human Feedback is a training method used to align models with human preferences.

### logit 

- **logit** is the model's opinion score before it turns that opinion into a probability
- computes predictions (logits)

### Backward pass: 

- .backward() computes gradients via backpropagation
- Figure out how much each weight contributed to the error, so we know how to adjust it.
- Which weights and biases contributed to this loss?
- For example:

```text
Weight W1 contributed a little.
Weight W2 contributed a lot.
Weight W3 contributed almost nothing.
```
This becomes gradients:
```text
W1.grad = 0.1
W2.grad = 2.3
W3.grad = 0.01
```

The larger the gradient, the more that parameter should be adjusted.

### Optimizer 

1. **AdamW** updates the weights

When `optimizer.step()` is called the **optimizer** (AdamW in this case) uses the gradients to modify the weights.
Conceptually:

```text
Old weight = 3.0
Gradient  = -16
```

A simple optimizer might do:

```text
new_weight = old_weight - learning_rate × gradient
```

For example:

```text
new_weight = 3.0 - 0.1 × (-16)
           = 4.6
```
AdamW is more sophisticated than this. 
It:
- remembers previous gradients,
- adapts the learning rate for each weight,
- applies weight decay (the "W" part),

but the basic goal is the same:
- Use the gradient to move the weight in a direction that should reduce the loss.

---

#### Core idea

Instead of only training on correct answers, you train based on:

“Which answer do humans prefer?”

### Supervised fine-tuning (SFT)

### BLEU (Bilingual Evaluation Understudy)

* measures n-gram overlap between a model's output and a reference answer. Score range: 0–100 (higher is better).

### autoregression

Autoregression is a concept used in statistics, time series analysis, and machine learning where a value is predicted based on its own past values.

In simple terms:
👉 “The future depends on the past.”

Language models like GPT series generate text one token at a time, each step depending on previously generated tokens.
This is called autoregressive generation.

### Attention Layer and Linear Layer 

- They are different but related

### Vector Embedding

#### Vector Database

#### d_model

* d_model = number of features in the profile.
* Similar profiles → similar people.

#### embedding dimension

The **embedding dimension (`d_model`)** is the number of values used to represent a token (word/subword) as a vector.

For example, if `d_model = 4`:

| Token | Embedding Vector       |
| ----- | ---------------------- |
| cat   | [0.2, -0.5, 1.1, 0.7]  |
| dog   | [0.3, -0.4, 1.0, 0.6]  |
| car   | [-1.2, 0.8, -0.3, 0.1] |

#### Vocabulary size vs d_model

Suppose:

* Vocabulary = 50,000 tokens
* `d_model = 768`

Then the embedding table has size:
50,000 × 768  
Each token gets its own 768-dimensional vector.


### The attention head count 

* The **attention head count** is the number of independent attention mechanisms running in parallel inside a Transformer layer.

### Relationship with d_model

Suppose:

* d_model = 768
* heads = 12

Then each head gets:


$d_{head} = \frac{768}{12} = 64$.
$d_{head} = \frac{768}{12} = 64$.

So:

* Q size = 64
* K size = 64
* V size = 64

for each head.

### Why not use one huge head?

A single 768-dimensional head could theoretically learn everything, but in practice multiple smaller heads work better.

Think of it like:

* 1 head = one person trying to analyze a document.
* 12 heads = 12 specialists, each looking for different patterns.

### Q, K, V for multiple heads

For a token embedding:

$x = [0.2,\ 0.8,\ 0.1,\ 0.4]$.

Head 1:

$q_1 = xW_{Q1}$


$k_1 = xW_{K1}$


$v_1 = xW_{V1}$

Head 2 uses completely different learned matrices:

$q_2 = xW_{Q2}$

$k_2 = xW_{K2}$

$v_2 = xW_{V2}$

So the same token is viewed differently by each head.

### Typical values

| Model                | d_model    | Heads  |
| -------------------- | ---------- | ------ |
| Original Transformer | 512        | 8      |
| OpenAI GPT-2 Small   | 768        | 12     |
| OpenAI GPT-3 175B    | 12288      | 96     |
| Many modern LLMs     | 4096–16384 | 32–128 |

A useful intuition is:

> **Embedding dimension (d_model) determines how much information can be represented, while the number of attention heads determines how many different relationship patterns the model can examine simultaneously.**

### Tokenizer

### Positional Embedding

* **gpt2** - 1024 x 768 Matrix
* In older model max context is limited to the positional embeddings dimension. eg. gpt2 has positional embedding for 1024
* Rows (1024): This is the maximum context window. GPT-2 can take in a maximum sequence length of 1024 tokens, so it needs 1024 distinct position vectors.
* Columns (768): This is the embedding dimensionality. Every token's position is represented by a vector of 768 values (which matches the size of the token embeddings so they can be added together).

#### Modern Approch

* modern AI models abandoned GPT-2's **Learned Absolute Positional Embeddings**
* The most common technique used today is called **Rotary Position Embeddings (RoPE)**

##### Limitation with LAPE

1. **Memory Explosion:** A context window of **2 million** tokens would need a matrix with **2,000,000** rows. At a modern hidden dimension size of 4,096 or 8,192, that matrix alone would take up billions of parameters just to store position numbers.
1. **Hard Ceiling:** If a model only learned rows up to 1,000,000 during training, it would completely break down if you tried to input 1,000,001 tokens, because row 1,000,001 wouldn't exist.

### RoPE

* Rotary Position Embeddings (RoPE)

#### How Modern Models Do It: Rotary Embeddings (RoPE)

### Multilayer Perceptron

* MLP is a foundational type of artificial neural network. It is a "feedforward" network, meaning data flows in one direction—from input to output—without looping back.

### Blueprint (GPT-3 175B Hyperparameters)

---

### central finite differences

#### 🔹 Example: Central Difference Visualization

A simple function:

$f(x) = x^2$

Its exact derivative is:

$f'(x) = 2x$

Now we approximate the derivative at a point using:

$f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}$

#### 📊 Plot Idea

We will show:

* The curve ( f(x) = x^2 )
* Two nearby points ( x+h ) and ( x-h )
* The slope between them (central difference idea)

---

#### 📈 Visualization

---

#### 🔹 How to interpret this visually

Pick a point, say ( x = 1 ), and a small step ( h = 1 ):

* Left point: ( f(0) = 0 )
* Right point: ( f(2) = 4 )

Central difference slope:

$\frac{4 - 0}{2} = 2$


Exact derivative:

$2x = 2(1) = 2

So here, the approximation is exact (for quadratic functions, central difference is very accurate).

### chain rule

- The chain rule is a fundamental shortcut in calculus used to find the derivative (the rate of change) of a **composite function** —a function nested inside another function.

### Derivative

- At its core, a derivative is simply a tool that measures the instantaneous rate of change. It tells you exactly how fast one variable is changing in response to another at a specific, frozen moment in time.
- 
---

## Jetson 
### gpu statistics
[Heading IDs](#cuda)
```

tegrastats
```

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
* http://192.168.0.227:8888
```
sudo docker run --runtime nvidia -it --rm --network host --volume ~/nvdli-data:/nvdli-nano/data --device /dev/video0 nvcr.io/nvidia/dli/dli-nano-ai:v2.0.1-r32.5.0
sudo docker run --runtime nvidia -it --rm --network host --volume ~/nvdli-data:/nvdli-nano/data --device /dev/video0 nvcr.io/nvidia/dli/dli-nano-ai:v2.0.1-r32.4.4
192.168.55.1:8888
dlinano
```

Running docker with Raspberry PI CSI Camera
```bash
sudo docker run --runtime nvidia -it --rm --network host --volume ~/nvdli-data:/nvdli-nano/data --volume /tmp/argus_socket:/tmp/argus_socket --device /dev/video0 nvcr.io/nvidia/dli/dli-nano-ai:v2.0.1-r32.5.0
```
---
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
sudo apt-get update
sudo apt-get install git cmake libpython3-dev python3-numpy
git clone --recursive https://github.com/dusty-nv/jetson-inference
cd jetson-inference
mkdir build
cd build
cmake ../
make -j$(nproc)
sudo make install
sudo ldconfig

cd jetson-inference/tools
./download-models.sh
nvgstcapture-1.0 --camsrc=0 --cap-dev-node=0
```
---
## cuda
### cuda c
* https://smist08.wordpress.com/2019/04/03/playing-with-cuda-on-my-nvidia-jetson-nano/
### cuda thread blocks straming processor
* https://stackoverflow.com/questions/3519598/streaming-multiprocessors-blocks-and-threads-cuda
### cuda and java
#### Good Read
* https://stackoverflow.com/questions/22866901/using-java-with-nvidia-gpus-cuda
---
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
### Switch On Off FAN
Command|Description|
---|---|
echo 255 > /sys/devices/pwm-fan/target_pwm|ON Full Speed|
echo 0 > /sys/devices/pwm-fan/target_pwm|OFF|
echo 125 > /sys/devices/pwm-fan/target_pwm|Medium Speed|
## Jetbot
### Jetbot getting started
```
cd jetbot
./scripts/configure_jetson.sh
```
* https://jetbot.org/v0.4.3/software_setup/docker.html
***
## Tensor flow lite
* https://github.com/bsatrom/Particle_TensorFlowLite
***
#### cuda deviceQuery output {#cuda}
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

## Improvements

- Capabilities of AI is increasing day by dya.
---

