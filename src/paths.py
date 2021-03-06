# -*- coding: utf-8-*-
import os
import logging

# Jasper main directory
APP_PATH = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir))

DATA_PATH = os.path.join(APP_PATH, "res")
LIB_PATH = os.path.join(APP_PATH, "src")
PLUGIN_PATH = os.path.join(APP_PATH, "plugins/conversation")
TTS_PATH = os.path.join(APP_PATH, "plugins/tts")
STT_PATH = os.path.join(APP_PATH, "plugins/stt")

CONFIG_PATH = os.path.expanduser(os.getenv('JANE_CONFIG', '~/.jane'))

logger = logging.getLogger(__name__)

# Create config dir if it does not exist yet
if not os.path.exists(CONFIG_PATH):
    try:
        os.makedirs(CONFIG_PATH)
    except OSError:
        logger.error("Could not create config dir: '%s'",
                     CONFIG_PATH, exc_info=True)
        raise

# Check if config dir is writable
if not os.access(CONFIG_PATH, os.W_OK):
    logger.critical("Config dir %s is not writable. Jasper " +
                    "won't work correctly.",
                    CONFIG_PATH)


def config(*fname):
    return os.path.join(CONFIG_PATH, *fname)


def data(*fname):
    return os.path.join(DATA_PATH, *fname)
