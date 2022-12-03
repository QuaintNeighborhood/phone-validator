import argparse
import phonenumbers
from phonenumbers import phonenumberutil
from phonenumbers import carrier


def main():
    parser = argparse.ArgumentParser(
        prog='PhoneValidator',
        description='Validates and provides extra information on phone numbers')
    parser.add_argument('-i', '--input', help='Input file', required=True)
    parser.add_argument('-o', '--output', help='Output file', required=True)
    args = parser.parse_args()

    # Open input file
    with open(args.input, 'r') as input_file, open(args.output, 'wt') as output_file:
        # Write header
        output_file.write("Number,Valid/Invalid,Type,Carrier\n")
        # Read all lines
        for row in input_file:
            # Write row to output file, line by line
            output_file.write(generate_row(row))


def generate_row(number_row: str) -> str:
    output_row = ""
    row = number_row.strip()
    output_row += row + ","
    try:
        parsed_number = phonenumbers.parse(row, None)
    except phonenumberutil.NumberParseException:
        output_row += "Invalid" + "\n"
        return output_row

    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    if not is_valid_number:
        output_row += "Invalid" + "\n"
        return output_row

    output_row += "Valid" + ","
    number_type_int = phonenumbers.number_type(parsed_number)
    number_type = phonenumberutil.PhoneNumberType.to_string(number_type_int)
    output_row += number_type + ","
    carrier_name = carrier.name_for_number(parsed_number, "en") or "Unknown"
    output_row += carrier_name + "\n"
    return output_row


if __name__ == '__main__':
    main()
