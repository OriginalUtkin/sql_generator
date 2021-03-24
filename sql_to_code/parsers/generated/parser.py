from antlr4 import CommonTokenStream, InputStream, LexerATNSimulator, ParseTreeWalker

from ...models import Context
from .PLpgSQLLexer import PLpgSQLLexer
from .PLpgSQLParser import PLpgSQLParser
from .PLpgSQLParserListener import PLpgSQLParserListener


class Listener(PLpgSQLParserListener):
    def __init__(self, context: Context):
        self.__context = context

    def enterCreate_table_statement(self, ctx: PLpgSQLParser.create_table_statement):
        print("\n\n=====\nenterCreate_table")

    def exitCreate_table_statement(self, ctx: PLpgSQLParser.create_table_statement):
        print("\n\n=====\nexitCreate_table_statement")
        print("create table", ctx.name.getText())
        for item in ctx.define_table().define_columns().children:
            if not isinstance(item, PLpgSQLParser.Table_column_defContext):
                continue
            print("name", item.table_column_definition().identifier().getText())
            print("datatype", item.table_column_definition().data_type().getText())
            try:
                print(
                    "default>",
                    item.table_column_definition()
                    .constraint_common()[0]
                    .constr_body()
                    .default_expr.getText(),
                )
            except Exception as e:
                pass
        # TODO fill self.__context


def parse_commands(content: str) -> Context:
    LexerATNSimulator.debug = False

    result = Context()
    lexer = PLpgSQLLexer(InputStream(content))
    stream = CommonTokenStream(lexer)

    parser = PLpgSQLParser(stream)
    tree = parser.sql()

    listener = Listener(context=result)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return result
