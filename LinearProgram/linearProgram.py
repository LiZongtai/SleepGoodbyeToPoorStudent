from scipy import  optimize as opt
import numpy as np
from scipy.optimize import minimize

# 新鲜鱼10℃三天腐败变质，两天内（48h）运回可上架，过期低价处理，上架价格1.1£/kg=1100£/tons

# profit
# profit=FP*harvest-distance/VS*OH*OP-VP-OC

# maximum of fish price when frash - £/tons
MP=400
# function of fish price - £
def FP(t):
    return (1-t/72)*MP
# consumption of oil per hour - L/h
def OH(cq):
    return 100*(1+cq/200)**(2/3)
# diesel oil price - 1.3£/L
OP=1.3
# vessel price - £
VP=550000
# other cost - £
OC=2000000
# fax rate - %
FX=0.4
# vessel speed - km/h
VS=20
# catching effciency - tons/h
CE=400/24
# function of catching time - h
def CT(cq,dp):
    return 2*dp/VS+cq/CE 
# relation function of distance-from-port and catch-quantity
def DC(dp):
    return 0.007*dp*dp+1.855*dp+73.52




# object function - maximize profits
def objective(x):
    return -(70*(FP(x[0])*x[1]-(2*x[2]/VS)*OH(x[1])*OP))*(1-FX)+VP+OC
# constraints
def constraint1(x):
    return 48-x[0]
def constraint2(x):
    return 500-x[1] 
def constraint3(x):
    return 400-x[2]
def constraint4(x):
    return x[0]-CT(x[1],x[2])
def constraint5(x):
    return x[1]-DC(x[2])
# bondary constraint
b = (0.0, None)
bnds = (b, b, b) 

con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'ineq', 'fun': constraint2}
con3 = {'type': 'ineq', 'fun': constraint3}
con4 = {'type': 'eq', 'fun': constraint4}
con5 = {'type': 'eq', 'fun': constraint5}
cons = ([con1, con2,con3,con4,con5]) 
x0 = np.asarray((24,200,100))
# 计算
res = minimize(objective, x0, method='SLSQP',bounds=bnds,constraints=cons)
print(abs(res.fun))
print(res.success)
print(res.x)
