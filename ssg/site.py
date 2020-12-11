import path from pathlib

class Site:
    def __init__(self, source, dest):
        self.path = path(source)

    def create_dir(self, path):
        self.directory = self.dest / self.path.relative_to(self.source)
        path.mkdir(self.directory, parents=True,exists_ok=True)

    def build(self):
        self.dest.mkdir(parents=True,exists_ok=True)

        for path in self.source.rglob("*"):
            if path.isdir():
                self.create_dir(path)

    