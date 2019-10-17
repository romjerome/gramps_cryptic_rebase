#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2004-2005 Donald N. Allingham
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

"""Exceptions generated by the Db package."""

#-------------------------------------------------------------------------
#
# Gramps modules
#
#-------------------------------------------------------------------------
from ..const import URL_WIKISTRING, URL_MANUAL_PAGE
from ..const import GRAMPS_LOCALE as glocale
_ = glocale.translation.gettext

#-------------------------------------------------------------------------
#
# Constants
#
#-------------------------------------------------------------------------
URL_WIKI_START = '<a href="' + URL_WIKISTRING
URL_MANUAL_START = URL_WIKI_START + URL_MANUAL_PAGE + '_-_Manage_Family_Trees'
URL_BACKUP1_START = URL_WIKI_START + 'How_to_make_a_backup">'
URL_BACKUP2_START = URL_MANUAL_START + '#Backing_up_a_Family_Tree">'
URL_EXPORT_START = URL_MANUAL_START + '#Export_into_Gramps_formats">'

class DbException(Exception):

    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return self.value

class DbWriteFailure(Exception):
    """
    Error used to indicate that a write to a database has failed.
    """
    def __init__(self, value, value2=""):
        Exception.__init__(self)
        self.value = value
        self.value2 = value2

    def __str__(self):
        return self.value

    def messages(self):
        return self.value, self.value2

class DbTransactionCancel(Exception):
    """
    Error used to indicate that a transaction needs to be canceled,
    for example becuase it is lengthy and the users requests so.
    """
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return self.value

class DbVersionError(Exception):
    """
    Error used to report that a file could not be read because it is written
    in an unsupported version of the file format.
    """
    def __init__(self, tree_vers, min_vers, max_vers):
        Exception.__init__(self)
        self.tree_vers = tree_vers
        self.min_vers = min_vers
        self.max_vers = max_vers

    def __str__(self):
        return _('The schema version is not supported by this version of '
                 'Gramps.\n\n'
                 'This Family Tree is schema version %(tree_vers)s, and this '
                 'version of Gramps supports versions %(min_vers)s to '
                 '%(max_vers)s\n\n'
                 'Please upgrade to the corresponding version or use '
                 'XML for porting data between different schema versions.') %\
                 {'tree_vers': self.tree_vers,
                  'min_vers': self.min_vers,
                  'max_vers': self.max_vers}

class DbPythonError(Exception):
    """
    Error used to report that a file could not be read because it is written
    in an unsupported version of the Python format.
    """
    def __init__(self, tree_vers, min_vers, max_vers):
        Exception.__init__(self)
        self.tree_vers = tree_vers
        self.min_vers = min_vers
        self.max_vers = max_vers

    def __str__(self):
        return _('The Python version is not supported by this version of '
                 'Gramps.\n\n'
                 'This Family Tree is Python version %(tree_vers)s, and this '
                 'version of Gramps supports versions %(min_vers)s to '
                 '%(max_vers)s\n\n'
                 'Please upgrade to the corresponding version or use '
                 'XML for porting data between different Python versions.') %\
                 {'tree_vers': self.tree_vers,
                  'min_vers': self.min_vers,
                  'max_vers': self.max_vers}

class BsddbDowngradeError(Exception):
    """
    Error used to report that the Berkeley database used to create the family
    tree is of a version that is too new to be supported by the current version.
    """
    def __init__(self, env_version, bdb_version):
        Exception.__init__(self)
        self.env_version = str(env_version)
        self.bdb_version = str(bdb_version)

    def __str__(self):
        return _('The Family Tree you are trying to load is in the Bsddb '
                 'version %(env_version)s format. This version of Gramps uses '
                 'Bsddb version %(bdb_version)s. So you are trying to load '
                 'data created in a newer format into an older program, and '
                 'this is bound to fail.\n\n'
                 'You should start your '
                 '%(bold_start)snewer%(bold_end)s version of Gramps and '
                 '%(wiki_backup_html_start)smake a backup%(html_end)s '
                 'of your Family Tree. You can then import '
                 'this backup into this version of Gramps.') % {
                     'wiki_backup_html_start' : URL_BACKUP1_START ,
                     'html_end'    : '</a>' ,
                     'bold_start'  : '<b>' ,
                     'bold_end'    : '</b>' ,
                     'env_version' : self.env_version,
                     'bdb_version' : self.bdb_version }

