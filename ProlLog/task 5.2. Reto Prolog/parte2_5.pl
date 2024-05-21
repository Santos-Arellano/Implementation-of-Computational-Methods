% Hechos
actividad(leer).
actividad(shopping).

autor(harry_potter, j_k_rowling).
autor(leer, murakami).

persona(maria, mujer).
persona(ana, mujer).
persona(jorge, hombre).

ciudad(nueva_york, grande).
ciudad(nueva_york, con_mucha_gente).
ciudad(tokio, grande).
ciudad(tokio, con_mucha_gente).
ciudad(colima, pequeño).
ciudad(colima, con_poca_gente).

vegetariano(ana).
vegetariano(jorge).

lee(maria, harry_potter).

% Reglas
le_gusta_ir_de_shopping(Persona) :- persona(Persona, mujer).

detesta(jorge, Ciudad) :-
    ciudad(Ciudad, grande),
    ciudad(Ciudad, con_mucha_gente).

le_gustan(Persona, zanahorias) :- vegetariano(Persona).

lee_libro_con_autor(Persona, Libro, Autor) :-
    lee(Persona, Libro),
    autor(Libro, Autor).
