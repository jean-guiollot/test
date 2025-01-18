import time
import ctypes

def move_mouse(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)

def get_cursor_position():
    class POINT(ctypes.Structure):
        _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

    point = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
    return point.x, point.y

def main():
    # Demander le temps que le programme doit tourner en heures
    try:
        hours = float(input("Entrez le temps que le programme doit tourner (en heures) : "))
        if hours <= 0:
            print("Veuillez entrer un nombre positif.")
            return
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre.")
        return

    # Convertir les heures en secondes
    runtime_seconds = hours * 3600
    start_time = time.time()

    print("Le programme a commencé. Vous pouvez le quitter en fermant la console.")

    while time.time() - start_time < runtime_seconds:
        # Obtenir la position actuelle de la souris
        x, y = get_cursor_position()

        # Déplacer la souris vers la gauche de 1 pixel
        move_mouse(x - 10, y)
        time.sleep(2)  # Attendre 2 secondes

        # Déplacer la souris vers la droite de 1 pixel
        move_mouse(x + 10, y)
        time.sleep(2)  # Attendre 2 secondes

    print("Le programme est terminé.")

if __name__ == "__main__":
    main()
