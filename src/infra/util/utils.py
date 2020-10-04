import hashlib
import json

from opentracing import Span, Format
from opentracing.ext import tags
from pydantic import BaseModel

from src.infra.config.open_tracing_config import tracer


def generate_hash_key(*args):
    keys = []

    for a in args:
        if is_pydantic_model(a):
            keys.append(hashlib.md5(a.json().encode()).hexdigest())
        else:
            keys.append(hashlib.md5(json.dumps(a).encode()).hexdigest())

    return str(hashlib.md5(json.dumps(keys).encode()).hexdigest())


def is_pydantic_model(model):
    return isinstance(model, BaseModel)


def generate_headers_for_span_context_injection(span: Span, http_method: str, http_url: str) -> dict:
    span.set_tag(tags.HTTP_METHOD, http_method)
    span.set_tag(tags.HTTP_URL, http_url)
    span.set_tag(tags.SPAN_KIND, tags.SPAN_KIND_RPC_CLIENT)
    headers = {}
    tracer.inject(span, Format.HTTP_HEADERS, headers)
    return headers
