cdef extern from "gsl/gsl_sf_bessel.h":

    ctypedef struct gsl_sf_result:
        double val
        double err

    int gsl_sf_bessel_I0_e(double x, gsl_sf_result *result)

cdef extern from "gsl/gsl_errno.h":

    ctypedef void gsl_error_handler_t
    int GSL_SUCCESS
    int GSL_EUNDRFLW
    char *gsl_strerror(int gsl_errno)
    gsl_error_handler_t* gsl_set_error_handler_off()

gsl_set_error_handler_off()

def I0(double x):
    cdef gsl_sf_result result
    cdef int status
    status = gsl_sf_bessel_I0_e(x, &result)
    if status == GSL_SUCCESS or status == GSL_EUNDRFLW:
        return result.val
    raise ValueError(gsl_strerror(status))
