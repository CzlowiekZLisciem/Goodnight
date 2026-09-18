from mindspace.routine import Routine
from mindspace.storage import save_routine
from mindspace.storage import load_routine


routine = Routine()

routine.add_item("medicine", "Take medicine")
routine.add_item("lights", "Turn off lights")
routine.complete_item("lights")

save_routine(routine)

loaded_routine = load_routine()
print(loaded_routine)