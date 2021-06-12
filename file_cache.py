import functools
import os
import pickle
import hashlib

def load_pickle(filepath):
    """Load a pickle at the given filepath and return the contents.

    Args:
        filepath (str): The filepath to load.
    Returns:
        The unpickled object.
    """
    with open(filepath, 'rb') as f:
        return pickle.load(f)


def save_pickle(obj, filepath):
    """Save the given object in a pickle at the given filepath.

    Args:
        obj (object): Some picklable object to be saved.
        filepath (str): The filepath to save at.
    Returns:
        The unpickled object.
    """
    with open(filepath, 'wb') as f:
        pickle.dump(obj, f)


def file_cache(cache_dir, load_func = load_pickle, save_func = save_pickle, lru_cache_size = 128):
    # TODO single arg for data type that overrides load_func and save_func if it's specified
    # TODO Check that cache_dir exists
    # TODO Option to autocreate cache dir
    # TODO Hash the function name and create a directory inside cache_dir so they can share dirs, then use that in the file_key initialization?
    def decorator_file_cache(func):

        @functools.lru_cache(lru_cache_size) # TODO replace with my own dictionary-based LRU cache class? Not exactly sure how this is going to work.
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            in_memory_cache = dict()

            # FIXME I wish this didn't depend on repr, but I can't seem to get reproducible hashing without it.
            str_key = repr(args) + repr(kwargs)
            key = hashlib.sha256().hexdigest()

            file_key = os.path.join(cache_dir, "cache" + key)
            # TODO Check for cache file in cache_dir
            if os.path.exists(file_key):
                return load_func(file_key)
            ret = func(*args, **kwargs)
            save_func(ret, file_key)
            return ret
        return wrapper
    return decorator_file_cache
