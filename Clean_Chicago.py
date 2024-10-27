def clean_Colors(STATIONS_DF):
    # Clean Line Colors

    """
    def get_line_color(line_string):
    Extracts the primary line color from a string describing multiple lines.
    if 'Blue' in line_string:
        return 'Blue'
    elif 'Green' in line_string:
        return 'Green'
    elif 'Brown' in line_string:
        return 'Brown'
    elif 'Red' in line_string:
        return 'Red'
    elif 'Orange' in line_string:
        return 'Orange'
    elif 'Pink' in line_string:
        return 'Pink'
    elif 'Purple' in line_string:
        return 'Purple'
    elif 'Yellow' in line_string:
        return 'Yellow'
    else:
        return 'Other'  # Handle cases with no recognizable color

    """

    def get_line_color(line_string):
        """Extracts the primary line color from a string describing multiple lines."""
        line_color = []
        if 'Blue' in line_string:
            line_color.append('Blue')
        if 'Green' in line_string:
            line_color.append('Green')
        if 'Brown' in line_string:
            line_color.append('Brown')
        if 'Red' in line_string:
            line_color.append('Red')
        if 'Orange' in line_string:
            line_color.append('Orange')
        if 'Pink' in line_string:
            line_color.append('Pink')
        if 'Purple' in line_string:
            line_color.append('Purple')
        if 'Yellow' in line_string:
            line_color.append('Yellow')

        return line_color

    # Apply the function to create the new column
    STATIONS_DF['LINE_COLOR'] = STATIONS_DF['LINES'].apply(get_line_color)


def clean_station_names( CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY):
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Western-Cermak', 'Western-Douglas')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Kedzie-Homan-Forest Park','Kedzie-Homan')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Kedzie-Brown','Kedzie-Ravenswood')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Kedzie-Cermak','Kedzie-Douglas')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Conservatory','Conservatory-Central Park')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Cicero-Cermak','Cicero-Douglas')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Cicero-Forest Park','Cicero-Congress')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Austin-Forest Park','Austin-Congress')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('East 63rd-Cottage Grove','Cottage Grove')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Western-Orange','Western-Midway')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Western-Forest Park','Western-Congress')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Western-Brown','Western-Ravenswood')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Pulaski-Forest Park','Pulaski-Congress')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Pulaski-Orange','Pulaski-Midway')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Pulaski-Cermak','Pulaski-Douglas')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Damen-Brown','Damen-Ravenswood')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Clinton-Forest Park','Clinton-Congress')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Addison-Brown','Addison-Ravenswood')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Irving Park-Brown','Irving Park-Ravenswood')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Morgan-Lake','Morgan')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Harlem-Forest Park','Harlem-Congress')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Halsted-Orange','Halsted-Midway')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Ashland-Orange','Ashland-Midway')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Oak Park-Forest Park','Oak Park-Congress')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Montrose-Brown','Montrose-Ravenswood')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('California-Cermak','California-Douglas')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Medical Center','Illinois Medical District')
    CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'] = CTA_RIDERSHIP_L_STATION_ENTRIES_DAILY['STATION_NAME'].replace('Damen-Cermak','Damen')
