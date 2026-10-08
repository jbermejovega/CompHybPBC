from svraftj.pauli import Pauli,typed_attitude

def test_pauli_relations():
    X=Pauli((1,),(0,))
    Z=Pauli((0,),(1,))
    Y=Pauli((1,),(1,),1)
    assert X.hermitian and Z.hermitian and Y.hermitian
    assert not X.commutes(Z)
    assert X.multiply(Z)==Pauli((1,),(1,),0)
    assert Z.multiply(X)==Pauli((1,),(1,),2)
    assert X.multiply(X)==Pauli((0,),(0,),0)
    assert Y.multiply(Y)==Pauli((0,),(0,),0)

def test_relation_witness():
    X=Pauli((1,),(0,))
    Z=Pauli((0,),(1,))
    assert typed_attitude(X,Z,context="G",witness="W")["relation"]=="ANTICOMMUTES"
    assert typed_attitude(X,Z,context="G")["verdict"]=="HOLD_QUNO"

def test_tensor_ports():
    X=Pauli((1,0),(0,0))
    Z=Pauli((0,0),(0,1))
    assert X.commutes(Z)

def test_nonhermitian_guard():
    bad=Pauli((1,),(1,),0)
    assert typed_attitude(bad,bad,context="G")["verdict"]=="REJECT"
