"""
boxplots, violinplots and lvplots
Seaborn's categorical plots also support several abstract representations of data. The API for each of these is the same so it is very convenient to try each plot and see if the data lends itself to one over the other.

In this exercise, we will use the color palette options presented in Chapter 2 to show how colors can easily be included in the plots.

Instructions 1/3
30 XP
1
2
3
Create and display a boxplot of the data with Award_Amount on the x axis and Model Selected on the y axis.
"""
# Create a boxplot
sns.boxplot(data=df,
            x='Award_Amount',
            y='Model Selected')

plt.show()
plt.clf()

"""Create and display a similar violinplot of the data, but use the husl palette for colors."""
# Create a violinplot with the husl palette
sns.violinplot(data=df,
               x='Award_Amount',
               y='Model Selected',
               palette='husl')

plt.show()
plt.clf()

"""Create and display an lvplot using the Paired palette and the Region column as the hue."""
# Create a lvplot with the Paired palette and the Region column as the hue
sns.lvplot(data=df,
           x='Award_Amount',
           y='Model Selected',
           palette='Paired',
           hue='Region')

plt.show()
plt.clf()


                    """DEVELOPER"""
                """BasitAminBhatti"""
                    """Github""""
        """https://github.com/basitaminbhatti"""