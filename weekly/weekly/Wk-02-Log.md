# Week 2 Log

## Research Progress and Reflection

During Week 2, I worked on narrowing down my research question for Fari, InGen Dynamics' indoor companion robot, while also experimenting with different image recognition models. Fari may encounter unfamiliar objects and changing indoor environments, so reliable open-vocabulary recognition is important.

One question I initially considered was whether fine-tuning a vision-language model on labeled household images could improve recognition accuracy. However, I decided that focusing only on accuracy would not fully address Fari's needs. A model could perform well on familiar images but still struggle with unfamiliar objects or different environmental conditions. I wanted to investigate not only whether predictions were correct, but also whether the model's confidence was reliable. This led me to focus on how accurately and reliably zero-shot vision-language models recognize objects in Fari-like environments, and whether adaptation can improve their performance without reducing reliability.

For the technical portion, I trained a CNN from scratch and experimented with pretrained ResNet-18 models using both frozen feature extraction and full fine-tuning. I compared performance using the full CIFAR-10 training set and a 10% subset, repeating each experiment with three random seeds. I also explored overfitting and tested data augmentation, weight decay, and early stopping.

One of the biggest challenges was the time required to run experiments with multiple epochs. Google Colab sometimes disconnected my runtime or restricted GPU access, which meant I had to reconnect and make sure my experiments had completed correctly. Running multiple seeds also took longer than I initially expected. I learned to monitor training and validation loss and accuracy rather than relying only on final test accuracy.

Overall, this week helped me better understand the practical challenges of training and evaluating models. It also showed me why consistent experiments and reliable evaluation methods are important when choosing models for real-world applications.
