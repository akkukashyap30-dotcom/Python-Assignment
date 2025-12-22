class A:
    value = "Value from class A"


class B(A):
    value = "Value from class B"


class C(B):
    value = "Value from class C"


class MainData:
    @staticmethod
    def main():
        a = A()
        b = B()
        c = C()

        print("---- Direct object access ----")
        print(a.value)
        print(b.value)
        print(c.value)

        print("\n---- Superclass reference ----")
        ref: A

        ref = b
        print(ref.value)  # Accessed from B object

        ref = c
        print(ref.value)  # Accessed from C object


MainData.main()
