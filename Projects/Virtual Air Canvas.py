# Virtual Air Canvas with Hand Gesture Controls

import cv2
import numpy as np
import mediapipe as mp
from tkinter import *
from tkinter import colorchooser, simpledialog, messagebox
import os

# ---------------------- Setup MediaPipe ----------------------
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# ---------------------- Global Variables ----------------------
drawing = False
color = (0, 0, 255)  # Default Red color
brush_thickness = 5
last_x, last_y = None, None
canvas_img = np.ones((480, 640, 3), np.uint8) * 255  # White canvas

# ---------------------- Gesture Functions ----------------------
def distance(pt1, pt2):
    return np.linalg.norm(np.array(pt1) - np.array(pt2))

# ---------------------- GUI Functions ----------------------
def pick_color():
    global color
    color_code = colorchooser.askcolor(title="Choose brush color")
    if color_code[0]:
        color = tuple(map(int, color_code[0][::-1]))  # Convert RGB to BGR

def change_brush_size():
    global brush_thickness
    size = simpledialog.askinteger("Brush Size", "Enter brush thickness (1-20):", minvalue=1, maxvalue=20)
    if size:
        brush_thickness = size

def clear_canvas():
    global canvas_img
    canvas_img = np.ones((480, 640, 3), np.uint8) * 255
    messagebox.showinfo("Canvas Cleared", "The canvas has been cleared!")

def save_drawing():
    filename = "AirCanvas_Saved.png"
    cv2.imwrite(filename, canvas_img)
    messagebox.showinfo("Saved", f"Drawing saved as {filename}")

# ---------------------- Tkinter GUI ----------------------
root = Tk()
root.title("Virtual Air Canvas - Controls")

Label(root, text="🎨 Virtual Air Canvas Controls", font=("Arial", 14, "bold")).pack(pady=10)
Button(root, text="Pick Color", command=pick_color, width=20).pack(pady=5)
Button(root, text="Change Brush Size", command=change_brush_size, width=20).pack(pady=5)
Button(root, text="Clear Canvas", command=clear_canvas, width=20).pack(pady=5)
Button(root, text="Save Drawing", command=save_drawing, width=20).pack(pady=5)
Label(root, text="\nGestures:\nPinch = Toggle Draw\n2 Fingers = Clear\n3 Fingers = Save",
      font=("Arial", 10)).pack(pady=10)

# ---------------------- Main Drawing Function ----------------------
def air_canvas():
    global drawing, last_x, last_y, canvas_img

    cap = cv2.VideoCapture(0)

    with mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7
    ) as hands:

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)

            if result.multi_hand_landmarks:
                for hand_landmarks in result.multi_hand_landmarks:
                    lm = hand_landmarks.landmark
                    h, w, _ = frame.shape

                    # Landmark points
                    index_finger = (int(lm[8].x * w), int(lm[8].y * h))
                    thumb = (int(lm[4].x * w), int(lm[4].y * h))
                    middle_finger = (int(lm[12].x * w), int(lm[12].y * h))
                    ring_finger = (int(lm[16].x * w), int(lm[16].y * h))
                    pinky = (int(lm[20].x * w), int(lm[20].y * h))

                    # Draw landmarks
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    # Gesture recognition
                    dist_thumb_index = distance(index_finger, thumb)

                    # Toggle drawing with pinch
                    if dist_thumb_index < 40:
                        drawing = not drawing
                        last_x, last_y = None, None

                    # Clear if two fingers up
                    if abs(middle_finger[1] - index_finger[1]) < 30:
                        clear_canvas()

                    # Save if three fingers up
                    if abs(ring_finger[1] - middle_finger[1]) < 30:
                        save_drawing()

                    # Drawing
                    if drawing:
                        if last_x is not None and last_y is not None:
                            cv2.line(canvas_img, (last_x, last_y), index_finger, color, brush_thickness)
                        last_x, last_y = index_finger
                    else:
                        last_x, last_y = None, None

            # Combine frame and canvas
            blended = cv2.addWeighted(frame, 0.6, canvas_img, 0.4, 0)
            cv2.imshow("Air Canvas", blended)

            if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
                break

    cap.release()
    cv2.destroyAllWindows()

# ---------------------- Start Air Canvas in Background ----------------------
import threading
threading.Thread(target=air_canvas, daemon=True).start()

