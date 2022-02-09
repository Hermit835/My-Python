import data_module

# Start Up
data_module.start_up()

while True:
    # Main Menu
    tables = data_module.pull_tables()
    main_menu = []
    for number, choice in enumerate(tables):
        print(f'{number + 1}: {choice[0]}')
        main_menu.append(choice[0].lower())

    print("4: Quit")
    main_menu.append('quit')
    # Main Menu
    while True:
        menu_select = input()
        if menu_select.isnumeric():
            if int(menu_select) <= len(main_menu):
                menu_select = main_menu[int(menu_select) - 1]
                break
        elif menu_select.lower() in main_menu:
            menu_select = menu_select.lower()
            break
        else:
            print("Please try again.")
            continue
    if menu_select == 'quit':
        break

    # Character Menu
    character_menu = ('view', 'search', 'add', 'remove', 'edit', 'go back')
    if menu_select == 'characters':
        while True:
            print('Character Menu')
            for number, choice in enumerate(character_menu):
                print(f'{number + 1}: {choice}')
            while True:
                character_select = input()
                if character_select.lower() in character_menu:
                    character_select = character_select.lower()
                    break
                elif character_select.isnumeric():
                    if int(character_select) <= len(character_menu):
                        character_select = character_menu[int(character_select) - 1]
                    break
                else:
                    print('Please use a valid option.')
            if character_select == 'go back':
                break

            # Character View Selection
            elif character_select == 'view':
                characters = data_module.show_characters()
                for character in characters:
                    print(f'{character[0]}')
                exit_view = input('Press Enter to continue.')

            # Character Search Selection
            elif character_select == 'search':
                print('Please enter the name of the character.')
                character_name = input()
                character_query = data_module.pull_character(character_name)
                if len(character_query) != 0:
                    character_query = character_query[0]
                    print(f'Name: {character_query[0]}\n'
                          f'Level: {character_query[1]}\n'
                          f'Experience: {character_query[2]}\n'
                          f'Skills:')
                    if character_query[3] is not None:
                        for skill in character_query[3]:
                            print(skill)
                    else:
                        print('None')
                else:
                    print('Character does not exist.')

            elif character_select == 'add':
                print("Enter Character's name: ")
                character_add = input()
                data_module.add_character(character_add)
                print(data_module.pull_character(character_add))

            elif character_select == 'remove':
                print("Enter the character's name you want to remove.")
                character_delete = input()
                if len(data_module.pull_character(character_delete)) != 0:
                    data_module.remove_character(character_delete)
                else:
                    print("Character already doesn't exist.")

            elif character_select == 'edit':
                print("Enter the character's name you wish to edit.")
                character_edit = input()
                if len(data_module.pull_character(character_edit)) != 0:
                    print(data_module.pull_character(character_edit))
                    print('What do you want to change?')
                    character_change = input()
                    if character_change == 'name':
                        print(f"What is {character_edit}'s new name?")
                        new_character_name = input()
                        data_module.edit_character_name(character_edit, new_character_name)
                        print(data_module.pull_character(new_character_name))
                    elif character_change == 'level':
                        while True:
                            print(f"What is {character_edit}'s new level?")
                            new_character_level = input()
                            if new_character_level.isnumeric():
                                print(f"Change {character_edit}'s level to {new_character_level}?")
                                new_character_level_confirm = input("yes/no\n ")
                                if new_character_level_confirm == 'yes':
                                    break
                                else:
                                    continue
                        data_module.edit_character_level(character_edit, int(new_character_level))
                        print(data_module.pull_character(character_edit))
                    elif character_change == 'experience':
                        while True:
                            print(f"What is {character_edit}'s new experience amount?")
                            new_character_experience = input()
                            if new_character_experience.isnumeric():
                                print(f"Change {character_edit}'s level to {new_character_experience}?")
                                new_character_experience_confirm = input("yes/no\n ")
                                if new_character_experience_confirm == 'yes':
                                    break
                                else:
                                    continue
                        data_module.edit_character_experience(character_edit, int(new_character_experience))
                        print(data_module.pull_character(character_edit))
                    elif character_change == 'skills':
                        skills = data_module.show_skills()
                        skill_list = []
                        for skill in skills:
                            skill_list.append(skill[0])
                        while True:
                            character = data_module.pull_character(character_edit)
                            character_skills = character[0][3]
                            character_skills = character_skills.split()
                            print(f"{character_edit}'s skills are: ")
                            for i in character_skills:
                                print(i)
                            print('Would you like to add/remove a skill?')
                            character_skill_change = input('yes/no')
                            if character_skill_change == 'yes':
                                character_skill_change = input('add/remove')
                                if character_skill_change == 'add':
                                    print('Enter skill name from list')
                                    for i in skill_list:
                                        print(i)
                                    character_skill_add = input()
                                    if character_skill_add in skill_list:
                                        character_skills.append(character_skill_add)
                                        character_skills = ' '.join(character_skills)
                                        data_module.edit_character_skills(character_edit, character_skills)
                                    else:
                                        print('Skill is not in List')
                                elif character_skill_change == 'remove':
                                    print(character_skills)
                                    print('What skill would you like to remove?')
                                    character_skill_remove = input()
                                    if character_skill_remove in character_skills:
                                        character_skills.remove(character_skill_remove)
                                        character_skills = ' '.join(character_skills)
                                        data_module.edit_character_skills(character_edit, character_skills)
                                    else:
                                        print('Skill is not in List')
                            else:
                                break
            else:
                print('Please select a valid option.')
    elif menu_select == 'items':
        print('Item Menu')
        item_menu = ('view', 'search', 'add', 'remove', 'edit', 'go back')
        while True:
            for number, item in enumerate(item_menu):
                print(f'{number + 1}: {item}')
            while True:
                item_menu_select = input()
                if item_menu_select.lower() in item_menu:
                    item_menu_select = item_menu_select.lower()
                    break
                elif item_menu_select.isnumeric():
                    if int(item_menu_select) <= len(item_menu):
                        item_menu_select = item_menu[int(item_menu_select) - 1]
                    break
                else:
                    print('Please use a valid option.')
            if item_menu_select == 'go back':
                break
            elif item_menu_select == 'view':
                item_view = data_module.show_items()
                for item in item_view:
                    print(f'{item[0]}')
                exit_view = input('Press Enter to continue')
            elif item_menu_select == 'search':
                print('What item do you want to search for?>')
                item_search = input()
                item_search_result = data_module.pull_item(item_search)
                if len(item_search_result) != 0:
                    print(item_search_result)
                else:
                    print("The item you searched for doesn't exist")
            elif item_menu_select == 'add':
                print('What item would you like to add?')
                item_add = input()
                item_add_check = data_module.pull_item(item_add)
                if len(item_add_check) != 0:
                    print('That item already exists.')
                else:
                    data_module.add_item(item_add)
            elif item_menu_select == 'remove':
                print('What item would you like to remove?')
                item_remove = input()
                item_remove_check = data_module.pull_item(item_remove)
                if len(item_remove_check) == 0:
                    print("That item doesn't exist.")
                else:
                    data_module.remove_item(item_remove)
            elif item_menu_select == 'edit':
                print('What item would you like to edit?')
                item_edit = input()
                item_edit_check = data_module.pull_item(item_edit)
                if len(item_edit_check) != 0:
                    print(f"name: {item_edit[0]}, description: {item_edit[1]}"
                          f"amount: {item_edit[2]}, special: {item_edit[3]}")
                    print(item_edit_check, '\n What would you like to change?')
                    item_edit_select = input()
                    if item_edit_select == 'name':
                        item_name = input('Please enter a new name: \n')
                        data_module.edit_item_name(item_edit, item_name)
                        print(data_module.pull_item(item_edit))
                    elif item_edit_select == 'description':
                        item_description = input("Please enter a new description:\n")
                        data_module.edit_item_description(item_edit, item_description)
                        print(data_module.pull_item(item_edit))
                    elif item_edit_select == 'amount':
                        while True:
                            item_amount = input("Please enter a new amount: \n")
                            if item_amount.isnumeric():
                                data_module.edit_item_amount(item_edit, int(item_amount))
                                print(data_module.pull_item(item_edit))
                                break
                            else:
                                print('Please enter a valid number.')
                    elif item_edit_select == 'special':
                        item_special = input('Please enter a new special effect.')
                        data_module.edit_item_special(item_edit, item_special)
                        print(data_module.pull_item(item_edit))
                    else:
                        print('Option not available.')
    elif menu_select == 'skills':
        skills_menu = ('view', 'search', 'add', 'remove', 'edit', 'go back')
        for number, i in enumerate(skills_menu):
            print(f'{number + 1}: {i}')
        while True:
            skills_menu_select = input()
            if skills_menu_select.isnumeric():
                if int(skills_menu_select) <= len(skills_menu):
                    skills_menu_select = skills_menu[int(skills_menu_select) - 1]
                    break
            elif skills_menu_select.lower() in skills_menu:
                skills_menu_select = skills_menu_select.lower()
                break
            else:
                print('Please select a valid option.')
        if skills_menu_select == 'view':
            skill_view = data_module.show_skills()
            for skill in skill_view:
                print(f'{skill_view[skill]}')
        elif skills_menu_select == 'search':
            skill_search = input('What item would you like to search for?\n')
            if len(data_module.pull_skill(skill_search)) != 0:
                skill_search_found = data_module.pull_skill(skill_search)
                print(f"name: {skill_search_found[0]}, "
                      f"level: {skill_search_found[1]}, "
                      f"experience{skill_search_found[2]}")
            else:
                print(f"{skill_search} doesn't exist")
        elif skills_menu_select == 'add':
            skill_add = input('What skill would you like to add?\n')
            if len(data_module.pull_skill(skill_add)) == 0:
                data_module.add_skill(skill_add)
                print(data_module.pull_skill(skill_add))
            else:
                print('That skill already exists')
        elif skills_menu_select == 'remove':
            skill_remove = input('What skill would you like to remove?\n')
            if len(data_module.pull_skill(skill_remove)) != 0:
                data_module.remove_skill(skill_remove)
                if len(data_module.pull_skill(skill_remove)) == 0:
                    print(f'{skill_remove} has been deleted')
                else:
                    print('Something went wrong')
            else:
                print(f'{skill_remove} does not exist')
        elif skills_menu_select == 'edit':
            skill_edit = input('What skill would you like to edit?\n')
            if data_module.skill_check(skill_edit):
                print(data_module.pull_skill(skill_edit))
                skill_edit_select = input('What would you like to change?\n')

                if skill_edit_select == 'name':
                    skill_edit_name = input('What is the new skill name?\n')
                    data_module.edit_item_name(skill_edit, skill_edit_name)
                    print(data_module.pull_skill(skill_edit_name))
                elif skill_edit_select == 'level':
                    skill_edit_level = input('What is the new skill level?\n')
                    if skill_edit_level.isnumeric():
                        skill_edit_level = int(skill_edit_level)
                        data_module.edit_skill_level(skill_edit, skill_edit_level)
                        print(data_module.pull_skill(skill_edit))
                    else:
                        print('Invalid entry. Please use a number.')
                elif skill_edit_select == 'experience':
                    skill_edit_experience = input('What is the new skill experience?\n')
                    if skill_edit_experience.isnumeric():
                        skill_edit_experience = int(skill_edit_experience)
                        data_module.edit_skill_experience(skill_edit, skill_edit_experience)
                        print(data_module.pull_skill(skill_edit))
                    else:
                        print('Invalid entry. Please use a number.')
                else:
                    print('Please use a valid option.')
        elif skills_menu_select == 'go back':
            break
    elif menu_select == 'quit':
        data_module.close_up()
        break
