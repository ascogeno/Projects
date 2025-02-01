-module(arithmetic_but_it_doesnt_work).

-export([start_factorializer/0, start_adder/0, start_subtracter/0, start_multiplier/0,
         start_divider/0, factorializer/0, adder/0, subtracter/0, multiplier/0, divider/0,
         factorial_of/2, add/3, subtract/3, multiply/3, divide/3]).

%%
%% Put your functions, described in the task HTML file here.

factorial_of(Pid, N) ->
    Pid ! {self(), {factorial, N}},
    receive
        {Pid, Result} ->
            Result;
        timeout ->
            {fail, timeout}
    after 5000 ->  % Timeout after 5 seconds
        {fail, timeout}
    end;
factorial_of(_, N) when is_atom(N) ->
    {fail, N, is_not_integer};
factorial_of(_, N) when is_number(N) ->
    {fail, N, is_not_integer};
factorial_of(_, N) when N < 0 ->
    {fail, N, is_negative};
factorial_of(_, _) ->
    {fail, unknown, is_not_integer}.

factorializer() ->
    receive
        {Caller, {factorial, 0}} ->
            Caller ! {self(), 1},
            factorializer();
        {Caller, {factorial, N}} when is_integer(N), N > 0 ->
            Result = lists:foldl(fun(X, Acc) -> X * Acc end, 1, lists:seq(1, N)),
            Caller ! {self(), Result},
            factorializer();
        {Caller, {factorial, N}} when N < 0 ->
            Caller ! {self(), {fail, N, is_negative}},
            factorializer();
        {Caller, {factorial, N}} when not is_integer(N) ->
            Caller ! {self(), {fail, N, is_not_integer}},
            factorializer()
    end.

start_factorializer() ->
    spawn(?MODULE, factorializer, []).

add(Pid, A, B) when is_number(A), is_number(B) ->
    Pid ! {self(), {add, A, B}},
    receive
        {Pid, Result} ->
            Result
    after 5000 ->
        {error, timeout}
    end;
add(_, A, _) when is_atom(A) ->
    {fail, A, is_not_number};
add(_, _, B) when is_atom(B) ->
    {fail, B, is_not_number};
add(_, _, _) ->
    {fail, unknown, is_not_number}.

adder() ->
    receive
        {Caller, {add, A, B}} when is_number(A), is_number(B) ->
            Caller ! {self(), A + B},
            adder();
        {Caller, {add, A, _}} when is_atom(A) ->
            Caller ! {self(), {fail, A, is_not_number}},
            adder();
        {Caller, {add, _, B}} when is_atom(B) ->
            Caller ! {self(), {fail, B, is_not_number}},
            adder();
        {Caller, {add, _, _}} ->
            Caller ! {self(), {fail, unknown, is_not_number}},
            adder()
    end.

start_adder() ->
    spawn(?MODULE, adder, []).

subtract(Pid, A, B) when is_number(A), is_number(B) ->
    Pid ! {self(), {subtract, A, B}},
    receive
        {Pid, Result} ->
            Result
    after 5000 ->
        {error, timeout}
    end;
subtract(_, A, _) when is_atom(A) ->
    {fail, A, is_not_number};
subtract(_, _, B) when is_atom(B) ->
    {fail, B, is_not_number};
subtract(_, _, _) ->
    {fail, unknown, is_not_number}.

subtracter() ->
    receive
        {Caller, {subtract, A, B}} when is_number(A), is_number(B) ->
            Caller ! {self(), A - B},
            subtracter();
        {Caller, {subtract, A, _}} when is_atom(A) ->
            Caller ! {self(), {fail, A, is_not_number}},
            subtracter();
        {Caller, {subtract, _, B}} when is_atom(B) ->
            Caller ! {self(), {fail, B, is_not_number}},
            subtracter();
        {Caller, {subtract, _, _}} ->
            Caller ! {self(), {fail, unknown, is_not_number}},
            subtracter()
    end.

