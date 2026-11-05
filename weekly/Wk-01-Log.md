# Week 1 Learning Log

This week was my first time learning about neural networks and backpropagation, so honestly, the hardest part was getting familiar with all the new concepts. Before this internship, I had not worked much with deep learning, so ideas like forward propagation, loss functions, gradients, and the chain rule were all new to me.

At first, I found it difficult to understand how all the steps connected. I could follow individual pieces of the code, but I wasn't always sure how the model used its predictions to figure out what needed to change. Working through the derivation helped me understand that backpropagation is essentially how a neural network figures out how much each weight contributed to its error.

What helped me the most was implementing the process myself instead of only reading about it. Writing the forward and backward passes in NumPy made me think more carefully about what each calculation was doing. I also compared my gradients with PyTorch's gradients, which helped me check whether my implementation was correct. Seeing the differences come out so small was reassuring because it showed that my calculations were working.

By the end, I had a much better understanding of how information moves through a neural network and how gradients are used to update its weights. I still have a lot to learn, but this gave me a starting point for understanding how deep learning models actually work.
