from database import METADATA
class MigrateVersion(object):
    table = METADATA.tables["migrate_version"]

    @classmethod
    def all(self):
        return self.table.select().execute()