start_subtracter() ->
    spawn(?MODULE, subtracter, []).

multiply(Pid, A, B) when is_number(A), is_number(B) ->
    Pid ! {self(), {multiply, A, B}},
    receive
        {Pid, Result} ->
            Result
    after 5000 ->
        {error, timeout}
    end;
multiply(_, A, _) when is_atom(A) ->
    {fail, A, is_not_number};
multiply(_, _, B) when is_atom(B) ->
    {fail, B, is_not_number};
multiply(_, _, _) ->
    {fail, unknown, is_not_number}.

multiplier() ->
    receive
        {Caller, {multiply, A, B}} when is_number(A), is_number(B) ->
            Caller ! {self(), A * B},
            multiplier();
        {Caller, {multiply, A, _}} when is_atom(A) ->
            Caller ! {self(), {fail, A, is_not_number}},
            multiplier();
        {Caller, {multiply, _, B}} when is_atom(B) ->
            Caller ! {self(), {fail, B, is_not_number}},
            multiplier();
        {Caller, {multiply, _, _}} ->
            Caller ! {self(), {fail, unknown, is_not_number}},
            multiplier()
    end.

start_multiplier() ->
    spawn(?MODULE, multiplier, []).

divide(Pid, A, B) when is_number(A), is_number(B), B /= 0 ->
    Pid ! {self(), {divide, A, B}},
    receive
        {Pid, Result} ->
            Result
    after 5000 ->
        {error, timeout}
    end;
divide(_, _, 0) ->
    {fail, 0, division_by_zero};
divide(_, A, _) when is_atom(A) ->
    {fail, A, is_not_number};
divide(_, _, B) when is_atom(B) ->
    {fail, B, is_not_number};
divide(_, _, _) ->
    {fail, unknown, is_not_number}.

divider() ->
    receive
        {Caller, {divide, A, B}} when is_number(A), is_number(B), B /= 0 ->
            Caller ! {self(), A / B},
            divider();
        {Caller, {divide, _, 0}} ->
            Caller ! {self(), {fail, 0, division_by_zero}},
            divider();
        {Caller, {divide, A, _}} when is_atom(A) ->
            Caller ! {self(), {fail, A, is_not_number}},
            divider();
        {Caller, {divide, _, B}} when is_atom(B) ->
            Caller ! {self(), {fail, B, is_not_number}},
            divider();
        {Caller, {divide, _, _}} ->
            Caller ! {self(), {fail, unknown, is_not_number}},
            divider()
    end.

start_divider() ->
    spawn(?MODULE, divider, []).

-ifdef(EUNIT).

%%
%% Unit tests go here.
%%

-include_lib("eunit/include/eunit.hrl").

factorializer_test_() ->
    {setup,
     fun() ->
        % runs before any of the tests
        Pid = spawn(?MODULE, factorializer, []),
        register(test_factorializer, Pid)
     end,
     % fun(_)-> % runs after all of the tests
     % there is no teardown needed, so this fun doesn't need to be implemented.
     % end,
     % factorializer tests start here
     [?_assertEqual(120,
                    factorial_of(test_factorializer, 5)),  % happy path, tests the obvious case.
      % test less obvious or edge cases
      ?_assertEqual(1, factorial_of(test_factorializer, 0)),
      ?_assertEqual({fail, -3, is_negative}, factorial_of(test_factorializer, -3)),
      ?_assertEqual({fail, bob, is_not_integer}, factorial_of(test_factorializer, bob)),
      ?_assertEqual({fail, 5.0, is_not_integer}, factorial_of(test_factorializer, 5.0))]}.

