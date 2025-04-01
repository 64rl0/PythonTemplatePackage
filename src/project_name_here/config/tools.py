# ======================================================================
# MODULE DETAILS
# This section provides metadata about the module, including its
# creation date, author, copyright information, and a brief description
# of the module's purpose and functionality.
# ======================================================================

#   __|    \    _ \  |      _ \   __| __ __| __ __|
#  (      _ \     /  |     (   | (_ |    |      |
# \___| _/  _\ _|_\ ____| \___/ \___|   _|     _|

# ProjectNameHere/src/project_name_here/config/tools.py
# Created 4/1/25 - 8:54 AM UK Time (London) by carlogtt
# Copyright (c) Amazon.com Inc. All Rights Reserved.
# AMAZON.COM CONFIDENTIAL

"""
This module ...
"""

# ======================================================================
# EXCEPTIONS
# This section documents any exceptions made code or quality rules.
# These exceptions may be necessary due to specific coding requirements
# or to bypass false positives.
# ======================================================================
#

# ======================================================================
# IMPORTS
# Importing required libraries and modules for the application.
# ======================================================================

# My Library Imports
import carlogtt_library as mylib

# Local Folder (Relative) Imports
from . import constants

# END IMPORTS
# ======================================================================


# List of public names in the module
__all__ = ['tools']

# Setting up logger for current module
# module_logger =

# Type aliases
#


class Tools:
    """
    Initialize the tools for the package.
    """

    def __init__(self):
        self.master_logger = self.initialize_logger()

    def initialize_logger(self):
        """
        Initialize the logger for the application.

        :return:
        """

        self.master_logger = mylib.Logger(
            log_name=constants.Constants.APP_NAME, log_level=constants.Constants.LOGGING_LEVEL
        )
        self.master_logger.add_console_handler()

        return self.master_logger


tools = Tools()
