from utils import build_from_cfg
from .registry import BODIES, COMPONENT


def build_component(cfg, default_args=None):
    component = build_from_cfg(cfg, COMPONENT, default_args)

    return component


def build_body(cfg, default_args=None):
    body = build_from_cfg(cfg, BODIES, default_args)

    return body
