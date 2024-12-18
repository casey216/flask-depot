from app.extensions import db

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(100))

    def __repr__(self):
        return f'<Role {self.role_name}>'

class Permission(db.Model):
    __tablename__ = 'permission'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    permission_name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(100))

    def __repr__(self):
        return f'<Permission {self.permission_name}>'


class PersonRole(db.Model):
    __tablename__ = 'person_role'
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), primary_key=True, nullable=False)

    def __repr__(self):
        return f'<PersonRole person_id={self.person_id} role_id={self.role_id}>'
    

class RolePermission(db.Model):
    __tablename__ = 'role_permission'
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), primary_key=True, nullable=False)
    permission_id = db.Column(db.Integer, db.ForeignKey('permission.id'), primary_key=True, nullable=False)

    def __repr__(self):
        return f'<RolePermission role_id={self.role_id} permission_id={self.permission_id}>'

