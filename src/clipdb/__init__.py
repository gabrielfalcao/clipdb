import ipdb


from clipdb.show_info import show_info


def set_trace() -> None:
    try:
        ipdb.set_trace()
    except KeyboardInterrupt:
        show_info(f"user cancelled with Control-C")
