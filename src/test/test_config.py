from grpc_temp.config import settings


def test_log_level():
    assert settings.log_level == "debug"
