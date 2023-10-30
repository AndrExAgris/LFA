#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {

    int num_states;
    char* states; //Q

    int num_input_symbols;
    char* input_symbols; //Σ -> Alfabeto do automato/fita

    int num_stack_symbols;
    char* stack_symbols; //Γ -> Alfabeto da pilha

    char initial_state; //q0

    char stack_empty_symbol; //Z0

    int num_transitions;
    struct Transition {
        char current_state;
        char next_state;
        char input_symbol;
        char stack_top;
        char* stack_write;
    } * transitions; //δ

    int num_final_states;
    char* final_states; //F 


}Automaton;


void initializePDA(Automaton* pda) {
    FILE *file;
    char line[256];

    file = fopen("imput", "r");
    if (file == NULL) {
        perror("Failed to open the file");
        return 1;
    }

    // Read and print each line from the file
    while (fgets(line, sizeof(line), file) != NULL) {
        
        printf("%s", line);
    }

    // Close the file
    fclose(file);
}

int main(int argc, char const *argv[])
{
    

    

    return 0;
}

