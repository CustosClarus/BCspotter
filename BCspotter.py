#!/usr/bin/python3
import re

def process_memory_dump(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File not found at {file_path}")
    except Exception as e:
        raise Exception(f"Error: Unable to open the file - {e}")

    hex_values = []

    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue

        hex_matches = re.findall(r"\b[0-9A-Fa-f]{2}\b", line)

        hex_values.extend(hex_matches)

    print(f"me {hex_values[5]}")
    return hex_values


        
def find_absent_bad_chars(hex_values, bad_chars):
    absent_bad_chars = []

    # Iterate over each index of bad_chars
    for char_index in range(len(bad_chars)):
        # Get the character from bad_chars
        char_to_check = bad_chars[char_index]

        # Flag to check if the character is present in hex_values
        char_present = False

        # Nested loop to check if the character is present in hex_values
        for hex_value in hex_values:
            if char_to_check in hex_value:
                char_present = True
                break

        # If the character is not present, append to the list
        if not char_present:
            absent_bad_chars.append(char_to_check)

    return absent_bad_chars

def hex_to_ascii(hex_value):
    # Convert hex value to decimal integer
    decimal_value = int(hex_value, 16)
    
    # Get ASCII representation if printable, otherwise 'non-printable'
    ascii_char = chr(decimal_value) if 32 <= decimal_value <= 126 else 'non-printable'
    
    return ascii_char

def print_hex_and_ascii(absent_bad_chars):
    for absent_bad_char in absent_bad_chars:
        ascii_representation = hex_to_ascii(absent_bad_char)
        print(f"Hex Value: {absent_bad_char} | ASCII or Non-Printable: {ascii_representation}")


def hex_to_character(hex_value):
    # Convert hex value to bytes
    byte_value = bytes.fromhex(hex_value)

    # Decode using different encodings
    try:
        # Try decoding using ASCII
        character = byte_value.decode('ascii')
    except UnicodeDecodeError:
        try:
            # If ASCII decoding fails, try decoding using UTF-8
            character = byte_value.decode('utf-8')
        except UnicodeDecodeError:
            # If both ASCII and UTF-8 decoding fail, mark as 'non-decodable'
            character = 'non-decodable'

    return character

def print_hex_and_character(hex_values):
    for hex_value in hex_values:
        character_representation = hex_to_character(hex_value)
        print(f"Hex Value: {hex_value} | Character Representation: {character_representation}")

# Define the file path and bad characters
file_path = "dump"  # Update the file name accordingly
bad_chars = [
    "00", "02", "03", "04", "05", "06", "07", "08", "09", "0A", "0B", "0C", "0D", "0E", "0F", "10",
    "11", "12", "13", "14", "15", "16", "17", "18", "19", "1A", "1B", "1C", "1D", "1E", "1F", "20",
    "21", "22", "23", "24", "25", "26", "27", "28", "29", "2A", "2B", "2C", "2D", "2E", "2F", "30",
    "31", "32", "33", "34", "35", "36", "37", "38", "39", "3A", "3B", "3C", "3D", "3E", "3F", "40",
    "41", "42", "43", "44", "45", "46", "47", "48", "49", "4A", "4B", "4C", "4D", "4E", "4F", "50",
    "51", "52", "53", "54", "55", "56", "57", "58", "59", "5A", "5B", "5C", "5D", "5E", "5F", "60",
    "61", "62", "63", "64", "65", "66", "67", "68", "69", "6A", "6B", "6C", "6D", "6E", "6F", "70",
    "71", "72", "73", "74", "75", "76", "77", "78", "79", "7A", "7B", "7C", "7D", "7E", "7F", "80",
    "81", "82", "83", "84", "85", "86", "87", "88", "89", "8A", "8B", "8C", "8D", "8E", "8F", "90",
    "91", "92", "93", "94", "95", "96", "97", "98", "99", "9A", "9B", "9C", "9D", "9E", "9F", "A0",
    "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "AA", "AB", "AC", "AD", "AE", "AF", "B0",
    "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "BA", "BB", "BC", "BD", "BE", "BF", "C0",
    "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "CA", "CB", "CC", "CD", "CE", "CF", "D0",
    "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "DA", "DB", "DC", "DD", "DE", "DF", "E0",
    "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "EA", "EB", "EC", "ED", "EE", "EF", "F0",
    "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "FA", "FB", "FC", "FD", "FE", "FF",
]
# Process the memory dump
hex_values = process_memory_dump(file_path)
absent_bad_chars = find_absent_bad_chars(hex_values, bad_chars)
print("Absent Bad Characters:", absent_bad_chars)
print_hex_and_character(absent_bad_chars)
