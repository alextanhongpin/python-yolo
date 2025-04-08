import marimo

__generated_with = "0.12.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import cv2
    import time

    import threading
    import matplotlib.pyplot as plt
    return cv2, mo, plt, threading, time


@app.cell
def _(cv2, time):
    def take_picture(sleep=3):
        # video capture source camera (Here webcam of laptop)
        cap = cv2.VideoCapture(0)

        time.sleep(sleep)  # wait for 2 seconds to let camera warm up
        _, frame = cap.read()  # return a single frame in variable `frame`
        cap.release()

        return frame
    return (take_picture,)


@app.cell
def _(mo, plt, take_picture):
    mo.stop(True, "cannot take photo")

    plt.imshow(take_picture())
    return


@app.cell
def _(cv2, mo):
    mo.stop(True, "cannot take video")


    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        _, frame = cap.read()
        cv2.imshow("image", frame)

        k = cv2.waitKey(30) & 0xFF  # press ESC to exit
        if k == 27 or cv2.getWindowProperty("image", 0) < 0:
            break
    cv2.destroyAllWindows()
    cap.release()
    return cap, frame, k


@app.cell
def _(cv2, mo, threading):
    def capture_video(button):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                raise Exception("webcam not available")
            frame = cv2.flip(frame, 1)  # if your camera reverses your image
            cv2.imshow("image", frame)
            if not button.value:
                cap.release()
                cv2.destroyAllWindows()


    button = mo.ui.button(label="Record", on_click=lambda value: not value)

    thread = threading.Thread(target=capture_video, args=(button,))
    thread.start()

    button
    return button, capture_video, thread


@app.cell
def _(button):
    button
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
