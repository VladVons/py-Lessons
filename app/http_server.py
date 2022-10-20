from urllib.parse import urlparse, parse_qs
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    CntLoad = 0

    def ParseQuery(self, aPath: str) -> dict:
        Query = urlparse(aPath).query
        if (Query == ''):
            Res = {}
        else:
            Pairs = Query.split('&')
            Res = dict(P.split('=') for P in Pairs)
        return Res

    def GetDigitStr(self, aNum: str) -> str:
        Digits = ['Null', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        if (len(aNum) == 1):
            Msg = Digits[int(aNum)]
        else:
            Msg = 'Unknown'
        return Msg

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        Query = self.ParseQuery(self.path)
        ParaNum = self.GetDigitStr(Query.get('number', '0'))
        ParaColor = Query.get('color', 'white')
        ParaRever = Query.get('rever', 'Reverse string')

        #self.CntLoad =+ 1

        Page = """
        <html>
            </head>
                <style>
                    body {
                        background-color: %s;
                    }
                </style>
                <meta charset='utf-8'>
                <title>Python HTTP server</title>
            </head>
            <body>
                <h1>color: %s</h1><br>
                <h1>number: %s</h1><br>
                <h1>rever: %s</h1><br>
                <h1>Loads: %s</h1><br>
            </body>
        </html>""" % (ParaColor, ParaColor, ParaNum, ParaRever[::-1], self.CntLoad)

        self.wfile.write(Page.encode())


httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
