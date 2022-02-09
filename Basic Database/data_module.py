import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()


# Start Up
def tables_verification() -> bool:
    """
    Check if tables exist in database.
    :return: Boolean
    """
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return len(tables) != 0


def create_tables() -> None:
    """
    Create Characters, Skills, and Items tables under the condition that they don't exist already.
    :return: None
    """
    cursor.execute('CREATE TABLE IF NOT EXISTS Characters(name TEXT, level INT, experience INT, skills LIST)')
    cursor.execute('CREATE TABLE IF NOT EXISTS Skills(name TEXT, level INT, experience INT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS Items(name TEXT, description TEXT, amount INT, special TEXT)')
    conn.commit()


def start_up() -> None:
    """
    Check if tables exist. If not, create Characters, Skills, and Items tables in database.
    :return: None
    """
    verify = tables_verification()
    if not verify:
        create_tables()


# Main Menu
def pull_tables() -> list:
    """
    Fetch tables from my_database. Return List.
    :return: List of tables.
    """
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return tables


# Character Menu
def show_characters() -> list:
    """
    Fetch list of rows from Characters Table
    :return: List of Characters
    """
    cursor.execute('SELECT * FROM Characters')
    characters = cursor.fetchall()
    return characters


def edit_character_name(character: str, replacement: str) -> None:
    """
    Replace name value of character.
    :param: character: Name of character
    :param: replacement: Replacement value
    :return: None
    """
    cursor.execute('UPDATE Characters SET name = :value WHERE name = :character',
                   {'value': replacement, 'character': character})
    conn.commit()


def edit_character_level(character: str, replacement: int) -> None:
    """
    Replace level value of character.
    :param: character: Name of character
    :param: replacement: Replacement value
    :return: None
    """
    cursor.execute('UPDATE Characters SET level = :value WHERE name = :character',
                   {'value': replacement, 'character': character})
    conn.commit()


def edit_character_experience(character: str, replacement: int) -> None:
    """
    Replace experience value in character.
    :param character: Name of character
    :param replacement: Replacement value
    :return: None
    """
    cursor.execute('UPDATE Characters SET experience = :value WHERE name = :character',
                   {'value': replacement, 'character': character})
    conn.commit()


def edit_character_skills(character: str, replacement: str) -> None:
    """
    Replace skills value in character.
    :param: character: Name of character
    :param: replacement: Replacement value
    :return: None
    """
    cursor.execute('UPDATE Characters SET skills = :value WHERE name = :character',
                   {'value': replacement, 'character': character})
    conn.commit()


def remove_character(character) -> None:
    """
    Remove row where name is equal to character.
    :param: character: Name of row/character
    :return: None
    """
    cursor.execute('DELETE FROM Characters WHERE name = :character',
                   {'character': character})
    conn.commit()


def add_character(character) -> None:
    """
    Add a new row to Characters Table with name equal to character.
    Level = 1, Experience = 0, Skills is NULL.
    :param: character: New row's name value / name of new character
    :return: None
    """
    cursor.execute('INSERT INTO Characters VALUES(:character, 1, 0, NULL)',
                   {'character': character})
    conn.commit()


def pull_character(character) -> list:
    """
    Fetch a single row from Characters Table where name value is equal to character parameter.
    :param: character: name value of row being fetched / character being pulled from table
    :return: List of values in row
    """
    cursor.execute('SELECT * FROM Characters WHERE name = :name',
                   {'name':  character})
    character = cursor.fetchall()
    return character


# Item Menu
def show_items() -> list:
    """
    Fetch all items from Items table. Return list of items.
    :return: List of items.
    """
    cursor.execute('SELECT * FROM Items')
    items = cursor.fetchall()
    return items


def pull_item(item: str) -> list:
    """
    Fetch a single row from Items Table where name value is equal to item parameter.
    :param: item: name value of row being fetched / item being pulled from table
    :return: List of values in row
    """
    cursor.execute('SELECT * FROM Items WHERE name = :item',
                   {'item': item})
    item = cursor.fetchall()
    return item


def edit_item_name(item: str, replacement: str) -> None:
    """
    Replace name value of item.
    :param: item: Name of item
    :param: replacement: Replacement value
    :return: None
    """
    cursor.execute('UPDATE Items SET name = :value WHERE name = :item',
                   {'value': replacement, 'item': item})
    conn.commit()


