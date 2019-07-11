# QuantizationIndexModulation
A Python implementation of QIM method from "Data Hiding Codes" from Moulin and Koetter, 2005

## Content

* Contains a Python class QIM implementing the embedding and detection watermarking algorithms.
* $\delta$ is the quantization parameter.$x$ is the host sample vector, $y$ the quantized vector and $z$ the received (or modified) vector.
* QIM class applies a "Scalar-QIM" on each component of a vector $x$ where $m$ is a binary message vector

## Bibtex citation
```
@article{moulin2005data,
  title={Data-hiding codes},
  author={Moulin, Pierre and Koetter, Ralf},
  journal={Proceedings of the IEEE},
  volume={93},
  number={12},
  pages={2083--2126},
  year={2005},
  publisher={IEEE}
}
```