class BsddbDowngradeRequiredError(Exception):
    """
    Error used to report that the Berkeley database used to create the family
    tree is of a version that is newer than the current version, but it may be
    possible to open the tree, because the difference is only a point upgrade
    (i.e. a difference in the last digit of the version tuple).
    """
    def __init__(self, env_version, bdb_version):
        Exception.__init__(self)
        self.env_version = str(env_version)
        self.bdb_version = str(bdb_version)

    def __str__(self):
        return _('The Family Tree you are trying to load is in the Bsddb '
                 'version %(env_version)s format. This version of Gramps uses '
                 'Bsddb version %(bdb_version)s. So you are trying to load '
                 'data created in a newer format into an older program. In '
                 'this particular case, the difference is very small, so it '
                 'may work.\n\n'
                 'If you have not already made a backup of your Family Tree, '
                 'then you should start your '
                 '%(bold_start)snewer%(bold_end)s version of Gramps and '
                 '%(wiki_backup_html_start)smake a backup%(html_end)s '
                 'of your Family Tree.') % {
                     'wiki_backup_html_start' : URL_BACKUP1_START ,
                     'html_end'    : '</a>' ,
                     'bold_start'  : '<b>' ,
                     'bold_end'    : '</b>' ,
                     'env_version' : self.env_version,
                     'bdb_version' : self.bdb_version }

class BsddbUpgradeRequiredError(Exception):
    """
    Error used to report that the Berkeley database used to create the family
    tree is of a version that is too new to be supported by the current version.
    """
    def __init__(self, env_version, bsddb_version):
        Exception.__init__(self)
        self.env_version = str(env_version)
        self.bsddb_version = str(bsddb_version)

    def __str__(self):
        return _('The Family Tree you are trying to load is in the Bsddb '
                 'version %(env_version)s format. This version of Gramps uses '
                 'Bsddb version %(bdb_version)s. Therefore you cannot load '
                 'this Family Tree without upgrading the Bsddb version of the '
                 'Family Tree.\n\n'
                 'Opening the Family Tree with this version of Gramps might '
                 'irretrievably corrupt your Family Tree. You are strongly '
                 'advised to backup your Family Tree.\n\n'
                 'If you have not already made a backup of your Family Tree, '
                 'then you should start your %(bold_start)sold%(bold_end)s '
                 'version of Gramps and '
                 '%(wiki_backup_html_start)smake a backup%(html_end)s '
                 'of your Family Tree.') % {
                     'wiki_backup_html_start' : URL_BACKUP1_START ,
                     'html_end'    : '</a>' ,
                     'bold_start'  : '<b>' ,
                     'bold_end'    : '</b>' ,
                     'env_version' : self.env_version,
                     'bdb_version' : self.bsddb_version }

class DbEnvironmentError(Exception):
    """
    Error used to report that the database 'environment' could not be opened.
    Most likely, the database was created by a different version of the underlying database engine.
    """
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

    def __str__(self):
        return (_("Gramps has detected a problem in opening the 'environment' "
                  "of the underlying Berkeley database used to store this "
                  "Family Tree. The most likely cause "
                  "is that the database was created with an old version "
                  "of the Berkeley database program, "
                  "and you are now using a new version. "
                  "It is quite likely that your database has not been "
                  "changed by Gramps.\nIf possible, you should revert to your "
                  "old version of Gramps and its support software; export "
                  "your database to XML; close the database; "
                  "then upgrade again "
                  "to this version of Gramps and import the XML file "
                  "in an empty Family Tree. Alternatively, it may be possible "
                  "to use the Berkeley database recovery tools.")
                  + '\n\n' + str(self.msg))

class DbUpgradeRequiredError(Exception):
    """
    Error used to report that a database needs to be upgraded before it can be
    used.
    """
    def __init__(self, oldschema, newschema):
        Exception.__init__(self)
        self.oldschema = oldschema
        self.newschema = newschema

    def __str__(self):
        return _('The Family Tree you are trying to load is in the schema '
                 'version %(oldschema)s format. This version of Gramps uses '
                 'schema version %(newschema)s. Therefore you cannot load this '
                 'Family Tree without upgrading the schema version of the '
                 'Family Tree.\n\n'
                 'If you upgrade then you won\'t be able to use the previous '
                 'version of Gramps, even if you subsequently '
                 '%(wiki_manual_backup_html_start)sbackup%(html_end)s or '
                 '%(wiki_manual_export_html_start)sexport%(html_end)s '
                 'your upgraded Family Tree.\n\n'
                 'Upgrading is a difficult task which could irretrievably '
                 'corrupt your Family Tree if it is interrupted or fails.\n\n'
                 'If you have not already made a backup of your Family Tree, '
                 'then you should start your %(bold_start)sold%(bold_end)s '
                 'version of Gramps and '
                 '%(wiki_backup_html_start)smake a backup%(html_end)s '
                 'of your Family Tree.') % {
                     'wiki_backup_html_start'        : URL_BACKUP1_START ,
                     'wiki_manual_backup_html_start' : URL_BACKUP2_START ,
                     'wiki_manual_export_html_start' : URL_EXPORT_START ,
                     'html_end'   : '</a>' ,
                     'bold_start' : '<b>' ,
                     'bold_end'   : '</b>' ,
                     'oldschema'  : self.oldschema,
                     'newschema'  : self.newschema }

