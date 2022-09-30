from methods import m_adding
from methods import m_delete
from methods import m_edit
from methods import m_search


def create(device=4):
    """

    @type device: object
    """
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>add: {} </p>\n' \
        .format(style, m_adding(device))
    html += '    <p {}>delete: {} </p>\n' \
        .format(style, m_delete(device))
    html += '    <p {}>edit: {} </p>\n' \
        .format(style, m_edit(device))
    html += '    <p {}>search: {} </p>\n' \
        .format(style, m_search(device))
    html += '  </body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)

    return html


def new_create(data):
    a, d, e, s = data
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>add:{} </p>\n' \
        .format(style, a)
    html += '    <p {}>delete:{} </p>\n' \
        .format(style, d)
    html += "    <p {}>edit:{} </p>\n" \
        .format(style, e)
    html += '    <p {}>search:{} </p>\n' \
        .format(style, s)
    html += '  </body>\n</html>'

    with open('new_index.html', 'w') as page:
        page.write(html)

    return data
