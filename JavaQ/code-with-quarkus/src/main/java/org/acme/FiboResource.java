package org.acme;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

@Path("/fibonacci")
public class FiboResource {

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    @Path("{number}")
    public String FibonacciView(long number) {
       return Long.toString(fib(number));
    }
    
    
    private long fib(long number) {
        if (number <= 1)
            return number;
        return fib(number - 1) + fib(number - 2);
    }
}


