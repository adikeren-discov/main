import random

from candidate_solution import (
    CandidateSolution
)


def initialize_population(
    protein_sequence,
    genetic_code,
    population_size
):
    """
    Creates an initial population
    that correctly encodes insulin.
    """

    aa_to_codons = (
        genetic_code
    )

    population = []

    for _ in range(
        population_size
    ):

        codons = []

        for amino_acid in (
            protein_sequence
        ):

            possible_codons = (
                aa_to_codons[
                    amino_acid
                ]
            )

            chosen_codon = (
                random.choice(
                    possible_codons
                )
            )

            codons.append(
                chosen_codon
            )

        candidate = (
            CandidateSolution(
                codons
            )
        )

        population.append(
            candidate
        )

    return population

