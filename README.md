# Sentinel
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

---

### Dependencies

1. **Create venv**
```zsh
python3 -m venv venv
```

2. **Activate venv**

MacOS/Linux
```zsh
source venv/bin/activate
```
Windows
```zsh
venv\Scripts\activate
```

3. **Install project dependencies**
```zsh
pip install -r requirements.txt
```

4. **Install your package in "editable mode"**
```zsh
pip install -e .
```

5. Now you are ready! Run:
```zsh
sentinel-start
```


### Documentation
Sentinel is a Swiss Army knife for cybersecurity, we try to keep it updated and add new features all the time.

After configuring venv and installing all dependencies, we can run the `sentinel-start` command. If everything has been done as explained above, a welcome message will appear with the sentinel logo and a link to this documentation.

Immediately after the welcome we can use the menu to use the different tools that are included within sentinel.

**Please note**, only tools are present in the menu, to see all the other commands on sentinel, scroll down to `commands`.