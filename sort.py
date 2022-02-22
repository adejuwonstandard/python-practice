{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from random import randint\n",
    "from timeit import repeat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def bubble_sort(array):\n",
    "    n=len(array)\n",
    "    \n",
    "    for i in range(n):\n",
    "        #create a flag that will allow the function to \n",
    "        #terminate early if there is nothing left to sort\n",
    "        already_sorted= True\n",
    "        \n",
    "        #start looking at each item of the list one by one, \n",
    "        #comparing it with its adjacent value. With each \n",
    "        #iteration, the portion of the array that you look at \n",
    "        #shrinks because the remaining items have already been sorted.\n",
    "        for j in range(n - i - 1):\n",
    "            if array[j] > array[j + 1]:\n",
    "                #if the item you are looking at is greater that its\n",
    "                #adjacent value, then swap them\n",
    "                array[j], array[j + 1]=array[j + 1], array[j]\n",
    "                \n",
    "                #since you had to swap two elements, set the already_sorted flag\n",
    "                # to False so the algorithm doesn't finish prematuredly\n",
    "                already_sorted=False\n",
    "        #if there were no swaps during the last iteration, the array is already\n",
    "        # sorted and you can terminate\n",
    "        if already_sorted:\n",
    "            break\n",
    "    return array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def run_sorting_algorithm(algorithm, array):\n",
    "    #set up the context and prepare the call to the specified \n",
    "    #algorithm using the supplied array. Only import the \n",
    "    #algorithm function if it is not the built-in.\n",
    "    setup_code = f\"from__main__import {algorithm}\"\\\n",
    "        if algorithm !=\"sorted\" else \"\"\n",
    "    stmt = f\"{algorithm}({array})\"\n",
    "    #execute the code ten different times and return the time in seconds that each execution took\n",
    "    times=repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)\n",
    "    \n",
    "    #finally, display the name of the algorithm and the minimum time it took to run\n",
    "    print(f\"Algorithm: {algorithm}. Minimum execution time: {min(times)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "def quicksort(array):\n",
    "    if len(array)<2:\n",
    "        return array\n",
    "    \n",
    "    low, same, high = [], [], []\n",
    "    \n",
    "    #select pivot element randomly\n",
    "    pivot=array[randit(0, len(array)-1)]\n",
    "    \n",
    "    for items in array:\n",
    "        if item <pivot:\n",
    "            low.append(item)\n",
    "        elif item ==pivot:\n",
    "            same.append(item)\n",
    "        elif item>pivot:\n",
    "            high.append(item)\n",
    "            \n",
    "    return quicksort(low) + same +quicksort(high)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "def insertion_sort(array, left=0, right=None):\n",
    "    if right is None:\n",
    "        right=len(array)-1\n",
    "    for i in range(left + 1, right+1):\n",
    "    \n",
    "        key_item = array[i]\n",
    "    \n",
    "        j=i -1\n",
    "    \n",
    "        while j>= left and array[j]> key_item:\n",
    "    \n",
    "            array[j+1]=array[j]\n",
    "            j-=1\n",
    "    \n",
    "        array[j + 1] = key_item\n",
    "    return array\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "def timsort(array):\n",
    "    min_run=32\n",
    "    n=len(array)\n",
    "    #start by slicing and sorting small portion of the input array. \n",
    "    #The size of these slices is defined by your min_run size.\n",
    "    for i in range(0, n, min_run):\n",
    "        insertion_sort(array, i, min((i+min_run-1), n-1))\n",
    "        \n",
    "    #Now you can start merging the sorted slices\n",
    "    #Start from min_run, doubling the size on each iteration\n",
    "    #until you surpass the length of the array.\n",
    "    size=min_run\n",
    "    while size<n:\n",
    "        #determine the arrays that will be merged together\n",
    "        for start in range(0, n, size*2):\n",
    "            #compute the midpoint (where the first array ends\n",
    "            #and the second starts) and the 'endpoint' (where\n",
    "            #the second array ends)\n",
    "            midpoint=start+size-1\n",
    "            end= min((start + size *2 - 1), (n-1))\n",
    "            #merge the two subarrays\n",
    "            #the left array should go from start to midpoint + 1\n",
    "            #while the right array should go from midpoint + 1 to end+1\n",
    "            \n",
    "            merged_array=merge(left=array[start:midpoint + 1], right=array[midpoint + 1:end +1])\n",
    "            \n",
    "            #finally, put the merged array back into your array\n",
    "            \n",
    "            array[start:start + len(merged_array)] = merged_array\n",
    "            \n",
    "            #each iteration should double the size of your arrays\n",
    "            size*=2\n",
    "    return array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ARRAY_LENGTH= 10000\n",
    "if __name__==\"__main__\":\n",
    "    #generate an array of 'ARRAY_LENGTH' items consisting of random integers values between 0 and\n",
    "    #999\n",
    "    array=[randint(0,1000) for i in range(ARRAY_LENGTH)]\n",
    "    \n",
    "    #CALL THE FUNCTION USING THE NAME OF THE SORTING ALGORITHM AND THE ARRAY YOU JUST CREATED\n",
    "    run_sorting_algorithm(algorithm=\"bubble_sort\", array=array)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
