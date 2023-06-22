# Producing Trusted Graphs in Online Social Networks using Learning Automata (Implementation of a paper)

## Description of the Project
People have been increasingly using online social networks (OSNs) to socialize and stay in touch with their friends, family members, colleagues or other ones around the world. To increase consumers' quality of service and experience, OSNs require trust evaluation models and algorithms. Graph-based techniques account for the majority of known ways in which the trust value is derived using a trusted graph. This project is an implementation of the paper entitled _"An automata algorithm for generating trusted graphs in online social networks"_ which combines graph-based and artificial intelligence methodologies to develop a hybrid model for enhancing OSN coverage and accuracy.

## Datasets
The implemented algorithm has been experimented on two datasets, containing trust relations between users, obtained from real-world social networks named Advogato and BitCoin. Due to the fact that the datasets are labeled using linguistical (in Advogato) or discrete numerical labels out of the [0:1] range (in BitCoin) which is commonly considered in the realm of trust estimation in online social networks, the dataset labels are transferred in order to map them to continuous trust values between 0 and 1. In this regard, the linguistical labels in Advogato are mapped to trust values of 1.0, 0.8, 0.6 and 0.4, and discrete trust values in BitCoin are mapped using a linear transformation function clearly defined in the main function.

## Reference
ref: @article{fatehi2022automata,
  title={An automata algorithm for generating trusted graphs in online social networks},
  author={Fatehi, Nina and Shahhoseini, Hadi Shahriar and Wei, Jesse and Chang, Ching-Ter},
  journal={Applied Soft Computing},
  volume={118},
  pages={108475},
  year={2022},
  publisher={Elsevier}
}
