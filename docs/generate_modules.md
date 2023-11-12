<!-- markdownlint-disable MD024 -->

# Generate Modules

This document shows the procedure for generating modules by yourself.  
You can choose the method to generate modules.

1. [Case 1: Use utility script](#case-1-use-utility-script)
2. [Case 2: Do it yourself all procedures](#case-2-do-it-yourself-all-procedures)

## Pre-requirement

### Python Version

The generating script can be run on Python >= 3.7.
Check your Python version is >= 3.7.

#### Install requirement packages

The generation script uses the packages listed on
[requirements.txt](../requirements.txt).  
Execute below command to install requirement packages.

```bash
git clone https://github.com/nutti/fake-bge-module.git
cd fake-bge-module
pip install -r requirements.txt
```

### Setup IDE

After generating modules, you need to setup IDE to enable a code completion.

* [PyCharm](docs/setup_pycharm.md)
* [Visual Studio Code](docs/setup_visual_studio_code.md)
* [All Text Editor (Install as Python module)](docs/setup_all_text_editor.md)

## Case 1: Use utility script

### 1. Download UPBGE binary

Download UPBGE binary from [UPBGE official site](https://upbge.org/).
Download UPBGE whose version is the version you try to generate modules.

### 2. Download UPBGE sources

```bash
git clone https://github.com/UPBGE/upbge.git
```

### 3. Download fake-bge-module sources

Download the fake-bge-module sources from GitHub.

Use Git and clone fake-bge-module repository.

```bash
git clone https://github.com/nutti/fake-bge-module.git
```

Or, you can download .zip file from GitHub.

[https://github.com/nutti/fake-bge-module/archive/master.zip](https://github.com/nutti/fake-bge-module/archive/master.zip)

### 4. Run script

<!-- markdownlint-disable MD013 -->
```bash
cd fake-bge-module/src
bash gen_module.sh <source-dir> <upbge-dir> <branch/tag/commit> <upbge-version> <output-dir> <mod-version>
```
<!-- markdownlint-enable MD013 -->

* `<source-dir>`: Specify UPBGE sources directory.
* `<upbge-dir>`: Specify UPBGE binary directory.
* `<branch/tag/commit>`: Specify target UPBGE source's branch for the
  generating modules.
  * If you want to generate modules for 0.2.5, specify `v0.2.5`
  * If you want to generate modules for newest UPBGE version, specify `master`
* `<blender-version>`: Specify blender version.
* `<output-dir>`: Specify directory where generated modules are output.
* `<mod_version>`: Modify APIs by using patch files located in `mods` directory.
  * If you specify `0.2.5`, all patch files under `mods/0.2.5` will be used.
  * Files located in `mods/common` directories will be used at any time.

#### Specify Python interpreter

By default, this command uses Python interpreter by calling `python` command.  
If you want to use other Python interpreter, you can specify by `PYTHON_BIN`
environment variable.

<!-- markdownlint-disable MD013 -->
```bash
PYTHON_BIN=/path/to/python3.7 bash gen_module.sh <source-dir> <upbge-dir> <branch/tag/commit> <output-dir> <mod-version>
```
<!-- markdownlint-enable MD013 -->

## Case 2: Do it yourself all procedures

### 1. Download UPBGE binary

Download UPBGE binary from [UPBGE official site](https://upbge.org/).  
Download UPBGE whose version is the version you try to generate modules.  
Place UPBGE binary to some directory.  
In this tutorial, UPBGE binary assumes to be placed on `/workspace/upbge-bin`.
(i.e. UPBGE executable is located on `/workspace/upbge-bin/blender`)

```bash
export WORKSPACE=/workspace
export UPBGE_BIN=${WORKSPACE}/upbge-bin
export UPBGE_SRC=${WORKSPACE}/upbge
```

### 2. Download UPBGE sources

```bash
cd ${WORKSPACE}
git clone https://github.com/UPBGE/upbge.git
```

### 3. Change to the target branch/tag/commit

Be sure to match the version between sources and binary.
If you try to generate modules for 0.2.5, you should use `git checkout v0.2.5`.

```bash
cd ${UPBGE_SRC}
git checkout [branch/tag/commit]
```

### 4. Generate .rst documents

Generated .rst documents are located on `${UPBGE_SRC}/doc/python_api/sphinx-in`.

<!-- markdownlint-disable MD013 -->
```bash
${UPBGE_BIN}/blender --background --factory-startup -noaudio --python doc/python_api/sphinx_doc_gen.py
```
<!-- markdownlint-enable MD013 -->

### 5. Download fake-bge-module sources

Download the fake-bge-module sources from GitHub.

Use Git and clone fake-bge-module repository.

```bash
cd ${WORKSPACE}
git clone https://github.com/nutti/fake-bge-module.git
```

Or, you can download .zip file from GitHub.

[https://github.com/nutti/fake-bge-module/archive/master.zip](https://github.com/nutti/fake-bge-module/archive/master.zip)

### 6. Generate mod files

<!-- markdownlint-disable MD013 -->
```bash
cd fake-bge-module/src

mkdir -p mods/generated_mods
${BLENDER_BIN}/blender --background --factory-startup -noaudio --python-exit-code 1 --python gen_modfile/gen_external_modules_modfile.py -- -m addon_utils -o mods/generated_mods/gen_modules_modfile
${BLENDER_BIN}/blender --background --factory-startup -noaudio --python-exit-code 1 --python gen_modfile/gen_external_modules_modfile.py -- -m keyingsets_builtins -a -o mods/generated_mods/gen_startup_modfile

mkdir -p mods/generated_mods/gen_bgl_modfile
python gen_modfile/gen_bgl_modfile.py -i ${BLENDER_SRC}/source/blender/python/generic/bgl.c -o mods/generated_mods/gen_bgl_modfile/bgl.json
```
<!-- markdownlint-enable MD013 -->

* `<upbge-version>`: Specify UPBGE version.

#### 7. Generate modules

<!-- markdownlint-disable MD013 -->
```bash
python gen.py -i <input-dir> -o <output-dir> -f <format> -b <upbge-version> -m <mod-version>
```
<!-- markdownlint-enable MD013 -->

* `-i <input-dir>`: Specify input directory (The directory where .rst files are
  located in process 4). In this document, `<input-dir>` should be
  `${UPBGE_SRC}/doc/python_api/sphinx-in`.
* `-o <output-dir>`: Specify output directory. (The directory where generated
  files will be located)
* `-d`: Dump internal data structures to `<output-dir>` as the files name with
  suffix `-dump.json`
* `-f <format>`: Format the generated code by `<format>` convention.
  * `pep8`: Format generated code by pep8.
* `-b <upbge-version>`: Specify upbge version.
* `-m <mod-version>`: Modify APIs by using patch files located in `mods` directory.
  * If you specify `0.2.5`, all patch files under `mods/0.2.5` will be used.
  * Files located in `mods/common` directories will be used at any time.
