-module(groceries).

-export([start/1, rpc/2, run/1]).

start(Initial_grocery_list) ->
    spawn(?MODULE, run, [Initial_grocery_list]).

rpc(Pid, Message) ->
    Pid ! {self(), Message},
    receive
        Response ->
            Response
    end.

run(Grocery_list) ->
    receive
        {Pid, {add_item, Item, Price1, Price2}} ->
            NewList = lists:keystore(Item, 1, Grocery_list, {Item, {Price1, Price2}}),
            Pid ! ok,
            run(NewList);
        {Pid, get_best_prices} ->
            BestPrices = find_best_prices(Grocery_list),
            Pid ! BestPrices,
            run(Grocery_list);
        {Pid, get_best_store} ->
            BestStore = find_best_store(Grocery_list),
            Pid ! BestStore,
            run(Grocery_list);
        {Pid, stop} ->
            Pid ! stopped
    end.

find_best_prices(Grocery_list) ->
    lists:map(fun({Item, {P1, P2}}) ->
                 BestPrice =
                     if P1 =< P2 -> {Item, P1, store1};
                        true -> {Item, P2, store2}
                     end,
                 BestPrice
              end,
              Grocery_list).

find_best_store(GroceryList) ->
    {Total1, Total2} =
        lists:foldl(fun({_, {P1, P2}}, {Sum1, Sum2}) -> {Sum1 + P1, Sum2 + P2} end,
                    {0, 0},
                    GroceryList),
    if Total1 =< Total2 ->
           store1;
       true ->
           store2
    end.
