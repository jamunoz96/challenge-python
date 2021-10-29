from sys import argv
from lxml import objectify

from db.run import Run
from models.category import Category
from models.creatorPage import CreatorPage


def rebuild():
    with open("categories.xml") as data:
        xml = data.read().encode("utf-8")

    db = Run()
    db.table_category()
    model = Category()

    content = objectify.fromstring(xml)
    rows = []
    for category in content.CategoryArray.getchildren():
        result = model.value_category(category)
        rows.append(
            (
                result.bestofferenabled,
                result.autopayenabled,
                result.categoryid,
                result.categorylevel,
                result.categoryname,
                result.categoryparentid,
            )
        )

    model.create_categories(rows)


def render_categories(id_parent):
    model = Category()
    concat = ""
    categories = model.get_categories(id_parent)
    if len(categories) == 0:
        return show_child(id_parent)

    concat += show_parent(id_parent)
    for node in categories:
        concat += render_categories(node[0])

    concat += "</ul>"
    concat += "</li>"
    return concat


def show_parent(parent):
    model = Category()
    result = model.get_category(parent)
    classbestoffer = "bestoffer" if result[4] else ""
    node = ' <li class={}><span class="caret">{} {}</span>'.format(
        classbestoffer, result[0], result[1]
    )
    node += '<ul class="nested">'
    return node


def show_child(parent):
    model = Category()
    result = model.get_category(parent)
    classbestoffer = "bestoffer" if result[4] else ""
    node = " <li class={}> {} {}</li>".format(classbestoffer, result[0], result[1])
    return node


def render(id_parent):
    model = Category()
    is_success = model.valide_table()
    if is_success is False:
        return print("Error: Withow database or table")

    parent = model.valide_category(id_parent)
    if parent is None:
        return print("Error: no category with ID: ", id_parent)

    content = render_categories(id_parent)
    CreatorPage(content, id_parent)


if __name__ == "__main__":

    if len(argv) == 1:
        print("Error: you must pass the arguments: --rebuild | --render")
    elif len(argv) == 2 and argv[1] == "--rebuild":
        rebuild()
    elif len(argv) == 3 and argv[1] == "--render":
        render(argv[2])
    else:
        print("Error: bad arguments")
