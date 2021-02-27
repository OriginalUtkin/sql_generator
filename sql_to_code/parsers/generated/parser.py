from antlr4 import CommonTokenStream, InputStream, LexerATNSimulator, ParseTreeWalker

from .PlSqlLexer import PlSqlLexer
from .PlSqlParser import PlSqlParser
from ...models import Context

# # from .SQLLexer import SQLLexer, LexerATNSimulator
# # from .SQLParserListener import SQLParserListener
# # from .SQLParser import SQLParser
# from .PostgreSqlLexer import PostgreSqlLexer


# class Listener(SQLParserListener):
#     def __init__(self, context: Context):
#         self.__context = context
#
#     def enterCreate_table(self, ctx: SQLParser.create_table_statement):
#         print("\n\n=====\nenterCreate_table")
#
#     def exitCreate_table(self, ctx: SQLParser.create_table_statement):
#         # print("create table", ctx.tableview_name().getText())
#         # for child in ctx.relational_table().children:
#         # from IPython import embed
#         # embed()
#         pass
#         # if not isinstance(child, PostgreSQLParser.Relational_propertyContext):
#         #     continue
#         # if child.column_definition() is None:
#         #     print("column_definition is None!")
#         #     continue
#         # print("name", child.column_definition().column_name().getText())
#         # # if child.column_definition().datatype() is None:
#         # #     from IPython import embed
#         # #     embed()
#         # print("datatype", child.column_definition().datatype().getText())



def parse_commands(content: str) -> Context:
    # from IPython import embed
    # embed()

    LexerATNSimulator.debug = False

    result = Context()
    lexer = PlSqlLexer(InputStream(content.upper()))
    stream = CommonTokenStream(lexer)

    parser = PlSqlParser(stream)
    tree = parser.sql_script()

    # listener = Listener(context=result)
    # walker = ParseTreeWalker()
    # walker.walk(listener, tree)

    return result
