import marimo

__generated_with = "0.12.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from pathlib import Path
    return Path, mo


@app.cell
def _(Path):
    labels = []
    faces = []

    dir = Path("images")
    for f in dir.glob("[!Samples]*/*.jpg"):
        print(f.name, f.parent.name)
    return dir, f, faces, labels


@app.cell
def _():
    from deepface import DeepFace
    from PIL import Image
    return DeepFace, Image


@app.cell
def _(Image):
    im = Image.open("images/Samples/Sample-1.jpg")
    im.thumbnail((640, 320))
    im
    return (im,)


@app.cell
def _(DeepFace):
    result = DeepFace.extract_faces("images/Samples/Sample-1.jpg", align=True)
    result
    return (result,)


@app.cell
def _(result):
    import matplotlib.pyplot as plt

    plt.xticks([])
    plt.yticks([])
    plt.imshow(result[0]["face"])
    return (plt,)


@app.cell
def _(result):
    result[0]["confidence"]
    return


@app.cell
def _(DeepFace):
    results = DeepFace.find(
        img_path="images/Samples/Sample-1.jpg", db_path="images/"
    )
    results
    return (results,)


@app.cell
def _(Image, plt, results):
    for df in results:
        _, axs = plt.subplots(1, df.shape[0], figsize=(12, 12))
        axs = axs.flatten()
        for index, row in df.iterrows():
            img = Image.open(row.identity)
            img = img.crop(
                (
                    row.target_x,
                    row.target_y,
                    row.target_x + row.target_w,
                    row.target_y + row.target_h,
                )
            )
            axs[index].set_xticks([])
            axs[index].set_yticks([])
            axs[index].imshow(img)
        plt.show()
    return axs, df, img, index, row


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
