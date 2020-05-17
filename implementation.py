# Necessary imports
import pandas as pd
import numpy as np
import lexicon_retriever as lex_retriever

# --------------------------------------------- Part 1: RSA Implementation ---------------------------------------------
# ///////////////////////////////////////////////////// Production /////////////////////////////////////////////////////
class Production:

    def __init__(self, lexicon, intention, order, dialogue_history=None):
        """
        Initialization of class.
        :param lexicon: array; the lexicon used by the speaker
        :param intention: int; the intended referent meant by the speaker
        :param order: int; the order of pragmatic reasoning of the speaker
        :param dialogue_history: list; the previously produced signals
        """

        self.lexicon = lexicon
        self.intention = intention
        self.order = order
        self.dialogue_history = dialogue_history

    def produce(self):
        """
        Start producing by calling the function corresponding to the order of pragmatic reasoning of the speaker.
        :return: int; signal by calling the corresponding production function.
        """

        if self.order = 0:
            return self.production_literal()
        else:
            return self.production_pragmatic()

    def production_literal(self):
        """
        For literal speakers, a signal is produced by choosing the signal that maximizes the probability given the
        intention, making use of the dialogue history if provided.
        :return: int; signal
        """

        #Perform conjunction if a dialogue history is available: the lexicon changes accordingly for this interaction
        if self.dialogue_history is not None:
            self.lexicon = self.conjunction()

        #Calculate which signal maximizes the probability, given the intention
        prob_lex = self.prob_literal()
        max_signal = np.amax(prob_lex, axis=0)[self.intention]
        indices = np.where(np.transpose(prob_lex)[self.intention] == max_signal)
        signal = int(np.random.choice(indices[0], 1, replace=False))

        #Update dialogue history with just chosen signal
        if self.dialogue_history is None:
            self.dialogue_history = []
        self.dialogue_history = self.dialogue_history.append(signal)
        return int(signal)

    def production_pragmatic(self):
        """
        For pragmatic speakers, a signal is produced by choosing the signal that maximizes the probability given the
        intention, determined by the order of pragmatic reasoning.
        :return: int; signal
        """

        #calculate which signal signal maximizes the probability --> call function

        return signal

    def conjunction(self):
        """
        Perform conjunction between the lexicon and the last produced signal.
        :return: array; new lexicon based on the conjunction
        """

        #Initialize new lexicon
        new_lexicon = np.zeros(self.lexicon.shape)
        index_signal = 0

        #Perform conjunction on last produced signal and the lexicon
        for signal in self.lexicon:
            index_referent = 0
            for ref, ref2 in zip(self.dialogue_history[:-1], signal):
                if ref == 1 & ref2 == 1:
                    new_lexicon[index_signal, index_referent] = 1
                index_referent += 1
            index_signal +=1

        return new_lexicon

    def prob_literal(self):
        """
        Calculate the probabilities of the signals given the referents to create a lexicon filled with probabilities.
        :return: array; lexicon with probabilities of signals given referents
        """

        #Initialize new lexicon for probabilities
        prob_lex = np.zeros(self.lexicon.shape)

        #Calculate the probabilities for every signal given the referent
        index_referent = 0
        for referent in np.transpose(self.lexicon):
            sum_signal_prob = np.sum(referent)
            index_signal = 0
            for signal in referent:
                prob_lex[index_signal][index_referent] = float(signal)/float(sum_signal_prob)
                index_signal += 1
            index_referent += 1

        return prob_lex

