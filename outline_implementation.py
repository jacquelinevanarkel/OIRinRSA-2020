# Necessary imports
import pandas as pd
import numpy as np
import lexicon_retriever as lex_retriever

# --------------------------------------------- Part 1: RSA Implementation ---------------------------------------------
# ///////////////////////////////////////////////////// Production /////////////////////////////////////////////////////
class production:

    # Initialization
    def __init__(self, lexicon, intention, n, dialogue_history=None):
        self.L = lexicon
        self.i = intention
        self.n = n
        self.D = dialogue_history

    def produce(self):
        if n = 0:
            return self.production_literal()
        else:
            return self.production_pragmatic()

    def production_literal(self):
        #QUESTION: In this case, you store a new lexicon after conjunction, so you do not have to make the calculation
        #again, this is way more efficient, but is this right under our assumptions?
        if self.D is not None:
            self.L = self.conjunction()

        #calculate which signal s maximizes the probability, using the new lexicon if D not empty
        prob_lex = self.prob_literal()
        max_s = np.amax(prob_lex, axis=0)[self.i]
        indices = np.where(np.transpose(prob_lex)[i] == max_s)
        s = int(np.random.choice(indices[0], 1, replace=False))

        #Update dialogue history D
        if self.D is None:
            self.D = []
        self.D = self.D.append(s)
        return int(s)

    def production_pragmatic(self):
        #calculate which signal s maximizes the probability --> call function

        return s

    def conjunction(self):

        new_lexicon = np.zeros(self.L.shape)
        index_signal = 0

        for signal in self.L:
            index_referent = 0
            for r, r2 in zip(self.D[:-1], signal):
                if r == 1 & r2 == 1:
                    new_lexicon[index_signal, index_referent] = 1
                index_referent += 1
            index_signal +=1

        return new_lexicon

    def prob_literal(self):
        #Initialize new lex for probabilities
        prob_lex = np.zeros(self.L.shape)
        i_r = 0

        for r in np.transpose(self.L):
            sum_s_prob = np.sum(r)
            i_s = 0
            for s in r:
                prob_lex[i_s][i_r] = float(s)/float(sum_s_prob)
                i_s += 1
            i_r += 1

        return prob_lex

# /////////////////////////////////////////////////// Interpretation ///////////////////////////////////////////////////
class interpretation:

    # Initialization
    def __init__(self, lexicon, signal, n, entropy_threshold, n_t = 2, dialogue_history=None):
        self.L = lexicon
        self.s = signal
        self.n_t = n_t
        self.n = n
        self.D = dialogue_history
        self.H_t = entropy_threshold

    def interpret(self):
        if n = 0:
            self.interpretation_literal()
        else:
            selfinterpretation_pragmatic()

    def interpretation_literal(self):
        # if D is not empty
        s = self.conjunction()

        #calculate posterior distribution given s and D
        prob_lex = self.prob_literal()
        max_r = np.amax(prob_lex, axis=1)[self.s]
        indices = np.where(prob_lex[self.s] == max_r)
        r = int(np.random.choice(indices[0], 1, replace=False))

        #calculate entropy of posterior distribution
        H = self.conditional_entropy(r)

        # when H < H_t: output inferred referent
        # output = referent --> call function

        # when H > H_t:
        # turn to speaker --> output = OIR
        output = "OIR"

        return output, 0

    def interpretation_pragmatic(self):
        #Initialize variables
        n_t_reached = 0

        #calculate posterior distribution given s and L

        #calculate the entropy of posterior distribution
        H = self.conditional_entropy(r)

        #if H > H_t & n < n_t
        interpretation(self.L, self.n+1, self.s, self.n_t)

        # if H < H_t or when n = n_t --> recursion till n=0
        #save when n_t is reached!
        #interpretation(D, L, n, s) --> call function!

        return r, n_t_reached

    def conditional_entropy(self, r):
        #sum of:
        # pragmatic/literal probability of r given the signal and the lexicon(or dialogue history)
        # times
        # log (1/prob as described above)



        return H

    def conjunction(self):
        combined_signals = np.zeros(L.shape[1])
        index = 0
        for r, r2 in zip(self.D[:-1], self.s):
            if r == 1 & r2 ==1:
                combined_signals[index] = 1
            index += 1

        return combined_signals

    def prob_literal(self):
        #Initialize new lex for probabilities
        prob_lex = np.zeros(self.L.shape)
        i_s = 0

        for s in self.L:
            sum_s_prob = np.sum(s)
            i_r = 0
            for r in s:
                prob_lex[i_s][i_r] = float(r)/float(sum_s_prob)
                i_r += 1
            i_s += 1

        return prob_lex


# ------------------------------------------------- Part 2: Simulation -------------------------------------------------
#                                            Simulate a Single Conversation

#Initializing Agents: order of pragmatic reasoning, ambiguity level lexicon, type (listener, speaker), optional: entropy threshold
class agent:
    #Initialization
    def __init__(self, order, agent_type, entropy_threshold):
        self.n = order
        self.type = agent_type
        self.H_t = entropy_threshold

def interaction(speaker, listener, lexicon):
    turns = 0

    #Intention: randomly generated from uniform distribution
    n_referents = lexicon.shape[1]
    intention = np.random.randint(n_referents + 1)

    #Start interaction
    produced_signal = production(lexicon, intention, speaker.n).produce()
    turns += 1
    listener_output, n_t_reached = interpretation(lexicon, produced_signal, listener.n, listener.H_t).interpret()
    turns += 1
    while listener_output == "OIR":
        produced_signal = production(lexicon, intention, speaker.n).produce()
        turns += 1
        listener_output, n_t_reached = interpretation(lexicon, produced_signal, listener.n, listener.H_t).interpret()
        turns += 1

    #QUESTION: DO WE WANT TO SAVE THE IN BETWEEN SIGNALS (all the produced signals in a conversation)?
    output = np.array([intention, listener_output, turns, speaker.n, communicative_success(intention,listener_output),
                       n_t_reached])
    return output

# ///////////////////////////////////////// Measurements: dependent variables /////////////////////////////////////////
#Communicative success
def communicative_success(i, r):
    if i == r:
        cs = 1
    else:
        cs = 0

    return cs

#Actually, how the results are formatted now, I'd say to calculate this while analysing the data?
def average_com_suc():
    sum = 0
    for i, r in interactions:
        sum += communicative_success(i, r)

    return sum / len(interactions)

#Complexity: also a measurement, but not included here

# //////////////////////////////////////////////// Running Simulations ////////////////////////////////////////////////
#Think about multiprocessing
def simulation(n_interactions, ambiguity_level, n_signals, n_referents, order, entropy_threshold):
    #Initialize agents: order of pragmatic reasoning, agent type, entropy threshold
    speaker = agent(order, "Speaker", entropy_threshold)
    listener = agent(order, "Listener", entropy_threshold)

    # Generate Lexicons
    lexicons_df = pd.read_json('lexiconset.json')
    n_lexicons = n_interactions
    lexicons = lex_retriever.retrieve_lex(lexicons_df, n_signals, n_referents, ambiguity_level, n_lexicons)

    #Initliaze dataframe to store results
    results = pd.DataFrame(
        columns=["Intention Speaker", "Inferred Referent Listener", "Number of Turns", "Order of Reasoning",
                 "Communicative Success", "Reached threshold n", "Ambiguity Level", "n_signals", "n_referents"])

    for i in range(n_interactions):
        result = interaction(speaker, listener, lexicons[i])
        results.loc[len(results)] = np.concatenate((result, np.array([ambiguity_level, n_signals, n_referents]), axis=None)

    return results
