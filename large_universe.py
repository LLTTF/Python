{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "28110e59-6d87-4967-894a-245f0d0e50d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "weight=int(input(\"Enter your weight(in kg)\"))\n",
    "weight_g=weight*1000\n",
    "o_mass=65*(weight_g)/100\n",
    "c_mass=18*(weight_g)/100\n",
    "h_mass=10*(weight_g)/100\n",
    "n_mass=3*(weight_g)/100\n",
    "c_mass=1.5*(weight_g)/100\n",
    "p_mass=weight_g/100\n",
    "others_mass=1.5*(weight_g)/100\n",
    "o_a=o_mass/16\n",
    "c_a=c_mass/12\n",
    "h_a=h_mass/1\n",
    "n_a=n_mass/14\n",
    "total=o_a+c_a+h_a+n_a\n",
    "print(f\"You are made up of {total} number of atoms(approximately)\")\n",
    "percentage=weight/1e53\n",
    "print(f\"You form {percentage} percentage of the universe(approximately)\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
