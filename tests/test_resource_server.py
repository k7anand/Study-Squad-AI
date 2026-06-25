from mcp_servers.resource_server import get_learning_resources


def main():
    print("\nFractions:\n")
    print(get_learning_resources("Fractions"))
    print("\nElectricity:\n")
    print(get_learning_resources("Electricity"))
    print("\nUnknown Topics:\n")
    print(get_learning_resources("Astronomy"))


if __name__ == "__main__":
    main()
