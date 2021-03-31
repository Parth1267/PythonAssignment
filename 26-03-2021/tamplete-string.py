from string import Template


def main():
    str1 = "you are watching {0} by {1}".format(
        "Advance pythone", "joe marini")
    print(str1)

    # TODO: create a template with placeholders
    templ = Template("you are watching ${title} by ${author}")
    # TODO: use the substitute method with keyword arguments
    str2 = templ.substitute(title="Advance pythone", author="joe marini")
    print(str2)
    # TODO: use the substitute method with a dictionary
    data = {
        "title": "Advance pythone",
        "author": "joe marini"
    }

    str3 = templ.substitute(data)
    print(str3)


if __name__ == '__main__':
    main()
