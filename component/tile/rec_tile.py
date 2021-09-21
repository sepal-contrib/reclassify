from sepal_ui import sepalwidgets as sw
from sepal_ui import reclassify as rec

from component import parameter as cp


class RecTile(sw.Tile):
    def __init__(self, gee):

        txt = "gee" if gee else "local"

        super().__init__(
            id_=f"rec_{txt}_tile",
            title=f"Reclassify {txt} asset",
            inputs=[rec.ReclassifyView(out_path=cp.result_dir, gee=gee).nest_tile()],
        )
