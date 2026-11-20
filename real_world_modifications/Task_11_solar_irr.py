from scipy.optimize import root_scalar

# Initial rooftop solar installation cost (-18,000) and 5 years of electricity bill savings
solar_cash_flows = [-18000, 4800, 5100, 5400, 5700, 6000]

def solar_npv(rate):
    return sum(cf / (1 + rate)**t for t, cf in enumerate(solar_cash_flows))

def d_solar_npv(rate):
    return sum(-t * cf / (1 + rate)**(t + 1) for t, cf in enumerate(solar_cash_flows) if t > 0)

newton_res = root_scalar(solar_npv, fprime=d_solar_npv, x0=0.10, method="newton", xtol=1e-12)
secant_res = root_scalar(solar_npv, x0=0.05, x1=0.20, method="secant", xtol=1e-12)

print(f"Solar IRR (Newton-Raphson): {newton_res.root:.4%} (in {newton_res.iterations} iterations)")
print(f"Solar IRR (Secant method):  {secant_res.root:.4%} (in {secant_res.iterations} iterations)")
print(f"NPV check at IRR:           {solar_npv(newton_res.root):.8f}")
