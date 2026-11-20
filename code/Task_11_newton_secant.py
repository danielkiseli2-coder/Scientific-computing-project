from scipy.optimize import root_scalar

print("=== Task 11: Original Run ===")
# Initial investment followed by annual cash inflows
cash_flows = [-12000, 3600, 4100, 4500, 3200]

def npv(rate):
    return sum(
        cf / (1 + rate)**t
        for t, cf in enumerate(cash_flows)
    )

def d_npv(rate):
    return sum(
        -t * cf / (1 + rate)**(t + 1)
        for t, cf in enumerate(cash_flows)
        if t > 0
    )

newton = root_scalar(
    npv,
    fprime=d_npv,
    x0=0.10,
    method="newton",
    xtol=1e-12
)

secant = root_scalar(
    npv,
    x0=0.05,
    x1=0.20,
    method="secant",
    xtol=1e-12
)

print(f"IRR using Newton-Raphson: {newton.root:.6%}")
print(f"IRR using Secant method:  {secant.root:.6%}")
print(f"NPV at Newton solution:   {npv(newton.root):.6f}")

# --- Part C: Modified Parameter Run ---
print("\n=== Task 11: Part C (Modified Parameter Run) ===")
# Reduce initial investment from -12000 to -10200
cash_flows_mod = [-10200, 3600, 4100, 4500, 3200]

def npv_mod(rate):
    return sum(cf / (1 + rate)**t for t, cf in enumerate(cash_flows_mod))

def d_npv_mod(rate):
    return sum(-t * cf / (1 + rate)**(t + 1) for t, cf in enumerate(cash_flows_mod) if t > 0)

newton_mod = root_scalar(npv_mod, fprime=d_npv_mod, x0=0.10, method="newton", xtol=1e-12)
secant_mod = root_scalar(npv_mod, x0=0.05, x1=0.20, method="secant", xtol=1e-12)

print(f"Modified Newton-Raphson IRR: {newton_mod.root:.6%} ({newton_mod.iterations} iterations)")
print(f"Modified Secant method IRR:  {secant_mod.root:.6%} ({secant_mod.iterations} iterations)")
