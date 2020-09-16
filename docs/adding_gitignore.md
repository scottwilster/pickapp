# Process used to add a gitignore while maintaining working site
- I tried adding a general python repo gitignore but this crashed the website
  - it's why the original repo wouldn't work when I cloned it
- To figure out what I needed, I uncommented sections of the .gitignore I wanted to add at at time
  - you can see what you are about to remove by running:
```
git ls-files --ignored --exclude-standard -z
```
  - then you can actually removing by piping that list to the xargs function:
```
git ls-files --ignored --exclude-standard -z | xargs -0 git rm --cached
```

- note, to do it step by step I would keep branching off the PR branch, test it, and if it succeeds merge it back in
  - if not I can delete the branch and start back at the PR branch
