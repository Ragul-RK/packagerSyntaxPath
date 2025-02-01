from syntaxGenerator import SyntaxGenerator
from typing import Dict, List

# Define the input dictionary containing plate names and their corresponding substrings
name_data: Dict[str, List[str]] = {
    "WOK_305_2026_mp01_v008": ["WOK_305", "2026", "mp01"]
}#"TSM_040_0095_mp01_roto_bot_v0001": ["TSM_040", "0095", "mp01"],"WOK_305_2026_mp01_v008": ["WOK_305", "2026", "mp01"]

# Create an instance of SyntaxGenerator
generator = SyntaxGenerator()

# Process the name_data dictionary to generate syntax paths
syntax_paths = generator.process_names(name_data)

# Print the generated slicing syntax
print(syntax_paths)  # Output: ['platename[0:7]/platename[8:12]/platename[13:17]', 'platename[...]']
