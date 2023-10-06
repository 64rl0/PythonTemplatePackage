# MODULE NAME ----------------------------------------------------------------------------------------------------------
# __init__.py -> config
# Created 7/19/23 - 10:24 AM UK Time (London) by carlogtt
# ----------------------------------------------------------------------------------------------------------------------

"""
This module contains the configuration for the application.
When importing this file, it will automatically load the environment variables from the.env file.
"""

# IMPORTS --------------------------------------------------------------------------------------------------------------
# Importing required libraries and modules for the application.

# Third Party Library Imports ------------------------------------------------------------------------------------------
import dotenv

# END IMPORTS ----------------------------------------------------------------------------------------------------------


# Load environment variables to filesystem
dotenv.load_dotenv()
