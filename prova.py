import random
import time

# Define stimuli for the task
target_stimuli = ['< < < < <', '> > > > >']
flanker_stimuli = ['< > > < >', '> < < > <']

# Define a function for a single trial
def flanker_trial(target):
    # Display target and flanker stimuli
    if target == 'congruent':
        stimulus = target_stimuli[0] if random.choice([True, False]) else target_stimuli[1]
    else:  # incongruent
        stimulus = flanker_stimuli[0] if random.choice([True, False]) else flanker_stimuli[1]
    
    print("Stimulus:", stimulus)
    start_time = time.time()
    response = input("Respond with the direction of the middle arrow (< or >): ")
    reaction_time = time.time() - start_time
    
    # Evaluate response
    correct_response = '<' if stimulus[2] == '<' else '>'
    correct = (response == correct_response)
    
    return correct, reaction_time

# Run the task with random congruent/incongruent trials
for _ in range(5):  # Adjust the number of trials
    trial_type = random.choice(['congruent', 'incongruent'])
    correct, rt = flanker_trial(trial_type)
    print("Correct:", correct, "| Reaction time:", rt)
