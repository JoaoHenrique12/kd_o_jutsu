# Criando os arquivos CSV.

Todos os arquivos csv foram baseados no projeto: [Naruto Fandom Scrapping](https://github.com/JoaoHenrique12/naruto_fandom_scraping/tree/main).

## Tratando os dados

O arquivo [procedures_treat_data.sql](procedures_treat_data.sql) foi criado para excluir e formatar as informações das
tabelas jutsu, seal, jutsu_have_seal. Sendo que este projeto somente usará os selos com id de 1 à 13. 

E removerá as subsequências de selos consecutivos que se repetem da tabela jutsu_have_seal. Ou seja, se um jutsu possuir
a seguinte sequência de selos:

```
desconhecido, desconhecido, carneiro, tigre, tigre, cavalo
```

A nova sequência de selos será:

```
 desconhecido, carneiro, tigre, cavalo
```


## Transformando tabelas para CSV

```bash
docker exec -it naruto_fandom_scraping_postgres_1 psql -U postgres -d naruto_db -P pager=off -P format=unaligned  -P fieldsep=\, -c "select * from seal order by id;"
docker exec -it naruto_fandom_scraping_postgres_1 psql -U postgres -d naruto_db -P pager=off -P format=unaligned  -P fieldsep=\, -c "select * from jutsu_have_seal order by jutsu_id;"
docker exec -it naruto_fandom_scraping_postgres_1 psql -U postgres -d naruto_db -P pager=off -P format=unaligned  -P fieldsep=\, -c "select id, title, image from jutsu where id in (select distinct(jutsu_id) from jutsu_have_seal) order by id;"
```

## Referências

https://www.postgresql.org/docs/current/app-psql.html
https://stackoverflow.com/questions/17463299/export-postgres-database-into-csv-file
