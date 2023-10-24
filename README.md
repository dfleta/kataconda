
conda-project gitignore

https://github.com/Anaconda-Platform/anaconda-project/blob/master/.gitignore 


https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf

https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html

https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-pkgs.html#

https://docs.conda.io/projects/miniconda/en/latest/

`bash Miniconda3-latest-Linux-x86_64.sh -b -u -p ~/miniconda3`

Crear un entorno virtual en el directorio local:

`conda create --prefix ./envs`

Para abreviar este prompt al activar el entorno:

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

[pytest]
testpaths =
    test

o:

pytest ./test

Sin los ficheros __ini__.py pytest no carbura con los módulos.
