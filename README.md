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

### Example notebook
![nb](https://user-images.githubusercontent.com/23008175/83876521-91f03800-a76b-11ea-8269-28f864e1394a.png)


* Running with `nbcat examples/example-cifar10.ipynb`:
<details>
    <summary> Output (click to expand)</summary>

```
                =========================================================================
   `markdown`   # CIFAR - 10 
                ## Decode data
                =========================================================================
   `markdown`   Activate virtual environment
                =========================================================================
        In [1]: %%bash
                source ~/kerai/bin/activate
                =========================================================================
   `markdown`   ### Imports
                =========================================================================
        In [2]: %matplotlib inline
                from helper import get_class_names, get_train_data, get_test_data, plot_images
                -------------------------------------------------------------------------
    `stderr`    Using TensorFlow backend.

                =========================================================================
   `markdown`   Get class names
                =========================================================================
        In [3]: class_names = get_class_names()
                class_names
                -------------------------------------------------------------------------
    `stdout`    Decoding file: data/batches.meta

        Out[3]: ['airplane',
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

![grep_cat](https://user-images.githubusercontent.com/23008175/89075159-2237ab80-d3b0-11ea-8872-d3361705833c.png)

* output of `nbcat':

![grep_nbcat](https://user-images.githubusercontent.com/23008175/89075189-34b1e500-d3b0-11ea-8fcd-6289cae6da17.png)


## Uninstall

```
pip uninstall nbcat
```

## License

Distributed under the MIT LICENSE. 

## Acknoledgement

Example notebook from: https://github.com/09rohanchopra/cifar10/blob/master/cifar10-basic.ipynb
