from .base import info


__version__ = '2.0.0'


def tool_info():
    info(a='=')
    info('Lethal Company Mods tool', a='|^|')
    info(f'version {__version__}', a='|^|')
    info('By WintryWind', a='|^|')
    info(a='=')