temperatura(alta).
pronostico(sol).
edad(11).
color(rojo).

% Reglas

ropa(abrigo) :- temperatura(baja), pronostico(lluvia), etapa_de_vida(adulto_mayor).
ropa(ropa_ligera) :- temperatura(alta), pronostico(sol), etapa_de_vida(niño).
ropa(prendas_intermedias) :- temperatura(moderada), pronostico(nublado), etapa_de_vida(adulto).

etapa_de_vida(adulto_mayor) :- edad(Edad), Edad > 65.
etapa_de_vida(adulto) :- edad(Edad), Edad >= 18, Edad =< 65.
etapa_de_vida(niño) :- edad(Edad), Edad < 18.

emocion(pasion) :- color(rojo).
emocion(calma) :- color(azul).
emocion(alegria) :- color(amarillo).