adder_test_() ->
    {setup,
     fun() ->
        %runs before any of the tests
        Pid = spawn(?MODULE, adder, []),
        register(test_adder, Pid)
     end,
     %fun(_)->%runs after all of the tests
     %there is no teardown needed, so this fun doesn't need to be implemented.
     %end,
     %factorializer tests start here
     [?_assertEqual(8, add(test_adder, 5, 3)), %happy path
      % test less obvious or edge cases
      ?_assertEqual(0, add(test_adder, 0, 0)),
      ?_assertEqual(0.0, add(test_adder, 0.0, 0.0)),
      ?_assertEqual(0, add(test_adder, -5, 5)),
      ?_assertEqual(1.5, add(test_adder, 0.75, 0.75)),
      ?_assertEqual({fail, bob, is_not_number}, add(test_adder, bob, 3)),
      ?_assertEqual({fail, sue, is_not_number}, add(test_adder, 3, sue)),
      ?_assertEqual({fail, bob, is_not_number}, add(test_adder, bob, sue))]}.

subtracter_test_() ->
    {setup,
     fun() ->
        %runs before any of the tests
        Pid = spawn(?MODULE, subtracter, []),
        register(test_subtracter, Pid)
     end,
     %fun(_)->%runs after all of the tests
     %there is no teardown needed, so this fun doesn't need to be implemented.
     %end,
     %factorializer tests start here
     [?_assertEqual(2, subtract(test_subtracter, 5, 3)), %happy path
      % test less obvious or edge cases
      ?_assertEqual(0, subtract(test_subtracter, 0, 0)),
      ?_assertEqual(0.0, subtract(test_subtracter, 0.0, 0.0)),
      ?_assertEqual(-10, subtract(test_subtracter, -5, 5)),
      ?_assertEqual(0.75, subtract(test_subtracter, 1.5, 0.75)),
      ?_assertEqual({fail, bob, is_not_number}, subtract(test_subtracter, bob, 3)),
      ?_assertEqual({fail, sue, is_not_number}, subtract(test_subtracter, 3, sue)),
      ?_assertEqual({fail, bob, is_not_number}, subtract(test_subtracter, bob, sue))]}.

multiplier_test_() ->
    {setup,
     fun() ->
        %runs before any of the tests
        Pid = spawn(?MODULE, multiplier, []),
        register(test_multiplier, Pid)
     end,
     %fun(_)->%runs after all of the tests
     %there is no teardown needed, so this fun doesn't need to be implemented.
     %end,
     %factorializer tests start here
     [?_assertEqual(15, multiply(test_multiplier, 5, 3)), %happy path
      % test less obvious or edge cases
      ?_assertEqual(0, multiply(test_multiplier, 0, 0)),
      ?_assertEqual(0.0, multiply(test_multiplier, 0.0, 0.0)),
      ?_assertEqual(-25, multiply(test_multiplier, -5, 5)),
      ?_assertEqual(1.125, multiply(test_multiplier, 1.5, 0.75)),
      ?_assertEqual({fail, bob, is_not_number}, multiply(test_multiplier, bob, 3)),
      ?_assertEqual({fail, sue, is_not_number}, multiply(test_multiplier, 3, sue)),
      ?_assertEqual({fail, bob, is_not_number}, multiply(test_multiplier, bob, sue))]}.

divider_test_() ->
    {setup,
     fun() ->
        %runs before any of the tests
        Pid = spawn(?MODULE, divider, []),
        register(test_divider, Pid)
     end,
     %fun(_)->%runs after all of the tests
     %there is no teardown needed, so this fun doesn't need to be implemented.
     %end,
     %factorializer tests start here
     [?_assert((1.6 < divide(test_divider, 5, 3))
               and (divide(test_divider, 5, 3) < 1.7)), %happy path
      % test less obvious or edge cases
      ?_assertEqual(-1.0, divide(test_divider, -5, 5)),
      ?_assertEqual(2.0, divide(test_divider, 1.5, 0.75)),
      ?_assertEqual({fail, bob, is_not_number}, divide(test_divider, bob, 3)),
      ?_assertEqual({fail, sue, is_not_number}, divide(test_divider, 3, sue)),
      ?_assertEqual({fail, bob, is_not_number}, divide(test_divider, bob, sue))]}.

-endif.
