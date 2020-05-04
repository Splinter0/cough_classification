#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:45:50 2020

@author: kthiruko
"""

from pydub import AudioSegment

def check_audio(file_path, threshold = -100):
    """
    Given a audio file, the function will say if the audio file is empty or not.
    Supports WAV

    Parameters
    ----------
    file_path : str()
        Path of the audio file to be tested.

    Returns
    -------
    0 :if the file is empty
    1 : if the file is not empty

    """
    
    
    sound = AudioSegment.from_file(file_path)
    
    loudness = sound.dBFS
    
    if loudness=="inf" or loudness < threshold:
        
        return 0
        
    else:
        return 1
    