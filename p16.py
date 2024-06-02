country={"india":"delhi",
         "china":"beijing",
         "japan":"tokyo",
         "qatar":"doha",
         "france":"merseilles"}
print(country)
country.update({"france":"paris"})
for country,capital in country.items():
    print(country,capital)


