
class page:
    page = ""
    body = ""

    def headers_css(self):
        return ""
    def headers_js(self):
        return ""
    def footers_js(self):
        return ""

    def render(self):
        self.page = "<html>"
        self.page += "<head>"
        self.page += self.headers_css()
        self.page += self.headers_js()
        self.page += "</head>"
        
        self.page += "<body>"
        self.page += self.body
        self.page += "</body>"
        
        self.page += self.footers_js()
        self.page += "</html>"
        return self.page

    def __init__(self, *args, **kwargs):
        self.body = kwargs.get('body', "")


class table:
    data = []
    rendered = ""

    def __init__(self, *args, **kwargs):
        self.data = kwargs.get('data',[])
        pass

    def cell(self, c):
        pass

    def row(self, cells):
        pass

    def sanitize(self):

        if not self.data: return ""
        for id, i in enumerate(self.data):
            for k, v in i.items():
                if isinstance(v, (int, float)):
                    self.data[id][k] = str(v) 

    def render(self):

        self.sanitize()

        if not self.data: return ""

        # if dict
        headers = "<thead><th>"+"</th><th>".join(self.data[0].keys())+"</th></thead>"
        
        rows = []
        for i in self.data:
            rows.append("<td>"+"</td><td>".join(i.values())+"</td>")

        body = "<tbody><tr>"+"</tr><tr>".join(rows)+"</tr></tbody>"

        self.rendered = "<table>"+headers+body+"</table>"
        return self.rendered


if __name__ == '__main__':

    d = [
        { 'id': 1, 'nome': 'stefano' },
        { 'id': 2, 'nome': 'pierdomenico' },
        { 'id': 3, 'nome': 'cristina' },
        { 'id': 4, 'nome': 'giuseppe' },
    ]
    p = page(body="ciao").render()
    t = table(data=d).render()
    print(t)
    print(p)
    



