# Week 2 Experiment Protocol

## 1. Purpose
This protocol establishes how all Week 2 experiments will be conducted so that results are fair, consistent, and reproducible.

## 2. Dataset Splits
- Training: 45,000 CIFAR-10 images.
- Validation: 5,000 CIFAR-10 images.
- Test: 10,000 CIFAR-10 images.
- Small training subset: 4,500 images (10% of training data).

The training and validation splits will remain fixed across experiments. The test set will only be used for final evaluation, not for training, tuning, or selecting models.

## 3. Replicates
Every training condition will be repeated using at least three random seeds: 42, 123, and 2026.

Results will be reported as mean ± standard deviation.

## 4. Experimental Conditions
The following three methods will be compared:
1. Small CNN trained from scratch.
2. ImageNet-pretrained ResNet-18 with a frozen feature extractor and a newly trained linear classification head.
3. ImageNet-pretrained ResNet-18 with full fine-tuning.

Each method will be tested using:
- 100% of the training data (45,000 images).
- 10% of the training data (4,500 images).

## 5. Controls
The frozen ResNet-18 will serve as the baseline for comparison with the fine-tuned ResNet-18.

The from-scratch CNN will provide a baseline for evaluating the value of pretrained representations.

## 6. Pre-registered Metrics
**Primary metric:**
- Top-1 accuracy.

**Secondary metrics:**
- Macro-F1.
- Expected Calibration Error (ECE).

## 7. Experiment Register
Every experiment, including failed runs, will be recorded in `results/register.csv`.

Required columns:
- run_id
- config
- commit
- seed
- split
- metric
- outcome

## 8. Reproducibility
Random seeds, model configurations, data splits, and training settings will be recorded for every run.
