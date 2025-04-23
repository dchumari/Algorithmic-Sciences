from typing import List

class SearchHandler:
    def __init__(self, file_path: str, reread_on_query: bool):
        self.file_path = file_path
        self.reread_on_query = reread_on_query
        self.cache: Optional[List[str]] = None
        if not self.reread_on_query:
            self.cache = self._read_file()

    def _read_file(self) -> List[str]:
        with open(self.file_path, 'r') as f:
            return f.readlines()

    def search(self, query: str) -> str:
        lines = self._read_file() if self.reread_on_query else self.cache
        for line in lines:
            if line.strip() == query:
                return "STRING EXISTS"
        return "STRING NOT FOUND"