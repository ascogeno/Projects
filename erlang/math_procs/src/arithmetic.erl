-module(arithmetic).

-export([start_factorializer/0, start_adder/0, start_subtracter/0, start_multiplier/0,
         start_divider/0, factorializer/0, adder/0, subtracter/0, multiplier/0, divider/0,
         factorial_of/2, add/3, subtract/3, multiply/3, divide/3]).

%%
%% Put your functions, described in the task HTML file here.

start_factorializer() ->
   spawn(?MODULE, factorializer, []).

start_adder() ->
   spawn(?MODULE, adder, []).

start_subtracter() ->
   spawn(?MODULE, subtracter, []).

start_multiplier() ->
   spawn(?MODULE, multiplier, []).

start_divider() ->
   spawn(?MODULE, divider, []).

%% Clients
factorial_of(Pid, Number) ->
   Pid ! {self(), Number},
   receive
      Response ->
         Response
   end.

add(Pid, A, B) ->
   Pid ! {self(), A, B},
   receive
      Response ->
         Response
   end.

subtract(Pid, A, B) ->
   Pid ! {self(), A, B},
   receive
      Response ->
         Response
   end.

multiply(Pid, A, B) ->
   Pid ! {self(), A, B},
   receive
      Response ->
         Response
   end.

divide(Pid, A, B) ->
   Pid ! {self(), A, B},
   receive
      Response ->
         Response
   end.

%% Process functions
factorializer() ->
   receive
      {Pid, Data} when is_integer(Data) == false ->
         Pid ! {fail, Data, is_not_integer};
      {Pid, Integer} when Integer < 0 ->
         Pid ! {fail, Integer, is_negative};
      {Pid, Number} ->
         Pid ! lists:foldl(fun(X, Accum) -> X * Accum end, 1, lists:seq(1, Number))
   end,
   factorializer().

adder() ->
   receive
      {Pid, A, _B} when is_number(A) == false ->
         Pid ! {fail, A, is_not_number};
      {Pid, _A, B} when is_number(B) == false ->
         Pid ! {fail, B, is_not_number};
      {Pid, A, B} ->
         Pid ! A + B
   end,
   adder().

subtracter() ->
   receive
      {Pid, A, _B} when is_number(A) == false ->
         Pid ! {fail, A, is_not_number};
      {Pid, _A, B} when is_number(B) == false ->
         Pid ! {fail, B, is_not_number};
      {Pid, A, B} ->
         Pid ! A - B
   end,
   subtracter().

multiplier() ->
   receive
      {Pid, A, B} when is_number(A) == false ->
         Pid ! {fail, A, is_not_number};
      {Pid, _A, B} when is_number(B) == false ->
         Pid ! {fail, B, is_not_number};
      {Pid, A, B} ->
         Pid ! A * B
   end,
   multiplier().

divider() ->
   receive
      {Pid, A, _B} when is_number(A) == false ->
         Pid ! {fail, A, is_not_number};
      {Pid, _A, B} when is_number(B) == false ->
         Pid ! {fail, B, is_not_number};
      {Pid, _A, 0} ->
         Pid ! {fail, division_by_zero};
      {Pid, A, B} ->
         Pid ! A / B
   end,
   divider().

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
