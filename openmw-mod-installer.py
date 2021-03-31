import os

def print_app_info():
    print('OpenMW Mod Installer\nv1.0\n\nType "-help" for help.')

def print_help_menu(default_file_location):
    print('Help:\n')  
    print('  Setup:')
    print('    - Make sure this executable is located in the same directory as all your mod folders.')
    print('    - Make sure the only folders in this directory are mod folders.')
    print('    - Mod folders must be structured according to OpenMW requirements (<mod_folder>\<resource folders>).')
    print()
    print('  Commands:\n    -help\t\t\t- Help menu.')
    print('    -exit, -e, -quit, -q\t- Exits the application.')
    print()
    print('  Default config file location: "{}"'.format(default_file_location))

def get_sibling_dirs():
    directories = []
    for directory in os.listdir():
        # make sure it's a directory
        if os.path.isdir(os.path.abspath(directory)):
            directories.append(directory)

    return(directories)

def create_file_backup(cfg_file_location, filename):
    old_cfg_file_path = cfg_file_location + filename + '.cfg'
    old_cfg_file = open(old_cfg_file_path, 'r')
    cfg_lines = old_cfg_file.readlines()
    old_cfg_file.close()
    cfg_file_backup = open(cfg_file_location + filename + '_backup.cfg', 'w')
    cfg_file_backup.writelines(cfg_lines)
    cfg_file_backup.close()

def get_cfg_file_input(default_file_location):
    cfg_file_location = ''

    # keep asking user for config file location until a valid one is found
    while True:
        cfg_file_location = input('\nEnter config file location (leave blank for default): ').strip()

        # check if using a command
        if cfg_file_location.startswith('-'):
            # check if exiting program
            if '-exit' in cfg_file_location or '-quit' in cfg_file_location \
                    or '-e' in cfg_file_location or '-q' in cfg_file_location:
                exit()

            # check if getting help menu
            if '-help' in cfg_file_location:
                print_help_menu(default_file_location)
                continue

            print('Invalid command(s).')
            continue

        # check if leaving blank, set it to default location if true
        if cfg_file_location == '':
            cfg_file_location = default_file_location
            print('Using default file location.')

        # adding a correct slash if its the wrong one
        if cfg_file_location.endswith('\\'):
            cfg_file_location = cfg_file_location[:-1]
            cfg_file_location += '/'

        # adding a slash if it doesn't exist
        if not cfg_file_location.endswith('/'):
            cfg_file_location += '/'

        print()

        # check if path exists and is an openmw.cfg file
        if not os.path.isdir(cfg_file_location):
            print('Not a valid directory.')
        elif not os.path.isfile(cfg_file_location + 'openmw.cfg'):
            print('Directory does not contain an OpenMW config file.')
        else:
            print('Config file found.\nCreating backup...')

            # create a backup of the file
            create_file_backup(cfg_file_location, 'openmw')

            print('Done.\n')

            break

    return(cfg_file_location)

def write_new_lines(cfg_file_location, mod_directories):
    cfg_file_path = cfg_file_location + 'openmw.cfg'

    # open the config file and read lines to memory as a list
    cfg_file = open(cfg_file_path, 'r')
    cfg_lines = cfg_file.readlines()
    cfg_file.close()

    # Look through the lines to get the ones before the data lines
    new_cfg_lines = []
    for line in cfg_lines:
        # check if its a 'data=' line
        if line.startswith('data='):
            # Check if it's the Morrowind\Data Files line and add it if true
            if line.endswith('Morrowind\Data Files"\n'):
                new_cfg_lines.append(line)

            break

        new_cfg_lines.append(line)

    # Append the new data lines
    for directory in mod_directories:
        new_line = 'data="' + os.path.abspath(directory) + '"\n'
        #print(new_line)
        new_cfg_lines.append(new_line)

    # Add the remaining lines after the data lines
    seen_data_section = False
    for line in cfg_lines:
        # flag that we've seen the data section already
        if line.startswith('data='):
            seen_data_section = True
        elif seen_data_section == True:
            # we've seen the data section and we're already past it, so add the line
            new_cfg_lines.append(line)

    # overwrite the config file with all the new lines
    cfg_file = open(cfg_file_path, 'w')
    cfg_file.writelines(new_cfg_lines)
    cfg_file.close()

def run_app():
    print_app_info()

    # get the config file location
    default_file_location = os.path.expanduser('~/Documents/My Games/OpenMW/')
    #default_file_location = os.path.abspath(os.getcwd() + '\config_test_files')
    cfg_file_location = get_cfg_file_input(default_file_location)

    # get all of the mod directories in this directory
    mod_directories = get_sibling_dirs()

    print('Found {} mod folders.\nWriting to config file...'.format(len(mod_directories)))

    write_new_lines(cfg_file_location, mod_directories)

    print('Done.\n')
    input('Press Enter to exit...')

run_app()