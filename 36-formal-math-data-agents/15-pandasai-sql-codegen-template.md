# PandasAI Code-Generation Prompt Template (templates/generate_python_code_with_sql.tmpl)

Title: PandasAI Code-Generation Prompt Template (templates/generate_python_code_with_sql.tmpl)
Source-URL: https://raw.githubusercontent.com/Sinaptik-AI/pandas-ai/main/pandasai/core/prompts/templates/generate_python_code_with_sql.tmpl
Source-Repo-or-Site: Sinaptik-AI/pandas-ai (https://github.com/Sinaptik-AI/pandas-ai)
Original-Path: pandasai/core/prompts/templates/generate_python_code_with_sql.tmpl
Category: data-agents / dataframe-agent
Tags: pandasai, dataframe, jinja-template, sql-codegen, output-contract
Retrieved: 2026-11-08
Value-Note: PandasAI pure prompt template: dataframe schemas, conversation memory, SQL helper contract and strict output-type rules composed via shared includes - chat-with-dataframes reasoning core.
Original-Lines: 32

--- ORIGINAL ---
````jinja
<tables>
{% for df in context.dfs %}
{% include 'shared/dataframe.tmpl' with context %}
{% endfor %}
</tables>

{% include 'shared/sql_functions.tmpl' with context %}

{% if last_code_generated and context.memory.count() > 0 %}
Last code generated:
{{ last_code_generated }}
{% else %}
Update this initial code:
```python
# TODO: import the required dependencies
import pandas as pd

# Write code here

# Declare result var: {% include 'shared/output_type_template.tmpl' with context %}
```
{% endif %}
{% include 'shared/vectordb_docs.tmpl' with context %}
{{ context.memory.get_last_message() }}

At the end, declare "result" variable as a dictionary of type and value in the following format:
{% include 'shared/output_type_template.tmpl' with context %}


Generate python code and return full updated code:

### Note: Use only relevant table for query and do aggregation, sorting, joins and grouby through sql query
````
