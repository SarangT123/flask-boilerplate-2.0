import os

while True:
    cmd = input("Flask-boilerplate >>>")
    command = cmd.split(' ', 2)
    cmd = cmd.split(' ', 3)
    if command[0] == "template" and command[1] == "add":
        f = open(f'website/templates/{command[2]}', 'w')
        f.write("""
{%extends 'base.html'%}
{%block title%} Homepage {%endblock%}
{%block css%}website/static/style.css{%endblock%}
{%block scripthead%}
{%endblock%}
{%block contents%}

<h1>Homepage</h1>

{%endblock%}
{%block script%}
{%endblock%}""")
        f.close()

    if cmd[0] == "template" and cmd[1] == "remove":
        os.remove(f"website/templates/{cmd[2]}")

    if cmd[0] in ['route', 'view'] and cmd[1] == "add":
        f = open('website/views.py', 'a')
        par = cmd[3].split(',')
        params = ""
        args = f"{par[0]}"
        for i in range(len(par)):
            params += f"/<{par[i]}>"
        for i in range(len(par)-1):
            args += f",{par[i+1]}"
        f.write(f"""
@app.route("/{cmd[2]}{params}")
def {cmd[2]}({args}):
    return """)
        f.close()
