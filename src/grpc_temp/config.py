# Configuration of application

import dynaconf

settings = dynaconf.Dynaconf(
    settings_files=["settings.yaml", ".secrets.yaml"],
)
