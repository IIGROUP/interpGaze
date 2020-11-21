# Controllable Continuous Gaze Redirection
[![Paper](http://img.shields.io/badge/paper-arxiv.2010.04513-blue.svg)](https://arxiv.org/abs/2010.04513)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/made%20with-python-blue.svg?style=flat-square)](https://www.python.org/)

Authors: Weihao Xia, Yujiu Yang, Jing-Hao Xue, Wensen Feng

Contact: weihaox@outlook.com

In this work, we present a novel method that works on both precise redirection and continuous interpolation. With the well-disentangled and hierarchically-organized latent space, we can adjust the order and strength of each attribute by altering the additional control vector. Furthermore, we contribute a high-quality gaze dataset, which contains a large range of gaze directions, to benefit researchers in related areas. 

This is a reproduction and may be slightly different from the original implementaion. If you found any problems including codes and processed data, please feel free to [pull requests](https://github.com/weihaox/InterpGaze/pulls) or [open issues](https://github.com/weihaox/InterpGaze/issues/new).

<details>
  <summary> Dependencies (click to expand) </summary>

## Dependencies

 pytorch == 1.7  
 numpy == 1.13.1  
 scipy == 0.19.1  
 matplotlib==2.2.4  
 pandas==0.24.2  
 imageio==2.5.0  
 requests==2.21.0  
 tqdm==4.31.1  
 numpy==1.16.3  
 scipy==1.2.1  
 colored==1.3.93  
 opencv_python==4.1.0.25  
 dlib==19.17.0  
 Pillow==6.2.2  
 tensorboardX==1.6  
 PyYAML==5.1.1  

</details>

## Dataset

We contribute a high-quality gaze dataset, which contains a large range of gaze directions and diversity on eye shapes, glasses, ages and genders, to benefit researchers in related areas. Samples are shown in the following pictures. We released the processed gaze patches on [Google Drive](https://drive.google.com/drive/folders/1ZZRcLiBPtfkohSlTHw7TE3CnntuFxoDT). 

<p align="center">
<img src="/asserts/examples/_MG_0568.jpg" width="150" height="100" /> &ensp; <img src="/asserts/examples/_MG_0569.jpg" width="150" height="100" /> &ensp; <img src="/asserts/examples/_MG_0570.jpg" width="150" height="100" /> 
</p>

We will release the dataset in the future.

The comparison of some popular gaze datasets is shown in the following table.

<p align="center">
<img src="/asserts/dataset.png"/> 
</p>

For fair comparison, we also train our model with the same dataset as in [He et. al.](https://github.com/HzDmS/gaze_redirection), which contains eye patch images parsed from [Columbia Gaze Dataset](http://www.cs.columbia.edu/~brian/projects/columbia_gaze.html). The dataset contains six subfolders, N30P/, N15P/, 0P/, P15P/, P30P/ and all/. Prefix 'N' means negative head pose, and 'P' means positive head pose. Folder all/ contains all eye patch images with different head poses.

You can directly download the dataset processed by [HzDmS](https://github.com/HzDmS) via this [link](https://drive.google.com/file/d/1tE3QfFjxtRco4ruLZwYyUhjyYSp2QIJL/view?usp=sharing) or use our provided scripts in the [repo](https://github.com/xiaweihao/InterpGaze/blob/master/tools/crop_eye.py) or on [Colab](https://colab.research.google.com/drive/119PGxpMFZPPKkA8rJGdksURTZgBUNHcj?usp=sharing), which is in keeping with their paper.

"We first run face alignment with dlib by parsing the face with 68 facial landmark points. After that, a minimal enclosed circle with center(x, y) and radius R was extracted from the 6 landmark points of each eye. The cropping region of the eye patch is set as a square box with center (x, y) and side length 3.4R. We flipped the right eye images horizontally to align with the left eye images. All eye patch images were resized to 64 × 64."


## Baselines

### He *et al.*

Photo-Realistic Monocular Gaze Redirection Using Generative Adversarial Networks proposed by [He *et al.*](https://github.com/HzDmS/gaze_redirection).
ICCV 2019. 

To train:
```
python main.py --mode train --data_path ./dataset/all/ --log_dir ./log/ --batch_size 32 --vgg_path ./vgg_16.ckpt
```

To test:
```
python main.py --mode eval --data_path ./dataset/0P/ --log_dir ./log/ --batch_size 21
```

Then, a folder named eval will be generated in folder ./log/. Generated images, input images and target images will be stored in eval/.

### Deepwarp

The official [DeepWarp Demo Page](http://163.172.78.19/) is currently on maintainace. Thus we use a Tensorflow [re-implement](https://github.com/BlueWinters/DeepWarp) of [DeepWarp](https://sites.skoltech.ru/compvision/projects/deepwarp/) by [BlueWinters](https://github.com/BlueWinters). 

We provide the dataset, pretrained model of He et.al. and Deepwarp at [BaiduYun](https://pan.baidu.com/s/1ia1M921-cz-63J0R5jzCjg). Please contact to acquire the password.

## Training

TBD

## Evaluation

TBD

## Experiments

This picture is illustration of interpolation between two given samples (green and blue). It can
be seen that other attributes like eyebrow, glass, hair and skin color are well-preserved in the redirected gaze images, which means our model works consistently well in generating person-specific gaze images.  Furthermore, since the encoder actually unfolds the natural image manifold, leading to a flat and smooth latent space that allows interpolation and even extrapolation, as shown in the last column.

<p align="center">
  <img src="/asserts/interpolation.png">
</p>

## Citation

If you find our work, code or pre-trained models helpful for your research, please consider to cite:

```
@inproceedings{xia2020gaze,
  title={Controllable Continuous Gaze Redirection},
  author={Xia, Weihao and Yang, Yujiu and Xue, Jing-Hao and Feng, Wensen},
  year={2020},
  booktitle={ACM MM},
}
```
