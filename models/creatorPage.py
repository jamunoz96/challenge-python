class CreatorPage:
    def __init__(self, content, name):

        html = '''
            <!DOCTYPE html>
            <html>
                <head>
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link rel=StyleSheet href="styles.css" type="text/css">
                </head>
                <body>
                    <ul id="myUL">
                        {}
                    </ul>
                </body>
            </html>
        '''.format(content)

        file = open("html/" + name + ".html","w")
        file.write(html)
        file.close()