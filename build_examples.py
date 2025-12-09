import zipfile
from pathlib import Path


def build_uapf(example_dir: Path) -> None:
    output = example_dir.with_suffix(".uapf")
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in example_dir.rglob("*"):
            if path.is_file():
                zf.write(path, path.relative_to(example_dir))


def main() -> None:
    base = Path(__file__).parent
    for name in ["acme-docflow", "rup-lifecycle"]:
        build_uapf(base / name)


if __name__ == "__main__":
    main()
