This SQL parser is generated with [ANTLR v4 tool](https://github.com/antlr/antlr4) from [PL/SQL grammar](https://github.com/antlr/grammars-v4/tree/master/sql/plsql).

Exact steps:

```shell

# download grammar files
curl -O https://raw.githubusercontent.com/antlr/grammars-v4/master/sql/plsql/PlSqlLexer.g4
curl -O https://raw.githubusercontent.com/antlr/grammars-v4/master/sql/plsql/PlSqlParser.g4

# download antlr v4 tool
curl -O https://www.antlr.org/download/antlr-4.9-complete.jar

# create output directory
mkdir out_python

# generate python3 parser
java -Xmx500M -cp antlr-4.9-complete.jar org.antlr.v4.Tool PlSqlLexer.g4 -o ./out_python -Dlanguage=Python3
java -Xmx500M -cp antlr-4.9-complete.jar org.antlr.v4.Tool PlSqlParser.g4 -o ./out_python -Dlanguage=Python3

```

Additionally, you need to manually create PlSqlLexerBase.py and PlSqlParserBase.py files.
