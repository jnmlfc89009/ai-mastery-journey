"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    
    # First, determine the length of the shorter string
    len1 = len(line1)
    len2 = len(line2)
    shorter_len = min(len1, len2)

    for idx in range(shorter_len):
        if line1[idx] != line2[idx]:
            return idx
   
    # If we got here, the prefix matches. 
    # Check if one is longer than the other.
    if len1 != len2:
        return shorter_len
    
    
    return IDENTICAL


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    
    # 1. Validation Bouncer
    # Check for newlines/carriage returns
    
    if "\n" in line1 or "\r" in line1 or "\n" in line2 or "\r" in line2:
        return ""
    
    shorter_len = min(len(line1), len(line2))
    
    if idx < 0 or idx > shorter_len:
        return ""
    
    # 2. Build the Separator
    
    separator = ("=" * idx) + "^"
    
    # 3. Assemble the 3 lines
    # We use \n to move to the next line after each part
    
    result = line1 + "\n" + separator + "\n" + line2 + "\n"
    
    return result


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    
    # Determine how many lines both lists share
    shorter_len = min(len(lines1), len(lines2))
    
    for line_idx in range(shorter_len):
    
        # Call your Problem 1 function for the current line
        char_idx = singleline_diff(lines1[line_idx], lines2[line_idx])
    
        # If a difference was found (not IDENTICAL)
        if char_idx != IDENTICAL:
            return (line_idx, char_idx)
    
    if len(lines1) != len(lines2):
        return (shorter_len, 0)
    
    return (IDENTICAL, IDENTICAL)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    
    # 1. Create an empty list to be our 'Collector'
    lines = []
    
    # 2. Use 'with' to open the file safely
    with open(filename, "rt", encoding="utf-8") as file:
        # 3. Loop through each line in the file object
        for line in file:
            # 4. Strip the invisible line endings and add to our list
            clean_line = line.rstrip('\n\r')
            lines.append(clean_line)
            
    # 5. Return the full list of clean lines
    return lines


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    
    line_idx, char_idx = multiline_diff(lines1, lines2)
    
    if line_idx == IDENTICAL:
        return "No differences\n"
    
    # Check if the line actually exists in the list before grabbing it
    line1 = lines1[line_idx] if line_idx < len(lines1) else ""
    line2 = lines2[line_idx] if line_idx < len(lines2) else ""

    # Now call your Problem 2 function
    formatting = singleline_diff_format(line1, line2, char_idx)
    
    return "Line " + str(line_idx) + ":" + "\n" + formatting

