from meu_erro import MeuErroPersonalizado

def error_handler_method(error):
    if isinstance(error, MeuErroPersonalizado):
        print('Tratar meu erro personalizado')
        return
    if isinstance(error, ZeroDivisionError):
        print('Tratar divvisao por zero')
        return
    if isinstance(error, Exception):
        print('Tratar error geral')
        return