root.mainloop()
import cv2
import numpy as np
import mediapipe as mp
from tkinter import *
from tkinter import colorchooser, simpledialog, messagebox
import os

# ---------------------- Setup MediaPipe ----------------------
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# ---------------------- Global Variables ----------------------
drawing = False
color = (0, 0, 255)  # Default Red color
brush_thickness = 5
last_x, last_y = None, None
canvas_img = np.ones((480, 640, 3), np.uint8) * 255  # White canvas

# ---------------------- Gesture Functions ----------------------
def distance(pt1, pt2):
    return np.linalg.norm(np.array(pt1) - np.array(pt2))

# ---------------------- GUI Functions ----------------------
def pick_color():
    global color
    color_code = colorchooser.askcolor(title="Choose brush color")
    if color_code[0]:
        color = tuple(map(int, color_code[0][::-1]))  # Convert RGB to BGR

def change_brush_size():
    global brush_thickness
    size = simpledialog.askinteger("Brush Size", "Enter brush thickness (1-20):", minvalue=1, maxvalue=20)
    if size:
        brush_thickness = size

def clear_canvas():
    global canvas_img
    canvas_img = np.ones((480, 640, 3), np.uint8) * 255
    messagebox.showinfo("Canvas Cleared", "The canvas has been cleared!")

def save_drawing():
    filename = "AirCanvas_Saved.png"
    cv2.imwrite(filename, canvas_img)
    messagebox.showinfo("Saved", f"Drawing saved as {filename}")

# ---------------------- Tkinter GUI ----------------------
root = Tk()
root.title("Virtual Air Canvas - Controls")

Label(root, text="🎨 Virtual Air Canvas Controls", font=("Arial", 14, "bold")).pack(pady=10)
Button(root, text="Pick Color", command=pick_color, width=20).pack(pady=5)
Button(root, text="Change Brush Size", command=change_brush_size, width=20).pack(pady=5)
Button(root, text="Clear Canvas", command=clear_canvas, width=20).pack(pady=5)
Button(root, text="Save Drawing", command=save_drawing, width=20).pack(pady=5)
Label(root, text="\nGestures:\nPinch = Toggle Draw\n2 Fingers = Clear\n3 Fingers = Save",
      font=("Arial", 10)).pack(pady=10)

# ---------------------- Main Drawing Function ----------------------
def air_canvas():
    global drawing, last_x, last_y, canvas_img

    cap = cv2.VideoCapture(0)

    with mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7
    ) as hands:

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)

            if result.multi_hand_landmarks:
                for hand_landmarks in result.multi_hand_landmarks:
                    lm = hand_landmarks.landmark
                    h, w, _ = frame.shape

                    # Landmark points
                    index_finger = (int(lm[8].x * w), int(lm[8].y * h))
                    thumb = (int(lm[4].x * w), int(lm[4].y * h))
                    middle_finger = (int(lm[12].x * w), int(lm[12].y * h))
                    ring_finger = (int(lm[16].x * w), int(lm[16].y * h))
                    pinky = (int(lm[20].x * w), int(lm[20].y * h))

                    # Draw landmarks
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    # Gesture recognition
                    dist_thumb_index = distance(index_finger, thumb)

                    # Toggle drawing with pinch
                    if dist_thumb_index < 40:
                        drawing = not drawing
                        last_x, last_y = None, None

                    # Clear if two fingers up
                    if abs(middle_finger[1] - index_finger[1]) < 30:
                        clear_canvas()

                    # Save if three fingers up
                    if abs(ring_finger[1] - middle_finger[1]) < 30:
                        save_drawing()

                    # Drawing
                    if drawing:
                        if last_x is not None and last_y is not None:
                            cv2.line(canvas_img, (last_x, last_y), index_finger, color, brush_thickness)
                        last_x, last_y = index_finger
                    else:
                        last_x, last_y = None, None

            # Combine frame and canvas
            blended = cv2.addWeighted(frame, 0.6, canvas_img, 0.4, 0)
            cv2.imshow("Air Canvas", blended)

            if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
                break

    cap.release()
    cv2.destroyAllWindows()

# ---------------------- Start Air Canvas in Background ----------------------
import threading
threading.Thread(target=air_canvas, daemon=True).start()

