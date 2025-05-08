BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Cliente" (
	"id_cliente"	INTEGER NOT NULL,
	"nome"	TEXT NOT NULL,
	"email"	TEXT NOT NULL UNIQUE,
	"cnpj"	TEXT NOT NULL UNIQUE,
	"cidade"	TEXT NOT NULL,
	"data_cadastro"	TEXT NOT NULL,
	PRIMARY KEY("id_cliente" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Item_Pedido" (
	"id_item"	INTEGER NOT NULL,
	"id_pedido"	INTEGER NOT NULL,
	"quantidade"	INTEGER NOT NULL CHECK("quantidade" > 0),
	"preco_unitario"	REAL NOT NULL CHECK("preco_unitario" > 0),
	"id_produto"	INTEGER NOT NULL,
	PRIMARY KEY("id_item" AUTOINCREMENT),
	FOREIGN KEY("id_pedido") REFERENCES "Pedido"("id_pedido"),
	FOREIGN KEY("id_produto") REFERENCES "Produto"("id_produto")
);
CREATE TABLE IF NOT EXISTS "Pedido" (
	"id_pedido"	INTEGER NOT NULL,
	"id_cliente"	INTEGER NOT NULL,
	"id_representante"	INTEGER NOT NULL,
	"data_pedido"	TEXT NOT NULL,
	PRIMARY KEY("id_pedido" AUTOINCREMENT),
	FOREIGN KEY("id_cliente") REFERENCES "Cliente",
	FOREIGN KEY("id_representante") REFERENCES "Representante"("id_representante")
);
CREATE TABLE IF NOT EXISTS "Produto" (
	"id_produto"	INTEGER NOT NULL,
	"nome"	TEXT NOT NULL,
	"categoria"	TEXT NOT NULL,
	"preco_unitario"	REAL NOT NULL,
	"quantidade_estoque"	INTEGER NOT NULL,
	PRIMARY KEY("id_produto" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Representante" (
	"id_representante"	INTEGER NOT NULL,
	"nome"	TEXT NOT NULL,
	"email"	TEXT NOT NULL UNIQUE,
	"regiao"	TEXT NOT NULL,
	"meta_mensal"	REAL NOT NULL CHECK("meta_mensal" >= 0),
	PRIMARY KEY("id_representante" AUTOINCREMENT)
);
INSERT INTO "Cliente" ("id_cliente","nome","email","cnpj","cidade","data_cadastro") VALUES (1,'Marianne Diniz','mariane.silva@penedo.ufal.br','76.341.474/0001-69','Campina Grande','2022-01-15');
INSERT INTO "Cliente" ("id_cliente","nome","email","cnpj","cidade","data_cadastro") VALUES (2,'Bruno Martins','bruno.martins@arapiraca.ufal.br','06.353.239/0001-21','Igreja Nova','2022-03-28');
INSERT INTO "Cliente" ("id_cliente","nome","email","cnpj","cidade","data_cadastro") VALUES (3,'Henrique Pereira','hsp1@aluno.ifal.edu.br','89.375.734/0001-69','São Sebastião','2022-02-05');
INSERT INTO "Cliente" ("id_cliente","nome","email","cnpj","cidade","data_cadastro") VALUES (4,'Joao Pedro','joao.pereira@arapiraca.ufal.br','31.994.139/0001-219','Penedo','2022-07-11');
INSERT INTO "Cliente" ("id_cliente","nome","email","cnpj","cidade","data_cadastro") VALUES (5,'Gabriel Fidelis','jose.fidelis@arapiraca.ufal.br','82.344.904/0001-07','Penedo','2022-06-03');
INSERT INTO "Cliente" ("id_cliente","nome","email","cnpj","cidade","data_cadastro") VALUES (6,'Cicero Anderson','cicero.silva@arapiraca.ufal.br','91.709.729/0001-97','Penedo','2022-04-19');
INSERT INTO "Cliente" ("id_cliente","nome","email","cnpj","cidade","data_cadastro") VALUES (7,'Amanda Moura','amanda.moura@arapiraca.ufal.br','11.234.567/0001-89','Arapiraca','2022-08-25');
INSERT INTO "Cliente" ("id_cliente","nome","email","cnpj","cidade","data_cadastro") VALUES (8,'Lucas Araújo','lucas.araujo@arapiraca.ufal.br','22.345.678/0001-45','Maceió','2022-09-13');
INSERT INTO "Cliente" ("id_cliente","nome","email","cnpj","cidade","data_cadastro") VALUES (9,'Bruna Oliveira','bruna.oliveira@arapiraca.ufal.br','33.456.789/0001-32','Penedo','2022-05-02');
INSERT INTO "Cliente" ("id_cliente","nome","email","cnpj","cidade","data_cadastro") VALUES (10,'Felipe Nunes','felipe.nunes@arapiraca.ufal.br','44.567.890/0001-21','Delmiro Gouveia','2022-12-31');
INSERT INTO "Cliente" ("id_cliente","nome","email","cnpj","cidade","data_cadastro") VALUES (11,'Vitória Ramos','vitoria.ramos@arapiraca.ufal.br','55.678.901/0001-10','Santana do Ipanema','2025-04-20');
INSERT INTO "Cliente" ("id_cliente","nome","email","cnpj","cidade","data_cadastro") VALUES (12,'Rodrigo Lima','rodrigo.lima@arapiraca.ufal.br','66.789.012/0001-88','União dos Palmares','2025-04-20');
INSERT INTO "Cliente" ("id_cliente","nome","email","cnpj","cidade","data_cadastro") VALUES (13,'Larissa Souza','larissa.souza@arapiraca.ufal.br','77.890.123/0001-77','São Miguel dos Campos','2025-04-20');
INSERT INTO "Cliente" ("id_cliente","nome","email","cnpj","cidade","data_cadastro") VALUES (14,'Thiago Silva','thiago.silva@arapiraca.ufal.br','88.901.234/0001-66','Piaçabuçu','2025-04-20');

INSERT INTO "Item_Pedido" ("id_item","id_pedido","quantidade","preco_unitario","id_produto") VALUES (1,1,2,3299.0,1);
INSERT INTO "Item_Pedido" ("id_item","id_pedido","quantidade","preco_unitario","id_produto") VALUES (2,1,1,1799.0,4);
INSERT INTO "Item_Pedido" ("id_item","id_pedido","quantidade","preco_unitario","id_produto") VALUES (3,2,1,4299.0,9);
INSERT INTO "Item_Pedido" ("id_item","id_pedido","quantidade","preco_unitario","id_produto") VALUES (4,3,2,999.0,11);
INSERT INTO "Item_Pedido" ("id_item","id_pedido","quantidade","preco_unitario","id_produto") VALUES (5,3,2,999.0,11);
INSERT INTO "Item_Pedido" ("id_item","id_pedido","quantidade","preco_unitario","id_produto") VALUES (6,3,2,999.0,11);
INSERT INTO "Item_Pedido" ("id_item","id_pedido","quantidade","preco_unitario","id_produto") VALUES (7,3,2,999.0,11);
INSERT INTO "Item_Pedido" ("id_item","id_pedido","quantidade","preco_unitario","id_produto") VALUES (8,3,2,999.0,1);
INSERT INTO "Item_Pedido" ("id_item","id_pedido","quantidade","preco_unitario","id_produto") VALUES (9,3,2,999.0,1);
INSERT INTO "Item_Pedido" ("id_item","id_pedido","quantidade","preco_unitario","id_produto") VALUES (10,3,2,999.0,1);
INSERT INTO "Item_Pedido" ("id_item","id_pedido","quantidade","preco_unitario","id_produto") VALUES (11,3,2,999.0,11);
INSERT INTO "Item_Pedido" ("id_item","id_pedido","quantidade","preco_unitario","id_produto") VALUES (12,3,2,999.0,11);
INSERT INTO "Item_Pedido" ("id_item","id_pedido","quantidade","preco_unitario","id_produto") VALUES (13,3,2,999.0,11);
INSERT INTO "Item_Pedido" ("id_item","id_pedido","quantidade","preco_unitario","id_produto") VALUES (14,3,2,999.0,11);
INSERT INTO "Item_Pedido" ("id_item","id_pedido","quantidade","preco_unitario","id_produto") VALUES (15,3,2,999.0,11);
INSERT INTO "Item_Pedido" ("id_item","id_pedido","quantidade","preco_unitario","id_produto") VALUES (16,3,2,999.0,11);
INSERT INTO "Item_Pedido" ("id_item","id_pedido","quantidade","preco_unitario","id_produto") VALUES (17,3,2,999.0,11);
INSERT INTO "Item_Pedido" ("id_item","id_pedido","quantidade","preco_unitario","id_produto") VALUES (18,3,2,999.0,11);
INSERT INTO "Item_Pedido" ("id_item","id_pedido","quantidade","preco_unitario","id_produto") VALUES (19,3,2,999.0,11);
INSERT INTO "Item_Pedido" ("id_item","id_pedido","quantidade","preco_unitario","id_produto") VALUES (20,3,2,999.0,11);

INSERT INTO "Pedido" ("id_pedido","id_cliente","id_representante","data_pedido") VALUES (1,1,1,'2023-10-15');
INSERT INTO "Pedido" ("id_pedido","id_cliente","id_representante","data_pedido") VALUES (2,2,1,'2023-10-16');
INSERT INTO "Pedido" ("id_pedido","id_cliente","id_representante","data_pedido") VALUES (3,3,2,'2023-10-17');
INSERT INTO "Produto" ("id_produto","nome","categoria","preco_unitario","quantidade_estoque") VALUES (1,'Notebook Gamer Acer Nitro V ANV15-51-57WS Intel® Core™ i5-13420H 13ªGeração 512SSD 8GB Nvidia® GeForce® RTX 3050 GDDR6','Eletrônico',4.374,20);
INSERT INTO "Produto" ("id_produto","nome","categoria","preco_unitario","quantidade_estoque") VALUES (4,'Smartphone Samsung Galaxy A54 5G 128GB 8GB RAM Câmera Tripla 50MP','Celular',799.0,25);
INSERT INTO "Produto" ("id_produto","nome","categoria","preco_unitario","quantidade_estoque") VALUES (5,'Notebook Dell Inspiron 15 i5 8GB 512GB SSD 15.6" FHD','Notebook',3299.0,15);
INSERT INTO "Produto" ("id_produto","nome","categoria","preco_unitario","quantidade_estoque") VALUES (6,'Notebook Lenovo IdeaPad 3i i5 8GB 256GB SSD 15.6"','Notebook',2799.0,12);
INSERT INTO "Produto" ("id_produto","nome","categoria","preco_unitario","quantidade_estoque") VALUES (7,'Notebook Acer Aspire 5 i5 8GB 512GB SSD 15.6" FHD','Notebook',3499.0,8);
INSERT INTO "Produto" ("id_produto","nome","categoria","preco_unitario","quantidade_estoque") VALUES (8,'Xiaomi Redmi Note 12 128GB 6GB RAM Câmera Tripla','Celular',1299.0,30);
INSERT INTO "Produto" ("id_produto","nome","categoria","preco_unitario","quantidade_estoque") VALUES (9,'iPhone 13 128GB Tela 6.1" Câmera Dupla','Celular',4299.0,10);
INSERT INTO "Produto" ("id_produto","nome","categoria","preco_unitario","quantidade_estoque") VALUES (10,'PC Gamer AMD Ryzen 5 16GB 1TB SSD Radeon Vega 7','Computador',2899.0,7);
INSERT INTO "Produto" ("id_produto","nome","categoria","preco_unitario","quantidade_estoque") VALUES (11,'Monitor Gamer LG 24" Full HD 144Hz 1ms','Monitor',999.0,14);
INSERT INTO "Produto" ("id_produto","nome","categoria","preco_unitario","quantidade_estoque") VALUES (12,'Placa de Vídeo RTX 3060 12GB GDDR6','Componente',2199.0,5);
INSERT INTO "Produto" ("id_produto","nome","categoria","preco_unitario","quantidade_estoque") VALUES (13,'Fone Bluetooth JBL Tune 510BT Pure Bass','Fone',199.0,40);
INSERT INTO "Produto" ("id_produto","nome","categoria","preco_unitario","quantidade_estoque") VALUES (14,'Smartwatch Xiaomi Mi Band 7','Acessório',299.0,35);
INSERT INTO "Produto" ("id_produto","nome","categoria","preco_unitario","quantidade_estoque") VALUES (15,'Caixa de Som Bluetooth JBL Go 3','Acessório',249.0,22);

INSERT INTO "Representante" ("id_representante","nome","email","regiao","meta_mensal") VALUES (1,'Ana Souza','ana.souza@ml.com','Sudeste',150000.0);
INSERT INTO "Representante" ("id_representante","nome","email","regiao","meta_mensal") VALUES (2,'Carlos Mendes','carlos.mendes@kabum.com.br','Sul',120000.0);
INSERT INTO "Representante" ("id_representante","nome","email","regiao","meta_mensal") VALUES (3,'Mariana Lima','mariana.lima@magazineluiza.com.br','Nordeste',110000.0);
INSERT INTO "Representante" ("id_representante","nome","email","regiao","meta_mensal") VALUES (4,'Rodrigo Santos','rodrigo.santos@ml.com','Centro-Oeste',95000.0);
INSERT INTO "Representante" ("id_representante","nome","email","regiao","meta_mensal") VALUES (5,'Patricia Gonçalves','patricia.goncalves@pichau.com.br','Norte',85000.0);
INSERT INTO "Representante" ("id_representante","nome","email","regiao","meta_mensal") VALUES (6,'Lucas Ferreira','lucas.ferreira@casasbahia.com.br','Sudeste',130000.0);
INSERT INTO "Representante" ("id_representante","nome","email","regiao","meta_mensal") VALUES (7,'Fernanda Oliveira','fernanda.oliveira@pichau.com.br','Nordeste',100000.0);
INSERT INTO "Representante" ("id_representante","nome","email","regiao","meta_mensal") VALUES (8,'Ricardo Almeida','ricardo.almeida@magazineluiza.com.br','Centro-Oeste',90000.0);
INSERT INTO "Representante" ("id_representante","nome","email","regiao","meta_mensal") VALUES (9,'Juliana Costa','juliana.costa@casasbahia.com.br','Norte',80000.0);
COMMIT;