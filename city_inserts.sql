INSERT INTO public.contact_country (id, name, population) VALUES (1, 'Brasil', 250000000);

INSERT INTO public.contact_state (id, name, population, acronym, country_id) VALUES (1, 'Santa Catarina', 7000000, 'SC', 1);
INSERT INTO public.contact_state (id, name, population, acronym, country_id) VALUES (2, 'Rio Grande Do Sul', 40000000, 'RS', 1);
INSERT INTO public.contact_state (id, name, population, acronym, country_id) VALUES (3, 'Parana', 38000000, 'PR', 1);

INSERT INTO public.contact_city (id, name, population, state_id) VALUES (1, 'Chapeco', 250000, 1);
INSERT INTO public.contact_city (id, name, population, state_id) VALUES (2, 'Sao Miguel Do Oeste', 30000, 1);
INSERT INTO public.contact_city (id, name, population, state_id) VALUES (3, 'Cruz Alta', 50000, 2);
INSERT INTO public.contact_city (id, name, population, state_id) VALUES (4, 'Pato Branco', 100000, 3);
INSERT INTO public.contact_city (id, name, population, state_id) VALUES (5, 'Treze Tilias', 20000, 1);