root.mainloop()
import cv2
import numpy as np
import mediapipe as mp
from tkinter import *
from tkinter import colorchooser, simpledialog, messagebox
import os

# ---------------------- Setup MediaPipe ----------------------
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# ---------------------- Global Variables ----------------------
drawing = False
color = (0, 0, 255)  # Default Red color
brush_thickness = 5
last_x, last_y = None, None
canvas_img = np.ones((480, 640, 3), np.uint8) * 255  # White canvas

# ---------------------- Gesture Functions ----------------------
def distance(pt1, pt2):
    return np.linalg.norm(np.array(pt1) - np.array(pt2))

# ---------------------- GUI Functions ----------------------
def pick_color():
    global color
    color_code = colorchooser.askcolor(title="Choose brush color")
    if color_code[0]:
        color = tuple(map(int, color_code[0][::-1]))  # Convert RGB to BGR

def change_brush_size():
    global brush_thickness
    size = simpledialog.askinteger("Brush Size", "Enter brush thickness (1-20):", minvalue=1, maxvalue=20)
    if size:
        brush_thickness = size

def clear_canvas():
    global canvas_img
    canvas_img = np.ones((480, 640, 3), np.uint8) * 255
    messagebox.showinfo("Canvas Cleared", "The canvas has been cleared!")

def save_drawing():
    filename = "AirCanvas_Saved.png"
    cv2.imwrite(filename, canvas_img)
    messagebox.showinfo("Saved", f"Drawing saved as {filename}")

# ---------------------- Tkinter GUI ----------------------
root = Tk()
root.title("Virtual Air Canvas - Controls")

Label(root, text="🎨 Virtual Air Canvas Controls", font=("Arial", 14, "bold")).pack(pady=10)
Button(root, text="Pick Color", command=pick_color, width=20).pack(pady=5)
Button(root, text="Change Brush Size", command=change_brush_size, width=20).pack(pady=5)
Button(root, text="Clear Canvas", command=clear_canvas, width=20).pack(pady=5)
Button(root, text="Save Drawing", command=save_drawing, width=20).pack(pady=5)
Label(root, text="\nGestures:\nPinch = Toggle Draw\n2 Fingers = Clear\n3 Fingers = Save",
      font=("Arial", 10)).pack(pady=10)

# ---------------------- Main Drawing Function ----------------------
def air_canvas():
    global drawing, last_x, last_y, canvas_img

    cap = cv2.VideoCapture(0)

    with mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7
    ) as hands:

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)

            if result.multi_hand_landmarks:
                for hand_landmarks in result.multi_hand_landmarks:
                    lm = hand_landmarks.landmark
                    h, w, _ = frame.shape

                    # Landmark points
                    index_finger = (int(lm[8].x * w), int(lm[8].y * h))
                    thumb = (int(lm[4].x * w), int(lm[4].y * h))
                    middle_finger = (int(lm[12].x * w), int(lm[12].y * h))
                    ring_finger = (int(lm[16].x * w), int(lm[16].y * h))
                    pinky = (int(lm[20].x * w), int(lm[20].y * h))

                    # Draw landmarks
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    # Gesture recognition
                    dist_thumb_index = distance(index_finger, thumb)

                    # Toggle drawing with pinch
                    if dist_thumb_index < 40:
                        drawing = not drawing
                        last_x, last_y = None, None

                    # Clear if two fingers up
                    if abs(middle_finger[1] - index_finger[1]) < 30:
                        clear_canvas()

                    # Save if three fingers up
                    if abs(ring_finger[1] - middle_finger[1]) < 30:
                        save_drawing()

                    # Drawing
                    if drawing:
                        if last_x is not None and last_y is not None:
                            cv2.line(canvas_img, (last_x, last_y), index_finger, color, brush_thickness)
                        last_x, last_y = index_finger
                    else:
                        last_x, last_y = None, None

            # Combine frame and canvas
            blended = cv2.addWeighted(frame, 0.6, canvas_img, 0.4, 0)
            cv2.imshow("Air Canvas", blended)

            if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
                break

    cap.release()
    cv2.destroyAllWindows()

# ---------------------- Start Air Canvas in Background ----------------------
import threading
threading.Thread(target=air_canvas, daemon=True).start()

root.mainloop()
