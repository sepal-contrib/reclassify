from sepal_ui import sepalwidgets as sw
from sepal_ui import reclassify as rec

from component import parameter as cp


class TableTile(sw.Tile):
    def __init__(self):

        super().__init__(
            id_=f"table_tile",
            title=f"Create classification table",
            inputs=[rec.TableView(out_path=cp.result_dir).nest_tile()],
        )
