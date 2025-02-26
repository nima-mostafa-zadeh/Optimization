import random
from typing import List, Callable, Tuple

def particle_swarm_optimization(
    objective_function: Callable[[List[float]], float],
    num_parameters: int,
    num_particles: int,
    lower_bounds: List[float],
    upper_bounds: List[float],
    cognitive_coefficient: float = 0.5,
    social_coefficient: float = 0.5,
    inertia_weight: float = 1.1,
    max_iterations: int = 5000
) -> Tuple[List[float], float]:
    

    # Initialize particle positions, velocities, and best positions
    positions = [[0.0] * num_parameters for _ in range(num_particles)]
    velocities = [[0.0] * num_parameters for _ in range(num_particles)]
    personal_best = [[0.0] * num_parameters for _ in range(num_particles)]
    global_best = [0.0] * num_parameters
    
    # Initialize particles with random positions and velocities
    for i in range(num_particles):
        random_values = [random.random() for _ in range(num_parameters)]
        for j in range(num_parameters):
            # Set initial position within bounds
            positions[i][j] = lower_bounds[j] + (upper_bounds[j] - lower_bounds[j]) * random_values[j]
            personal_best[i][j] = positions[i][j]
            
            # Set initial velocity
            range_width = abs(upper_bounds[j] - lower_bounds[j])
            velocities[i][j] = -range_width + 2 * range_width * random_values[j]
        
        # Update global best if this particle is better
        if objective_function(personal_best[i]) < objective_function(global_best):
            global_best = personal_best[i].copy()
    
    # Main optimization loop
    for _ in range(max_iterations):
        for i in range(num_particles):
            for j in range(num_parameters):
                # Random coefficients
                r_personal = random.random()
                r_global = random.random()
                
                # Update velocity
                velocities[i][j] = (inertia_weight * velocities[i][j] + 
                                   cognitive_coefficient * r_personal * (personal_best[i][j] - positions[i][j]) + 
                                   social_coefficient * r_global * (global_best[j] - positions[i][j]))
                
                # Update position
                positions[i][j] += velocities[i][j]
            
            # Update personal best if current position is better
            if objective_function(positions[i]) < objective_function(personal_best[i]):
                personal_best[i] = positions[i].copy()
                
                # Update global best if this personal best is better
                if objective_function(personal_best[i]) < objective_function(global_best):
                    global_best = personal_best[i].copy()
    
    # Return best position and its objective function value
    return global_best, objective_function(global_best)