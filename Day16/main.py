import prettytable

table = prettytable.PrettyTable()
table.add_column("Pokemon",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "s"

print(table)

