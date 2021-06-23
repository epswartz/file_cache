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


LOAD_FUNCS = {
    "pickle":load_pickle
}

SAVE_FUNCS = {
    "pickle":save_pickle
}

def file_cache(cache_dir, save_type=None, load_func = LOAD_FUNCS["pickle"], save_func = SAVE_FUNCS["pickle"], lru_cache_size = 128):
    """Decorator used to cache the output of a function on disk.

    Args:
        cache_dir(str): A directory to cache the function call return values in. This value MUST be unique to this function.
        save_type(str): A filetype. Currently, only "pickle" is supported.
        load_func(function): Function with a single string parameter, the filepath. Loads the contents of the file into a python object.
        save_func(function): Function with two params, the function return value and the filepath to save to. Saves the function return value into a file
        lru_cache_size(int): Size (in entries, not bytes) of in memory function cache.

    Returns:
        The decorated function.
    """

    # if save type is specified, make sure to use the proper saving/loading functions.
    if save_type:
        load_func = LOAD_FUNCS[save_type]
        save_func = SAVE_FUNCS[save_type]

    # TODO Handle multiple returns. Is this just a tuple, is it already done?
    # TODO single arg for data type that overrides load_func and save_func if it's specified
    # Check that cache_dir exists, create if it does not.
    if not os.path.exists(cache_dir):
        os.mkdir(cache_dir)

    def decorator_file_cache(func):

        @functools.lru_cache(lru_cache_size) # TODO replace with my own dictionary-based LRU cache class? Not exactly sure how this is going to work.
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            in_memory_cache = dict()

            # TODO I wish this didn't depend on repr, but I can't seem to get reproducible hashing without it.
            str_key = repr(args) + repr(kwargs)
            key = hashlib.sha256().hexdigest()

            file_key = os.path.join(cache_dir, "cache" + key)
            # Check for cache file in cache_dir
            if os.path.exists(file_key):
                return load_func(file_key)
            ret = func(*args, **kwargs)
            save_func(ret, file_key)
            return ret
        return wrapper
    return decorator_file_cache
