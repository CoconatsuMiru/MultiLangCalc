% logic_check.pl

validate(Expression) :-
    atom_string(Atom, Expression),
    split_string(Atom, " ", "", [A, Op, B]),
    (Op = "/" -> number_string(Denominator, B), Denominator =\= 0 -> write('OK'); Op \= "/" -> write('OK'); write('INVALID')).
