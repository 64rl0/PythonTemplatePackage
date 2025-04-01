# ======================================================================
# MODULE DETAILS
# This section provides metadata about the module, including its
# creation date, author, copyright information, and a brief description
# of the module's purpose and functionality.
# ======================================================================

#   __|    \    _ \  |      _ \   __| __ __| __ __|
#  (      _ \     /  |     (   | (_ |    |      |
# \___| _/  _\ _|_\ ____| \___/ \___|   _|     _|

# ProjectNameHere/src/project_name_here/config/constants.py
# Created 2/17/25 - 8:14 PM UK Time (London) by carlogtt
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

# Standard Library Imports
import os
import pathlib

# END IMPORTS
# ======================================================================


# List of public names in the module
__all__ = ['Constants']

# Setting up logger for current module
# module_logger =

# Type aliases
#


class Constants:
    """
    This class holds constants for the project.
    It provides a centralized location for storing and accessing various
    configuration values used throughout the application.
    """

    HOME_DIR = pathlib.Path.home()
    PROJECT_ROOT_DIR = pathlib.Path(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    )

    # Logging
    APP_NAME = 'ProjectNameHere'  # if this line changes, update icarus
    LOGGING_LEVEL = 'DEBUG'
