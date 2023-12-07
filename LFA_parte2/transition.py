from stack import populate, stack, reset_stack

def reset_global_variables():
    global stack
    reset_stack() 

def epsilon_transition():
    global stack
    transitions = {
        'S': {'a': 'car_a A', 'car_b': 'car_b B', 'car_c': 'car_c C', 'car_d': 'car_d D'},
        'A': {'mod_aa': 'cor_preto rodas_estrada arcond', 'mod_ab': 'cor_preto rodas_estrada'},
        'A1': {},
        'A2': {},
        'B': {'mod_ba': 'cor_preto rodas_offroad multimidia', 'mod_bb': 'cor_vermelho rodas_offroad arcond'},
        'B1': {},
        'B2': {},
        'C': {'mod_ca': 'cor_vermelho rodas_estrada arcond multimidia', 'mod_cb': 'cor_preto rodas_estrada arcond multimidea'},
        'C1': {},  
        'C2': {}, 
        'D': {'mod_da': 'cor_preto rodas_estrada', 'mod_db': 'cor_vermelho rodas_estrada'},
        'D1': {}, 
        'D2': {}, 
    }

    current_state = stack[-1]
    
    if current_state in transitions:
        symbol_on_top_of_stack = stack[-1]
        if symbol_on_top_of_stack in transitions[current_state]:
            transition = transitions[current_state][symbol_on_top_of_stack]
            populate(pop_v=current_state, push_v=transition)
            return 1
    
    return 0

def tape_transition(fita):
    global stack
    transitions = {
        'car_a': '&',
        'car_b': '&',
        'car_c': '&',
        'car_d': '&',
        'mod_aa': '&',
        'mod_ab': '&',
        'mod_ba': '&',
        'mod_bb': '&',
        'mod_ca': '&',
        'mod_cb': '&',
        'mod_da': '&',
        'mod_db': '&',
        'cor_preto': '&',
        'cor_vermelho': '&',
        'arcond': '&',
        'multimidia': '&',
        'rodas_offroad': '&',
        'rodas_estrada': '&',
    }

    if fita and stack and fita[0] in transitions and stack[-1] == fita[0]:
        if fita[0] == 'erro':
            return 2  
        populate(pop_v=fita[0], push_v=transitions[fita[0]])
        fita.pop(0)
        return 1
    
    if not stack:
        return 2 
    
    return 0

def run_transitions(fita):
    global stack
    
    while fita:
        if 'erro' == fita[0]:
            return fita

        if not stack:
            reset_global_variables()
            return fita

        if not epsilon_transition():
            if not fita and stack:
                epsilon_transition()
                reset_global_variables()
                return fita

        if not tape_transition(fita):
            reset_global_variables()
            return fita

    return fita
