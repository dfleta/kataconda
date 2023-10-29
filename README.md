
Kata gestión entornos virtuales con (mini)Conda
===============================================


## conda-project gitignore

[gitignore](https://github.com/Anaconda-Platform/anaconda-project/blob/master/.gitignore)

https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf

https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html

https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-pkgs.html#

https://docs.conda.io/projects/miniconda/en/latest/

`bash Miniconda3-latest-Linux-x86_64.sh -b -u -p ~/miniconda3`

## Crear un entorno virtual en el directorio local:

`conda create --prefix ./envs`

#### Para abreviar este prompt al activar el entorno:

`(/Users/USER_NAME/research/data-science/PROJECT_NAME/envs) $`

modify the env_prompt setting in your .condarc file:

`$ conda config --set env_prompt '({name})'`

```bash
$ conda env list
# conda environments:
#
                      *  /home/davidg/Escritorio/codigo/loose_change/loose_change/envs
base                     /home/davidg/miniconda3


conda activate ./envs

conda list

conda search python

conda install python=3.11.5

# (3.12 daba problemas de dependencias con pytest)

conda list

conda install pytest

# editar pytest.ini para excluir directorios test de conda

conda deactivate
```


-------------------------

Para evitar que pytest ejecute los test del directorio envs de conda:
crear el fichero init.py e incluir:

```
[pytest]
testpaths =
    test
```

o ejecutar:

`pytest ./test``

Sin los ficheros `__ini__.py` pytest no carbura con los módulos.

Con el entorno activado:

`$ conda env export > environment.yml`

## Importar entorno

Para instalar un entorno exportado entre plataformas (OSX, Linux) eliminar del `environment.yml` la parte específica de la versión de los paquetes:

```
dependencies:
  - pytest=7.4.0=py311h06a4308_0 <=>  pytest=7.4.0
  - python=3.11.5
```

He modificado en `environment.yml` el nombre del entorno y del prefix para dejarlo en env. Mejor darle un nombre que lo identifique en la lista de entornos.

```
name: env   <==
channels:
  - defaults
dependencies:
  - pytest=7.4.0
  - python=3.11.5
prefix: env <==
```

He dejado en `environment.yml` sólo los paqueteo instaladas explícitamente por mi en el entorno para evitar que se instalen paquetes no compatibles entre plataformas. El comando para crear el fichero de entorno es:

`conda env export --from-history > environment.yml`

pero este te permite visualizarlo antes de entubarlo:

`conda env export --from-history`

aunque la salida no es exactamento como indica el manual de conda.


### Crear el entorno desde un fichero:

`conda env create -f environment_manual.yml`

Para indicar el nombre del entorno:

`conda env create -n env -f environment_manual.yml`

`conda activate env`

```bash
conda env list
# conda environments:
#
base                     /Users/usu/miniconda3
env                   *  /Users/usu/miniconda3/envs/env
test                     /Users/usu/miniconda3/envs/test
```

### Para renombrar el entorno:

The base environment and the currently-active environment cannot be renamed.

https://docs.conda.io/projects/conda/en/latest/commands/rename.html

```bash
$ conda deactivate
(base) $ conda rename -n env kataconda
Source:      /Users/usu/miniconda3/envs/env
Destination: /Users/usu/miniconda3/envs/kataconda

$ conda env list
# conda environments:
#
base                  *  /Users/usu/miniconda3
kataconda                /Users/usu/miniconda3/envs/kataconda
```


https://www.freecodecamp.org/news/what-is-a-channel-in-conda/

`conda config --show channels`

To install a package using the default channel, you use the conda install 

`conda install package-name`

`conda install -c conda-forge jupyterlab`

You can add a channel to the list of channels using the conda config --add channels channel-name command. That is:

`conda config --add channels conda-forge`

### Canales: JupyterLab

If you install JupyterLab with conda or mamba, we recommend using the conda-forge channel.

Once installed, launch JupyterLab with:

jupyter lab

Buscar jupyter en el canal recomendado conda-forge pues está más actualizado que en el defautl pkgs/main

```bash
$ conda search -c conda-forge jupyterlab
jupyterlab                     4.0.7    pyhd8ed1ab_0  conda-forge         

 $ conda search jupyterlab
jupyterlab                     3.6.3  py39hecd8cb5_0  pkgs/main
```

`conda install -c conda-forge jupyterlab`

#### Averiguar si un paquete está en un entorno:

```bash
$ conda list -n kataconda jupyterlab
# packages in environment at /Users/usu/miniconda3/envs/kataconda:                   
# Name                    Version                   Build    Channel
jupyterlab                4.0.7              pyhd8ed1ab_0    conda-forge           
jupyterlab_pygments       0.2.2              pyhd8ed1ab_0    conda-forge
jupyterlab_server         2.25.0             pyhd8ed1ab_0    conda-forge     
```


### Añadrr canal

Añado el canal conda-forge a mi sistema:

```bash

$ conda config --add channels conda-forge`

$ conda config --show channels
channels:
  - conda-forge
  - defaults

# funciona?
$ conda search pytest
pytest                         7.4.0    py39hecd8cb5_0  pkgs/main     <===     
pytest                         7.4.0    pyhd8ed1ab_0  conda-forge     <===   
pytest                         7.4.1    pyhd8ed1ab_0  conda-forge         
pytest                         7.4.2    pyhd8ed1ab_0  conda-forge      
```

#### Quitar un canal

`conda config --remove channels 'conda-forge'`


### Actualiar un paquete instalado en el entorno:

```bash
$ conda list -n kataconda pytest
# packages in environment at /Users/usu/miniconda3/envs/kataconda:
#
# Name                    Version         Build  Channel
pytest                    7.4.0           py311hecd8cb5_0  

(kataconda)$ conda update pytest   (env activado)

## Package Plan ##
  environment location: /Users/usu/miniconda3/envs/kataconda
  added / updated specs:
    - pytest
The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    colorama-0.4.6             |     pyhd8ed1ab_0          25 KB  conda-forge
    pytest-7.4.2               |     pyhd8ed1ab_0         239 KB  conda-forge  
    
    <=== los baja del canal donde estan más actualizados!!

$ conda list -n kataconda pytest
# packages in environment at /Users/usu/miniconda3/envs/kataconda:
#
# Name                    Version                   Build  Channel
pytest                    7.4.2              pyhd8ed1ab_0    conda-forge
```

### Actualizar conda:

`conda update -n base -c defaults conda`

Or to minimize the number of packages updated during conda update use:

**DESDE EL ENTORNO BASE!!!**

`(base)$ conda install conda=23.9.0`

