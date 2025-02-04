-module(ctemplate).

-export([start/0, rpc/2, loop/1]).

% Start the process and pass an initial state.
start() ->
    spawn(?MODULE, loop, [[]]).

% RPC function to send a message and wait for a response.
rpc(Pid, Request) ->
    Pid ! {self(), Request},
    receive
        {Pid, Response} ->
            Response
    end.

% Process loop that receives messages, processes them, and continues.
loop(State) ->
    receive
        {Caller, Message} ->
            io:format("Received: ~p~n", [Message]),
            Caller ! {self(), ok},  % Example response
            loop(State);  % Continue looping with the same state
        _Other ->
            loop(State)  % Ignore unknown messages
    end.
