import ipdb
import inspect

from clipdb.show_info import show_info


def set_trace(*args, **kw) -> None:
    if not 'frame' in kw.keys():
        curframe = inspect.currentframe()
        kw['frame'] = curframe.f_back

    try:
        ipdb.set_trace(*args, **kw)
    except KeyboardInterrupt:
        show_info(f"user cancelled with Control-C")
