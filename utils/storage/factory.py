"""Storage backend factory."""

from __future__ import annotations

from functools import lru_cache

from core.config import use_supabase
from utils.storage.json_backend import JsonStorageBackend
from utils.storage.supabase_backend import SupabaseStorageBackend


@lru_cache(maxsize=1)
def get_storage():
    if use_supabase():
        return SupabaseStorageBackend()
    return JsonStorageBackend()
