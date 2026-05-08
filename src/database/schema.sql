CREATE TABLE cinema (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT,
  endereco TEXT,
  capacidade INTEGER
);

CREATE TABLE filme (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  titulo TEXT,
  duracao INTEGER,
  genero TEXT,
  diretor TEXT
);

CREATE TABLE sessao (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  horario TEXT,
  publico INTEGER,
  cinema_id INTEGER,
  filme_id INTEGER
);
