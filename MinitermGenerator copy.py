import itertools

class PredicateMintermGenerator:
    def __init__(self, predicates):
        self.predicates = predicates

    def create_miniterms(self):
        """
        Produces miniterms in a structured manner based on combinations of predicates.
        """
        miniterms = []
        
        # Loop over combination lengths, starting from 1 up to the total number of predicates
        for length in range(1, len(self.predicates) + 1):
            predicate_combinations = itertools.combinations(self.predicates, length)
            
            # Process each combination of predicates
            for combo in predicate_combinations:
                term_variants = self._generate_combinations(combo)
                miniterms.extend(term_variants)
        
        return miniterms

    def _generate_combinations(self, predicates_subset):
        """
        Helper function to generate true/false configurations for a subset of predicates.
        """
        fragment_list = []
        for config in range(2 ** len(predicates_subset)):
            fragment_terms = [
                predicates_subset[i] if (config >> i) & 1 else f"NOT {predicates_subset[i]}"
                for i in range(len(predicates_subset))
            ]
            fragment_list.append(" AND ".join(fragment_terms))
        
        return fragment_list


# Usage
predicates = ["A > 5", "B < 10", "C = 'X'"]
generator = PredicateMintermGenerator(predicates)
fragments = generator.create_miniterms()
for fragment in fragments:
    print(fragment)
