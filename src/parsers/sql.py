import traceback
import ast
import json
import sqlglot

from typing import List

from sqlglot import expressions
from utils.logs import get_logger
from .base_parser import BaseParser

logger = get_logger(__name__)

class SQLParser(BaseParser):
    _EXTENSIONS = ['.sql']

    def get_itr(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            buffer = []
            for line in f:
                try:
                    stripped = line.strip()
                    if not stripped or stripped.startswith('--') or stripped.startswith('/*'):
                        continue
                        
                    buffer.append(line)
                    if stripped.endswith(';'):
                        full_sql = "".join(buffer).strip()
                        
                        if full_sql.upper().startswith("INSERT"):
                            yield from self.parse_insert(full_sql)
                        else:
                            firstLine = full_sql.split('\n')[0]
                            logger.info("Disregarding command due to not detecting an INSERT: %s", firstLine)
                            
                        buffer = []
                except Exception:
                    traceback.print_exc()

    def _try_parse_json(self, value):
        if not isinstance(value, str):
            return value
        
        # Quick check to avoid unnecessary parsing attempts on non-JSON strings
        stripped = value.strip()
        if not (stripped.startswith('{') or stripped.startswith('[')):
            return value

        try:
            parsed = json.loads(stripped)
            if isinstance(parsed, (dict, list)):
                return parsed
        except (json.JSONDecodeError, TypeError):
            pass
            
        return value

    def _extract_value(self, item):
        val = None
        if isinstance(item, expressions.Literal):
            if item.is_string:
                val = item.this
            elif item.is_number:
                try:
                    val = ast.literal_eval(item.this)
                except (ValueError, SyntaxError):
                    val = item.this
            else:
                val = item.this
        elif isinstance(item, expressions.Null):
            val = None
        elif isinstance(item, expressions.Boolean):
            val = item.this
        else:
            val = item.sql()
            
        # Detect if the extracted value is actually a JSON structure
        return self._try_parse_json(val)

    def parse_insert(self, sql):
        try:
            parsed = sqlglot.parse_one(sql, read="mysql")

            if not parsed or not isinstance(parsed, expressions.Insert):
                logger.warning("Statement parsed but is not an INSERT statement.")
                return

            # Extract Table Name and Columns
            target = parsed.this
            columns: List[str] = []
            
            #TODO: Use this
            table_name = ""

            if isinstance(target, expressions.Schema):
                table_name = target.this.name
                columns = [col.name for col in target.expressions]
            elif isinstance(target, expressions.Table):
                table_name = target.name
            else:
                table_name = target.sql()

            # Extract Values and yield row by row
            values_node = parsed.expression

            
            if values_node and isinstance(values_node, expressions.Values):
                for value_tuple in values_node.expressions:
                    raw_values = [self._extract_value(v) for v in value_tuple.expressions]
                    
                    if columns and len(columns) == len(raw_values):
                        raw_values.append(str(dict(zip(columns, raw_values))))
                        yield dict(zip([*columns, "line"], raw_values))
                    else:
                        logger.warning(f"Column length and values length does not match: {columns} {raw_values}")


        except Exception as e:
            traceback.print_exc()
            logger.error(f"Error parsing INSERT statement: {e}")