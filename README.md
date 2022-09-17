# NBCAT

`nbcat` is a self-contained command line tool for viewing jupyter notebook files in terminal. It parses notebook's underlying json content, hence it runs *without the dependency of jupyter/ipython core*. 

## Install

```
pip install git+https://github.com/ktw361/nbcat.git
```

No python? Checkout the [c++ implementation](https://github.com/ktw361/jcat).


## Usage

```
nbcat example.ipynb
```

### Example notebook ([link](https://github.com/ktw361/nbcat/blob/master/examples/example-cifar10.ipynb))
![nb](https://user-images.githubusercontent.com/23008175/190876086-e53da30a-8f3f-40b7-83a4-5ff4fecafa4a.png)

* Running with `nbcat examples/example-cifar10.ipynb -a`:
<details>
    <summary> Output (click to expand)</summary>

```
=========================================================================
# `markdown`
# CIFAR - 10 
## Decode data
=========================================================================
# `markdown`
Activate virtual environment
=========================================================================
# In [1]: 
%%bash
source ~/kerai/bin/activate
=========================================================================
# `markdown`
### Imports
=========================================================================
# In [2]: 
%matplotlib inline
from helper import get_class_names, get_train_data, get_test_data, plot_images
-------------------------------------------------------------------------
# `stderr`
Using TensorFlow backend.

=========================================================================
# `markdown`
Get class names
=========================================================================
# In [3]: 
class_names = get_class_names()
class_names
-------------------------------------------------------------------------
# `stdout`
Decoding file: data/batches.meta

# Out[3]: 
['airplane',
 'automobile',
 'bird',
 'cat',
 'deer',
 'dog',
 'frog',
 'horse',
 'ship',
 'truck']
=========================================================================
```
</details>


### Use nbcat with grep to get rid of annoying image datas

* output of `cat`:

![grep_cat](https://user-images.githubusercontent.com/23008175/190876201-4e929b48-d604-4761-aae1-c47753ab5ab6.png)

* output of `nbcat':

![grep_nbcat](https://user-images.githubusercontent.com/23008175/190876265-84a57e6c-8919-4970-9755-734dd78f86f9.png)


## Uninstall

```
pip uninstall nbcat
```

## License

Distributed under the MIT LICENSE. 

## Acknoledgement

Example notebook from: https://github.com/09rohanchopra/cifar10/blob/master/cifar10-basic.ipynb
