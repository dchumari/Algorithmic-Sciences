import mmap

class SearchHandler:
    def __init__(self, file_path: str, reread_on_query: bool):
        self.file_path = file_path
        self.reread_on_query = reread_on_query
        self.cache = None
        if not self.reread_on_query:
            self.cache = self._read_file()

    def _read_file(self) -> list:
        with open(self.file_path, 'r') as f:
            return f.readlines()

    def _read_with_mmap(self, query: str) -> str:
        with open(self.file_path, 'r+b') as f:
            mmapped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            if mmapped_file.find(query.encode('utf-8')) != -1:
                return "STRING EXISTS"
            return "STRING NOT FOUND"

    def search(self, query: str) -> str:
        if self.reread_on_query:
            return self._read_with_mmap(query)
        else:
            for line in self.cache:
                if line.strip() == query:
                    return "STRING EXISTS"
            return "STRING NOT FOUND"