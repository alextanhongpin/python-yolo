import marimo

__generated_with = "0.12.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Face Recognition and Detection with DeepFace


        This notebook demonstrates how to perform face detection and recognition with the `deepface` library.

        - detect faces in images
        - plot the face region
        - perform face recognition from a given labeled dataset
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    from deepface import DeepFace
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    from PIL import Image
    import pathlib
    from collections import Counter
    return Counter, DeepFace, Image, mo, patches, pathlib, plt


@app.cell
def _(mo):
    f = mo.ui.file_browser(initial_path="images", multiple=False)
    f
    return (f,)


@app.cell
def _(Image, f):
    im = Image.open(f.path())
    im.thumbnail((640, 320))
    im
    return (im,)


@app.cell
def _():
    ## Performing face detection
    return


@app.cell
def _(DeepFace, f):
    faces = DeepFace.extract_faces(f.path(), align=True)

    print(f"Found {len(faces)} faces")
    return (faces,)


@app.cell
def _(faces, plt):
    fig, axes = plt.subplots(
        1, len(faces), subplot_kw={"xticks": [], "yticks": []}
    )
    for index, ax in enumerate(axes.flatten()):
        ax.imshow(faces[index]["face"])
    plt.show()
    return ax, axes, fig, index


@app.cell
def _(Image, f, faces, patches, plt):
    def plot_faces(im, faces):
        # Create figure and axes
        fig, ax = plt.subplots(subplot_kw={"xticks": [], "yticks": []})

        im = Image.open(im)
        # Display the image
        ax.imshow(im)

        # Create a Rectangle patch
        for face in faces:
            area = face["facial_area"]
            rect = patches.Rectangle(
                (area["x"], area["y"]),
                area["w"],
                area["h"],
                linewidth=1,
                edgecolor="r",
                facecolor="none",
            )

            # Add the patch to the Axes
            ax.add_patch(rect)

        return plt.gca()


    plot_faces(f.path(), faces)
    return (plot_faces,)


@app.cell
def _(mo):
    mo.md(r"""## Performing face recognition""")
    return


@app.cell
def _(DeepFace, faces):
    dfs = DeepFace.find(
        img_path=faces[0]["face"], db_path="images", enforce_detection=False
    )
    dfs
    return (dfs,)


@app.cell
def _(dfs):
    # Find the top-k results with the shortest distance (most similar)
    k = 5
    top_k = dfs[0].sort_values(by="distance", ascending=True).head(k)
    top_k
    return k, top_k


@app.cell
def _(Counter, pathlib, top_k):
    # Extract the folder path (our label) and count the most common one
    Counter(
        map(
            lambda path: pathlib.Path(path).parent.name,
            top_k["identity"].values,
        )
    ).most_common()[0][0]
    return


@app.cell
def _(Counter, DeepFace, pathlib):
    def recognise_face(im, k=5):
        dfs = DeepFace.find(
            img_path=im, db_path="images", enforce_detection=False, silent=True
        )
        top_k = dfs[0].sort_values(by="distance", ascending=True).head(k)
        return Counter(
            map(
                lambda path: pathlib.Path(path).parent.name,
                top_k["identity"].values,
            )
        ).most_common()[0][0]
    return (recognise_face,)


@app.cell
def _(plt, recognise_face):
    def plot_faces_with_labels(faces):
        fig, axes = plt.subplots(
            1, len(faces), subplot_kw={"xticks": [], "yticks": []}
        )
        for index, ax in enumerate(axes.flatten()):
            label = recognise_face(faces[index]["face"])
            ax.imshow(faces[index]["face"])
            ax.set_title(label)
        return plt.gca()
    return (plot_faces_with_labels,)


@app.cell
def _(faces, plot_faces_with_labels):
    plot_faces_with_labels(faces)
    return


if __name__ == "__main__":
    app.run()
