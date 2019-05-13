from skbuild import setup

setup(
    name = 'mypylib',
    version = '1.0',
    cmake_with_sdist = True,
    cmake_args=['-DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.9'],
    packages = ['mypylib'],
    zip_safe = False
)
