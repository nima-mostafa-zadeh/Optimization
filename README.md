# Optimization
## Particle Swarm Optimization (PSO)

A Python implementation of the Particle Swarm Optimization algorithm for continuous function optimization problems.

### Overview

Particle Swarm Optimization (PSO) is a population-based stochastic optimization technique inspired by the social behavior of birds flocking or fish schooling. This implementation provides a clean, type-hinted Python function that can be used to minimize any objective function.

### Features

- **Type-hinted API**: Clear function signatures with type annotations
- **Configurable parameters**: Easily adjust swarm behavior with cognitive and social coefficients
- **Flexible bounds**: Set different bounds for each parameter dimension
- **Simple interface**: Requires only an objective function and parameter bounds

### Usage

```python
from pso import particle_swarm_optimization

# Example: Minimize the Rosenbrock function
def rosenbrock(x):
    """Rosenbrock function with global minimum at (1,1,...,1)"""
    result = 0
    for i in range(len(x) - 1):
        result += 100 * (x[i+1] - x[i]**2)**2 + (x[i] - 1)**2
    return result

# Define problem parameters
num_parameters = 2  # 2D problem
num_particles = 30
lower_bounds = [-5.0, -5.0]
upper_bounds = [5.0, 5.0]

# Run the optimization
best_position, best_value = particle_swarm_optimization(
    objective_function=rosenbrock,
    num_parameters=num_parameters,
    num_particles=num_particles,
    lower_bounds=lower_bounds,
    upper_bounds=upper_bounds,
    max_iterations=1000
)

print(f"Best solution found: {best_position}")
print(f"Objective function value: {best_value}")
```

### Function Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `objective_function` | Callable[[List[float]], float] | Function to minimize | (required) |
| `num_parameters` | int | Number of dimensions in the problem | (required) |
| `num_particles` | int | Size of the particle swarm | (required) |
| `lower_bounds` | List[float] | Lower bounds for each parameter | (required) |
| `upper_bounds` | List[float] | Upper bounds for each parameter | (required) |
| `cognitive_coefficient` | float | Weight for particle's own best position | 0.5 |
| `social_coefficient` | float | Weight for swarm's best position | 0.5 |
| `inertia_weight` | float | Weight for previous velocity | 1.1 |
| `max_iterations` | int | Maximum number of iterations | 5000 |

### Algorithm Details

The PSO algorithm works as follows:

1. **Initialization**: Particles are randomly positioned within the search space and given random initial velocities.

2. **Evaluation**: Each particle's position is evaluated using the objective function.

3. **Update**: For each iteration:
   - Particle velocities are updated based on:
     - The particle's previous velocity (inertia component)
     - The particle's personal best position (cognitive component)
     - The swarm's global best position (social component)
   - Particle positions are updated based on their velocities
   - Personal and global best positions are updated if better solutions are found

4. **Termination**: The algorithm terminates after the specified number of iterations.

### Parameter Tuning

- Increase `num_particles` for better exploration at the cost of computation time
- Adjust coefficients to control swarm behavior:
  - Higher `cognitive_coefficient`: Particles explore their own discoveries more
  - Higher `social_coefficient`: Particles are more drawn to the global best
  - Higher `inertia_weight`: Particles maintain more momentum
