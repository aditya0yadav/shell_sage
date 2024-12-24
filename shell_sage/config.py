# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_config.ipynb.

# %% auto 0
__all__ = ['providers', 'ShellSageConfig', 'get_cfg']

# %% ../nbs/01_config.ipynb 3
from dataclasses import dataclass
from fastcore.all import *
from fastcore.xdg import *
from typing import get_type_hints

import claudette as cla, cosette as cos

# %% ../nbs/01_config.ipynb 4
_shell_sage_home_dir = 'shell_sage' # sub-directory of xdg base dir
_shell_sage_cfg_name = 'shell_sage.conf'

# %% ../nbs/01_config.ipynb 5
def _cfg_path(): return xdg_config_home() / _shell_sage_home_dir / _shell_sage_cfg_name

# %% ../nbs/01_config.ipynb 7
providers = {
    'anthropic': cla.models,
    'openai': cos.models
}

# %% ../nbs/01_config.ipynb 9
@dataclass
class ShellSageConfig:
    provider: str = "anthropic"
    model: str = providers['anthropic'][1]
    base_url: str = ''
    api_key: str = ''
    history_lines: int = -1
    code_theme: str = "monokai"
    code_lexer: str = "python"

# %% ../nbs/01_config.ipynb 11
def get_cfg():
    path = _cfg_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    _types = get_type_hints(ShellSageConfig)
    return Config(path.parent, path.name, create=asdict(ShellSageConfig()), types=_types)
