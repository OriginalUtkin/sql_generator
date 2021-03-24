# Generated from PLpgSQLParser.g4 by ANTLR 4.9
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .PLpgSQLParser import PLpgSQLParser
else:
    from PLpgSQLParser import PLpgSQLParser

# This class defines a complete listener for a parse tree produced by PLpgSQLParser.
class PLpgSQLParserListener(ParseTreeListener):

    # Enter a parse tree produced by PLpgSQLParser#sql.
    def enterSql(self, ctx: PLpgSQLParser.SqlContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#sql.
    def exitSql(self, ctx: PLpgSQLParser.SqlContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#qname_parser.
    def enterQname_parser(self, ctx: PLpgSQLParser.Qname_parserContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#qname_parser.
    def exitQname_parser(self, ctx: PLpgSQLParser.Qname_parserContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#function_args_parser.
    def enterFunction_args_parser(self, ctx: PLpgSQLParser.Function_args_parserContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#function_args_parser.
    def exitFunction_args_parser(self, ctx: PLpgSQLParser.Function_args_parserContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#vex_eof.
    def enterVex_eof(self, ctx: PLpgSQLParser.Vex_eofContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#vex_eof.
    def exitVex_eof(self, ctx: PLpgSQLParser.Vex_eofContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#plpgsql_function.
    def enterPlpgsql_function(self, ctx: PLpgSQLParser.Plpgsql_functionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#plpgsql_function.
    def exitPlpgsql_function(self, ctx: PLpgSQLParser.Plpgsql_functionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#plpgsql_function_test_list.
    def enterPlpgsql_function_test_list(
        self, ctx: PLpgSQLParser.Plpgsql_function_test_listContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#plpgsql_function_test_list.
    def exitPlpgsql_function_test_list(
        self, ctx: PLpgSQLParser.Plpgsql_function_test_listContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#statement.
    def enterStatement(self, ctx: PLpgSQLParser.StatementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#statement.
    def exitStatement(self, ctx: PLpgSQLParser.StatementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#data_statement.
    def enterData_statement(self, ctx: PLpgSQLParser.Data_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#data_statement.
    def exitData_statement(self, ctx: PLpgSQLParser.Data_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#script_statement.
    def enterScript_statement(self, ctx: PLpgSQLParser.Script_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#script_statement.
    def exitScript_statement(self, ctx: PLpgSQLParser.Script_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#script_transaction.
    def enterScript_transaction(self, ctx: PLpgSQLParser.Script_transactionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#script_transaction.
    def exitScript_transaction(self, ctx: PLpgSQLParser.Script_transactionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#transaction_mode.
    def enterTransaction_mode(self, ctx: PLpgSQLParser.Transaction_modeContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#transaction_mode.
    def exitTransaction_mode(self, ctx: PLpgSQLParser.Transaction_modeContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#lock_table.
    def enterLock_table(self, ctx: PLpgSQLParser.Lock_tableContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#lock_table.
    def exitLock_table(self, ctx: PLpgSQLParser.Lock_tableContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#lock_mode.
    def enterLock_mode(self, ctx: PLpgSQLParser.Lock_modeContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#lock_mode.
    def exitLock_mode(self, ctx: PLpgSQLParser.Lock_modeContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#script_additional.
    def enterScript_additional(self, ctx: PLpgSQLParser.Script_additionalContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#script_additional.
    def exitScript_additional(self, ctx: PLpgSQLParser.Script_additionalContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#additional_statement.
    def enterAdditional_statement(self, ctx: PLpgSQLParser.Additional_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#additional_statement.
    def exitAdditional_statement(self, ctx: PLpgSQLParser.Additional_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#explain_statement.
    def enterExplain_statement(self, ctx: PLpgSQLParser.Explain_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#explain_statement.
    def exitExplain_statement(self, ctx: PLpgSQLParser.Explain_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#explain_query.
    def enterExplain_query(self, ctx: PLpgSQLParser.Explain_queryContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#explain_query.
    def exitExplain_query(self, ctx: PLpgSQLParser.Explain_queryContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#execute_statement.
    def enterExecute_statement(self, ctx: PLpgSQLParser.Execute_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#execute_statement.
    def exitExecute_statement(self, ctx: PLpgSQLParser.Execute_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#declare_statement.
    def enterDeclare_statement(self, ctx: PLpgSQLParser.Declare_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#declare_statement.
    def exitDeclare_statement(self, ctx: PLpgSQLParser.Declare_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#show_statement.
    def enterShow_statement(self, ctx: PLpgSQLParser.Show_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#show_statement.
    def exitShow_statement(self, ctx: PLpgSQLParser.Show_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#explain_option.
    def enterExplain_option(self, ctx: PLpgSQLParser.Explain_optionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#explain_option.
    def exitExplain_option(self, ctx: PLpgSQLParser.Explain_optionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#user_name.
    def enterUser_name(self, ctx: PLpgSQLParser.User_nameContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#user_name.
    def exitUser_name(self, ctx: PLpgSQLParser.User_nameContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#table_cols_list.
    def enterTable_cols_list(self, ctx: PLpgSQLParser.Table_cols_listContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#table_cols_list.
    def exitTable_cols_list(self, ctx: PLpgSQLParser.Table_cols_listContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#table_cols.
    def enterTable_cols(self, ctx: PLpgSQLParser.Table_colsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#table_cols.
    def exitTable_cols(self, ctx: PLpgSQLParser.Table_colsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#vacuum_mode.
    def enterVacuum_mode(self, ctx: PLpgSQLParser.Vacuum_modeContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#vacuum_mode.
    def exitVacuum_mode(self, ctx: PLpgSQLParser.Vacuum_modeContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#vacuum_option.
    def enterVacuum_option(self, ctx: PLpgSQLParser.Vacuum_optionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#vacuum_option.
    def exitVacuum_option(self, ctx: PLpgSQLParser.Vacuum_optionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#analyze_mode.
    def enterAnalyze_mode(self, ctx: PLpgSQLParser.Analyze_modeContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#analyze_mode.
    def exitAnalyze_mode(self, ctx: PLpgSQLParser.Analyze_modeContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#boolean_value.
    def enterBoolean_value(self, ctx: PLpgSQLParser.Boolean_valueContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#boolean_value.
    def exitBoolean_value(self, ctx: PLpgSQLParser.Boolean_valueContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#fetch_move_direction.
    def enterFetch_move_direction(self, ctx: PLpgSQLParser.Fetch_move_directionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#fetch_move_direction.
    def exitFetch_move_direction(self, ctx: PLpgSQLParser.Fetch_move_directionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#schema_statement.
    def enterSchema_statement(self, ctx: PLpgSQLParser.Schema_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#schema_statement.
    def exitSchema_statement(self, ctx: PLpgSQLParser.Schema_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#schema_create.
    def enterSchema_create(self, ctx: PLpgSQLParser.Schema_createContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#schema_create.
    def exitSchema_create(self, ctx: PLpgSQLParser.Schema_createContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#schema_alter.
    def enterSchema_alter(self, ctx: PLpgSQLParser.Schema_alterContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#schema_alter.
    def exitSchema_alter(self, ctx: PLpgSQLParser.Schema_alterContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#schema_drop.
    def enterSchema_drop(self, ctx: PLpgSQLParser.Schema_dropContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#schema_drop.
    def exitSchema_drop(self, ctx: PLpgSQLParser.Schema_dropContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#schema_import.
    def enterSchema_import(self, ctx: PLpgSQLParser.Schema_importContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#schema_import.
    def exitSchema_import(self, ctx: PLpgSQLParser.Schema_importContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_function_statement.
    def enterAlter_function_statement(
        self, ctx: PLpgSQLParser.Alter_function_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_function_statement.
    def exitAlter_function_statement(
        self, ctx: PLpgSQLParser.Alter_function_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_aggregate_statement.
    def enterAlter_aggregate_statement(
        self, ctx: PLpgSQLParser.Alter_aggregate_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_aggregate_statement.
    def exitAlter_aggregate_statement(
        self, ctx: PLpgSQLParser.Alter_aggregate_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_extension_statement.
    def enterAlter_extension_statement(
        self, ctx: PLpgSQLParser.Alter_extension_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_extension_statement.
    def exitAlter_extension_statement(
        self, ctx: PLpgSQLParser.Alter_extension_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_extension_action.
    def enterAlter_extension_action(
        self, ctx: PLpgSQLParser.Alter_extension_actionContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_extension_action.
    def exitAlter_extension_action(
        self, ctx: PLpgSQLParser.Alter_extension_actionContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#extension_member_object.
    def enterExtension_member_object(
        self, ctx: PLpgSQLParser.Extension_member_objectContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#extension_member_object.
    def exitExtension_member_object(
        self, ctx: PLpgSQLParser.Extension_member_objectContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_schema_statement.
    def enterAlter_schema_statement(
        self, ctx: PLpgSQLParser.Alter_schema_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_schema_statement.
    def exitAlter_schema_statement(
        self, ctx: PLpgSQLParser.Alter_schema_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_language_statement.
    def enterAlter_language_statement(
        self, ctx: PLpgSQLParser.Alter_language_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_language_statement.
    def exitAlter_language_statement(
        self, ctx: PLpgSQLParser.Alter_language_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_table_statement.
    def enterAlter_table_statement(
        self, ctx: PLpgSQLParser.Alter_table_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_table_statement.
    def exitAlter_table_statement(
        self, ctx: PLpgSQLParser.Alter_table_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#table_action.
    def enterTable_action(self, ctx: PLpgSQLParser.Table_actionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#table_action.
    def exitTable_action(self, ctx: PLpgSQLParser.Table_actionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#column_action.
    def enterColumn_action(self, ctx: PLpgSQLParser.Column_actionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#column_action.
    def exitColumn_action(self, ctx: PLpgSQLParser.Column_actionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#identity_body.
    def enterIdentity_body(self, ctx: PLpgSQLParser.Identity_bodyContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#identity_body.
    def exitIdentity_body(self, ctx: PLpgSQLParser.Identity_bodyContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_identity.
    def enterAlter_identity(self, ctx: PLpgSQLParser.Alter_identityContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_identity.
    def exitAlter_identity(self, ctx: PLpgSQLParser.Alter_identityContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#storage_option.
    def enterStorage_option(self, ctx: PLpgSQLParser.Storage_optionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#storage_option.
    def exitStorage_option(self, ctx: PLpgSQLParser.Storage_optionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#validate_constraint.
    def enterValidate_constraint(self, ctx: PLpgSQLParser.Validate_constraintContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#validate_constraint.
    def exitValidate_constraint(self, ctx: PLpgSQLParser.Validate_constraintContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#drop_constraint.
    def enterDrop_constraint(self, ctx: PLpgSQLParser.Drop_constraintContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#drop_constraint.
    def exitDrop_constraint(self, ctx: PLpgSQLParser.Drop_constraintContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#table_deferrable.
    def enterTable_deferrable(self, ctx: PLpgSQLParser.Table_deferrableContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#table_deferrable.
    def exitTable_deferrable(self, ctx: PLpgSQLParser.Table_deferrableContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#table_initialy_immed.
    def enterTable_initialy_immed(self, ctx: PLpgSQLParser.Table_initialy_immedContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#table_initialy_immed.
    def exitTable_initialy_immed(self, ctx: PLpgSQLParser.Table_initialy_immedContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#function_actions_common.
    def enterFunction_actions_common(
        self, ctx: PLpgSQLParser.Function_actions_commonContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#function_actions_common.
    def exitFunction_actions_common(
        self, ctx: PLpgSQLParser.Function_actions_commonContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#function_def.
    def enterFunction_def(self, ctx: PLpgSQLParser.Function_defContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#function_def.
    def exitFunction_def(self, ctx: PLpgSQLParser.Function_defContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_index_statement.
    def enterAlter_index_statement(
        self, ctx: PLpgSQLParser.Alter_index_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_index_statement.
    def exitAlter_index_statement(
        self, ctx: PLpgSQLParser.Alter_index_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#index_def_action.
    def enterIndex_def_action(self, ctx: PLpgSQLParser.Index_def_actionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#index_def_action.
    def exitIndex_def_action(self, ctx: PLpgSQLParser.Index_def_actionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_default_privileges.
    def enterAlter_default_privileges(
        self, ctx: PLpgSQLParser.Alter_default_privilegesContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_default_privileges.
    def exitAlter_default_privileges(
        self, ctx: PLpgSQLParser.Alter_default_privilegesContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#abbreviated_grant_or_revoke.
    def enterAbbreviated_grant_or_revoke(
        self, ctx: PLpgSQLParser.Abbreviated_grant_or_revokeContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#abbreviated_grant_or_revoke.
    def exitAbbreviated_grant_or_revoke(
        self, ctx: PLpgSQLParser.Abbreviated_grant_or_revokeContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#grant_option_for.
    def enterGrant_option_for(self, ctx: PLpgSQLParser.Grant_option_forContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#grant_option_for.
    def exitGrant_option_for(self, ctx: PLpgSQLParser.Grant_option_forContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_sequence_statement.
    def enterAlter_sequence_statement(
        self, ctx: PLpgSQLParser.Alter_sequence_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_sequence_statement.
    def exitAlter_sequence_statement(
        self, ctx: PLpgSQLParser.Alter_sequence_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_view_statement.
    def enterAlter_view_statement(self, ctx: PLpgSQLParser.Alter_view_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_view_statement.
    def exitAlter_view_statement(self, ctx: PLpgSQLParser.Alter_view_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_event_trigger.
    def enterAlter_event_trigger(self, ctx: PLpgSQLParser.Alter_event_triggerContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_event_trigger.
    def exitAlter_event_trigger(self, ctx: PLpgSQLParser.Alter_event_triggerContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_event_trigger_action.
    def enterAlter_event_trigger_action(
        self, ctx: PLpgSQLParser.Alter_event_trigger_actionContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_event_trigger_action.
    def exitAlter_event_trigger_action(
        self, ctx: PLpgSQLParser.Alter_event_trigger_actionContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_type_statement.
    def enterAlter_type_statement(self, ctx: PLpgSQLParser.Alter_type_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_type_statement.
    def exitAlter_type_statement(self, ctx: PLpgSQLParser.Alter_type_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_domain_statement.
    def enterAlter_domain_statement(
        self, ctx: PLpgSQLParser.Alter_domain_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_domain_statement.
    def exitAlter_domain_statement(
        self, ctx: PLpgSQLParser.Alter_domain_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_server_statement.
    def enterAlter_server_statement(
        self, ctx: PLpgSQLParser.Alter_server_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_server_statement.
    def exitAlter_server_statement(
        self, ctx: PLpgSQLParser.Alter_server_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_server_action.
    def enterAlter_server_action(self, ctx: PLpgSQLParser.Alter_server_actionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_server_action.
    def exitAlter_server_action(self, ctx: PLpgSQLParser.Alter_server_actionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_fts_statement.
    def enterAlter_fts_statement(self, ctx: PLpgSQLParser.Alter_fts_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_fts_statement.
    def exitAlter_fts_statement(self, ctx: PLpgSQLParser.Alter_fts_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_fts_configuration.
    def enterAlter_fts_configuration(
        self, ctx: PLpgSQLParser.Alter_fts_configurationContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_fts_configuration.
    def exitAlter_fts_configuration(
        self, ctx: PLpgSQLParser.Alter_fts_configurationContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#type_action.
    def enterType_action(self, ctx: PLpgSQLParser.Type_actionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#type_action.
    def exitType_action(self, ctx: PLpgSQLParser.Type_actionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#set_def_column.
    def enterSet_def_column(self, ctx: PLpgSQLParser.Set_def_columnContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#set_def_column.
    def exitSet_def_column(self, ctx: PLpgSQLParser.Set_def_columnContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#drop_def.
    def enterDrop_def(self, ctx: PLpgSQLParser.Drop_defContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#drop_def.
    def exitDrop_def(self, ctx: PLpgSQLParser.Drop_defContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_index_statement.
    def enterCreate_index_statement(
        self, ctx: PLpgSQLParser.Create_index_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_index_statement.
    def exitCreate_index_statement(
        self, ctx: PLpgSQLParser.Create_index_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#index_rest.
    def enterIndex_rest(self, ctx: PLpgSQLParser.Index_restContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#index_rest.
    def exitIndex_rest(self, ctx: PLpgSQLParser.Index_restContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#index_sort.
    def enterIndex_sort(self, ctx: PLpgSQLParser.Index_sortContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#index_sort.
    def exitIndex_sort(self, ctx: PLpgSQLParser.Index_sortContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#including_index.
    def enterIncluding_index(self, ctx: PLpgSQLParser.Including_indexContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#including_index.
    def exitIncluding_index(self, ctx: PLpgSQLParser.Including_indexContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#index_where.
    def enterIndex_where(self, ctx: PLpgSQLParser.Index_whereContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#index_where.
    def exitIndex_where(self, ctx: PLpgSQLParser.Index_whereContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_extension_statement.
    def enterCreate_extension_statement(
        self, ctx: PLpgSQLParser.Create_extension_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_extension_statement.
    def exitCreate_extension_statement(
        self, ctx: PLpgSQLParser.Create_extension_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_language_statement.
    def enterCreate_language_statement(
        self, ctx: PLpgSQLParser.Create_language_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_language_statement.
    def exitCreate_language_statement(
        self, ctx: PLpgSQLParser.Create_language_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_event_trigger.
    def enterCreate_event_trigger(self, ctx: PLpgSQLParser.Create_event_triggerContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_event_trigger.
    def exitCreate_event_trigger(self, ctx: PLpgSQLParser.Create_event_triggerContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_type_statement.
    def enterCreate_type_statement(
        self, ctx: PLpgSQLParser.Create_type_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_type_statement.
    def exitCreate_type_statement(
        self, ctx: PLpgSQLParser.Create_type_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_domain_statement.
    def enterCreate_domain_statement(
        self, ctx: PLpgSQLParser.Create_domain_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_domain_statement.
    def exitCreate_domain_statement(
        self, ctx: PLpgSQLParser.Create_domain_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_server_statement.
    def enterCreate_server_statement(
        self, ctx: PLpgSQLParser.Create_server_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_server_statement.
    def exitCreate_server_statement(
        self, ctx: PLpgSQLParser.Create_server_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_fts_dictionary.
    def enterCreate_fts_dictionary(
        self, ctx: PLpgSQLParser.Create_fts_dictionaryContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_fts_dictionary.
    def exitCreate_fts_dictionary(
        self, ctx: PLpgSQLParser.Create_fts_dictionaryContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#option_with_value.
    def enterOption_with_value(self, ctx: PLpgSQLParser.Option_with_valueContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#option_with_value.
    def exitOption_with_value(self, ctx: PLpgSQLParser.Option_with_valueContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_fts_configuration.
    def enterCreate_fts_configuration(
        self, ctx: PLpgSQLParser.Create_fts_configurationContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_fts_configuration.
    def exitCreate_fts_configuration(
        self, ctx: PLpgSQLParser.Create_fts_configurationContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_fts_template.
    def enterCreate_fts_template(self, ctx: PLpgSQLParser.Create_fts_templateContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_fts_template.
    def exitCreate_fts_template(self, ctx: PLpgSQLParser.Create_fts_templateContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_fts_parser.
    def enterCreate_fts_parser(self, ctx: PLpgSQLParser.Create_fts_parserContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_fts_parser.
    def exitCreate_fts_parser(self, ctx: PLpgSQLParser.Create_fts_parserContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_collation.
    def enterCreate_collation(self, ctx: PLpgSQLParser.Create_collationContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_collation.
    def exitCreate_collation(self, ctx: PLpgSQLParser.Create_collationContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_collation.
    def enterAlter_collation(self, ctx: PLpgSQLParser.Alter_collationContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_collation.
    def exitAlter_collation(self, ctx: PLpgSQLParser.Alter_collationContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#collation_option.
    def enterCollation_option(self, ctx: PLpgSQLParser.Collation_optionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#collation_option.
    def exitCollation_option(self, ctx: PLpgSQLParser.Collation_optionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_user_mapping.
    def enterCreate_user_mapping(self, ctx: PLpgSQLParser.Create_user_mappingContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_user_mapping.
    def exitCreate_user_mapping(self, ctx: PLpgSQLParser.Create_user_mappingContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_user_mapping.
    def enterAlter_user_mapping(self, ctx: PLpgSQLParser.Alter_user_mappingContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_user_mapping.
    def exitAlter_user_mapping(self, ctx: PLpgSQLParser.Alter_user_mappingContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_user_or_role.
    def enterAlter_user_or_role(self, ctx: PLpgSQLParser.Alter_user_or_roleContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_user_or_role.
    def exitAlter_user_or_role(self, ctx: PLpgSQLParser.Alter_user_or_roleContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_user_or_role_set_reset.
    def enterAlter_user_or_role_set_reset(
        self, ctx: PLpgSQLParser.Alter_user_or_role_set_resetContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_user_or_role_set_reset.
    def exitAlter_user_or_role_set_reset(
        self, ctx: PLpgSQLParser.Alter_user_or_role_set_resetContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#user_or_role_set_reset.
    def enterUser_or_role_set_reset(
        self, ctx: PLpgSQLParser.User_or_role_set_resetContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#user_or_role_set_reset.
    def exitUser_or_role_set_reset(
        self, ctx: PLpgSQLParser.User_or_role_set_resetContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_group.
    def enterAlter_group(self, ctx: PLpgSQLParser.Alter_groupContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_group.
    def exitAlter_group(self, ctx: PLpgSQLParser.Alter_groupContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_group_action.
    def enterAlter_group_action(self, ctx: PLpgSQLParser.Alter_group_actionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_group_action.
    def exitAlter_group_action(self, ctx: PLpgSQLParser.Alter_group_actionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_tablespace.
    def enterAlter_tablespace(self, ctx: PLpgSQLParser.Alter_tablespaceContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_tablespace.
    def exitAlter_tablespace(self, ctx: PLpgSQLParser.Alter_tablespaceContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_owner.
    def enterAlter_owner(self, ctx: PLpgSQLParser.Alter_ownerContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_owner.
    def exitAlter_owner(self, ctx: PLpgSQLParser.Alter_ownerContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_tablespace_action.
    def enterAlter_tablespace_action(
        self, ctx: PLpgSQLParser.Alter_tablespace_actionContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_tablespace_action.
    def exitAlter_tablespace_action(
        self, ctx: PLpgSQLParser.Alter_tablespace_actionContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_statistics.
    def enterAlter_statistics(self, ctx: PLpgSQLParser.Alter_statisticsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_statistics.
    def exitAlter_statistics(self, ctx: PLpgSQLParser.Alter_statisticsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_foreign_data_wrapper.
    def enterAlter_foreign_data_wrapper(
        self, ctx: PLpgSQLParser.Alter_foreign_data_wrapperContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_foreign_data_wrapper.
    def exitAlter_foreign_data_wrapper(
        self, ctx: PLpgSQLParser.Alter_foreign_data_wrapperContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_foreign_data_wrapper_action.
    def enterAlter_foreign_data_wrapper_action(
        self, ctx: PLpgSQLParser.Alter_foreign_data_wrapper_actionContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_foreign_data_wrapper_action.
    def exitAlter_foreign_data_wrapper_action(
        self, ctx: PLpgSQLParser.Alter_foreign_data_wrapper_actionContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_operator_statement.
    def enterAlter_operator_statement(
        self, ctx: PLpgSQLParser.Alter_operator_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_operator_statement.
    def exitAlter_operator_statement(
        self, ctx: PLpgSQLParser.Alter_operator_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_operator_action.
    def enterAlter_operator_action(
        self, ctx: PLpgSQLParser.Alter_operator_actionContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_operator_action.
    def exitAlter_operator_action(
        self, ctx: PLpgSQLParser.Alter_operator_actionContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#operator_set_restrict_join.
    def enterOperator_set_restrict_join(
        self, ctx: PLpgSQLParser.Operator_set_restrict_joinContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#operator_set_restrict_join.
    def exitOperator_set_restrict_join(
        self, ctx: PLpgSQLParser.Operator_set_restrict_joinContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#drop_user_mapping.
    def enterDrop_user_mapping(self, ctx: PLpgSQLParser.Drop_user_mappingContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#drop_user_mapping.
    def exitDrop_user_mapping(self, ctx: PLpgSQLParser.Drop_user_mappingContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#drop_owned.
    def enterDrop_owned(self, ctx: PLpgSQLParser.Drop_ownedContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#drop_owned.
    def exitDrop_owned(self, ctx: PLpgSQLParser.Drop_ownedContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#drop_operator_statement.
    def enterDrop_operator_statement(
        self, ctx: PLpgSQLParser.Drop_operator_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#drop_operator_statement.
    def exitDrop_operator_statement(
        self, ctx: PLpgSQLParser.Drop_operator_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#target_operator.
    def enterTarget_operator(self, ctx: PLpgSQLParser.Target_operatorContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#target_operator.
    def exitTarget_operator(self, ctx: PLpgSQLParser.Target_operatorContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#domain_constraint.
    def enterDomain_constraint(self, ctx: PLpgSQLParser.Domain_constraintContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#domain_constraint.
    def exitDomain_constraint(self, ctx: PLpgSQLParser.Domain_constraintContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_transform_statement.
    def enterCreate_transform_statement(
        self, ctx: PLpgSQLParser.Create_transform_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_transform_statement.
    def exitCreate_transform_statement(
        self, ctx: PLpgSQLParser.Create_transform_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_access_method.
    def enterCreate_access_method(self, ctx: PLpgSQLParser.Create_access_methodContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_access_method.
    def exitCreate_access_method(self, ctx: PLpgSQLParser.Create_access_methodContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_user_or_role.
    def enterCreate_user_or_role(self, ctx: PLpgSQLParser.Create_user_or_roleContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_user_or_role.
    def exitCreate_user_or_role(self, ctx: PLpgSQLParser.Create_user_or_roleContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#user_or_role_option.
    def enterUser_or_role_option(self, ctx: PLpgSQLParser.User_or_role_optionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#user_or_role_option.
    def exitUser_or_role_option(self, ctx: PLpgSQLParser.User_or_role_optionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#user_or_role_option_for_alter.
    def enterUser_or_role_option_for_alter(
        self, ctx: PLpgSQLParser.User_or_role_option_for_alterContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#user_or_role_option_for_alter.
    def exitUser_or_role_option_for_alter(
        self, ctx: PLpgSQLParser.User_or_role_option_for_alterContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#user_or_role_or_group_common_option.
    def enterUser_or_role_or_group_common_option(
        self, ctx: PLpgSQLParser.User_or_role_or_group_common_optionContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#user_or_role_or_group_common_option.
    def exitUser_or_role_or_group_common_option(
        self, ctx: PLpgSQLParser.User_or_role_or_group_common_optionContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#user_or_role_common_option.
    def enterUser_or_role_common_option(
        self, ctx: PLpgSQLParser.User_or_role_common_optionContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#user_or_role_common_option.
    def exitUser_or_role_common_option(
        self, ctx: PLpgSQLParser.User_or_role_common_optionContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#user_or_role_or_group_option_for_create.
    def enterUser_or_role_or_group_option_for_create(
        self, ctx: PLpgSQLParser.User_or_role_or_group_option_for_createContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#user_or_role_or_group_option_for_create.
    def exitUser_or_role_or_group_option_for_create(
        self, ctx: PLpgSQLParser.User_or_role_or_group_option_for_createContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_group.
    def enterCreate_group(self, ctx: PLpgSQLParser.Create_groupContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_group.
    def exitCreate_group(self, ctx: PLpgSQLParser.Create_groupContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#group_option.
    def enterGroup_option(self, ctx: PLpgSQLParser.Group_optionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#group_option.
    def exitGroup_option(self, ctx: PLpgSQLParser.Group_optionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_tablespace.
    def enterCreate_tablespace(self, ctx: PLpgSQLParser.Create_tablespaceContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_tablespace.
    def exitCreate_tablespace(self, ctx: PLpgSQLParser.Create_tablespaceContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_statistics.
    def enterCreate_statistics(self, ctx: PLpgSQLParser.Create_statisticsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_statistics.
    def exitCreate_statistics(self, ctx: PLpgSQLParser.Create_statisticsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_foreign_data_wrapper.
    def enterCreate_foreign_data_wrapper(
        self, ctx: PLpgSQLParser.Create_foreign_data_wrapperContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_foreign_data_wrapper.
    def exitCreate_foreign_data_wrapper(
        self, ctx: PLpgSQLParser.Create_foreign_data_wrapperContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#option_without_equal.
    def enterOption_without_equal(self, ctx: PLpgSQLParser.Option_without_equalContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#option_without_equal.
    def exitOption_without_equal(self, ctx: PLpgSQLParser.Option_without_equalContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_operator_statement.
    def enterCreate_operator_statement(
        self, ctx: PLpgSQLParser.Create_operator_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_operator_statement.
    def exitCreate_operator_statement(
        self, ctx: PLpgSQLParser.Create_operator_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#operator_name.
    def enterOperator_name(self, ctx: PLpgSQLParser.Operator_nameContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#operator_name.
    def exitOperator_name(self, ctx: PLpgSQLParser.Operator_nameContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#operator_option.
    def enterOperator_option(self, ctx: PLpgSQLParser.Operator_optionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#operator_option.
    def exitOperator_option(self, ctx: PLpgSQLParser.Operator_optionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_aggregate_statement.
    def enterCreate_aggregate_statement(
        self, ctx: PLpgSQLParser.Create_aggregate_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_aggregate_statement.
    def exitCreate_aggregate_statement(
        self, ctx: PLpgSQLParser.Create_aggregate_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#aggregate_param.
    def enterAggregate_param(self, ctx: PLpgSQLParser.Aggregate_paramContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#aggregate_param.
    def exitAggregate_param(self, ctx: PLpgSQLParser.Aggregate_paramContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#set_statement.
    def enterSet_statement(self, ctx: PLpgSQLParser.Set_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#set_statement.
    def exitSet_statement(self, ctx: PLpgSQLParser.Set_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#set_action.
    def enterSet_action(self, ctx: PLpgSQLParser.Set_actionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#set_action.
    def exitSet_action(self, ctx: PLpgSQLParser.Set_actionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#session_local_option.
    def enterSession_local_option(self, ctx: PLpgSQLParser.Session_local_optionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#session_local_option.
    def exitSession_local_option(self, ctx: PLpgSQLParser.Session_local_optionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#set_statement_value.
    def enterSet_statement_value(self, ctx: PLpgSQLParser.Set_statement_valueContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#set_statement_value.
    def exitSet_statement_value(self, ctx: PLpgSQLParser.Set_statement_valueContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_rewrite_statement.
    def enterCreate_rewrite_statement(
        self, ctx: PLpgSQLParser.Create_rewrite_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_rewrite_statement.
    def exitCreate_rewrite_statement(
        self, ctx: PLpgSQLParser.Create_rewrite_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#rewrite_command.
    def enterRewrite_command(self, ctx: PLpgSQLParser.Rewrite_commandContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#rewrite_command.
    def exitRewrite_command(self, ctx: PLpgSQLParser.Rewrite_commandContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_trigger_statement.
    def enterCreate_trigger_statement(
        self, ctx: PLpgSQLParser.Create_trigger_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_trigger_statement.
    def exitCreate_trigger_statement(
        self, ctx: PLpgSQLParser.Create_trigger_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#trigger_referencing.
    def enterTrigger_referencing(self, ctx: PLpgSQLParser.Trigger_referencingContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#trigger_referencing.
    def exitTrigger_referencing(self, ctx: PLpgSQLParser.Trigger_referencingContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#when_trigger.
    def enterWhen_trigger(self, ctx: PLpgSQLParser.When_triggerContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#when_trigger.
    def exitWhen_trigger(self, ctx: PLpgSQLParser.When_triggerContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#rule_common.
    def enterRule_common(self, ctx: PLpgSQLParser.Rule_commonContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#rule_common.
    def exitRule_common(self, ctx: PLpgSQLParser.Rule_commonContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#rule_member_object.
    def enterRule_member_object(self, ctx: PLpgSQLParser.Rule_member_objectContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#rule_member_object.
    def exitRule_member_object(self, ctx: PLpgSQLParser.Rule_member_objectContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#columns_permissions.
    def enterColumns_permissions(self, ctx: PLpgSQLParser.Columns_permissionsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#columns_permissions.
    def exitColumns_permissions(self, ctx: PLpgSQLParser.Columns_permissionsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#table_column_privileges.
    def enterTable_column_privileges(
        self, ctx: PLpgSQLParser.Table_column_privilegesContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#table_column_privileges.
    def exitTable_column_privileges(
        self, ctx: PLpgSQLParser.Table_column_privilegesContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#permissions.
    def enterPermissions(self, ctx: PLpgSQLParser.PermissionsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#permissions.
    def exitPermissions(self, ctx: PLpgSQLParser.PermissionsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#permission.
    def enterPermission(self, ctx: PLpgSQLParser.PermissionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#permission.
    def exitPermission(self, ctx: PLpgSQLParser.PermissionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#other_rules.
    def enterOther_rules(self, ctx: PLpgSQLParser.Other_rulesContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#other_rules.
    def exitOther_rules(self, ctx: PLpgSQLParser.Other_rulesContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#grant_to_rule.
    def enterGrant_to_rule(self, ctx: PLpgSQLParser.Grant_to_ruleContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#grant_to_rule.
    def exitGrant_to_rule(self, ctx: PLpgSQLParser.Grant_to_ruleContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#revoke_from_cascade_restrict.
    def enterRevoke_from_cascade_restrict(
        self, ctx: PLpgSQLParser.Revoke_from_cascade_restrictContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#revoke_from_cascade_restrict.
    def exitRevoke_from_cascade_restrict(
        self, ctx: PLpgSQLParser.Revoke_from_cascade_restrictContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#roles_names.
    def enterRoles_names(self, ctx: PLpgSQLParser.Roles_namesContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#roles_names.
    def exitRoles_names(self, ctx: PLpgSQLParser.Roles_namesContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#role_name_with_group.
    def enterRole_name_with_group(self, ctx: PLpgSQLParser.Role_name_with_groupContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#role_name_with_group.
    def exitRole_name_with_group(self, ctx: PLpgSQLParser.Role_name_with_groupContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#comment_on_statement.
    def enterComment_on_statement(self, ctx: PLpgSQLParser.Comment_on_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#comment_on_statement.
    def exitComment_on_statement(self, ctx: PLpgSQLParser.Comment_on_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#security_label.
    def enterSecurity_label(self, ctx: PLpgSQLParser.Security_labelContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#security_label.
    def exitSecurity_label(self, ctx: PLpgSQLParser.Security_labelContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#comment_member_object.
    def enterComment_member_object(
        self, ctx: PLpgSQLParser.Comment_member_objectContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#comment_member_object.
    def exitComment_member_object(
        self, ctx: PLpgSQLParser.Comment_member_objectContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#label_member_object.
    def enterLabel_member_object(self, ctx: PLpgSQLParser.Label_member_objectContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#label_member_object.
    def exitLabel_member_object(self, ctx: PLpgSQLParser.Label_member_objectContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_function_statement.
    def enterCreate_function_statement(
        self, ctx: PLpgSQLParser.Create_function_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_function_statement.
    def exitCreate_function_statement(
        self, ctx: PLpgSQLParser.Create_function_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_funct_params.
    def enterCreate_funct_params(self, ctx: PLpgSQLParser.Create_funct_paramsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_funct_params.
    def exitCreate_funct_params(self, ctx: PLpgSQLParser.Create_funct_paramsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#transform_for_type.
    def enterTransform_for_type(self, ctx: PLpgSQLParser.Transform_for_typeContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#transform_for_type.
    def exitTransform_for_type(self, ctx: PLpgSQLParser.Transform_for_typeContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#function_ret_table.
    def enterFunction_ret_table(self, ctx: PLpgSQLParser.Function_ret_tableContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#function_ret_table.
    def exitFunction_ret_table(self, ctx: PLpgSQLParser.Function_ret_tableContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#function_column_name_type.
    def enterFunction_column_name_type(
        self, ctx: PLpgSQLParser.Function_column_name_typeContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#function_column_name_type.
    def exitFunction_column_name_type(
        self, ctx: PLpgSQLParser.Function_column_name_typeContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#function_parameters.
    def enterFunction_parameters(self, ctx: PLpgSQLParser.Function_parametersContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#function_parameters.
    def exitFunction_parameters(self, ctx: PLpgSQLParser.Function_parametersContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#function_args.
    def enterFunction_args(self, ctx: PLpgSQLParser.Function_argsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#function_args.
    def exitFunction_args(self, ctx: PLpgSQLParser.Function_argsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#agg_order.
    def enterAgg_order(self, ctx: PLpgSQLParser.Agg_orderContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#agg_order.
    def exitAgg_order(self, ctx: PLpgSQLParser.Agg_orderContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#character_string.
    def enterCharacter_string(self, ctx: PLpgSQLParser.Character_stringContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#character_string.
    def exitCharacter_string(self, ctx: PLpgSQLParser.Character_stringContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#function_arguments.
    def enterFunction_arguments(self, ctx: PLpgSQLParser.Function_argumentsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#function_arguments.
    def exitFunction_arguments(self, ctx: PLpgSQLParser.Function_argumentsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#argmode.
    def enterArgmode(self, ctx: PLpgSQLParser.ArgmodeContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#argmode.
    def exitArgmode(self, ctx: PLpgSQLParser.ArgmodeContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_sequence_statement.
    def enterCreate_sequence_statement(
        self, ctx: PLpgSQLParser.Create_sequence_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_sequence_statement.
    def exitCreate_sequence_statement(
        self, ctx: PLpgSQLParser.Create_sequence_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#sequence_body.
    def enterSequence_body(self, ctx: PLpgSQLParser.Sequence_bodyContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#sequence_body.
    def exitSequence_body(self, ctx: PLpgSQLParser.Sequence_bodyContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#signed_number_literal.
    def enterSigned_number_literal(
        self, ctx: PLpgSQLParser.Signed_number_literalContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#signed_number_literal.
    def exitSigned_number_literal(
        self, ctx: PLpgSQLParser.Signed_number_literalContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#signed_numerical_literal.
    def enterSigned_numerical_literal(
        self, ctx: PLpgSQLParser.Signed_numerical_literalContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#signed_numerical_literal.
    def exitSigned_numerical_literal(
        self, ctx: PLpgSQLParser.Signed_numerical_literalContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#sign.
    def enterSign(self, ctx: PLpgSQLParser.SignContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#sign.
    def exitSign(self, ctx: PLpgSQLParser.SignContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_schema_statement.
    def enterCreate_schema_statement(
        self, ctx: PLpgSQLParser.Create_schema_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_schema_statement.
    def exitCreate_schema_statement(
        self, ctx: PLpgSQLParser.Create_schema_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_policy_statement.
    def enterCreate_policy_statement(
        self, ctx: PLpgSQLParser.Create_policy_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_policy_statement.
    def exitCreate_policy_statement(
        self, ctx: PLpgSQLParser.Create_policy_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_policy_statement.
    def enterAlter_policy_statement(
        self, ctx: PLpgSQLParser.Alter_policy_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_policy_statement.
    def exitAlter_policy_statement(
        self, ctx: PLpgSQLParser.Alter_policy_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#drop_policy_statement.
    def enterDrop_policy_statement(
        self, ctx: PLpgSQLParser.Drop_policy_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#drop_policy_statement.
    def exitDrop_policy_statement(
        self, ctx: PLpgSQLParser.Drop_policy_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_subscription_statement.
    def enterCreate_subscription_statement(
        self, ctx: PLpgSQLParser.Create_subscription_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_subscription_statement.
    def exitCreate_subscription_statement(
        self, ctx: PLpgSQLParser.Create_subscription_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_subscription_statement.
    def enterAlter_subscription_statement(
        self, ctx: PLpgSQLParser.Alter_subscription_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_subscription_statement.
    def exitAlter_subscription_statement(
        self, ctx: PLpgSQLParser.Alter_subscription_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_subscription_action.
    def enterAlter_subscription_action(
        self, ctx: PLpgSQLParser.Alter_subscription_actionContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_subscription_action.
    def exitAlter_subscription_action(
        self, ctx: PLpgSQLParser.Alter_subscription_actionContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_cast_statement.
    def enterCreate_cast_statement(
        self, ctx: PLpgSQLParser.Create_cast_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_cast_statement.
    def exitCreate_cast_statement(
        self, ctx: PLpgSQLParser.Create_cast_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#drop_cast_statement.
    def enterDrop_cast_statement(self, ctx: PLpgSQLParser.Drop_cast_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#drop_cast_statement.
    def exitDrop_cast_statement(self, ctx: PLpgSQLParser.Drop_cast_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_operator_family_statement.
    def enterCreate_operator_family_statement(
        self, ctx: PLpgSQLParser.Create_operator_family_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_operator_family_statement.
    def exitCreate_operator_family_statement(
        self, ctx: PLpgSQLParser.Create_operator_family_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_operator_family_statement.
    def enterAlter_operator_family_statement(
        self, ctx: PLpgSQLParser.Alter_operator_family_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_operator_family_statement.
    def exitAlter_operator_family_statement(
        self, ctx: PLpgSQLParser.Alter_operator_family_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#operator_family_action.
    def enterOperator_family_action(
        self, ctx: PLpgSQLParser.Operator_family_actionContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#operator_family_action.
    def exitOperator_family_action(
        self, ctx: PLpgSQLParser.Operator_family_actionContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#add_operator_to_family.
    def enterAdd_operator_to_family(
        self, ctx: PLpgSQLParser.Add_operator_to_familyContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#add_operator_to_family.
    def exitAdd_operator_to_family(
        self, ctx: PLpgSQLParser.Add_operator_to_familyContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#drop_operator_from_family.
    def enterDrop_operator_from_family(
        self, ctx: PLpgSQLParser.Drop_operator_from_familyContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#drop_operator_from_family.
    def exitDrop_operator_from_family(
        self, ctx: PLpgSQLParser.Drop_operator_from_familyContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#drop_operator_family_statement.
    def enterDrop_operator_family_statement(
        self, ctx: PLpgSQLParser.Drop_operator_family_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#drop_operator_family_statement.
    def exitDrop_operator_family_statement(
        self, ctx: PLpgSQLParser.Drop_operator_family_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_operator_class_statement.
    def enterCreate_operator_class_statement(
        self, ctx: PLpgSQLParser.Create_operator_class_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_operator_class_statement.
    def exitCreate_operator_class_statement(
        self, ctx: PLpgSQLParser.Create_operator_class_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_operator_class_option.
    def enterCreate_operator_class_option(
        self, ctx: PLpgSQLParser.Create_operator_class_optionContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_operator_class_option.
    def exitCreate_operator_class_option(
        self, ctx: PLpgSQLParser.Create_operator_class_optionContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_operator_class_statement.
    def enterAlter_operator_class_statement(
        self, ctx: PLpgSQLParser.Alter_operator_class_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_operator_class_statement.
    def exitAlter_operator_class_statement(
        self, ctx: PLpgSQLParser.Alter_operator_class_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#drop_operator_class_statement.
    def enterDrop_operator_class_statement(
        self, ctx: PLpgSQLParser.Drop_operator_class_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#drop_operator_class_statement.
    def exitDrop_operator_class_statement(
        self, ctx: PLpgSQLParser.Drop_operator_class_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_conversion_statement.
    def enterCreate_conversion_statement(
        self, ctx: PLpgSQLParser.Create_conversion_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_conversion_statement.
    def exitCreate_conversion_statement(
        self, ctx: PLpgSQLParser.Create_conversion_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_conversion_statement.
    def enterAlter_conversion_statement(
        self, ctx: PLpgSQLParser.Alter_conversion_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_conversion_statement.
    def exitAlter_conversion_statement(
        self, ctx: PLpgSQLParser.Alter_conversion_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_publication_statement.
    def enterCreate_publication_statement(
        self, ctx: PLpgSQLParser.Create_publication_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_publication_statement.
    def exitCreate_publication_statement(
        self, ctx: PLpgSQLParser.Create_publication_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_publication_statement.
    def enterAlter_publication_statement(
        self, ctx: PLpgSQLParser.Alter_publication_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_publication_statement.
    def exitAlter_publication_statement(
        self, ctx: PLpgSQLParser.Alter_publication_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_publication_action.
    def enterAlter_publication_action(
        self, ctx: PLpgSQLParser.Alter_publication_actionContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_publication_action.
    def exitAlter_publication_action(
        self, ctx: PLpgSQLParser.Alter_publication_actionContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#only_table_multiply.
    def enterOnly_table_multiply(self, ctx: PLpgSQLParser.Only_table_multiplyContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#only_table_multiply.
    def exitOnly_table_multiply(self, ctx: PLpgSQLParser.Only_table_multiplyContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_trigger_statement.
    def enterAlter_trigger_statement(
        self, ctx: PLpgSQLParser.Alter_trigger_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_trigger_statement.
    def exitAlter_trigger_statement(
        self, ctx: PLpgSQLParser.Alter_trigger_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alter_rule_statement.
    def enterAlter_rule_statement(self, ctx: PLpgSQLParser.Alter_rule_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alter_rule_statement.
    def exitAlter_rule_statement(self, ctx: PLpgSQLParser.Alter_rule_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#copy_statement.
    def enterCopy_statement(self, ctx: PLpgSQLParser.Copy_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#copy_statement.
    def exitCopy_statement(self, ctx: PLpgSQLParser.Copy_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#copy_from_statement.
    def enterCopy_from_statement(self, ctx: PLpgSQLParser.Copy_from_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#copy_from_statement.
    def exitCopy_from_statement(self, ctx: PLpgSQLParser.Copy_from_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#copy_to_statement.
    def enterCopy_to_statement(self, ctx: PLpgSQLParser.Copy_to_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#copy_to_statement.
    def exitCopy_to_statement(self, ctx: PLpgSQLParser.Copy_to_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#copy_option_list.
    def enterCopy_option_list(self, ctx: PLpgSQLParser.Copy_option_listContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#copy_option_list.
    def exitCopy_option_list(self, ctx: PLpgSQLParser.Copy_option_listContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#copy_option.
    def enterCopy_option(self, ctx: PLpgSQLParser.Copy_optionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#copy_option.
    def exitCopy_option(self, ctx: PLpgSQLParser.Copy_optionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_view_statement.
    def enterCreate_view_statement(
        self, ctx: PLpgSQLParser.Create_view_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_view_statement.
    def exitCreate_view_statement(
        self, ctx: PLpgSQLParser.Create_view_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#if_exists.
    def enterIf_exists(self, ctx: PLpgSQLParser.If_existsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#if_exists.
    def exitIf_exists(self, ctx: PLpgSQLParser.If_existsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#if_not_exists.
    def enterIf_not_exists(self, ctx: PLpgSQLParser.If_not_existsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#if_not_exists.
    def exitIf_not_exists(self, ctx: PLpgSQLParser.If_not_existsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#view_columns.
    def enterView_columns(self, ctx: PLpgSQLParser.View_columnsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#view_columns.
    def exitView_columns(self, ctx: PLpgSQLParser.View_columnsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#with_check_option.
    def enterWith_check_option(self, ctx: PLpgSQLParser.With_check_optionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#with_check_option.
    def exitWith_check_option(self, ctx: PLpgSQLParser.With_check_optionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_table_statement.
    def enterCreate_table_statement(
        self, ctx: PLpgSQLParser.Create_table_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_table_statement.
    def exitCreate_table_statement(
        self, ctx: PLpgSQLParser.Create_table_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_table_as_statement.
    def enterCreate_table_as_statement(
        self, ctx: PLpgSQLParser.Create_table_as_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_table_as_statement.
    def exitCreate_table_as_statement(
        self, ctx: PLpgSQLParser.Create_table_as_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#create_foreign_table_statement.
    def enterCreate_foreign_table_statement(
        self, ctx: PLpgSQLParser.Create_foreign_table_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#create_foreign_table_statement.
    def exitCreate_foreign_table_statement(
        self, ctx: PLpgSQLParser.Create_foreign_table_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#define_table.
    def enterDefine_table(self, ctx: PLpgSQLParser.Define_tableContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#define_table.
    def exitDefine_table(self, ctx: PLpgSQLParser.Define_tableContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#define_partition.
    def enterDefine_partition(self, ctx: PLpgSQLParser.Define_partitionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#define_partition.
    def exitDefine_partition(self, ctx: PLpgSQLParser.Define_partitionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#for_values_bound.
    def enterFor_values_bound(self, ctx: PLpgSQLParser.For_values_boundContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#for_values_bound.
    def exitFor_values_bound(self, ctx: PLpgSQLParser.For_values_boundContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#partition_bound_spec.
    def enterPartition_bound_spec(self, ctx: PLpgSQLParser.Partition_bound_specContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#partition_bound_spec.
    def exitPartition_bound_spec(self, ctx: PLpgSQLParser.Partition_bound_specContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#partition_bound_part.
    def enterPartition_bound_part(self, ctx: PLpgSQLParser.Partition_bound_partContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#partition_bound_part.
    def exitPartition_bound_part(self, ctx: PLpgSQLParser.Partition_bound_partContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#define_columns.
    def enterDefine_columns(self, ctx: PLpgSQLParser.Define_columnsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#define_columns.
    def exitDefine_columns(self, ctx: PLpgSQLParser.Define_columnsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#define_type.
    def enterDefine_type(self, ctx: PLpgSQLParser.Define_typeContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#define_type.
    def exitDefine_type(self, ctx: PLpgSQLParser.Define_typeContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#partition_by.
    def enterPartition_by(self, ctx: PLpgSQLParser.Partition_byContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#partition_by.
    def exitPartition_by(self, ctx: PLpgSQLParser.Partition_byContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#partition_method.
    def enterPartition_method(self, ctx: PLpgSQLParser.Partition_methodContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#partition_method.
    def exitPartition_method(self, ctx: PLpgSQLParser.Partition_methodContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#partition_column.
    def enterPartition_column(self, ctx: PLpgSQLParser.Partition_columnContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#partition_column.
    def exitPartition_column(self, ctx: PLpgSQLParser.Partition_columnContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#define_server.
    def enterDefine_server(self, ctx: PLpgSQLParser.Define_serverContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#define_server.
    def exitDefine_server(self, ctx: PLpgSQLParser.Define_serverContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#define_foreign_options.
    def enterDefine_foreign_options(
        self, ctx: PLpgSQLParser.Define_foreign_optionsContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#define_foreign_options.
    def exitDefine_foreign_options(
        self, ctx: PLpgSQLParser.Define_foreign_optionsContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#foreign_option.
    def enterForeign_option(self, ctx: PLpgSQLParser.Foreign_optionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#foreign_option.
    def exitForeign_option(self, ctx: PLpgSQLParser.Foreign_optionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#foreign_option_name.
    def enterForeign_option_name(self, ctx: PLpgSQLParser.Foreign_option_nameContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#foreign_option_name.
    def exitForeign_option_name(self, ctx: PLpgSQLParser.Foreign_option_nameContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#list_of_type_column_def.
    def enterList_of_type_column_def(
        self, ctx: PLpgSQLParser.List_of_type_column_defContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#list_of_type_column_def.
    def exitList_of_type_column_def(
        self, ctx: PLpgSQLParser.List_of_type_column_defContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#table_column_def.
    def enterTable_column_def(self, ctx: PLpgSQLParser.Table_column_defContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#table_column_def.
    def exitTable_column_def(self, ctx: PLpgSQLParser.Table_column_defContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#table_of_type_column_def.
    def enterTable_of_type_column_def(
        self, ctx: PLpgSQLParser.Table_of_type_column_defContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#table_of_type_column_def.
    def exitTable_of_type_column_def(
        self, ctx: PLpgSQLParser.Table_of_type_column_defContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#table_column_definition.
    def enterTable_column_definition(
        self, ctx: PLpgSQLParser.Table_column_definitionContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#table_column_definition.
    def exitTable_column_definition(
        self, ctx: PLpgSQLParser.Table_column_definitionContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#like_option.
    def enterLike_option(self, ctx: PLpgSQLParser.Like_optionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#like_option.
    def exitLike_option(self, ctx: PLpgSQLParser.Like_optionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#constraint_common.
    def enterConstraint_common(self, ctx: PLpgSQLParser.Constraint_commonContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#constraint_common.
    def exitConstraint_common(self, ctx: PLpgSQLParser.Constraint_commonContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#constr_body.
    def enterConstr_body(self, ctx: PLpgSQLParser.Constr_bodyContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#constr_body.
    def exitConstr_body(self, ctx: PLpgSQLParser.Constr_bodyContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#all_op.
    def enterAll_op(self, ctx: PLpgSQLParser.All_opContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#all_op.
    def exitAll_op(self, ctx: PLpgSQLParser.All_opContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#all_simple_op.
    def enterAll_simple_op(self, ctx: PLpgSQLParser.All_simple_opContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#all_simple_op.
    def exitAll_simple_op(self, ctx: PLpgSQLParser.All_simple_opContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#op_chars.
    def enterOp_chars(self, ctx: PLpgSQLParser.Op_charsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#op_chars.
    def exitOp_chars(self, ctx: PLpgSQLParser.Op_charsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#index_parameters.
    def enterIndex_parameters(self, ctx: PLpgSQLParser.Index_parametersContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#index_parameters.
    def exitIndex_parameters(self, ctx: PLpgSQLParser.Index_parametersContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#names_in_parens.
    def enterNames_in_parens(self, ctx: PLpgSQLParser.Names_in_parensContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#names_in_parens.
    def exitNames_in_parens(self, ctx: PLpgSQLParser.Names_in_parensContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#names_references.
    def enterNames_references(self, ctx: PLpgSQLParser.Names_referencesContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#names_references.
    def exitNames_references(self, ctx: PLpgSQLParser.Names_referencesContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#storage_parameter.
    def enterStorage_parameter(self, ctx: PLpgSQLParser.Storage_parameterContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#storage_parameter.
    def exitStorage_parameter(self, ctx: PLpgSQLParser.Storage_parameterContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#storage_parameter_option.
    def enterStorage_parameter_option(
        self, ctx: PLpgSQLParser.Storage_parameter_optionContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#storage_parameter_option.
    def exitStorage_parameter_option(
        self, ctx: PLpgSQLParser.Storage_parameter_optionContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#storage_parameter_name.
    def enterStorage_parameter_name(
        self, ctx: PLpgSQLParser.Storage_parameter_nameContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#storage_parameter_name.
    def exitStorage_parameter_name(
        self, ctx: PLpgSQLParser.Storage_parameter_nameContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#with_storage_parameter.
    def enterWith_storage_parameter(
        self, ctx: PLpgSQLParser.With_storage_parameterContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#with_storage_parameter.
    def exitWith_storage_parameter(
        self, ctx: PLpgSQLParser.With_storage_parameterContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#storage_parameter_oid.
    def enterStorage_parameter_oid(
        self, ctx: PLpgSQLParser.Storage_parameter_oidContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#storage_parameter_oid.
    def exitStorage_parameter_oid(
        self, ctx: PLpgSQLParser.Storage_parameter_oidContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#on_commit.
    def enterOn_commit(self, ctx: PLpgSQLParser.On_commitContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#on_commit.
    def exitOn_commit(self, ctx: PLpgSQLParser.On_commitContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#table_space.
    def enterTable_space(self, ctx: PLpgSQLParser.Table_spaceContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#table_space.
    def exitTable_space(self, ctx: PLpgSQLParser.Table_spaceContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#action.
    def enterAction(self, ctx: PLpgSQLParser.ActionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#action.
    def exitAction(self, ctx: PLpgSQLParser.ActionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#owner_to.
    def enterOwner_to(self, ctx: PLpgSQLParser.Owner_toContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#owner_to.
    def exitOwner_to(self, ctx: PLpgSQLParser.Owner_toContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#rename_to.
    def enterRename_to(self, ctx: PLpgSQLParser.Rename_toContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#rename_to.
    def exitRename_to(self, ctx: PLpgSQLParser.Rename_toContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#set_schema.
    def enterSet_schema(self, ctx: PLpgSQLParser.Set_schemaContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#set_schema.
    def exitSet_schema(self, ctx: PLpgSQLParser.Set_schemaContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#table_column_privilege.
    def enterTable_column_privilege(
        self, ctx: PLpgSQLParser.Table_column_privilegeContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#table_column_privilege.
    def exitTable_column_privilege(
        self, ctx: PLpgSQLParser.Table_column_privilegeContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#usage_select_update.
    def enterUsage_select_update(self, ctx: PLpgSQLParser.Usage_select_updateContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#usage_select_update.
    def exitUsage_select_update(self, ctx: PLpgSQLParser.Usage_select_updateContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#partition_by_columns.
    def enterPartition_by_columns(self, ctx: PLpgSQLParser.Partition_by_columnsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#partition_by_columns.
    def exitPartition_by_columns(self, ctx: PLpgSQLParser.Partition_by_columnsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#cascade_restrict.
    def enterCascade_restrict(self, ctx: PLpgSQLParser.Cascade_restrictContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#cascade_restrict.
    def exitCascade_restrict(self, ctx: PLpgSQLParser.Cascade_restrictContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#collate_identifier.
    def enterCollate_identifier(self, ctx: PLpgSQLParser.Collate_identifierContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#collate_identifier.
    def exitCollate_identifier(self, ctx: PLpgSQLParser.Collate_identifierContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#indirection_var.
    def enterIndirection_var(self, ctx: PLpgSQLParser.Indirection_varContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#indirection_var.
    def exitIndirection_var(self, ctx: PLpgSQLParser.Indirection_varContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#dollar_number.
    def enterDollar_number(self, ctx: PLpgSQLParser.Dollar_numberContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#dollar_number.
    def exitDollar_number(self, ctx: PLpgSQLParser.Dollar_numberContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#indirection_list.
    def enterIndirection_list(self, ctx: PLpgSQLParser.Indirection_listContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#indirection_list.
    def exitIndirection_list(self, ctx: PLpgSQLParser.Indirection_listContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#indirection.
    def enterIndirection(self, ctx: PLpgSQLParser.IndirectionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#indirection.
    def exitIndirection(self, ctx: PLpgSQLParser.IndirectionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#drop_function_statement.
    def enterDrop_function_statement(
        self, ctx: PLpgSQLParser.Drop_function_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#drop_function_statement.
    def exitDrop_function_statement(
        self, ctx: PLpgSQLParser.Drop_function_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#drop_trigger_statement.
    def enterDrop_trigger_statement(
        self, ctx: PLpgSQLParser.Drop_trigger_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#drop_trigger_statement.
    def exitDrop_trigger_statement(
        self, ctx: PLpgSQLParser.Drop_trigger_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#drop_rule_statement.
    def enterDrop_rule_statement(self, ctx: PLpgSQLParser.Drop_rule_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#drop_rule_statement.
    def exitDrop_rule_statement(self, ctx: PLpgSQLParser.Drop_rule_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#drop_statements.
    def enterDrop_statements(self, ctx: PLpgSQLParser.Drop_statementsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#drop_statements.
    def exitDrop_statements(self, ctx: PLpgSQLParser.Drop_statementsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#if_exist_names_restrict_cascade.
    def enterIf_exist_names_restrict_cascade(
        self, ctx: PLpgSQLParser.If_exist_names_restrict_cascadeContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#if_exist_names_restrict_cascade.
    def exitIf_exist_names_restrict_cascade(
        self, ctx: PLpgSQLParser.If_exist_names_restrict_cascadeContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#id_token.
    def enterId_token(self, ctx: PLpgSQLParser.Id_tokenContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#id_token.
    def exitId_token(self, ctx: PLpgSQLParser.Id_tokenContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#identifier.
    def enterIdentifier(self, ctx: PLpgSQLParser.IdentifierContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#identifier.
    def exitIdentifier(self, ctx: PLpgSQLParser.IdentifierContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#identifier_nontype.
    def enterIdentifier_nontype(self, ctx: PLpgSQLParser.Identifier_nontypeContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#identifier_nontype.
    def exitIdentifier_nontype(self, ctx: PLpgSQLParser.Identifier_nontypeContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#col_label.
    def enterCol_label(self, ctx: PLpgSQLParser.Col_labelContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#col_label.
    def exitCol_label(self, ctx: PLpgSQLParser.Col_labelContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#tokens_nonreserved.
    def enterTokens_nonreserved(self, ctx: PLpgSQLParser.Tokens_nonreservedContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#tokens_nonreserved.
    def exitTokens_nonreserved(self, ctx: PLpgSQLParser.Tokens_nonreservedContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#tokens_nonreserved_except_function_type.
    def enterTokens_nonreserved_except_function_type(
        self, ctx: PLpgSQLParser.Tokens_nonreserved_except_function_typeContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#tokens_nonreserved_except_function_type.
    def exitTokens_nonreserved_except_function_type(
        self, ctx: PLpgSQLParser.Tokens_nonreserved_except_function_typeContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#tokens_reserved_except_function_type.
    def enterTokens_reserved_except_function_type(
        self, ctx: PLpgSQLParser.Tokens_reserved_except_function_typeContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#tokens_reserved_except_function_type.
    def exitTokens_reserved_except_function_type(
        self, ctx: PLpgSQLParser.Tokens_reserved_except_function_typeContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#tokens_reserved.
    def enterTokens_reserved(self, ctx: PLpgSQLParser.Tokens_reservedContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#tokens_reserved.
    def exitTokens_reserved(self, ctx: PLpgSQLParser.Tokens_reservedContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#tokens_nonkeyword.
    def enterTokens_nonkeyword(self, ctx: PLpgSQLParser.Tokens_nonkeywordContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#tokens_nonkeyword.
    def exitTokens_nonkeyword(self, ctx: PLpgSQLParser.Tokens_nonkeywordContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#schema_qualified_name_nontype.
    def enterSchema_qualified_name_nontype(
        self, ctx: PLpgSQLParser.Schema_qualified_name_nontypeContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#schema_qualified_name_nontype.
    def exitSchema_qualified_name_nontype(
        self, ctx: PLpgSQLParser.Schema_qualified_name_nontypeContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#type_list.
    def enterType_list(self, ctx: PLpgSQLParser.Type_listContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#type_list.
    def exitType_list(self, ctx: PLpgSQLParser.Type_listContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#data_type.
    def enterData_type(self, ctx: PLpgSQLParser.Data_typeContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#data_type.
    def exitData_type(self, ctx: PLpgSQLParser.Data_typeContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#array_type.
    def enterArray_type(self, ctx: PLpgSQLParser.Array_typeContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#array_type.
    def exitArray_type(self, ctx: PLpgSQLParser.Array_typeContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#predefined_type.
    def enterPredefined_type(self, ctx: PLpgSQLParser.Predefined_typeContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#predefined_type.
    def exitPredefined_type(self, ctx: PLpgSQLParser.Predefined_typeContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#interval_field.
    def enterInterval_field(self, ctx: PLpgSQLParser.Interval_fieldContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#interval_field.
    def exitInterval_field(self, ctx: PLpgSQLParser.Interval_fieldContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#type_length.
    def enterType_length(self, ctx: PLpgSQLParser.Type_lengthContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#type_length.
    def exitType_length(self, ctx: PLpgSQLParser.Type_lengthContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#precision_param.
    def enterPrecision_param(self, ctx: PLpgSQLParser.Precision_paramContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#precision_param.
    def exitPrecision_param(self, ctx: PLpgSQLParser.Precision_paramContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#vex.
    def enterVex(self, ctx: PLpgSQLParser.VexContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#vex.
    def exitVex(self, ctx: PLpgSQLParser.VexContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#vex_b.
    def enterVex_b(self, ctx: PLpgSQLParser.Vex_bContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#vex_b.
    def exitVex_b(self, ctx: PLpgSQLParser.Vex_bContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#op.
    def enterOp(self, ctx: PLpgSQLParser.OpContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#op.
    def exitOp(self, ctx: PLpgSQLParser.OpContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#all_op_ref.
    def enterAll_op_ref(self, ctx: PLpgSQLParser.All_op_refContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#all_op_ref.
    def exitAll_op_ref(self, ctx: PLpgSQLParser.All_op_refContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#datetime_overlaps.
    def enterDatetime_overlaps(self, ctx: PLpgSQLParser.Datetime_overlapsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#datetime_overlaps.
    def exitDatetime_overlaps(self, ctx: PLpgSQLParser.Datetime_overlapsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#value_expression_primary.
    def enterValue_expression_primary(
        self, ctx: PLpgSQLParser.Value_expression_primaryContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#value_expression_primary.
    def exitValue_expression_primary(
        self, ctx: PLpgSQLParser.Value_expression_primaryContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#unsigned_value_specification.
    def enterUnsigned_value_specification(
        self, ctx: PLpgSQLParser.Unsigned_value_specificationContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#unsigned_value_specification.
    def exitUnsigned_value_specification(
        self, ctx: PLpgSQLParser.Unsigned_value_specificationContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#unsigned_numeric_literal.
    def enterUnsigned_numeric_literal(
        self, ctx: PLpgSQLParser.Unsigned_numeric_literalContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#unsigned_numeric_literal.
    def exitUnsigned_numeric_literal(
        self, ctx: PLpgSQLParser.Unsigned_numeric_literalContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#truth_value.
    def enterTruth_value(self, ctx: PLpgSQLParser.Truth_valueContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#truth_value.
    def exitTruth_value(self, ctx: PLpgSQLParser.Truth_valueContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#case_expression.
    def enterCase_expression(self, ctx: PLpgSQLParser.Case_expressionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#case_expression.
    def exitCase_expression(self, ctx: PLpgSQLParser.Case_expressionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#cast_specification.
    def enterCast_specification(self, ctx: PLpgSQLParser.Cast_specificationContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#cast_specification.
    def exitCast_specification(self, ctx: PLpgSQLParser.Cast_specificationContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#function_call.
    def enterFunction_call(self, ctx: PLpgSQLParser.Function_callContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#function_call.
    def exitFunction_call(self, ctx: PLpgSQLParser.Function_callContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#vex_or_named_notation.
    def enterVex_or_named_notation(
        self, ctx: PLpgSQLParser.Vex_or_named_notationContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#vex_or_named_notation.
    def exitVex_or_named_notation(
        self, ctx: PLpgSQLParser.Vex_or_named_notationContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#pointer.
    def enterPointer(self, ctx: PLpgSQLParser.PointerContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#pointer.
    def exitPointer(self, ctx: PLpgSQLParser.PointerContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#function_construct.
    def enterFunction_construct(self, ctx: PLpgSQLParser.Function_constructContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#function_construct.
    def exitFunction_construct(self, ctx: PLpgSQLParser.Function_constructContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#extract_function.
    def enterExtract_function(self, ctx: PLpgSQLParser.Extract_functionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#extract_function.
    def exitExtract_function(self, ctx: PLpgSQLParser.Extract_functionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#system_function.
    def enterSystem_function(self, ctx: PLpgSQLParser.System_functionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#system_function.
    def exitSystem_function(self, ctx: PLpgSQLParser.System_functionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#date_time_function.
    def enterDate_time_function(self, ctx: PLpgSQLParser.Date_time_functionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#date_time_function.
    def exitDate_time_function(self, ctx: PLpgSQLParser.Date_time_functionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#string_value_function.
    def enterString_value_function(
        self, ctx: PLpgSQLParser.String_value_functionContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#string_value_function.
    def exitString_value_function(
        self, ctx: PLpgSQLParser.String_value_functionContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#xml_function.
    def enterXml_function(self, ctx: PLpgSQLParser.Xml_functionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#xml_function.
    def exitXml_function(self, ctx: PLpgSQLParser.Xml_functionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#xml_table_column.
    def enterXml_table_column(self, ctx: PLpgSQLParser.Xml_table_columnContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#xml_table_column.
    def exitXml_table_column(self, ctx: PLpgSQLParser.Xml_table_columnContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#comparison_mod.
    def enterComparison_mod(self, ctx: PLpgSQLParser.Comparison_modContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#comparison_mod.
    def exitComparison_mod(self, ctx: PLpgSQLParser.Comparison_modContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#filter_clause.
    def enterFilter_clause(self, ctx: PLpgSQLParser.Filter_clauseContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#filter_clause.
    def exitFilter_clause(self, ctx: PLpgSQLParser.Filter_clauseContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#window_definition.
    def enterWindow_definition(self, ctx: PLpgSQLParser.Window_definitionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#window_definition.
    def exitWindow_definition(self, ctx: PLpgSQLParser.Window_definitionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#frame_clause.
    def enterFrame_clause(self, ctx: PLpgSQLParser.Frame_clauseContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#frame_clause.
    def exitFrame_clause(self, ctx: PLpgSQLParser.Frame_clauseContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#frame_bound.
    def enterFrame_bound(self, ctx: PLpgSQLParser.Frame_boundContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#frame_bound.
    def exitFrame_bound(self, ctx: PLpgSQLParser.Frame_boundContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#array_expression.
    def enterArray_expression(self, ctx: PLpgSQLParser.Array_expressionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#array_expression.
    def exitArray_expression(self, ctx: PLpgSQLParser.Array_expressionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#array_elements.
    def enterArray_elements(self, ctx: PLpgSQLParser.Array_elementsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#array_elements.
    def exitArray_elements(self, ctx: PLpgSQLParser.Array_elementsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#type_coercion.
    def enterType_coercion(self, ctx: PLpgSQLParser.Type_coercionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#type_coercion.
    def exitType_coercion(self, ctx: PLpgSQLParser.Type_coercionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#schema_qualified_name.
    def enterSchema_qualified_name(
        self, ctx: PLpgSQLParser.Schema_qualified_nameContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#schema_qualified_name.
    def exitSchema_qualified_name(
        self, ctx: PLpgSQLParser.Schema_qualified_nameContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#set_qualifier.
    def enterSet_qualifier(self, ctx: PLpgSQLParser.Set_qualifierContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#set_qualifier.
    def exitSet_qualifier(self, ctx: PLpgSQLParser.Set_qualifierContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#table_subquery.
    def enterTable_subquery(self, ctx: PLpgSQLParser.Table_subqueryContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#table_subquery.
    def exitTable_subquery(self, ctx: PLpgSQLParser.Table_subqueryContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#select_stmt.
    def enterSelect_stmt(self, ctx: PLpgSQLParser.Select_stmtContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#select_stmt.
    def exitSelect_stmt(self, ctx: PLpgSQLParser.Select_stmtContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#after_ops.
    def enterAfter_ops(self, ctx: PLpgSQLParser.After_opsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#after_ops.
    def exitAfter_ops(self, ctx: PLpgSQLParser.After_opsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#select_stmt_no_parens.
    def enterSelect_stmt_no_parens(
        self, ctx: PLpgSQLParser.Select_stmt_no_parensContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#select_stmt_no_parens.
    def exitSelect_stmt_no_parens(
        self, ctx: PLpgSQLParser.Select_stmt_no_parensContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#with_clause.
    def enterWith_clause(self, ctx: PLpgSQLParser.With_clauseContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#with_clause.
    def exitWith_clause(self, ctx: PLpgSQLParser.With_clauseContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#with_query.
    def enterWith_query(self, ctx: PLpgSQLParser.With_queryContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#with_query.
    def exitWith_query(self, ctx: PLpgSQLParser.With_queryContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#select_ops.
    def enterSelect_ops(self, ctx: PLpgSQLParser.Select_opsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#select_ops.
    def exitSelect_ops(self, ctx: PLpgSQLParser.Select_opsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#select_ops_no_parens.
    def enterSelect_ops_no_parens(self, ctx: PLpgSQLParser.Select_ops_no_parensContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#select_ops_no_parens.
    def exitSelect_ops_no_parens(self, ctx: PLpgSQLParser.Select_ops_no_parensContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#select_primary.
    def enterSelect_primary(self, ctx: PLpgSQLParser.Select_primaryContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#select_primary.
    def exitSelect_primary(self, ctx: PLpgSQLParser.Select_primaryContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#select_list.
    def enterSelect_list(self, ctx: PLpgSQLParser.Select_listContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#select_list.
    def exitSelect_list(self, ctx: PLpgSQLParser.Select_listContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#select_sublist.
    def enterSelect_sublist(self, ctx: PLpgSQLParser.Select_sublistContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#select_sublist.
    def exitSelect_sublist(self, ctx: PLpgSQLParser.Select_sublistContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#into_table.
    def enterInto_table(self, ctx: PLpgSQLParser.Into_tableContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#into_table.
    def exitInto_table(self, ctx: PLpgSQLParser.Into_tableContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#from_item.
    def enterFrom_item(self, ctx: PLpgSQLParser.From_itemContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#from_item.
    def exitFrom_item(self, ctx: PLpgSQLParser.From_itemContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#from_primary.
    def enterFrom_primary(self, ctx: PLpgSQLParser.From_primaryContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#from_primary.
    def exitFrom_primary(self, ctx: PLpgSQLParser.From_primaryContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#alias_clause.
    def enterAlias_clause(self, ctx: PLpgSQLParser.Alias_clauseContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#alias_clause.
    def exitAlias_clause(self, ctx: PLpgSQLParser.Alias_clauseContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#from_function_column_def.
    def enterFrom_function_column_def(
        self, ctx: PLpgSQLParser.From_function_column_defContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#from_function_column_def.
    def exitFrom_function_column_def(
        self, ctx: PLpgSQLParser.From_function_column_defContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#groupby_clause.
    def enterGroupby_clause(self, ctx: PLpgSQLParser.Groupby_clauseContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#groupby_clause.
    def exitGroupby_clause(self, ctx: PLpgSQLParser.Groupby_clauseContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#grouping_element_list.
    def enterGrouping_element_list(
        self, ctx: PLpgSQLParser.Grouping_element_listContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#grouping_element_list.
    def exitGrouping_element_list(
        self, ctx: PLpgSQLParser.Grouping_element_listContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#grouping_element.
    def enterGrouping_element(self, ctx: PLpgSQLParser.Grouping_elementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#grouping_element.
    def exitGrouping_element(self, ctx: PLpgSQLParser.Grouping_elementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#values_stmt.
    def enterValues_stmt(self, ctx: PLpgSQLParser.Values_stmtContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#values_stmt.
    def exitValues_stmt(self, ctx: PLpgSQLParser.Values_stmtContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#values_values.
    def enterValues_values(self, ctx: PLpgSQLParser.Values_valuesContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#values_values.
    def exitValues_values(self, ctx: PLpgSQLParser.Values_valuesContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#orderby_clause.
    def enterOrderby_clause(self, ctx: PLpgSQLParser.Orderby_clauseContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#orderby_clause.
    def exitOrderby_clause(self, ctx: PLpgSQLParser.Orderby_clauseContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#sort_specifier_list.
    def enterSort_specifier_list(self, ctx: PLpgSQLParser.Sort_specifier_listContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#sort_specifier_list.
    def exitSort_specifier_list(self, ctx: PLpgSQLParser.Sort_specifier_listContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#sort_specifier.
    def enterSort_specifier(self, ctx: PLpgSQLParser.Sort_specifierContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#sort_specifier.
    def exitSort_specifier(self, ctx: PLpgSQLParser.Sort_specifierContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#order_specification.
    def enterOrder_specification(self, ctx: PLpgSQLParser.Order_specificationContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#order_specification.
    def exitOrder_specification(self, ctx: PLpgSQLParser.Order_specificationContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#null_ordering.
    def enterNull_ordering(self, ctx: PLpgSQLParser.Null_orderingContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#null_ordering.
    def exitNull_ordering(self, ctx: PLpgSQLParser.Null_orderingContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#insert_stmt_for_psql.
    def enterInsert_stmt_for_psql(self, ctx: PLpgSQLParser.Insert_stmt_for_psqlContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#insert_stmt_for_psql.
    def exitInsert_stmt_for_psql(self, ctx: PLpgSQLParser.Insert_stmt_for_psqlContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#insert_columns.
    def enterInsert_columns(self, ctx: PLpgSQLParser.Insert_columnsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#insert_columns.
    def exitInsert_columns(self, ctx: PLpgSQLParser.Insert_columnsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#indirection_identifier.
    def enterIndirection_identifier(
        self, ctx: PLpgSQLParser.Indirection_identifierContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#indirection_identifier.
    def exitIndirection_identifier(
        self, ctx: PLpgSQLParser.Indirection_identifierContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#conflict_object.
    def enterConflict_object(self, ctx: PLpgSQLParser.Conflict_objectContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#conflict_object.
    def exitConflict_object(self, ctx: PLpgSQLParser.Conflict_objectContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#conflict_action.
    def enterConflict_action(self, ctx: PLpgSQLParser.Conflict_actionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#conflict_action.
    def exitConflict_action(self, ctx: PLpgSQLParser.Conflict_actionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#delete_stmt_for_psql.
    def enterDelete_stmt_for_psql(self, ctx: PLpgSQLParser.Delete_stmt_for_psqlContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#delete_stmt_for_psql.
    def exitDelete_stmt_for_psql(self, ctx: PLpgSQLParser.Delete_stmt_for_psqlContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#update_stmt_for_psql.
    def enterUpdate_stmt_for_psql(self, ctx: PLpgSQLParser.Update_stmt_for_psqlContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#update_stmt_for_psql.
    def exitUpdate_stmt_for_psql(self, ctx: PLpgSQLParser.Update_stmt_for_psqlContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#update_set.
    def enterUpdate_set(self, ctx: PLpgSQLParser.Update_setContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#update_set.
    def exitUpdate_set(self, ctx: PLpgSQLParser.Update_setContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#notify_stmt.
    def enterNotify_stmt(self, ctx: PLpgSQLParser.Notify_stmtContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#notify_stmt.
    def exitNotify_stmt(self, ctx: PLpgSQLParser.Notify_stmtContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#truncate_stmt.
    def enterTruncate_stmt(self, ctx: PLpgSQLParser.Truncate_stmtContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#truncate_stmt.
    def exitTruncate_stmt(self, ctx: PLpgSQLParser.Truncate_stmtContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#identifier_list.
    def enterIdentifier_list(self, ctx: PLpgSQLParser.Identifier_listContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#identifier_list.
    def exitIdentifier_list(self, ctx: PLpgSQLParser.Identifier_listContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#anonymous_block.
    def enterAnonymous_block(self, ctx: PLpgSQLParser.Anonymous_blockContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#anonymous_block.
    def exitAnonymous_block(self, ctx: PLpgSQLParser.Anonymous_blockContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#comp_options.
    def enterComp_options(self, ctx: PLpgSQLParser.Comp_optionsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#comp_options.
    def exitComp_options(self, ctx: PLpgSQLParser.Comp_optionsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#function_block.
    def enterFunction_block(self, ctx: PLpgSQLParser.Function_blockContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#function_block.
    def exitFunction_block(self, ctx: PLpgSQLParser.Function_blockContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#start_label.
    def enterStart_label(self, ctx: PLpgSQLParser.Start_labelContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#start_label.
    def exitStart_label(self, ctx: PLpgSQLParser.Start_labelContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#declarations.
    def enterDeclarations(self, ctx: PLpgSQLParser.DeclarationsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#declarations.
    def exitDeclarations(self, ctx: PLpgSQLParser.DeclarationsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#declaration.
    def enterDeclaration(self, ctx: PLpgSQLParser.DeclarationContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#declaration.
    def exitDeclaration(self, ctx: PLpgSQLParser.DeclarationContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#type_declaration.
    def enterType_declaration(self, ctx: PLpgSQLParser.Type_declarationContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#type_declaration.
    def exitType_declaration(self, ctx: PLpgSQLParser.Type_declarationContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#arguments_list.
    def enterArguments_list(self, ctx: PLpgSQLParser.Arguments_listContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#arguments_list.
    def exitArguments_list(self, ctx: PLpgSQLParser.Arguments_listContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#data_type_dec.
    def enterData_type_dec(self, ctx: PLpgSQLParser.Data_type_decContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#data_type_dec.
    def exitData_type_dec(self, ctx: PLpgSQLParser.Data_type_decContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#exception_statement.
    def enterException_statement(self, ctx: PLpgSQLParser.Exception_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#exception_statement.
    def exitException_statement(self, ctx: PLpgSQLParser.Exception_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#function_statements.
    def enterFunction_statements(self, ctx: PLpgSQLParser.Function_statementsContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#function_statements.
    def exitFunction_statements(self, ctx: PLpgSQLParser.Function_statementsContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#function_statement.
    def enterFunction_statement(self, ctx: PLpgSQLParser.Function_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#function_statement.
    def exitFunction_statement(self, ctx: PLpgSQLParser.Function_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#base_statement.
    def enterBase_statement(self, ctx: PLpgSQLParser.Base_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#base_statement.
    def exitBase_statement(self, ctx: PLpgSQLParser.Base_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#var.
    def enterVar(self, ctx: PLpgSQLParser.VarContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#var.
    def exitVar(self, ctx: PLpgSQLParser.VarContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#diagnostic_option.
    def enterDiagnostic_option(self, ctx: PLpgSQLParser.Diagnostic_optionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#diagnostic_option.
    def exitDiagnostic_option(self, ctx: PLpgSQLParser.Diagnostic_optionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#perform_stmt.
    def enterPerform_stmt(self, ctx: PLpgSQLParser.Perform_stmtContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#perform_stmt.
    def exitPerform_stmt(self, ctx: PLpgSQLParser.Perform_stmtContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#assign_stmt.
    def enterAssign_stmt(self, ctx: PLpgSQLParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#assign_stmt.
    def exitAssign_stmt(self, ctx: PLpgSQLParser.Assign_stmtContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#execute_stmt.
    def enterExecute_stmt(self, ctx: PLpgSQLParser.Execute_stmtContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#execute_stmt.
    def exitExecute_stmt(self, ctx: PLpgSQLParser.Execute_stmtContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#control_statement.
    def enterControl_statement(self, ctx: PLpgSQLParser.Control_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#control_statement.
    def exitControl_statement(self, ctx: PLpgSQLParser.Control_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#cursor_statement.
    def enterCursor_statement(self, ctx: PLpgSQLParser.Cursor_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#cursor_statement.
    def exitCursor_statement(self, ctx: PLpgSQLParser.Cursor_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#option.
    def enterOption(self, ctx: PLpgSQLParser.OptionContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#option.
    def exitOption(self, ctx: PLpgSQLParser.OptionContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#transaction_statement.
    def enterTransaction_statement(
        self, ctx: PLpgSQLParser.Transaction_statementContext
    ):
        pass

    # Exit a parse tree produced by PLpgSQLParser#transaction_statement.
    def exitTransaction_statement(
        self, ctx: PLpgSQLParser.Transaction_statementContext
    ):
        pass

    # Enter a parse tree produced by PLpgSQLParser#message_statement.
    def enterMessage_statement(self, ctx: PLpgSQLParser.Message_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#message_statement.
    def exitMessage_statement(self, ctx: PLpgSQLParser.Message_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#log_level.
    def enterLog_level(self, ctx: PLpgSQLParser.Log_levelContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#log_level.
    def exitLog_level(self, ctx: PLpgSQLParser.Log_levelContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#raise_using.
    def enterRaise_using(self, ctx: PLpgSQLParser.Raise_usingContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#raise_using.
    def exitRaise_using(self, ctx: PLpgSQLParser.Raise_usingContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#raise_param.
    def enterRaise_param(self, ctx: PLpgSQLParser.Raise_paramContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#raise_param.
    def exitRaise_param(self, ctx: PLpgSQLParser.Raise_paramContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#return_stmt.
    def enterReturn_stmt(self, ctx: PLpgSQLParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#return_stmt.
    def exitReturn_stmt(self, ctx: PLpgSQLParser.Return_stmtContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#loop_statement.
    def enterLoop_statement(self, ctx: PLpgSQLParser.Loop_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#loop_statement.
    def exitLoop_statement(self, ctx: PLpgSQLParser.Loop_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#loop_start.
    def enterLoop_start(self, ctx: PLpgSQLParser.Loop_startContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#loop_start.
    def exitLoop_start(self, ctx: PLpgSQLParser.Loop_startContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#using_vex.
    def enterUsing_vex(self, ctx: PLpgSQLParser.Using_vexContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#using_vex.
    def exitUsing_vex(self, ctx: PLpgSQLParser.Using_vexContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#if_statement.
    def enterIf_statement(self, ctx: PLpgSQLParser.If_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#if_statement.
    def exitIf_statement(self, ctx: PLpgSQLParser.If_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#case_statement.
    def enterCase_statement(self, ctx: PLpgSQLParser.Case_statementContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#case_statement.
    def exitCase_statement(self, ctx: PLpgSQLParser.Case_statementContext):
        pass

    # Enter a parse tree produced by PLpgSQLParser#plpgsql_query.
    def enterPlpgsql_query(self, ctx: PLpgSQLParser.Plpgsql_queryContext):
        pass

    # Exit a parse tree produced by PLpgSQLParser#plpgsql_query.
    def exitPlpgsql_query(self, ctx: PLpgSQLParser.Plpgsql_queryContext):
        pass


del PLpgSQLParser
