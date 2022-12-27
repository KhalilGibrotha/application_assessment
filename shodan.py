import shodan

# Replace YOUR_API_KEY with your Shodan API key
#api = shodan.Shodan("YOUR_API_KEY")
api = "hzUwW29Ni4wvzgYCeKRSzHMOGgTgMkkI"
ip_address = input("Enter the IP address: ")
port = input("Enter the port: ")

# Replace IP_ADDRESS and PORT with the specific IP address and port you want to search for
results = api.search(f"ip:{ip_address} port:{port}")

print(results)


#https://api.shodan.io/shodan/host/search?key=hzUwW29Ni4wvzgYCeKRSzHMOGgTgMkkI&query=ip: