my_last(X, [X]).
my_last(X, [_|Tail]) :- my_last(X, Tail).

element_at(X, [X|_], 1).
element_at(X, [_|Tail], K) :- 
    K > 1, 
    K1 is K - 1, 
    element_at(X, Tail, K1).