# /////////////////////////////////////////////////// Interpretation ///////////////////////////////////////////////////
class Interpretation:

    def __init__(self, lexicon, signal, order, entropy_threshold, order_threshold = 2, dialogue_history=None):
        """
        Initialization of class.
        :param lexicon: array; the lexicon used by the listener
        :param signal: int; the received signal from the speaker
        :param order: int; order of pragmatic reasoning of the listener
        :param entropy_threshold: int; the entropy threshold
        :param order_threshold: int; the order of pragmatic reasoning threshold
        :param dialogue_history: list; the previously produced signals by the speaker
        """

        self.lexicon = lexicon
        self.signal = signal
        self.order_threshold = order_threshold
        self.order = order
        self.dialogue_history = dialogue_history
        self.entropy_threshold = entropy_threshold

    def interpret(self):
        """
        Start interpreting the signal of the speaker by calling the function corresponding to the order of pragmatic
        reasoning of the listener.
        :return: inferred referent (int) or OIR (string) and whether the threshold of the order or pragmatic reasoning
        was reached (Boolean) by calling the corresponding production function
        """

        if n = 0:
            output, order_threshold_reached = self.interpretation_literal()
            return output, order_threshold_reached
        else:
            output, order_threshold_reached = self.interpretation_pragmatic()
            return output, order_threshold_reached

    def interpretation_literal(self):
        """
        Interpret the signal by calculating the posterior distribution of the referents given the signal, lexicon and
        dialogue history if not empty. The entropy over the posterior distribution decides how certain the listener is
        of the inferred referent: if uncertain, the listener will signal other-initiated repair (OIR) to give the turn
        to the speaker again. If certain, the listener will output the inferred referent.
        :return: output which can consist of either an inferred referent or other-initiated repair (OIR) and 0
        (meaning that the threshold of the order of pragmatic reasoning was not reached)
        """

        #Perform conjunction if a dialogue history is available, returning a combined signal (from previous signal +
        # current signal)
        self.signal = self.conjunction()

        #Calculate posterior distribution given the signal, lexicon, and dialogue history if not empty
        prob_lex = self.prob_literal()
        max_referent = np.amax(prob_lex, axis=1)[self.signal]
        indices = np.where(prob_lex[self.signal] == max_referent)
        referent = int(np.random.choice(indices[0], 1, replace=False))

        #Calculate conditional entropy of posterior distribution
        entropy = self.conditional_entropy(referent)

        # when H < entropy_threshold: output inferred referent
        # output = referent --> call function

        # when H > entropy_threshold:
        # turn to speaker --> output = OIR
        output = "OIR"

        return output, 0

    def interpretation_pragmatic(self):
        """
        Interpret the signal by calcullating the posterior distribution of the referents given the signal, lexicon and
        dialogue history if not empty. The entropy over the posterior distribution decides how certain the listener is
        of the inferred referent: if uncertain, the listener will go a level up on the order of pragmatic reasoning and
        interpret the signal again, with a higher order of pragmatic reasoning. If certain, the listener will output
        the inferred referent.
        :return: inferred referent (int) and whether the threshold of the order of pragmatic reasoning is reached
        (Boolean)
        """

        #Initialize the variable for whether the threshold of the order of pragmatic reasoning is reached
        order_threshold_reached = 0

        #Calculate posterior distribution given signal and lexicon

        #Calculate the conditional entropy of posterior distribution
        entropy = self.conditional_entropy(referent)

        #if H > entropy_threshold & order < order_threshold
        interpretation(self.lexicon, self.order + 1, self.signal, self.order_threshold)

        # if H < entropy_threshold or when order = order_threshold --> recursion till order=0
        #save when order_threshold is reached!
        #interpretation(dialogue_history, lexicon, order, signal) --> call function!

        return referent, order_threshold_reached

    def conditional_entropy(self, referent):
        """
        Calculate the conditional entropy over the posterior distribution of the referents given the signal, lexicon and
        dialogue history if not empty.
        :param referent: int; inferred referent
        :return: int; the entropy of the inferred referent
        """
        #sum of:
        # pragmatic/literal probability of r given the signal and the lexicon(or dialogue history)
        # times
        # log (1/prob as described above)



        return entropy

    def conjunction(self):
        """
        Perform conjunction between the current signal and the last produced signal by the speaker.
        :return: array; the conjunction of both signals into a combined signal
        """

        #Initialize an array to store the combined signal in
        combined_signal = np.zeros(self.lexicon.shape[1])

        #Perform the conjunction between the current and previous signal (from the dialogue history)
        index = 0
        for ref, ref2 in zip(self.dialogue_history[:-1], self.signal):
            if ref == 1 & ref2 ==1:
                combined_signal[index] = 1
            index += 1
        return combined_signal

    def prob_literal(self):
        """
        Calculate the probabilities of the referents given the signal to create a lexicon filled with probabilities.
        :return: array; lexicon with probabilities of referents given the signal
        """

        #Initialize new lexicon for probabilities
        prob_lex = np.zeros(self.lexicon.shape)

        #Calculate the probabilities for every referent given the signal
        index_signal = 0
        for signal in self.lexicon:
            sum_signal_prob = np.sum(signal)
            index_referent = 0
            for referent in signal:
                prob_lex[index_signal][index_referent] = float(referent)/float(sum_signal_prob)
                index_referent += 1
            index_signal += 1

        return prob_lex


# ------------------------------------------------- Part 2: Simulation -------------------------------------------------
#                                            Simulate a Single Conversation

#Initializing Agents: order of pragmatic reasoning, ambiguity level lexicon, type (listener, speaker), optional: entropy threshold
class Agent:

    def __init__(self, order, agent_type, entropy_threshold):
        """
        Initialization of class.
        :param order: int; order of pragmatic reasoning of agent
        :param agent_type: string; speaker or listener type
        :param entropy_threshold: int; entropy threshold
        """
        self.order = order
        self.type = agent_type
        self.entropy_threshold = entropy_threshold

