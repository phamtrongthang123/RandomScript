# Merge and Visualize Merged mask
For example we have tree folder like this: 
```
input/
├── 1
│   ├── 00000.png
│   ├── 00005.png
│   ├── 00010.png
│   ├── 00015.png
├── 2
│   ├── 00000.png
│   ├── 00005.png
│   ├── 00010.png
│   ├── 00015.png
├── 3
│   ├── 00000.png
│   ├── 00005.png
│   ├── 00010.png
│   ├── 00015.png
├── 4
│   ├── 00000.png
│   ├── 00005.png
│   ├── 00010.png
│   ├── 00015.png
└── 5
    ├── 00000.png
    ├── 00005.png
    ├── 00010.png
    ├── 00015.png
```
Where i=1,2,..5 is the `ith` object's mask, `num.png` is the mask of the ith object at frame `num`.

We want to merge/stack/overwrite/arrange with order masks so that could give a little tweak where the frontmost mask should be in the front.
```
output
├── 00000.png
├── 00005.png
├── 00010.png
├── 00015.png

```
## Usage
call: 
`python merge.py ./input --outdir ./output -o 1 2 3 4 5`
where `./input` is the path to input, `--outdit ./output` points to path to output folder, `-o 1 2 3 4 5` means order should be 1 first, then 2, 3, 4, 5 respectively. 

## Note:
But using `merge.py` only gives you the merged mask without blending. In order to see/visualize them you have to use vis.py. Just call `python vis.py` it will do that for you. Because of my laziness, if you defined output folder name different to ./output, you need to change the path I wrote inside `vis.py`.
