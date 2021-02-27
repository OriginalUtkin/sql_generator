from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker

from ...models import Context
from .PlSqlLexer import PlSqlLexer
from .PlSqlParser import PlSqlParser
from .PlSqlParserListener import PlSqlParserListener


class Listener(PlSqlParserListener):
    def __init__(self, context: Context):
        self.__context = context

    def enterCreate_table(self, ctx: PlSqlParser.Create_tableContext):
        print("\n\n=====\nenterCreate_table")

    def exitCreate_table(self, ctx: PlSqlParser.Create_tableContext):
        print("create table", ctx.tableview_name().getText())
        for child in ctx.relational_table().children:
            if not isinstance(child, PlSqlParser.Relational_propertyContext):
                continue
            if child.column_definition() is None:
                print("column_definition is None!")
                continue
            print("name", child.column_definition().column_name().getText())
            # if child.column_definition().datatype() is None:
            #     from IPython import embed
            #     embed()
            print("datatype", child.column_definition().datatype().getText())


def parse_commands(content: str) -> Context:

    result = Context()

    lexer = PlSqlLexer(InputStream(content))
    stream = CommonTokenStream(lexer)
    parser = PlSqlParser(stream)
    tree = parser.sql_script()
    listener = Listener(context=result)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return result
