# ml

## Terminilogy

- **Machine Learning**: Teaching computers to learn patterns from data without explicit programming
- **Linear Regression**: A method to predict continuous values using a straight line equation
- **Gradient Descent**: An optimization algorithm that finds minimum loss by following the steepest downhill direction
- **Training**: The process of teaching a model by showing it examples and adjusting parameters
- **Model**: The mathematical representation that learns patterns (here: a single linear layer)
- **Parameters**: The learnable values in a model (weights and biases)
- **Loss**: A measure of how wrong the model's predictions are
- **Epoch**: One complete pass through all training data
- **Forward Pass**: Computing predictions through the model
- **Backward Pass**: Computing gradients to know how to improve parameters
- **Optimization**: The process of finding the best parameters to minimize loss
- **Inference/Prediction**: Using a trained model to make predictions on new data
- **Convolution**: to roll or twist together. a **mathematical** operation where a **small matrix (filter)** slides over a **larger matrix (image)** and computes dot products.
- 
## Training Algorithm Terms

- **Loss Function**: Mathematical function that measures prediction error
- **MSE (Mean Squared Error)**: Loss function that squares the difference between predictions and actual values
- **Optimizer**: Algorithm that updates model parameters to reduce loss
- **SGD (Stochastic Gradient Descent)**: Simple optimizer that updates parameters using gradients
- **Learning Rate**: How much to change parameters each step (0.01 = small, careful steps)
- **Backpropagation**: Algorithm to compute gradients of loss with respect to all parameters
- **Gradients**: Partial derivatives showing how loss changes with parameter changes
- **Zero Gradients**: Clearing old gradient values before computing new ones
- **Step**: The optimizer's update operation (moving parameters in the right direction)

## Workflow

> ML workflow : Train → Save → Load → Predict! 🎯

## Regression 

### Regression Analsyis

- Primarily used for forecasting, predicting, and identifying relationships between variables

---
## nanoGPT
- https://github.com/karpathy/nanoGPT

### 6-layer Transformer with 6 heads in each layer

- ✔ The model has 6 stacked Transformer blocks
- ✔ In each block, it has 6 attention heads working in parallel

#### Total attention heads = 👉 6 layers × 6 heads = 36 attention heads

#### Why do this?
- More layers → deeper understanding
- More heads → richer view of relationships

But:
- More layers = more compute
- More heads = more memory
> So this is a medium-sized architecture, not tiny, not huge.
---

## AI Models
The algorithms themselves:
- **Traditional ML models:** Linear regression, Random Forest, SVM
- **Deep learning models:** CNNs (images), RNNs/LSTMs (sequences), Transformers (NLP)
- **Foundation models / Large Language Models:** GPT, LLaMA, Claude
  
## Training
## train and validation difference
In machine learning, "train" and "validation" refer to splits of the dataset used for different purposes during model training:
- **Train data:** The portion of the data (90% here) used to teach the model by adjusting its parameters (weights) through forward and backward passes. The model learns patterns from this data.
- **Validation data:** The remaining portion (10% here) used to evaluate the model's performance on unseen data during training. It helps monitor for overfitting (when the model performs well on train data but poorly on new data) and tune hyperparameters. Validation loss is checked periodically (e.g., every 250 iterations in this config) to decide if the model improves

---  
## RAG (Retrieval-Augmented Generation)
RAG is a technique where a language model (like GPT) doesn’t just generate text from its training data; it retrieves relevant information from external sources to produce more accurate, up-to-date, or context-specific answers
