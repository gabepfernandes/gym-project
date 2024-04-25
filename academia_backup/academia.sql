--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: equipamento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.equipamento (
    codequip integer NOT NULL,
    nome text,
    quantidade integer
);


ALTER TABLE public.equipamento OWNER TO postgres;

--
-- Name: Equipamento_codEquip_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.equipamento ALTER COLUMN codequip ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Equipamento_codEquip_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: exercicio; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.exercicio (
    codexerc integer NOT NULL,
    nome text,
    cod_equip integer
);


ALTER TABLE public.exercicio OWNER TO postgres;

--
-- Name: Exercicio_codExerc_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.exercicio ALTER COLUMN codexerc ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Exercicio_codExerc_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: plano; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.plano (
    "codPlano" integer NOT NULL,
    categoria text,
    preco numeric
);


ALTER TABLE public.plano OWNER TO postgres;

--
-- Name: Plano_codPlano_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.plano ALTER COLUMN "codPlano" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Plano_codPlano_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: treino; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.treino (
    codtreino integer NOT NULL,
    duracao integer,
    cpf_aluno text NOT NULL,
    cpf_instrutor text NOT NULL,
    foco text
);


ALTER TABLE public.treino OWNER TO postgres;

--
-- Name: Treino_codTreino_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.treino ALTER COLUMN codtreino ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Treino_codTreino_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: pessoa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pessoa (
    nome text NOT NULL,
    telefone text,
    sexo "char",
    "dtNascimento" date,
    email text,
    cpf text NOT NULL
);


ALTER TABLE public.pessoa OWNER TO postgres;

--
-- Name: aluno; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.aluno (
    peso numeric,
    altura numeric,
    cod_plano integer
)
INHERITS (public.pessoa);


ALTER TABLE public.aluno OWNER TO postgres;

--
-- Name: atividade; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.atividade (
    cod_treino integer NOT NULL,
    cod_exerc integer NOT NULL,
    nroseries integer
);


ALTER TABLE public.atividade OWNER TO postgres;

--
-- Name: instrutor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.instrutor (
    "nroContrato" integer,
    salario numeric,
    cref numeric
)
INHERITS (public.pessoa);


ALTER TABLE public.instrutor OWNER TO postgres;

--
-- Data for Name: aluno; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.aluno (nome, telefone, sexo, "dtNascimento", email, peso, altura, cod_plano, cpf) FROM stdin;
Caio	990844563	M	2000-07-02	caio@gmail.com	83.40	187	1	05423074813
Guilherme	992988384	M	1982-09-13	gui@gmail.com	95.20	196	3	04698345087
Pablo	989494245	M	2000-11-01	pablo@gmail.com	57.60	173	1	08492038303
Maria	990844563	F	1969-03-27	caio@gmail.com	75.20	175	2	08434387901
Matheus	988483920	M	1988-01-26	matheus@gmail.com	77.20	184	2	09901202430
Adriana	999098712	F	1997-04-22	adriana@gmail.com	52.30	158	3	08573810283
Camila	998762831	F	2002-12-03	camila@gmail.com	73.40	169	3	03278394612
\.


--
-- Data for Name: atividade; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.atividade (cod_treino, cod_exerc, nroseries) FROM stdin;
1	1	5
1	3	3
1	4	3
2	1	5
2	8	4
2	9	3
3	9	3
3	15	4
3	1	4
4	1	4
4	3	5
4	15	4
5	17	\N
5	15	5
6	2	5
6	3	5
6	9	3
7	2	3
7	6	4
7	7	4
7	10	3
8	11	3
8	12	4
8	13	4
8	17	4
9	14	4
9	16	3
9	6	5
10	10	3
10	11	3
10	13	4
10	16	4
\.


--
-- Data for Name: equipamento; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.equipamento (codequip, nome, quantidade) FROM stdin;
1	Cadeira extensora	3
2	Cadeira flexora	2
3	Leg Press	2
4	Barra guiada	2
5	Elevação pélvica	1
6	Panturrilha sentada	2
7	Peck Deck	2
8	Supino	4
9	Polia	5
10	Abdominal articulado	1
11	Cross Over	3
12	Esteira	15
13	Bicicleta ergométrica 	10
14	Elíptico	10
15	Step	5
\.


--
-- Data for Name: exercicio; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.exercicio (codexerc, nome, cod_equip) FROM stdin;
1	Agachamento Livre	4
2	Supino Inclinado 	8
3	Cadeira Extensora	1
4	Cadeira Flexora	2
6	Supino	4
7	Cross Over	11
8	Elevação Pélvica	5
9	Panturrilha Sentado	6
10	Triceps Frances	9
11	Extensão de Triceps	9
12	Rosca Direta	9
13	Elevação Lateral	9
14	Pullover	9
15	Leg Press	3
16	Peck Deck	7
17	Abdominal	10
\.


