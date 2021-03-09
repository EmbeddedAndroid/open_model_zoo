# ctdet_coco_dlav0_384

## Use Case and High-Level Description

CenterNet object detection model `ctdet_coco_dlav0_384` originally trained with PyTorch\*.
CenterNet models an object as a single point - the center point of its bounding box
and uses keypoint estimation to find center points and regresses to object size.
For details see [paper](https://arxiv.org/abs/1904.07850), [repository](https://github.com/xingyizhou/CenterNet/).

## Specification

| Metric                          | Value                                     |
|---------------------------------|-------------------------------------------|
| Type                            | Detection                                 |
| GFlops                          | 34.994                                    |
| MParams                         | 17.911                                    |
| Source framework                | PyTorch\*                                 |

## Accuracy

| Metric | Original model | Converted model |
| ------ | -------------- | --------------- |
| mAP    | 41.81%          | 41.61%            |

## Input

### Original Model

Image, name: `input.1`, shape: [1x3x384x384], format: [BxCxHxW]
where:

   - B - batch size
   - C - number of channels
   - H - image height
   - W - image width

Expected color order: BGR.
   Mean values: [104.04, 113.985, 119.85], scale values: [73.695, 69.87, 70.89].

### Converted Model

Image, name: `input.1`, shape: [1x3x384x384], format: [BxCxHxW]
where:

   - B - batch size
   - C - number of channels
   - H - image height
   - W - image width

Expected color order: BGR.

## Output

1. Object center points heatmap, name: `center_heatmap`. Contains predicted objects center point, for each of the 80 categories, according to MSCOCO\* dataset version with 80 categories of objects, without background label, mapping to class names provided in `<omz_dir>/data/dataset_classes/coco_00cl.txt` file.
2. Object size output, name: `width_height`. Contains predicted width and height for each object.
3. Regression output, name: `regression`. Contains offsets for each prediction.

## Legal Information

The original model is distributed under the following
[license](https://raw.githubusercontent.com/xingyizhou/CenterNet/master/LICENSE)

```
MIT License

Copyright (c) 2019 Xingyi Zhou
All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```