def edit_item_description(item: str, replacement: str) -> None:
    """
    Replace description value of item.
    :param item: name of item
    :param replacement: Replacement value
    :return: None
    """
    cursor.execute('UPDATE Items SET description = :value WHERE name = :item',
                   {'value': replacement, 'item': item})
    conn.commit()


def edit_item_amount(item: str, replacement: int) -> None:
    """
    Replace amount value of item.
    :param: item: name of item
    :param: replacement: Replacement value
    :return: None
    """
    cursor.execute('UPDATE Items SET amount = :value WHERE name = :item',
                   {'value': replacement, 'item': item})
    conn.commit()


def edit_item_special(item: str, replacement: str) -> None:
    """
    Replace special value of item.
    :param: item: name of item
    :param: replacement: Replacement value
    :return: None
    """
    cursor.execute('UPDATE Items SET special = :value WHERE name = :item',
                   {'value': replacement, 'item': item})
    conn.commit()


def add_item(item) -> None:
    """
    Add a new row to Items Table with name equal to item.
    description = Null, amount = 1, special is NULL.
    :param: item: New row's name value / name of new item
    :return: None
    """
    cursor.execute('INSERT INTO Items VALUES(:item, NULL, 1, NULL)',
                   {'item': item})
    conn.commit()


def remove_item(item) -> None:
    """
    Remove row where name is equal to item.
    :param: item: Name of row/item
    :return: None
    """
    cursor.execute('DELETE FROM Items WHERE name = :item',
                   {'item': item})
    conn.commit()


# Skills Menu
def show_skills() -> list:
    """
    Fetch all skills from Skills table. Return list of skills.
    :return: List of skills.
    """
    cursor.execute('SELECT * FROM Skills')
    skills = cursor.fetchall()
    return skills


def pull_skill(skill: str) -> list:
    """
    Fetch a single row from Skills Table where name value is equal to skill parameter.
    :param: skill: name value of row being fetched / skill being pulled from table
    :return: List of values in row
    """
    cursor.execute('SELECT * FROM Skills WHERE name = :skill',
                   {'skill': skill})
    skill = cursor.fetchall()
    return skill


def add_skill(skill) -> None:
    """
    Add a new row to Skills Table with name equal to skill.
    level = 1, experience = 0.
    :param: skill: New row's name value / name of new skill
    :return: None
    """
    cursor.execute('INSERT INTO Skills VALUES(:skill, 1, 0)',
                   {'skill': skill})
    conn.commit()


def remove_skill(skill) -> None:
    """
    Remove row where name is equal to skill.
    :param: skill: Name of row/skill
    :return: None
    """
    cursor.execute('DELETE FROM Skills WHERE name = :skill',
                   {'skill': skill})
    conn.commit()


def edit_skill_name(skill: str, replacement: str) -> None:
    """
    Replace name value of skill.
    :param: character: Name of skill
    :param: replacement: Replacement value
    :return: None
    """
    cursor.execute('UPDATE Skills SET name = :value WHERE name = :character',
                   {'value': replacement, 'skill': skill})
    conn.commit()


def edit_skill_level(skill: str, replacement: int) -> None:
    """
    Replace level value of skill.
    :param: character: Name of skill
    :param: replacement: Replacement value
    :return: None
    """
    cursor.execute('UPDATE Skills SET level = :value WHERE name = :skill',
                   {'value': replacement, 'skill': skill})
    conn.commit()


def edit_skill_experience(skill: str, replacement: int) -> None:
    """
    Replace experience value of skill.
    :param: character: Name of skill
    :param: replacement: Replacement value
    :return: None
    """
    cursor.execute('UPDATE Skills SET experience = :value WHERE name = :skill',
                   {'value': replacement, 'skill': skill})
    conn.commit()


def skill_check(skill: str) -> bool:
    """
    Take skill name, capitalize first letter.
    Return True if skill is in Skills Table
    :param skill: Name of skill
    :return: Bool
    """
    return len(pull_skill(skill.capitalize())) != 0


def close_up():
    conn.close()


print(skill_check('fire'))
