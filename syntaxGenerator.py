from typing import Dict, List

class SyntaxGenerator:
    def __init__(self) -> None:
        # Stores the generated slicing syntax for multiple plate names
        self.syntax_paths: List[str] = []

    def find_slice_indices(self, platename: str, slise_names: List[str]) -> str:
        """
        Finds the start and end indices for each `slise_name` in `platename`
        and returns the formatted slicing syntax.
        
        Args:
            platename (str): The full plate name.
            slise_names (List[str]): A list of substrings to find in platename.

        Returns:
            str: A formatted slicing syntax string.
        """
        slice_syntax = []
        
        for slise_name in slise_names:
            # Find the starting index of the substring in the plate name
            start = platename.find(slise_name)
            if start == -1:
                continue  # Skip if the substring is not found
            
            # Calculate the end index
            end = start + len(slise_name)
            
            # Append the slicing syntax to the list
            slice_syntax.append(f"platename[{start}:{end}]")
        
        # Join all slicing syntaxes with '/' to match the expected output format
        return "/".join(slice_syntax)

    def process_names(self, name_data: Dict[str, List[str]]) -> List[str]:
        """
        Processes multiple plate names and extracts slicing syntax.
        
        Args:
            name_data (Dict[str, List[str]]): A dictionary where keys are plate names
            and values are lists of substrings to find in each plate name.

        Returns:
            List[str]: A list of formatted slicing syntax strings.
        """
        # Generate slicing syntax for each platename and store results
        self.syntax_paths = [self.find_slice_indices(platename, slise_names) 
                             for platename, slise_names in name_data.items()]
        return self.syntax_paths
