from conta import ContaBancaria
c1= ContaBancaria('Rafael', 30000)
c2= ContaBancaria('Bielzot', 100)

c1.depositar(30000)
c2.exibir()

c2.depositar(c1.sacar(10000))
c2.exibir()