class PythonDowngradeError(Exception):
    """
    Error used to report that the Python version used to create the family tree
    (i.e. Python3) is a version that is newer than the current version
    (i.e. Python2), so the Family Tree cannot be opened
    """
    def __init__(self, db_python_version, current_python_version):
        Exception.__init__(self)
        self.db_python_version = str(db_python_version)
        self.current_python_version = str(current_python_version)

    def __str__(self):
        return _('The Family Tree you are trying to load was created with '
                 'Python version %(db_python_version)s. This version of Gramps '
                 'uses Python version %(current_python_version)s.  So you are '
                 'trying to load '
                 'data created in a newer format into an older program, and '
                 'this is bound to fail.\n\n'
                 'You should start your '
                 '%(bold_start)snewer%(bold_end)s version of Gramps and '
                 '%(wiki_backup_html_start)smake a backup%(html_end)s '
                 'of your Family Tree. You can then import '
                 'this backup into this version of Gramps.') % {
                     'wiki_backup_html_start' : URL_BACKUP1_START ,
                     'html_end'    : '</a>' ,
                     'bold_start'  : '<b>' ,
                     'bold_end'    : '</b>' ,
                     'db_python_version': self.db_python_version,
                     'current_python_version': self.current_python_version }

class PythonUpgradeRequiredError(Exception):
    """
    Error used to report that the Python version used to create the family tree
    (i.e. Python2) is earlier than the current Python version (i.e. Python3), so
    the Family Tree needs to be upgraded.
    """
    def __init__(self, db_python_version, current_python_version):
        Exception.__init__(self)
        self.db_python_version = str(db_python_version)
        self.current_python_version = str(current_python_version)

    def __str__(self):
        return _('The Family Tree you are trying to load is in the Python '
                 'version %(db_python_version)s format. This version of Gramps '
                 'uses Python version %(current_python_version)s. Therefore '
                 'you cannot load this Family Tree without upgrading the '
                 'Python version of the Family Tree.\n\n'
                 'If you upgrade then you won\'t be able to use the previous '
                 'version of Gramps, even if you subsequently '
                 '%(wiki_manual_backup_html_start)sbackup%(html_end)s or '
                 '%(wiki_manual_export_html_start)sexport%(html_end)s '
                 'your upgraded Family Tree.\n\n'
                 'Upgrading is a difficult task which could irretrievably '
                 'corrupt your Family Tree if it is interrupted or fails.\n\n'
                 'If you have not already made a backup of your Family Tree, '
                 'then you should start your %(bold_start)sold%(bold_end)s '
                 'version of Gramps and '
                 '%(wiki_backup_html_start)smake a backup%(html_end)s '
                 'of your Family Tree.') % {
                     'wiki_backup_html_start'        : URL_BACKUP1_START ,
                     'wiki_manual_backup_html_start' : URL_BACKUP2_START ,
                     'wiki_manual_export_html_start' : URL_EXPORT_START ,
                     'html_end'    : '</a>' ,
                     'bold_start'  : '<b>' ,
                     'bold_end'    : '</b>' ,
                     'db_python_version': self.db_python_version,
                     'current_python_version': self.current_python_version }

class DbConnectionError(Exception):
    """
    Error used to report that a database connection failed.
    """
    def __init__(self, msg, settings_file):
        Exception.__init__(self)
        self.msg = msg
        self.settings_file = settings_file

    def __str__(self):
        return _('Database connection failed.\n\n'
                 '%(message)s\n'
                 'Please check your connection settings file:\n'
                 '%(settings_file)s') % {
                    'message': self.msg,
                    'settings_file': self.settings_file}

if __name__ == "__main__":
    """
    Call this from the CLI (in order to find the imported modules):
        cd /path/to/gramps; GRAMPS_RESOURCES=. ; PYTHONPATH=.
        python gramps/gen/db/exceptions.py
    """
    import sys

    print("\nDbVersionError:\n",
             DbVersionError('1.6.0', '1.5.0', '1.5.1'))
    print("\nBsddbDowngradeError:\n",
             BsddbDowngradeError('4.8.30', '4.8.29'))
    print("\nBsddbDowngradeRequiredError:\n",
             BsddbDowngradeRequiredError('4.8.30', '4.8.29'))
    print("\nBsddbUpgradeRequiredError:\n",
             BsddbUpgradeRequiredError('4.8.29', '4.8.30'))
    print("\nDbEnvironmentError:\n",
             DbEnvironmentError('test message'))
    print("\nDbUpgradeRequiredError:\n",
             DbUpgradeRequiredError('1.5.1', '1.6.0'))
    print("\nPythonDowngradeError:\n",
             PythonDowngradeError('3', '2'))
    print("\nPythonUpgradeRequiredError:\n",
             PythonUpgradeRequiredError('2', '3'))
    sys.exit(0)

    print("\nxxx:\n",
             xxx('4.8.30', '4.8.29'))
