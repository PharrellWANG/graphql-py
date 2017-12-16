import graphene


class Query(graphene.ObjectType):
	hello = graphene.String(context=graphene.String(default_value="stranger"))
	
	def resolve_hello(self, args, context):
		return 'Hello world!' + context


schema = graphene.Schema(query=Query)
result = schema.execute('{ hello }')
print(result.data['hello'])