--
-- Data for Name: instrutor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.instrutor (nome, telefone, sexo, "dtNascimento", email, "nroContrato", salario, cref, cpf) FROM stdin;
Lucas	991265312	M	2003-07-17	lucas@gmail.com	82419	1400.00	102	92102864016
William	9912039103	M	2001-03-10	william@gmail.com	13206	1400.00	703	93283019268
Denise	9903771829	F	1992-08-15	denise@gmail.com	19573	3500.00	361	02854392810
\.


--
-- Data for Name: pessoa; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pessoa (nome, telefone, sexo, "dtNascimento", email, cpf) FROM stdin;
\.


--
-- Data for Name: plano; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.plano ("codPlano", categoria, preco) FROM stdin;
1	gold	109.90
2	platinum	149.90
3	silver	89.90
\.


--
-- Data for Name: treino; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.treino (codtreino, duracao, cpf_aluno, cpf_instrutor, foco) FROM stdin;
1	75	03278394612	02854392810	Inferiores
2	75	08434387901	02854392810	Inferiores
3	90	08573810283	02854392810	Inferiores
4	90	08492038303	02854392810	Inferiores
5	90	05423074813	92102864016	Inferiores
6	90	09901202430	92102864016	Inferiores
7	60	09901202430	93283019268	Superiores
8	60	04698345087	93283019268	Superiores
9	60	05423074813	93283019268	Superiores
10	60	08573810283	92102864016	Superiores
\.


--
-- Name: Equipamento_codEquip_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Equipamento_codEquip_seq"', 15, true);


--
-- Name: Exercicio_codExerc_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Exercicio_codExerc_seq"', 17, true);


--
-- Name: Plano_codPlano_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Plano_codPlano_seq"', 3, true);


--
-- Name: Treino_codTreino_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Treino_codTreino_seq"', 10, true);


--
-- Name: aluno Aluno_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aluno
    ADD CONSTRAINT "Aluno_pkey" PRIMARY KEY (cpf);


--
-- Name: atividade Atividade_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.atividade
    ADD CONSTRAINT "Atividade_pkey" PRIMARY KEY (cod_treino, cod_exerc);


--
-- Name: equipamento Equipamento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipamento
    ADD CONSTRAINT "Equipamento_pkey" PRIMARY KEY (codequip);


--
-- Name: exercicio Exercicio_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exercicio
    ADD CONSTRAINT "Exercicio_pkey" PRIMARY KEY (codexerc);


--
-- Name: instrutor Instrutor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.instrutor
    ADD CONSTRAINT "Instrutor_pkey" PRIMARY KEY (cpf);


--
-- Name: pessoa Pessoa_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pessoa
    ADD CONSTRAINT "Pessoa_pkey" PRIMARY KEY (cpf);


--
-- Name: plano Plano_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.plano
    ADD CONSTRAINT "Plano_pkey" PRIMARY KEY ("codPlano");


--
-- Name: treino Treino_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.treino
    ADD CONSTRAINT "Treino_pkey" PRIMARY KEY (codtreino);


--
-- Name: aluno aluno_plano_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aluno
    ADD CONSTRAINT aluno_plano_fk FOREIGN KEY (cod_plano) REFERENCES public.plano("codPlano");


--
-- Name: treino aluno_treino_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.treino
    ADD CONSTRAINT aluno_treino_fk FOREIGN KEY (cpf_aluno) REFERENCES public.aluno(cpf);


--
-- Name: atividade exerc_atv_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.atividade
    ADD CONSTRAINT exerc_atv_fk FOREIGN KEY (cod_exerc) REFERENCES public.exercicio(codexerc);


--
-- Name: exercicio exerc_equip_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exercicio
    ADD CONSTRAINT exerc_equip_fk FOREIGN KEY (cod_equip) REFERENCES public.equipamento(codequip);


--
-- Name: treino instrutor_treino_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.treino
    ADD CONSTRAINT instrutor_treino_fk FOREIGN KEY (cpf_instrutor) REFERENCES public.instrutor(cpf) NOT VALID;


--
-- Name: atividade treino_atv_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.atividade
    ADD CONSTRAINT treino_atv_fk FOREIGN KEY (cod_treino) REFERENCES public.treino(codtreino) NOT VALID;


--
-- PostgreSQL database dump complete
--

