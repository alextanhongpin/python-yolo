import marimo

__generated_with = "0.12.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import cv2
    import time
    return cv2, mo, time


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
def _(mo, take_picture):
    mo.stop(True, "cannot take photo")

    import matplotlib.pyplot as plt

    plt.imshow(take_picture())
    return (plt,)


@app.cell
def _(cv2, mo):
    mo.stop(True, "cannot take video")

    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, image = cap.read()
        image = cv2.resize(
            image, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA
        )
        cv2.imshow("image", image)

        k = cv2.waitKey(30) & 0xFF  # press ESC to exit
        if k == 27 or cv2.getWindowProperty("image", 0) < 0:
            break
    cv2.destroyAllWindows()
    cap.release()
    return cap, image, k, ret


if __name__ == "__main__":
    app.run()