def interaction(speaker, listener, lexicon):
    """
    Perform one interaction (until the listener is certain enough about an inferred referent or the threshold for the
    order of pragmatic reasoning is reached) between listener and speaker.
    :param speaker: the agent with type "speaker"
    :param listener: the agent with type "listener"
    :param lexicon: array; lexicon for the speaker and listener (assumption: both agents have the same lexicon)
    :return: array; the array contains the following information about the interaction: the intention, the inferred
    referent by the listener, the amount of turns, the order of speaker and listener (assumed to be equal), the
    communicative success and whether the threshold of the order of pragmatic reasoning was reached
    """
    #Initialize the amount of turns
    turns = 0

    #Generate intention: randomly generated from uniform distribution
    n_referents = lexicon.shape[1]
    intention = np.random.randint(n_referents + 1)

    #Start interaction by the speaker producing a signal and the listener interpreting that signal, if (and as long as)
    #the listener signals other-initiated repair (OIR), the speaker and listener will continue the interaction by
    #producing and interpreting new signals.
    produced_signal = Production(lexicon, intention, speaker.order).produce()
    turns += 1
    listener_output, n_t_reached = Interpretation(lexicon, produced_signal, listener.order, listener.entropy_threshold).interpret()
    turns += 1
    while listener_output == "OIR":
        produced_signal = Production(lexicon, intention, speaker.order).produce()
        turns += 1
        listener_output, n_t_reached = Interpretation(lexicon, produced_signal, listener.order, listener.entropy_threshold).interpret()
        turns += 1

    #Save the wanted information in an array to be returned
    #QUESTION: DO WE WANT TO SAVE THE IN BETWEEN SIGNALS (all the produced signals in a conversation)? --> yes
    output = np.array([intention, listener_output, turns, speaker.order, communicative_success(intention, listener_output),
                       order_threshold_reached])
    return output

# ///////////////////////////////////////// Measurements: dependent variables /////////////////////////////////////////
def communicative_success(intention, referent):
    """
    Calculate the communicative success: 1 if the intention and inferred referent are equal, 0 otherwise.
    :param intention: int; the intention of the speaker
    :param referent: int; the inferred referent by the listener
    :return: int; communicative success
    """

    if intention == referent:
        com_suc = 1
    else:
        com_suc = 0

    return com_suc

def average_com_suc(interactions):
    """
    Calculate the average communicative success: average of communicative success over all interactions.
    :return: float; average communicative success
    """

    sum = 0
    for intention, referent in interactions:
        sum += communicative_success(intention, referent)

    return sum / len(interactions)

#Complexity: also a measurement, but not included here

# //////////////////////////////////////////////// Running Simulations ////////////////////////////////////////////////
#Think about multiprocessing
def simulation(n_interactions, ambiguity_level, n_signals, n_referents, order, entropy_threshold):
    """
    Run a simulation of a number of interactions (n_interactions), with the specified parameters.
    :param n_interactions: int; the number of interactions to be performed in the simulation
    :param ambiguity_level: float (between 0.0 and 1.0); the desired ambiguity level of the lexicon
    :param n_signals: int; the number of signals in the lexicon
    :param n_referents: int; the number of referents in the lexicon
    :param order: int; the order of pragmatic reasoning for both agents
    :param entropy_threshold: int; the entropy threshold
    :return: dataframe; consisting of the following information: the intention of the speaker, the inferred referent of
    the listener, the number of turns, the order of pragmatic reasoning, the communicative success, whether the
    threshold of the order of pragmatic reasoning was reached, the ambiguity level, the number of signals, the number
    of referents
    """
    #Initialize agents with the order of pragmatic reasoning, agent type, and entropy threshold
    speaker = Agent(order, "Speaker", entropy_threshold)
    listener = Agent(order, "Listener", entropy_threshold)

    #Generate Lexicons with the number of signals, the number of referents, the ambiguity level and the number of
    #lexicons
    lexicons_df = pd.read_json('lexiconset.json')
    n_lexicons = n_interactions
    lexicons = lex_retriever.retrieve_lex(lexicons_df, n_signals, n_referents, ambiguity_level, n_lexicons)

    #Initliaze pandas dataframe to store results
    results = pd.DataFrame(
        columns=["Intention Speaker", "Inferred Referent Listener", "Number of Turns", "Order of Reasoning",
                 "Communicative Success", "Reached Threshold Order", "Ambiguity Level", "Number of Signals",
                 "Number of referents"])

    #Run the desired number of interactions for the simulation and store the results in the pandas dataframe
    for i in range(n_interactions):
        result = interaction(speaker, listener, lexicons[i])
        results.loc[len(results)] = np.concatenate((result, np.array([ambiguity_level, n_signals, n_referents]), axis=None)

    return results