from model.model import AppModel
class MigrateVersion(AppModel):
    __tablename__ = 'migrate_version'

    @classmethod
    def all(cls):
        session = cls._get_session()
        return session.query(cls).all()
