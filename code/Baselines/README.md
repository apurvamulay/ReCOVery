# Baselines
We provide the benchmark performance of methods using ReCOVery data:
- [LIWC](https://repositories.lib.utexas.edu/bitstream/handle/2152/31333/LIWC2015_LanguageManual.pdf?Sequence=3)
- [RST](https://www.aclweb.org/anthology/P14-1002.pdf)
- [Text-CNN](https://www.aclweb.org/anthology/D14-1181.pdf)
- [SAFE](https://arxiv.org/pdf/2003.04981.pdf)

## LIWC
LIWC (Linguistic Inquiry and Word Count) is a widely-accepted psycholinguistic lexicon. Given a news story, LIWC can count the words in the text falling into one or more of 93 linguistic, psychological, and topical categories, based on which 93 features are extracted and often classified within a traditional statistical learning framework. To obtain liwc_title.csv and liwc_body.csv necessary for running get_best_liwc.py, please download the LIWC software at https://liwc.wpengine.com/.

## RST
RST (Rhetorical Structure Theory) organizes a piece of content as a tree that captures the rhetorical relation among its phrases and sentences. We use a [pretrained RST parser](https://github.com/jiyfeng/DPLP}) to obtain the tree for each news article and count each rhetorical relation (in total, 45) within a tree, based on which 45 features are extracted (saved as rst-features.npy) and classified in a traditional statistical learning framework.

## Text-CNN
Text-CNN relies on a Convolutional Neural Networks for text classification, which contains a convolutional layer and max pooling.

## SAFE
SAFE is a neural-network-based method that utilizes news multimodal information for fake news detection, where news representation is learned jointly by news textual and visual information along with their relationship. SAFE facilitates recognizing the news falseness in its text, images, and/or the "irrelevance" between the text and images. Original codes of SAFE are from: https://github.com/Jindi0/SAFE. Please cite the following paper if you use the codes.
```
@inproceedings{zhou2020multimodal,
  title={SAFE: Similarity-Aware Multi-modal Fake News Detection},
  author={Zhou, Xinyi and Wu, Jindi and Zafarani, Reza},
  booktitle={The 24th Pacific-Asia Conference on Knowledge Discovery and Data Mining},
  year={2020},
  organization={Springer}
}
```

## Implementation Details
The overall dataset is randomly divided into training and testing datasets with a proportion of 0.8:0.2. As the dataset has an unbalanced distribution between reliable and unreliable news articles (~2:1), we evaluate the prediction results in terms of precision, recall, and the F1 score. For methods relying on traditional statistical learners, multiple well-established classifiers are adopted in our experiments: Logistic Regression (LR), Naive Bayes (NB), K-Nearest Neighbor (KNN), Random Forest (RF), Decision Tree (DT), and Support Vector Machines (SVM). Hyperparameter setting can be seen in the code files.

## Results



