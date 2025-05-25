class QueryModel:
    def __init__(self, query=None):
        self.query = query

    def get_query(self):
        return self.query

    def load_query_file(self, file_path):
        with open(file_path, 'r') as file:
            self.query = file.read().strip()
        return self.query
