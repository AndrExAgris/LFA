#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {

    int num_states;
    char* states; //Q

    int num_input_symbols;
    char* input_symbols; //Sigma -> Alfabeto da fita

    int num_stack_symbols;
    char* stack_symbols; //Gama -> Alfabeto da pilha

    char initial_state; //q0

    char stack_empty_symbol; //Z0

    int num_transitions;
    struct Transition {
        char current_state;
        char next_state;
        char input_symbol;
        char stack_top;
        char* stack_write;
    } * transitions; //Delta

    int num_final_states;
    char* final_states; //F 


}Automaton;


void initializePDA(Automaton* pda) {

}

void visualizePDA(const Automaton* pda) {
    
}

