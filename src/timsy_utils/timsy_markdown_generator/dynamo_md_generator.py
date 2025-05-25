import os
from typing import List, Dict, Any, Optional

class DynamoMarkdownGenerator:
    """
    Generates Markdown/HTML documentation for DynamoDB-like items or SQL table definitions.
    """
    def __init__(self, output_dir: str = "output"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def get_unique_filename(self, base_name: str, extension: str = ".md") -> str:
        file_path = os.path.join(self.output_dir, f"{base_name}{extension}")
        counter = 1
        while os.path.exists(file_path):
            file_path = os.path.join(self.output_dir, f"{base_name}_{counter}{extension}")
            counter += 1
        return file_path

    def generate_markdown(self, item: Dict[str, Any]) -> str:
        """
        Generates markdown/HTML content for a given item (DynamoDB or SQL table dict).
        """
        table_rows = ""
        details_sections = ""
        details = item.get("_Details", {})
        for key, value in item.items():
            if key == "_Details":
                continue
            details_link = ""
            if key in details:
                details_link = f' - <a href="#{key.lower()}-details">See details</a>'
            table_rows += f"""
<tr>
<td style=\"border: 1px solid #ccc; padding: 8px;\">{key}</td>
<td style=\"border: 1px solid #ccc; padding: 8px;\">{value}</td>
<td style=\"border: 1px solid #ccc; padding: 8px;\">{details.get(key, {}).get('Description', '')}{details_link}</td>
<td style=\"border: 1px solid #ccc; padding: 8px;\">{details.get(key, {}).get('Pattern', '')}</td>
</tr>
            """
        for detail_key, detail in details.items():
            key_value_description_section = ""
            pattern_section = ""
            if detail.get("IsPattern", False):
                pattern_values = ""
                for value in detail.get("PatternValues", []):
                    options = ""
                    if len(value) > 2:
                        options = f" (Options: {', '.join(value[2])})"
                    pattern_values += f"<li><strong>{value[0]}</strong>: {value[1]}{options}</li>"
                pattern_section = f"""
<p>The pattern for this attribute is: <code>{detail['Pattern']}</code></p>
<ul>
{pattern_values}
</ul>
"""
            key_value_description = detail.get("KeyValueDescription", "")
            if key_value_description:
                key_value_description_section = f"""
<h4 style=\"font-family: Arial, sans-serif; color: #333;\">Value Description</h4>
<p>{key_value_description}</p>
"""
            details_sections += f"""
<div style=\"border: 1px solid #ccc; padding: 15px; border-radius: 5px; background-color: #fff; margin-bottom: 20px;\">
<h3 id=\"{detail_key.lower()}-details\" style=\"font-family: Arial, sans-serif; color: #333;\">{detail_key} Details</h3>
<p>{detail['Description']}</p>
{key_value_description_section}
{pattern_section}
</div>
"""
        template = f"""
<div style=\"border: 1px solid #ddd; padding: 20px; border-radius: 5px; background-color: #f9f9f9; margin-bottom: 20px;\">
<h2 style=\"font-family: Arial, sans-serif; color: #333;\">{{item_name}}</h2>
<div style=\"border: 1px solid #ccc; padding: 15px; border-radius: 5px; background-color: #fff; margin-bottom: 20px;\">
<table style=\"width: 100%; border-collapse: collapse; margin-top: 10px;\">
<tr>
<th style=\"border: 1px solid #ccc; padding: 8px; background-color: #f1f1f1; text-align: left;\">Attribute</th>
<th style=\"border: 1px solid #ccc; padding: 8px; background-color: #f1f1f1; text-align: left;\">Value</th>
<th style=\"border: 1px solid #ccc; padding: 8px; background-color: #f1f1f1; text-align: left;\">Description</th>
<th style=\"border: 1px solid #ccc; padding: 8px; background-color: #f1f1f1; text-align: left;\">Pattern</th>
</tr>
{{table_rows}}
</table>
</div>
{{details_sections}}
</div>
"""
        return template.replace("{{item_name}}", str(item.get("item_name", item.get("table_name", "Unknown Item")))) \
                      .replace("{{table_rows}}", table_rows) \
                      .replace("{{details_sections}}", details_sections)

    def write_markdown(self, item: Dict[str, Any], base_name: Optional[str] = None) -> str:
        """
        Writes the generated markdown to a file and returns the file path.
        """
        if not base_name:
            base_name = item.get("item_name", item.get("table_name", "item")).replace(" ", "_")
        file_path = self.get_unique_filename(base_name)
        markdown_content = self.generate_markdown(item)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(markdown_content)
        return file_path

    def process_items(self, items: List[Dict[str, Any]]):
        """
        Processes a list of items and writes markdown files for each.
        """
        for item in items:
            self.write_markdown(item)

    @staticmethod
    def from_sql_table(table_name: str, columns: List[Dict[str, Any]], details: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Converts SQL table metadata to the item dict format expected by the generator.
        columns: List of dicts with keys: name, type, description, is_primary, etc.
        details: Optional dict for richer attribute documentation.
        """
        item = {
            "item_name": table_name,
        }
        for col in columns:
            item[col["name"]] = col.get("type", "")
        if details:
            item["_Details"] = details
        return item

# Example usage:
if __name__ == "__main__":
    # Example DynamoDB items (replace with your own data source)
    dynamodb_items = [
        {
            "item_name": "User Profile",
            "PK": "12345",
            "SK": "PROFILE#12345",
            "Name": "John Doe",
            "Email": "john.doe@example.com",
            "EmailIsVerified": True,
            "Signup Date": "2023-05-18",
            "UserReferralCode": "EMPLOYEE#ABCD1234",
            "_Details": {
                "PK": {
                    "Type": "String",
                    "Description": "The primary key for the item.",
                    "IsPattern": False,
                    "KeyValueDescription": "The User ID"
                },
                "SK": {
                    "Type": "String",
                    "Description": "The sort key for the item.",
                    "IsPattern": True,
                    "Pattern": "PROFILE#{{user_id}}",
                    "PatternValues": [
                        ("PROFILE", "DynamoDB Item Type"),
                        ("User ID", "Unique User ID")
                    ]
                },
                "EmailIsVerified": {
                    "Type": "Boolean",
                    "Description": "Indicates if the user's email is verified.",
                    "IsPattern": False,
                    "KeyValueDescription": "Whether the email has been verified"
                },
                "UserReferralCode": {
                    "Type": "String",
                    "Description": "The referral code used to sign the user up.",
                    "IsPattern": True,
                    "Pattern": "{{user_type}}#{{user_code}}",
                    "PatternValues": [
                        ("User Type", "Type of user", ["EMPLOYEE", "CUSTOMER"]),
                        ("User Code", "Unique user code")
                    ]
                }
            }
        },
        {
            "item_name": "Product Order Detail",
            "PK": "ORDER#Laptop",
            "SK": "ORDERDETAIL#ONLINE#67890",
            "Product": "Laptop",
            "Quantity": 1,
            "Order Date": "2023-05-20",
            "_Details": {
                "PK": {
                    "Type": "String",
                    "Description": "The primary key for the item.",
                    "IsPattern": True,
                    "Pattern": "ORDER#{{product_type}}",
                    "PatternValues": [
                        ("ORDER", "DynamoDB Item Type"),
                        ("Product Type", "Product type")
                    ]
                },
                "SK": {
                    "Type": "String",
                    "Description": "The sort key for the item.",
                    "IsPattern": True,
                    "Pattern": "ORDERDETAIL#{{order_location}}#{{order_id}}",
                    "PatternValues": [
                        ("ORDERDETAIL", "DynamoDB Item Type"),
                        ("Order Location", "Location of the order", ["ONLINE", "IN-STORE"]),
                        ("Order ID", "Unique Order ID")
                    ]
                },
                "Quantity": {
                    "Type": "Number",
                    "Description": "The quantity of the product ordered.",
                    "IsPattern": False,
                    "KeyValueDescription": "The number of products ordered."
                }
            }
        }
    ]
    generator = DynamoMarkdownGenerator()
    generator.process_items(dynamodb_items)

    # Example for SQL table (simulate SQL metadata)
    sql_columns = [
        {"name": "id", "type": "INT", "description": "Primary key", "is_primary": True},
        {"name": "username", "type": "VARCHAR(255)", "description": "User's name"},
        {"name": "email", "type": "VARCHAR(255)", "description": "User's email address"},
    ]
    sql_details = {
        "id": {"Type": "INT", "Description": "Primary key", "IsPattern": False},
        "username": {"Type": "VARCHAR(255)", "Description": "User's name", "IsPattern": False},
        "email": {"Type": "VARCHAR(255)", "Description": "User's email address", "IsPattern": False},
    }
    sql_item = DynamoMarkdownGenerator.from_sql_table("User", sql_columns, sql_details)
    generator.write_markdown(sql_item)

