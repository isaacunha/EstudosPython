{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "classificacao.py",
      "provenance": [],
      "toc_visible": true,
      "mount_file_id": "1Tjouj20fSa2s7Bx_-li-lZvBUCRKEa6b",
      "authorship_tag": "ABX9TyNfyxcLXiATLIQ79zj9fQ25",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/isaacunha/EstudosPython/blob/main/classificacao.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "# Pré Processamento"
      ],
      "metadata": {
        "id": "jgMKauRZrRsZ"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "vs26JRR2pSyi"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import numpy as np"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv('/content/drive/MyDrive/MLwithPython/heart_tratado.csv',\n",
        "                 sep=';', encoding = 'utf-8')"
      ],
      "metadata": {
        "id": "BHw3xNjjqiMc"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "uW7-Ry-MrJ4Z",
        "outputId": "507d2d7e-23fe-4dd7-df74-14de5c2c7b56"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Age Sex ChestPainType  RestingBP  Cholesterol  FastingBS RestingECG  MaxHR  \\\n",
              "0   40   M           ATA        140        289.0          0     Normal    172   \n",
              "1   49   F           NAP        160        180.0          0     Normal    156   \n",
              "2   37   M           ATA        130        283.0          0         ST     98   \n",
              "3   48   F           ASY        138        214.0          0     Normal    108   \n",
              "4   54   M           NAP        150        195.0          0     Normal    122   \n",
              "\n",
              "  ExerciseAngina  Oldpeak ST_Slope  HeartDisease  \n",
              "0              N      0.0       Up             0  \n",
              "1              N      1.0     Flat             1  \n",
              "2              N      0.0       Up             0  \n",
              "3              Y      1.5     Flat             1  \n",
              "4              N      0.0       Up             0  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-45482d52-5a2a-46eb-9ba4-c8745a7cdb72\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Age</th>\n",
              "      <th>Sex</th>\n",
              "      <th>ChestPainType</th>\n",
              "      <th>RestingBP</th>\n",
              "      <th>Cholesterol</th>\n",
              "      <th>FastingBS</th>\n",
              "      <th>RestingECG</th>\n",
              "      <th>MaxHR</th>\n",
              "      <th>ExerciseAngina</th>\n",
              "      <th>Oldpeak</th>\n",
              "      <th>ST_Slope</th>\n",
              "      <th>HeartDisease</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>40</td>\n",
              "      <td>M</td>\n",
              "      <td>ATA</td>\n",
              "      <td>140</td>\n",
              "      <td>289.0</td>\n",
              "      <td>0</td>\n",
              "      <td>Normal</td>\n",
              "      <td>172</td>\n",
              "      <td>N</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Up</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>49</td>\n",
              "      <td>F</td>\n",
              "      <td>NAP</td>\n",
              "      <td>160</td>\n",
              "      <td>180.0</td>\n",
              "      <td>0</td>\n",
              "      <td>Normal</td>\n",
              "      <td>156</td>\n",
              "      <td>N</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Flat</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>37</td>\n",
              "      <td>M</td>\n",
              "      <td>ATA</td>\n",
              "      <td>130</td>\n",
              "      <td>283.0</td>\n",
              "      <td>0</td>\n",
              "      <td>ST</td>\n",
              "      <td>98</td>\n",
              "      <td>N</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Up</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>48</td>\n",
              "      <td>F</td>\n",
              "      <td>ASY</td>\n",
              "      <td>138</td>\n",
              "      <td>214.0</td>\n",
              "      <td>0</td>\n",
              "      <td>Normal</td>\n",
              "      <td>108</td>\n",
              "      <td>Y</td>\n",
              "      <td>1.5</td>\n",
              "      <td>Flat</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>54</td>\n",
              "      <td>M</td>\n",
              "      <td>NAP</td>\n",
              "      <td>150</td>\n",
              "      <td>195.0</td>\n",
              "      <td>0</td>\n",
              "      <td>Normal</td>\n",
              "      <td>122</td>\n",
              "      <td>N</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Up</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-45482d52-5a2a-46eb-9ba4-c8745a7cdb72')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-45482d52-5a2a-46eb-9ba4-c8745a7cdb72 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-45482d52-5a2a-46eb-9ba4-c8745a7cdb72');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NRPNTyE1rNtK",
        "outputId": "a68c3d1c-2429-48cc-ed8a-e590bd69c709"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(917, 12)"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Transformando as variáveis categóricas nominais em variáveis categóricas ordinais"
      ],
      "metadata": {
        "id": "wBNzpM9yrY3E"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "substituir variaveis que tem letras por numero (FM-> 01)"
      ],
      "metadata": {
        "id": "d4eCJH-7rlV4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df2 = pd.DataFrame.copy(df)"
      ],
      "metadata": {
        "id": "nx1_rlC5rjyL"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df2['Sex'].replace({'M':0, 'F':1}, inplace = True)\n",
        "df2['ChestPainType'].replace({'TA':0, 'ATA': 1, 'NAP':2, 'ASY': 3}, inplace=True)\n",
        "df2['RestingECG'].replace({'Normal':0, 'ST': 1, 'LVH':2}, inplace=True)\n",
        "df2['ExerciseAngina'].replace({'N':0, 'Y': 1}, inplace=True)\n",
        "df2['ST_Slope'].replace({'Up':0, 'Flat': 1, 'Down':2}, inplace=True)"
      ],
      "metadata": {
        "id": "V3TAObE2rzsB"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df2.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "vCowJM-1sOW3",
        "outputId": "30e2922c-ca89-4502-eb07-59e41683579b"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Age  Sex  ChestPainType  RestingBP  Cholesterol  FastingBS  RestingECG  \\\n",
              "0   40    0              1        140        289.0          0           0   \n",
              "1   49    1              2        160        180.0          0           0   \n",
              "2   37    0              1        130        283.0          0           1   \n",
              "3   48    1              3        138        214.0          0           0   \n",
              "4   54    0              2        150        195.0          0           0   \n",
              "\n",
              "   MaxHR  ExerciseAngina  Oldpeak  ST_Slope  HeartDisease  \n",
              "0    172               0      0.0         0             0  \n",
              "1    156               0      1.0         1             1  \n",
              "2     98               0      0.0         0             0  \n",
              "3    108               1      1.5         1             1  \n",
              "4    122               0      0.0         0             0  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-ddfba256-30b5-4706-b19c-2fbed8d6d1b8\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Age</th>\n",
              "      <th>Sex</th>\n",
              "      <th>ChestPainType</th>\n",
              "      <th>RestingBP</th>\n",
              "      <th>Cholesterol</th>\n",
              "      <th>FastingBS</th>\n",
              "      <th>RestingECG</th>\n",
              "      <th>MaxHR</th>\n",
              "      <th>ExerciseAngina</th>\n",
              "      <th>Oldpeak</th>\n",
              "      <th>ST_Slope</th>\n",
              "      <th>HeartDisease</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>40</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>140</td>\n",
              "      <td>289.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>172</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>49</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>160</td>\n",
              "      <td>180.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>156</td>\n",
              "      <td>0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>37</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>130</td>\n",
              "      <td>283.0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>98</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>48</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>138</td>\n",
              "      <td>214.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>108</td>\n",
              "      <td>1</td>\n",
              "      <td>1.5</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>54</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>150</td>\n",
              "      <td>195.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>122</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-ddfba256-30b5-4706-b19c-2fbed8d6d1b8')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-ddfba256-30b5-4706-b19c-2fbed8d6d1b8 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-ddfba256-30b5-4706-b19c-2fbed8d6d1b8');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    }
  ]
}