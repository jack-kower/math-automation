import math

def circle_domain_range(h, k, r):
    # Domain: [h - r, h + r]
    domain = (h - r, h + r)
    # Range: [k - r, k + r]
    range_ = (k - r, k + r)
    return domain, range_

# Example: (x - 2)^2 + (y + 3)^2 = 16
h = -2      # x-coordinate of center
k = 3     # y-coordinate of center
r = math.sqrt(9)  # radius

domain, range_ = circle_domain_range(h, k, r)
print(f"Domain: [{domain[0]}, {domain[1]}]")
print(f"Range: [{range_[0]}, {range_[1]}]")