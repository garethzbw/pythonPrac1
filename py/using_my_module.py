import my_module

from my_module import __version__

if __name__ == '__main__':
    my_module.func_say_hi()

    print __version__

    print dir(my_module)
    print __name__