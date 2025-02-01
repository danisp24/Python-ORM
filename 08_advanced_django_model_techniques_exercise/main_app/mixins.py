from django.db import models


class RechargeEnergyMixin(models.Model):

    def recharge_energy(self, amount: int):

        self.energy += amount
        if self.energy > 100:
            self.energy = 100

        self.save()
