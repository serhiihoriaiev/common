import os


class Config:
    pass

class TestConfig:
    pass

class ProdConfig:
    pass


def run_config():
    if os.environ.get('ENV') == 'TEST':
        return TestConfig
    elif os.environ.get('ENV') == 'PROD':
        return ProdConfig
    else:
        return Config