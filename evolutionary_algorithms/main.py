import config

from processing import (
    protein_sequence_processing,
    process_genetic_code,
    process_ecoli_frequencies,
    build_codon_lookup
)

from mutation_engine import (
    initialize_population
)

from fitness import (
    fitness
)


def main():

    protein = (
        protein_sequence_processing()
    )

    aa_to_codons = (
        process_genetic_code()
    )

    codon_lookup = (
        build_codon_lookup(
            aa_to_codons
        )
    )

    ecoli_freqs = (
        process_ecoli_frequencies()
    )

    population = (
        initialize_population(
            protein_sequence=protein,
            genetic_code=aa_to_codons,
            population_size=5
        )
    )

    print(
        "\n=== POPULATION ==="
    )

    for i, candidate in enumerate(
        population
    ):

        score = fitness(
            codon_sequence=(
                candidate.codons
            ),
            ecoli_frequencies=(
                ecoli_freqs
            ),
            target_protein=(
                protein
            ),
            codon_lookup=(
                codon_lookup
            )
        )

        print(
            f"\nCandidate "
            f"{i+1}"
        )

        print(candidate)

        print(
            f"Fitness: "
            f"{score:.3f}"
        )

if __name__ == "__main__":
    main()