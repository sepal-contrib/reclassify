from pathlib import Path

utils_dir = Path(__file__).parents[2] / "utils"

default_classification = {
    f.stem.replace("_", " "): str(f) for f in utils_dir.glob("*.csv")
}
