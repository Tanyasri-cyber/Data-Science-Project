{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6e46f277-838f-426f-88af-89a18ae12566",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hai\n"
     ]
    }
   ],
   "source": [
    "print(\"Hai\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "547008d0-57ab-4866-88c8-b9834d6c75c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dataset Shape: (200, 11)\n",
      "        queue  priority software_used   hardware_used  \\\n",
      "0    Hardware         2           NaN  Wireless Mouse   \n",
      "1    Hardware         2           NaN          IP PBX   \n",
      "2    Hardware         2           NaN    SFX-Netzteil   \n",
      "3  Accounting         2           NaN             NaN   \n",
      "4    Software         2      Arbitrum             NaN   \n",
      "\n",
      "                     accounting_category language  \\\n",
      "0                                    NaN       en   \n",
      "1                                    NaN       fr   \n",
      "2                                    NaN       de   \n",
      "3  Customer Inquiries::Technical Support       en   \n",
      "4                                    NaN       en   \n",
      "\n",
      "                                 subject  \\\n",
      "0  Wireless Mouse suddenly stops working   \n",
      "1          Problème de connexions IP PBX   \n",
      "2        Problem mit meinem SFX-Netzteil   \n",
      "3             Invoice Adjustment Request   \n",
      "4    Issue with Arbitrum: UI not loading   \n",
      "\n",
      "                                                text UserID AssignedStaff  \\\n",
      "0  Dear Support Team, I've been using the Wireles...   U001       Staff_1   \n",
      "1  Bonjour, nous rencontrons un problème avec not...   U002       Staff_2   \n",
      "2  Sehr geehrte Damen und Herren, mein SFX-Netzte...   U003       Staff_3   \n",
      "3  Dear Customer Support,\\nI recently received my...   U004       Staff_4   \n",
      "4  Hello Support Team,\\nI've been experiencing an...   U005       Staff_5   \n",
      "\n",
      "   ResolutionTime  \n",
      "0              91  \n",
      "1             105  \n",
      "2             100  \n",
      "3             103  \n",
      "4             114  \n",
      "MAE: 36.609\n",
      "R2 Score: -0.27850374050422033\n",
      "Processed file saved.\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAk4AAAGGCAYAAACNCg6xAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAPQlJREFUeJzt3XlclWX+//H3AeEgCigimwFS7oOZS9loKbig5JJpLqmJS9akae6lTiPOpKaNpWNNq+G+1GTqZDlaouaY31zSMnMNlxK1VDYXVLh/f/jjTEdAbvHIOcDr+XicR9zXfZ37fM7xKO+u+7qv22IYhiEAAAAUys3ZBQAAAJQUBCcAAACTCE4AAAAmEZwAAABMIjgBAACYRHACAAAwieAEAABgEsEJAADAJIITAACASQQn4A6YN2+eLBaL7VGuXDmFhISoV69eOnTokLPLs9V39OjRW37uyZMnlZCQoN27d+fZl5CQIIvFcvsF3oLc1yzsER0draNHj8pisWjevHnFWuPNREdHKyoqqlhe68KFC3rllVfUsGFDVaxYURUrVlTDhg01ffp0Xbp0qVhqAEq6cs4uACjNEhMTVadOHV2+fFn//e9/NWXKFCUlJWn//v2qXLmys8srkpMnT2ry5MmqXr267rvvPrt9Tz31lNq3b1+s9dz4mikpKeratauGDRum3r1729p9fX0VEhKir7/+Wvfcc0+x1ugKTp8+rTZt2ujIkSMaPny4ZsyYIUnasGGDJk+erOXLl2vdunUKCAhwcqWAayM4AXdQVFSUmjRpIun6yEJ2drYmTZqklStXasCAAU6uzvHuuusu3XXXXU59zdxRtPDwcD344IN5+ufXVhb069dP+/fvV1JSkh566CFbe9u2bdWhQwfFxMRo0KBBWrVqlROrBFwfp+qAYpQbok6fPm3XvmPHDnXu3Fn+/v7y8vJSw4YN9eGHH9r1uXjxosaMGaPIyEh5eXnJ399fTZo00dKlS+36rV69Wn/84x/l7e0tHx8ftW3bVl9//XWhtVWvXl39+/fP0x4dHa3o6GhJ0saNG3X//fdLkgYMGGA7DZaQkCAp/1N1OTk5mjFjhurUqSOr1arAwED169dPP//8c57XiYqK0vbt2/Xwww/L29tbd999t1555RXl5OQUWr8Z+Z2qy635u+++U/fu3eXn5yd/f3+NGjVK165d04EDB9S+fXv5+PioevXqtpGa30tPT7f92Xh6eqpatWoaMWKELly4YLq2r776Sg8++KDKly+vatWq6aWXXlJ2drYkyTAM1axZU+3atcvzvMzMTPn5+Wno0KEFHnvHjh1at26dBg0aZBeacj300EMaOHCgVq9erT179hT4WeX6/Z95rkOHDql3794KDAyU1WpV3bp19eabb9r1KegU8caNG2WxWLRx40a79i+++EKtW7eWr6+vvL291bx5c3355ZcFvk+gOBCcgGKUnJwsSapVq5atLSkpSc2bN1dqaqrefvttrVq1Svfdd5969uxp90tr1KhReuuttzR8+HCtXbtWCxcuVPfu3XX27FlbnyVLlujRRx+Vr6+vli5dqrlz5+r8+fOKjo7Wli1bbrv+Ro0aKTExUZL05z//WV9//bW+/vprPfXUUwU+59lnn9ULL7ygtm3bavXq1frb3/6mtWvXqlmzZvrtt9/s+p46dUp9+vRR3759tXr1asXFxWn8+PFatGjRbddemB49eqhBgwb6+OOPNXjwYL3++usaOXKkunTpog4dOuiTTz5Rq1at9MILL2jFihW25128eFEtW7bU/PnzNXz4cH3++ed64YUXNG/ePHXu3FmGYRT62qdOnVKvXr3Up08frVq1So8//rhefvllPf/885KuB5Vhw4Zp/fr1eebILViwQOnp6TcNTuvXr5ckdenSpcA+ufvWrVtXaL032rdvn+6//37t3btXM2fO1KeffqoOHTpo+PDhmjx58i0fT5IWLVqk2NhY+fr6av78+frwww/l7++vdu3aEZ7gXAYAh0tMTDQkGdu2bTOuXr1qZGRkGGvXrjWCg4ONFi1aGFevXrX1rVOnjtGwYUO7NsMwjI4dOxohISFGdna2YRiGERUVZXTp0qXA18zOzjZCQ0ON+vXr255jGIaRkZFhBAYGGs2aNctTX3Jysq0tIiLCiI+Pz3Pcli1bGi1btrRtb9++3ZBkJCYm5uk7adIk4/f/rPz444+GJGPIkCF2/f7v//7PkGRMmDDB7nUkGf/3f/9n17devXpGu3btCnzfN0pOTjYkGa+++mqB+35fe27NM2fOtOt73333GZKMFStW2NquXr1qVK1a1ejatautbdq0aYabm5uxfft2u+f/61//MiQZn3322U3rzX3fq1atsmsfPHiw4ebmZhw7dswwDMNIT083fHx8jOeff96uX7169YyYmJibvsaf/vQnQ5Kxf//+Avvk/lkNHTrUMIz8P6tckoxJkybZttu1a2fcddddRlpaml2/5557zvDy8jLOnTtnGEb+3zvDMIykpCRDkpGUlGQYhmFcuHDB8Pf3Nzp16mTXLzs722jQoIHxwAMP3PT9AncSI07AHfTggw/Kw8NDPj4+at++vSpXrqxVq1apXLnr0wsPHz6s/fv3q0+fPpKka9eu2R6PPPKIUlJSdODAAUnSAw88oM8//1wvvviiNm7cmOcqqAMHDujkyZN68skn5eb2v7/aFStWVLdu3bRt2zZdvHixmN75dUlJSZKU5xTgAw88oLp16+YZOQgODtYDDzxg13bvvffq2LFjd7ROSerYsaPddt26dWWxWBQXF2drK1eunGrUqGFXz6effqqoqCjdd999dn9+7dq1y/f0U358fHzUuXNnu7bevXsrJydHmzdvtvUZMGCA5s2bZzsFuGHDBu3bt0/PPfdcUd+2jfH/R8Zu9arIy5cv68svv9Rjjz0mb2/vPN/hy5cva9u2bbd0zK1bt+rcuXOKj4+3O15OTo7at2+v7du339JpUMCRCE7AHbRgwQJt375dGzZs0DPPPKMff/xRTzzxhG1/7lynMWPGyMPDw+4xZMgQSbKdzvrHP/6hF154QStXrlRMTIz8/f3VpUsX26mb3FN2ISEheeoIDQ1VTk6Ozp8/f0ff740Kq+n3pxklqUqVKnn6Wa3WYrlU3t/f327b09NT3t7e8vLyytN++fJl2/bp06f13Xff5fnz8/HxkWEYeU5H5icoKChPW3BwsCTZfUbDhg1TRkaGFi9eLEl64403dNddd+nRRx+96fHDw8Ml/e9UcX5y5x2FhYUVWu/vnT17VteuXdOcOXPyfAaPPPKIJJn6DH4v9+/F448/nueY06dPl2EYOnfu3C0dE3AUrqoD7qC6devaJoTHxMQoOztb77//vv71r3/p8ccft136PX78eHXt2jXfY9SuXVuSVKFCBU2ePFmTJ0/W6dOnbaNPnTp10v79+22hIyUlJc8xTp48KTc3t5sugeDl5aWsrKw87b/99luRL1H/fU03Xm138uTJUnHpe0BAgMqXL68PPvigwP2FufFiAen6vCfJPkzWqFFDcXFxevPNNxUXF6fVq1dr8uTJcnd3v+nxY2NjNWHCBK1cubLA5SJWrlwpSWrVqpUk2QLjjd+JG8Nu5cqV5e7urieffLLAeVaRkZE3PeaNwSr3M5szZ06BV0HmFzaB4kBwAorRjBkz9PHHH+svf/mLunbtqtq1a6tmzZras2ePpk6davo4QUFB6t+/v/bs2aNZs2bp4sWLql27tqpVq6YlS5ZozJgxtlMuFy5c0Mcff2y70q4g1atX13fffWfXdvDgQR04cMDul7/VapUkU6NAub+EFy1aZLsaT5K2b9+uH3/8URMnTjT9nl1Vx44dNXXqVFWpUsUWEG5VRkaGVq9ebXe6bsmSJXJzc1OLFi3s+j7//POKjY1VfHy83N3dNXjw4EKP37hxY7Vr105z587Vk08+qebNm9vt37Jliz744AM1b97cFvSDgoLk5eWV5ztx43IF3t7eiomJ0bfffqt7771Xnp6eBdZRvXp1SdJ3331n+x8C6fqVoL/XvHlzVapUyWGnIQFHIjgBxahy5coaP368xo0bpyVLlqhv37565513FBcXp3bt2ql///6qVq2azp07px9//FG7du3SRx99JElq2rSpOnbsqHvvvVeVK1fWjz/+qIULF9oFohkzZqhPnz7q2LGjnnnmGWVlZenVV19VamqqXnnllZvW9uSTT6pv374aMmSIunXrpmPHjmnGjBmqWrWqXb977rlH5cuX1+LFi1W3bl1VrFhRoaGhCg0NzXPM2rVr6+mnn9acOXPk5uamuLg4HT16VC+99JLCwsI0cuRIB32yzjNixAh9/PHHatGihUaOHKl7771XOTk5On78uNatW6fRo0eradOmNz1GlSpV9Oyzz+r48eOqVauWPvvsM7333nt69tlnbafZcrVt21b16tVTUlKS+vbtq8DAQFN1zp8/X61bt1ZsbKyGDx+u1q1bS7o+T2r27NkKDg7W8uXLbf0tFov69u2rDz74QPfcc48aNGigb775RkuWLMlz7NmzZ+uhhx7Sww8/rGeffVbVq1dXRkaGDh8+rH//+9/asGGDJOn+++9X7dq1NWbMGF27dk2VK1fWJ598kueKz4oVK2rOnDmKj4/XuXPn9PjjjyswMFC//vqr9uzZo19//VVvvfWWqfcNOJyTJ6cDpVLu1UM3XmllGIZx6dIlIzw83KhZs6Zx7do1wzAMY8+ePUaPHj2MwMBAw8PDwwgODjZatWplvP3227bnvfjii0aTJk2M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J1eMsqpmzZqSrgd5Dw8PSde/t6dPn7b1mTZtmqxWq4YPH65y5fiVXhz4lOEwMTEx+uijj9S9e3edPHlS3bt317333quFCxfq559/1j333OPsEgEbd3d3GYahnJwc9erVSxaLRU8++aRWr16tI0eOaPv27YQmuAQ3NzfbtAiLxWJbRuMvf/mLXn75ZX377beEpmLE5HA43K5duzRq1CglJyerXLly8vDw0NKlS9WwYUNnlwbkkftPoMViUevWrbV7925t3LhR9evXd3JlwP/kznFKSEhQSkqKatasqT//+c/aunWrGjVq5OzyyhQiKhyuUaNGWr16tc6dO6fMzEwFBwcz6RYuy2KxKDs7W2PHjlVSUpJ2795NaILLyZ3X5OHhoffee0++vr7asmULockJGHECUOZlZ2dr3rx5aty4MevjwKXt2LFDDzzwgPbu3at69eo5u5wyieAEABJr4qDEuHDhgu0iBxQ/ghMAAIBJrOMEAABgEsEJAADAJIITAACASQQnAAAAkwhOAAAAJhGcAAAATCI4AQAAmERwAgAAMIngBAAAYBLBCUCJdOHCBfXr108VK1ZUSEiIZs6cqejoaI0YMULS9Zv3rly50u45lSpV0rx582zbv/zyi3r27KnKlSurSpUqevTRR3X06FHb/t8fL1eXLl3Uv39/2/aVK1c0btw4VatWTRUqVFDTpk21ceNGh75XAK6D4ASgRBo7dqySkpL0ySefaN26ddq4caN27txp+vkXL15UTEyMKlasqM2bN2vLli2qWLGi2rdvrytXrpg+zoABA/Tf//5Xy5Yt03fffafu3burffv2OnToUFHeFgAXV87ZBQDArcrMzNTcuXO1YMECtW3bVpI0f/583XXXXaaPsWzZMrm5uen999+33dw3MTFRlSpV0saNGxUbG1voMY4cOaKlS5fq559/VmhoqCRpzJgxWrt2rRITEzV16tQivDsArozgBKDEOXLkiK5cuaI//vGPtjZ/f3/Vrl3b9DF27typw4cPy8fHx6798uXLOnLkiKlj7Nq1S4ZhqFatWnbtWVlZqlKliulaAJQcBCcAJY5hGIX2sVgsefpdvXrV9nNOTo4aN26sxYsX53lu1apVJUlubm6FHsPd3V07d+6Uu7u7Xb+KFSsW/kYAlDgEJwAlTo0aNeTh4aFt27YpPDxcknT+/HkdPHhQLVu2lHQ9/KSkpNiec+jQIV28eNG23ahRIy1fvlyBgYHy9fXN93VuPEZ2drb27t2rmJgYSVLDhg2VnZ2tM2fO6OGHH3b4+wTgepgcDqDEqVixogYNGqSxY8fqyy+/1N69e9W/f3+5uf3vn7RWrVrpjTfe0K5du7Rjxw796U9/koeHh21/nz59FBAQoEcffVRfffWVkpOTtWnTJj3//PP6+eefbcdYs2aN1qxZo/3792vIkCFKTU21HaNWrVrq06eP+vXrpxUrVig5OVnbt2/X9OnT9dlnnxXb5wGg+DDiBKBEevXVV5WZmanOnTvLx8dHo0ePVlpamm3/zJkzNWDAALVo0UKhoaGaPXu23VV33t7e2rx5s1544QV17dpVGRkZqlatmlq3bm0bgRo4cKD27Nmjfv36qVy5cho5cqRttClXYmKiXn75ZY0ePVq//PKLqlSpoj/+8Y965JFHiueDAFCsLIaZyQIAUAJER0frvvvu06xZs5xdCoBSilN1AAAAJhGcAAAATOJUHQAAgEmMOAEAAJhEcAIAADCJ4AQAAGASwQkAAMAkghMAAIBJBCcAAACTCE4AAAAmEZwAAABMIjgBAACY9P8AGppfc0DwynAAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 600x400 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import os\n",
    "os.environ[\"OMP_NUM_THREADS\"] = \"1\"\n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import LabelEncoder, StandardScaler\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "from sklearn.cluster import KMeans\n",
    "from sklearn.metrics import mean_absolute_error, r2_score\n",
    "import joblib\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "def main():\n",
    "    # Load dataset — change path accordingly\n",
    "    df = pd.read_excel(r\"C:\\Users\\GURU GAYATHRI\\OneDrive\\Desktop\\helpdesk_with_user_staff.xlsx\")\n",
    "    print(\"Dataset Shape:\", df.shape)\n",
    "    print(df.head())\n",
    "\n",
    "    # Drop rows without target\n",
    "    df = df.dropna(subset=[\"ResolutionTime\"])\n",
    "\n",
    "    # Encode categorical columns\n",
    "    categorical_cols = [\n",
    "        \"queue\", \"software_used\", \"hardware_used\",\n",
    "        \"accounting_category\", \"language\",\n",
    "        \"UserID\", \"AssignedStaff\"\n",
    "    ]\n",
    "\n",
    "    le_dict = {}\n",
    "    for col in categorical_cols:\n",
    "        le = LabelEncoder()\n",
    "        df[col] = df[col].astype(str)\n",
    "        df[col] = le.fit_transform(df[col])\n",
    "        le_dict[col] = le\n",
    "\n",
    "    # Prepare features and target\n",
    "    X = df.drop(columns=[\"ResolutionTime\", \"subject\", \"text\"], errors=\"ignore\")\n",
    "    y = df[\"ResolutionTime\"]\n",
    "\n",
    "    # Split train / test\n",
    "    X_train, X_test, y_train, y_test = train_test_split(\n",
    "        X, y, test_size=0.2, random_state=42\n",
    "    )\n",
    "\n",
    "    # Train regression model\n",
    "    reg = RandomForestRegressor(n_estimators=100, random_state=42)\n",
    "    reg.fit(X_train, y_train)\n",
    "\n",
    "    # Predict and evaluate\n",
    "    y_pred = reg.predict(X_test)\n",
    "    print(\"MAE:\", mean_absolute_error(y_test, y_pred))\n",
    "    print(\"R2 Score:\", r2_score(y_test, y_pred))\n",
    "\n",
    "    # Save the model\n",
    "    joblib.dump(reg, \"reg_model.pkl\")\n",
    "\n",
    "    # Clustering\n",
    "    scaler = StandardScaler()\n",
    "    X_scaled = scaler.fit_transform(X)\n",
    "    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)\n",
    "    df[\"Cluster\"] = kmeans.fit_predict(X_scaled)\n",
    "\n",
    "    # Optional plot\n",
    "    plt.figure(figsize=(6, 4))\n",
    "    sns.boxplot(x=\"queue\", y=\"ResolutionTime\", data=df)\n",
    "    plt.title(\"Resolution Time by Queue\")\n",
    "    plt.xticks(rotation=45)\n",
    "    plt.tight_layout()\n",
    "    #plt.show()  # You can choose to show or save\n",
    "\n",
    "    # Save processed dataset\n",
    "    df.to_excel(\"helpdesk_processed_with_clusters.xlsx\", index=False)\n",
    "    print(\"Processed file saved.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "c2501685-81b8-4869-999d-7d72bb58e2b8",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
