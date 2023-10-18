import cv2

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands

tipIds = []

# Definir una función para contar dedos
def countFingers(image, hand_landmarks, handNo=0):
    
    if hand_landmarks:
        # Obtener todos los puntos de referencia de la primera mano visible
        landmarks = hand_landmarks[handNo].landmark
        # print(landmarks)

        # Contar dedos
        fingers = []

        for lm_index in tipIds:
                # Obtener puntas de los dedos y valor de posición "y" inferior
                finger_tip_y = landmarks[lm_index].y 
                finger_bottom_y = landmarks[lm_index - 2].y

                # Verificar si algún dedo está abierto o cerrado
                

        # print(fingers)
        

        # Mostrar texto
        text = f'Fingers: {totalFingers}'

        cv2.putText(image, text, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

# Definir una función para dibujar conexiones
def drawHandLanmarks(image, hand_landmarks):

    # Dibujar las conexiones entre los puntos de referencia
    if hand_landmarks:

      for landmarks in hand_landmarks:
               
        #mp_drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)

while True:
    success, image = cap.read()

    image = cv2.flip(image, 1)
    
    # Detectar los puntos de referencia de las manos
    

    # Obtener la posición de los puntos de referencia del resultado procesado
    

    # Dibujar puntos de referencia
    

    # Obtener las posiciones de los dedos de la mano
    

    cv2.imshow("Media Controller", image)

    key = cv2.waitKey(1)
    if key == 32:
        break

cv2.destroyAllWindows()

