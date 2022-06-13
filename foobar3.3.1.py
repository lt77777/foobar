from fractions import Fraction

def convert_prob(m):        
    for r in range(len(m)):
        total = 0
        for c in range(len(m[r])):
            total += m[r][c]
        if total != 0:
            for c1 in range(len(m[r])):
                m[r][c1] /= float(total)
    return m
def RQ(m, term_state, non_term_state):
    R = []
    Q = []
    for i in non_term_state:
        temp1 = []
        temp2 = []
        for j in term_state:
            temp1.append(m[i][j])
        for j in non_term_state:
            temp2.append(m[i][j])
        R.append(temp1)
        Q.append(temp2)
    return R, Q
def identity_minus_Q(Q):
    n = len(Q)
    for r in range(len(Q)):
        for c in range(len(Q[r])):
            if r == c:
                Q[r][c] = 1 - Q[r][c]
            else:
                Q[r][c] = -1 * Q[r][c]
    return Q
def get_minor(m,i,j):
    minor = []
    for row in m[:i] + m[i+1:]:
        temp = []
        for element in row[:j] + row[j+1:]:
            temp.append(element)
        minor.append(temp)
    return minor
def get_det(m):
    if len(m) == 1:
        return m[0][0]
    if len(m) == 2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]
    det = 0
    for first_element in range(len(m[0])):
        minor_matrix = get_minor(m, 0, first_element)
        det += (((-1)**first_element)*m[0][first_element] * get_det(minor_matrix))
    return det
def transpose(m):
    for i in range(len(m)):
        for j in range(i, len(m)):
            m[i][j] = m[j][i]
            m[j][i] = m[i][j]
    return m
def get_inverse(m):
    m1 = []
    for r in range(len(m)):
        temp = []
        for c in range(len(m[r])):
            minor_matrix = get_minor(m, r, c)
            det = get_det(minor_matrix)
            temp.append(((-1)**(r+c))*det)
        m1.append(temp)
    det1 = get_det(m)
    Q1 = transpose(m1)
    for i in range(len(m)):
        for j in range(len(m[i])):
            Q1[i][j] /= float(det1)
    return Q1
def multiply_matrix(m, n):
    rtn = []
    dim = len(m)
    for r in range(len(m)):
        temp = []
        for c in range(len(n[0])):
            prod = 0
            for curr in range(dim):
                prod += (m[r][curr]*n[curr][c])
            temp.append(prod)
        rtn.append(temp)
    return rtn
def gcd(a ,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)   
def reduce(m):
    temp = m[0]
    rtn = [Fraction(i).limit_denominator() for i in temp]
    lcm = 1
    for i in rtn:
        if i.denominator != 1:
            lcm = i.denominator
    for j in rtn:
        if j.denominator != 1:
            lcm = lcm*j.denominator/gcd(lcm, j.denominator)
    rtn = [(k*lcm).numerator for k in rtn]
    rtn.append(lcm)
    return rtn
def solution(m):
    # Use linear algebra formulation of absorbing Markov Chains
    n = len(m)
    if n==1:
        if len(m[0]) == 1 and m[0][0] == 0:
            return [1, 1]
    term_state = []
    non_term_state = []
    for r in range(len(m)):
        temp = 0
        for c in range(len(m[r])):
            if m[r][c] == 0:
                temp += 1
        if temp == n:
            term_state.append(r)
        else:
            non_term_state.append(r)
    prob = convert_prob(m)
    R, Q = RQ(prob, term_state, non_term_state)
    Q1 = identity_minus_Q(Q)
    fundamental_m = get_inverse(Q1)
    final_prob = multiply_matrix(fundamental_m, R)
    return reduce(final_prob)