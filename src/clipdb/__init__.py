import ipdb


from clipdb.show_info import show_info


def set_trace(*args, **kw) -> None:
    try:
        ipdb.set_trace(*args, **kw)
    except KeyboardInterrupt:
        show_info(f"user cancelled with Control-C")
