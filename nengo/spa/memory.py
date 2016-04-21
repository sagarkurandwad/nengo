import warnings

import nengo
from nengo.spa.buffer import Buffer


class Memory(Buffer):
    """A SPA module capable of storing a vector over time.

    Parameters are the same as Buffer, with the following additions:

    Parameters
    ----------
    dimensions : int
        Number of dimensions for the vector
    subdimensions : int, optional
        Size of the individual ensembles making up the vector.  Must divide
        evenly into dimensions
    neurons_per_dimensions : int, optional
        Number of neurons in an ensemble will be this*subdimensions
    synapse : float, optional
        synaptic filter to use on recurrent connection
    vocab : Vocabulary, optional
        The vocabulary to use to interpret this vector
    tau : float or None, optional
        Effective time constant of the integrator. If None, it should
        have an infinite time constant.
    direct : boolean, optional
        Whether or not to use direct mode for the neurons

    label : str, optional
        A name for the ensemble. Used for debugging and visualization.
        Default: None
    seed : int, optional
        The seed used for random number generation.
        Default: None
    add_to_container : bool, optional
        Determines if this Network will be added to the current container.
        Defaults to true iff currently within a Network.
    """

    def __init__(self, dimensions, subdimensions=16, neurons_per_dimension=50,
                 synapse=0.01, vocab=None, tau=None, direct=False,
                 label=None, seed=None, add_to_container=None):
        warnings.warn("Memory is deprecated in favour of spa.State",
                      DeprecationWarning)
        super(Memory, self).__init__(
            dimensions=dimensions,
            subdimensions=subdimensions,
            neurons_per_dimension=neurons_per_dimension,
            vocab=vocab,
            direct=direct,
            label=label,
            seed=seed,
            add_to_container=add_to_container)

        if tau is None:
            transform = 1.0
        else:
            transform = 1.0 - synapse / tau

        with self:
            nengo.Connection(self.state.output, self.state.input,
                             transform=transform, synapse=synapse)
