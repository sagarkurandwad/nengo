import nengo
from nengo.spa.buffer import Buffer


class Memory(Buffer):
    """A SPA module capable of storing a vector over time.

    Parameters are the same as Buffer, with the following additions:

    Parameters
    ----------
    synapse : float
        synapse to use on recurrent connection
    tau : float or None
        Effective time constant of the integrator.  If None, it should
        have an infinite time constant.
    """

    def __init__(self, dimensions, subdimensions=16, neurons_per_dimension=50,
                 synapse=0.01, vocab=None, tau=None):
        super(Memory, self).__init__(
            dimensions=dimensions,
            subdimensions=subdimensions,
            neurons_per_dimension=neurons_per_dimension,
            vocab=vocab)

        if tau is None:
            transform = 1.0
        else:
            transform = 1.0 - synapse / tau

        nengo.Connection(self.state.output, self.state.input,
                         transform=transform, synapse=synapse)