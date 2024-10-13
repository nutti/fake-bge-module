# Fake Blender Game Engine (BGE) Python API module collection: fake-bge-module

fake-bge-module is the collections of the fake Blender Game Engine (BGE) Python
API modules for the code completion in commonly used IDEs.

*Note: The similar project for Blender is available on
[fake-bpy-module](https://github.com/nutti/fake-bpy-module) which targets
[Blender](https://www.blender.org/).*

*To realize the long support of this project, your support is helpful.*
*You can support the development of this project via*
**[GitHub Sponsors](https://github.com/sponsors/nutti)**.
*See [the contribution document](CONTRIBUTING.md) for the detail of*
*the support.*

## Requirements

fake-bpy-module requires Python 3.12.

## Install

fake-bge-module can be installed via a pip package, or pre-generated modules.
You can also generate and install modules manually.

### Install via pip package

fake-bge-module is registered to PyPI.  
You can install it as a pip package.

#### Install a latest package

If you install fake-bpy-module for Blender latest build (master branch daily
build powered by [nutti/upbge-daily-build](https://github.com/nutti/upbge-daily-build)),
run below command.

```sh
pip install fake-bge-module
```

or, specify version "latest".

```sh
pip install fake-bge-module-latest
```

#### Install a version specific package

If you want to install a version specific package, run below command.

```sh
pip install fake-bge-module-<version>
```

If you install fake-bge-module for UPBGE 0.2.5, run below command.

```sh
pip install fake-bge-module-0.2.5
```

*Note: For PyCharm users, change the value `idea.max.intellisense.filesize` in
`idea.properties` file to more than 2600 because some modules have the issue of
being too big for intelliSense to work.*

##### Supported UPBGE Version

|Version|PyPI|
|---|---|
|0.2.5|[https://pypi.org/project/fake-bge-module-0.2.5/](https://pypi.org/project/fake-bge-module-0.2.5/)|
|0.30|[https://pypi.org/project/fake-bge-module-0.30/](https://pypi.org/project/fake-bge-module-0.30/)|
|0.36|[https://pypi.org/project/fake-bge-module-0.36/](https://pypi.org/project/fake-bge-module-0.36/)|
|latest|[https://pypi.org/project/fake-bge-module/](https://pypi.org/project/fake-bge-module/)|
||[https://pypi.org/project/fake-bge-module-latest/](https://pypi.org/project/fake-bge-module-latest/)|

### Install via pre-generated modules

Download Pre-generated modules from [Release page](https://github.com/nutti/fake-bge-module/releases).

The process of installation via pre-generated modules is different by IDE.
See the installation processes as follows for detail.

* [PyCharm](docs/setup_pycharm.md)
* [Visual Studio Code](docs/setup_visual_studio_code.md)
* [All Text Editor (Install as Python module)](docs/setup_all_text_editor.md)

### Generate Modules Manually

You can also generate modules manually.
See [Generate Modules](docs/generate_modules.md) for detail.

## Change Log

See [CHANGELOG.md](CHANGELOG.md)

## Bug report / Feature request / Disscussions

If you want to report bug, request features or discuss about this add-on, see
[ISSUES.md](ISSUES.md).

## Contribution

If you want to contribute to this project, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Project Authors

### Owner

[**@nutti**](https://github.com/nutti)

Indie Game/Application Developer.  
Especially, I spend most time to improve Blender and Unreal Game Engine via
providing the extensions.

Support via [GitHub Sponsors](https://github.com/sponsors/nutti)

* CONTACTS: [Twitter](https://twitter.com/nutti__)
* WEBSITE: [Japanese Only](https://colorful-pico.net/)
