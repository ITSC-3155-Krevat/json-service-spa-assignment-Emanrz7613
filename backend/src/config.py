import os


class Config:

    def __init__(self) -> None:
        self.DB = self.DBConfig()

    class DBConfig:

        def __init__(self) -> None:
            self.URI = os.getenv('DATABASE_URL')


# Initialize config singleton
cfg = Config()
