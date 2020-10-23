import gzip

class GzipService:
    def run(self, payload, compression_level=6):
        output = gzip.compress(payload, compression_level)
        return output


