from pywinauto import Application
from pywinauto.application import AppStartError
from logging import info


def before_feature(context, feature):
    if 'calc' in feature.tags:
        context.app = Application(backend="uia").start('calc.exe', timeout=10)
        context.app.connect(best_match="Calculator", timeout=5)
        info("Apllication started successfully")
    elif 'custom_app' in feature.tags:
        # context.app = Application(backend="uia").start('C:\Program Files (x86)\CANHacker\CANHacker.exe', timeout=10)
        context.app = Application(backend="uia").start('C:\Program Files (x86)\CANHacker\CANHacker.exe', timeout=10)
        info("Apllication started successfully")

def after_feature(context, feature):
    context.app.kill(soft=True)