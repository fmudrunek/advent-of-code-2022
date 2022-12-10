# Day 7: No Space Left On Device ([link](https://adventofcode.com/2022/day/7))

## Input
A list of Unix comands and outputs that map a structure of a filesystem. E.g.
```
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
```

## Part 1
Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

## Part 2
Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?