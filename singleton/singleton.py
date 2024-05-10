class RoundRobin:
    _instance = None

    def __new__(cls):
        # Initialize the instance if it doesn't exist ans store the instance in the _instance attribute
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super(RoundRobin, cls).__new__(cls)
            # Put any initialization here.
            # In this case list of servers and the current index
            cls.servers = []
            cls.index = 0
        return cls._instance

    # Add a new server to the list of servers
    def add_server(self, server):
        self.servers.append(server)

    # Get the next server
    def get_next_server(self):
        if not len(self.servers):
            raise Exception("No servers available")

        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server


lb1 = RoundRobin()
lb2 = RoundRobin()

print("Singleton -->", lb1 == lb2)

lb1.add_server("Server 1")
lb1.add_server("Server 2")
lb1.add_server("Server 3")

print(lb1.get_next_server())
print(lb1.get_next_server())
print(lb1.get_next_server())
print(lb1.get_next_server())
print(lb1.get_next_server())
