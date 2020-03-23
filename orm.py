#!/usr/bin/python
# -*- coding:utf-8 -*-

class Field(object):
	def __init__(self, name, column_type):
		seft.name = name
		seft.column_type = column_type

	def __str__(seft):
		return '<%s:%s>' % (seft.__class__.__name__, seft.name)

class StringField(Field):
	def __init__(seft, name):
		super(StringField, seft).__init__(name, 'vchar(100)')

class IntergerField(Field):
	def __init__(seft, name):
		super(IntegerField, seft).__init__(name, 'binint')

class Model(dict, metaclass=ModelMetaclass):
	def __init__(self, **kw):
		super(Model, self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AtrributeError(r"'Model' object has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value

	def save(self):
		fields = []
		params = []
		args = []
		
		for k, v in self.__mappings__.items():
			filelds.append(v.name)
			params.append('?')
			args.append(getattr(self, k, None))
		sql = 'insert into %s (%s) values (%s)' % self.__table__, ','.join(fields), ','.join(params))
		print('SQL:%s' % sql)
		print('ARGS:%s' % str(args))

class User(Model):
	id = IntergerFiled('id')
	name = StringFiled('username')
	email = StringField('email')
	password = StringField('password')

u = User(id=12345, name='Micheal', email='test@orm.com', password='12345')
u.save()
