#include <stdio.h>
#include <gsl/gsl_multimin.h>

// Defining Rosenbrock function
double rosenbrock(const gsl_vector *v, void *params) {
    double x, y;
    x = gsl_vector_get(v, 0);
    y = gsl_vector_get(v, 1);

    return (1 - x) * (1 - x) + 100 * (y - x * x) * (y - x * x);
}

int main() {
    const gsl_multimin_fminimizer_type *T;
    gsl_multimin_fminimizer *s;
    gsl_vector *x, *step_size;
    gsl_multimin_function my_func;

    size_t iter = 0;
    int status;
    double size;

    // Setting step size
    step_size = gsl_vector_alloc(2);
    gsl_vector_set(step_size, 0, 0.01);
    gsl_vector_set(step_size, 1, 0.01);

    // Initial guess
    x = gsl_vector_alloc(2);
    gsl_vector_set(x, 0, 0.5);  // Modify the initial guess for x
    gsl_vector_set(x, 1, 0.5);  // Modify the initial guess for y

    // Function to minimize
    my_func.n = 2;
    my_func.f = rosenbrock;
    my_func.params = NULL;

    // Choosing the minimizer type and allocating the minimizer
    T = gsl_multimin_fminimizer_nmsimplex2;
    s = gsl_multimin_fminimizer_alloc(T, 2);

    // Setting initial position and size of the steps
    gsl_multimin_fminimizer_set(s, &my_func, x, step_size);

    // Iterating until convergence
    do {
        iter++;
        status = gsl_multimin_fminimizer_iterate(s);

        if (status)
            break;

        size = gsl_multimin_fminimizer_size(s);
        status = gsl_multimin_test_size(size, 1e-4);

        if (status == GSL_SUCCESS) {
            printf("Converged to minimum at iteration %zu\n", iter);
        }

        printf("Iteration %zu: x = %f, y = %f, f(x, y) = %f\n", iter,
               gsl_vector_get(s->x, 0), gsl_vector_get(s->x, 1),
               s->fval);
    } while (status == GSL_CONTINUE && iter < 100);

    // Free allocated memory
    gsl_vector_free(x);
    gsl_vector_free(step_size);
    gsl_multimin_fminimizer_free(s);

    return 0;
}
