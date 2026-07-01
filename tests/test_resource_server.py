from mcp_servers.resource_server import get_learning_resources, get_beginner_resources, get_intermediate_resources, get_advanced_resources


def main():

    print("\nAll Fraction Resources:\n")
    print(get_learning_resources("Fractions"))
    print("\n\nBeginner Resources:\n")
    print(get_beginner_resources("Fractions"))
    print("\n\nIntermediate Resources:\n")
    print(get_intermediate_resources("Fractions"))
    print("\n\nAdvanced Resources:\n")
    print(get_advanced_resources("Fractions"))
    print("\n\nUnknown Topics:\n")
    print(get_learning_resources("Astronomy"))
    print("\n\nElectricity - Beginner:\n")
    print(get_beginner_resources("Electricity"))
    print("\n\nOrganic Chemistry - Intermediate:\n")
    print(get_intermediate_resources("Organic Chemistry"))
    print("\n\nTrigonometry - Advanced:\n")
    print(get_advanced_resources("Trigonometry"))


if __name__ == "__main__":
    main()
    
