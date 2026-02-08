#!/usr/bin/env python3
def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    # Handle empty inputs
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        content = template

        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"
        try:
            with open(filename, "w") as file:
                file.write(content)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
