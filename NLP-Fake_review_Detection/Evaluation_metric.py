#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score,accuracy_score,precision_score,average_precision_score
from sklearn.metrics import roc_curve, roc_auc_score, auc
import pickle
import xlsxwriter


MODELS = ['SVM','LR','MLP']
workbook = xlsxwriter.Workbook("..\\..\\..\\Data\\Results\\YelpNYC\\Classifiers Performance on YelpNYC_zhw.xlsx")			# Change the path according to the file location
worksheet = []
# Reviewer-Centric ......................................................................
for k in range(0,len(MODELS)):
	recall_b = []
	f1_mic_b = []
	f1_mac_b = []
	ap_b = []
	recall_t = []
	f1_mic_t = []
	f1_mac_t = []
	ap_t = []
	models = []
	models1 = []

	for u in range(0,9):
		models.append(pickle.load(open('..\\..\\..\\Data\\Results\\YelpNYC\\Reviewer Behavioral\\'+str(MODELS[k])+'\\Model_'+str(u+1)+'.sav', 'rb')))		# Change the path according to the file location
	for u in range(0,9):
		models1.append(pickle.load(open('..\\..\\..\\Data\\Results\\YelpNYC\\Reviewer Textual\\'+str(MODELS[k])+'\\Model_'+str(u+1)+'.sav', 'rb')))			# Change the path according to the file location

	# Average of results of five-folds across all the balanced instance sets ............
	for m in models:
		ap_b.append(sum(m['test_ap'])/len(m['test_ap']))
		f1_mic_b.append(sum(m['test_f1_micro'])/len(m['test_f1_micro']))
		f1_mac_b.append(sum(m['test_f1_macro'])/len(m['test_f1_macro']))
		recall_b.append(sum(m['test_recall'])/len(m['test_recall']))
	for m in models1:
		ap_t.append(sum(m['test_ap'])/len(m['test_ap']))
		f1_mic_t.append(sum(m['test_f1_micro'])/len(m['test_f1_micro']))
		f1_mac_t.append(sum(m['test_f1_macro'])/len(m['test_f1_macro']))
		recall_t.append(sum(m['test_recall'])/len(m['test_recall']))

	avg_results_behavioral = [sum(ap_b)/float(len(ap_b)),sum(recall_b)/float(len(recall_b)),sum(f1_mac_b)/float(len(f1_mac_b)),sum(f1_mic_b)/float(len(f1_mic_b))]
	avg_results_textual    = [sum(ap_t)/float(len(ap_t)),sum(recall_t)/float(len(recall_t)),sum(f1_mac_t)/float(len(f1_mac_t)),sum(f1_mic_t)/float(len(f1_mic_t))]

	worksheet.append(workbook.add_worksheet(MODELS[k]))
	worksheet[k].write('A1', MODELS[k])
	worksheet[k].write('B1', 'Reviewer-centric Setting')
	worksheet[k].write('B2', 'Behavioral')
	worksheet[k].write('D2', 'Textual')
	worksheet[k].write('A3', 'average precision')
	worksheet[k].write('A4', 'recall')
	worksheet[k].write('A5', 'f1-score (Macro)')
	worksheet[k].write('A6', 'f1-score (Micro)')
	col = 1
	row = 2
	for i in range(0, len(avg_results_behavioral)):
		worksheet[k].write_number(row, col,avg_results_behavioral[i])
		row = row + 1
	col = 3	
	row = 2
	for i in range(0, len(avg_results_textual)):
		worksheet[k].write_number(row, col,avg_results_textual[i])
		row = row + 1
# Review-Centric ........................................................................
for k in range(0,len(MODELS)):
	recall_b = []
	f1_mic_b = []
	f1_mac_b = []
	ap_b = []
	recall_t = []
	f1_mic_t = []
	f1_mac_t = []
	ap_t = []
	models = []
	models1 = []

	for u in range(0,13):
		models.append(pickle.load(open('..\\..\\..\\Data\\Results\\YelpNYC\\Review Behavioral\\'+str(MODELS[k])+'\\Model_'+str(u+1)+'.sav', 'rb')))			# Change the path according to the file location
	for u in range(0,13):
		models1.append(pickle.load(open('..\\..\\..\\Data\\Results\\YelpNYC\\Review Textual\\'+str(MODELS[k])+'\\Model_'+str(u+1)+'.sav', 'rb')))			# Change the path according to the file location

	# Average of results of five-folds across all the balanced instance sets ............
	for m in models:
		ap_b.append(sum(m['test_ap'])/len(m['test_ap']))
		f1_mic_b.append(sum(m['test_f1_micro'])/len(m['test_f1_micro']))
		f1_mac_b.append(sum(m['test_f1_macro'])/len(m['test_f1_macro']))
		recall_b.append(sum(m['test_recall'])/len(m['test_recall']))
	for m in models1:
		ap_t.append(sum(m['test_ap'])/len(m['test_ap']))
		f1_mic_t.append(sum(m['test_f1_micro'])/len(m['test_f1_micro']))
		f1_mac_t.append(sum(m['test_f1_macro'])/len(m['test_f1_macro']))
		recall_t.append(sum(m['test_recall'])/len(m['test_recall']))

	avg_results_behavioral = [sum(ap_b)/float(len(ap_b)),sum(recall_b)/float(len(recall_b)),sum(f1_mac_b)/float(len(f1_mac_b)),sum(f1_mic_b)/float(len(f1_mic_b))]
	avg_results_textual    = [sum(ap_t)/float(len(ap_t)),sum(recall_t)/float(len(recall_t)),sum(f1_mac_t)/float(len(f1_mac_t)),sum(f1_mic_t)/float(len(f1_mic_t))]

	worksheet[k].write('F1', 'Review-centric Setting')
	worksheet[k].write('F2', 'Behavioral')
	worksheet[k].write('H2', 'Textual')
	col = 5
	row = 2
	for i in range(0, len(avg_results_behavioral)):
		worksheet[k].write_number(row, col,avg_results_behavioral[i])
		row = row + 1
	col = 7	
	row = 2
	for i in range(0, len(avg_results_textual)):
		worksheet[k].write_number(row, col,avg_results_textual[i])
		row = row + 1
# Product-Centric ........................................................................
for k in range(0,len(MODELS)):
	recall_b = []
	f1_mic_b = []
	f1_mac_b = []
	ap_b = []
	recall_t = []
	f1_mic_t = []
	f1_mac_t = []
	ap_t = []
	models = []
	models1 = []

	for u in range(0,5):
		models.append(pickle.load(open('..\\..\\..\\Data\\Results\\YelpNYC\\Product Behavioral\\'+str(MODELS[k])+'\\Model_'+str(u+1)+'.sav', 'rb')))		# Change the path according to the file location
	for u in range(0,5):
		models1.append(pickle.load(open('..\\..\\..\\Data\\Results\\YelpNYC\\Product Textual\\'+str(MODELS[k])+'\\Model_'+str(u+1)+'.sav', 'rb')))			# Change the path according to the file location

	# Average of results of five-folds across all the balanced instance sets ............
	for m in models:
		ap_b.append(sum(m['test_ap'])/len(m['test_ap']))
		f1_mic_b.append(sum(m['test_f1_micro'])/len(m['test_f1_micro']))
		f1_mac_b.append(sum(m['test_f1_macro'])/len(m['test_f1_macro']))
		recall_b.append(sum(m['test_recall'])/len(m['test_recall']))
	for m in models1:
		ap_t.append(sum(m['test_ap'])/len(m['test_ap']))
		f1_mic_t.append(sum(m['test_f1_micro'])/len(m['test_f1_micro']))
		f1_mac_t.append(sum(m['test_f1_macro'])/len(m['test_f1_macro']))
		recall_t.append(sum(m['test_recall'])/len(m['test_recall']))

	avg_results_behavioral = [sum(ap_b)/float(len(ap_b)),sum(recall_b)/float(len(recall_b)),sum(f1_mac_b)/float(len(f1_mac_b)),sum(f1_mic_b)/float(len(f1_mic_b))]
	avg_results_textual    = [sum(ap_t)/float(len(ap_t)),sum(recall_t)/float(len(recall_t)),sum(f1_mac_t)/float(len(f1_mac_t)),sum(f1_mic_t)/float(len(f1_mic_t))]

	worksheet[k].write('J1', 'Product-centric Setting')
	worksheet[k].write('J2', 'Behavioral')
	worksheet[k].write('L2', 'Textual')
	col = 9
	row = 2
	for i in range(0, len(avg_results_behavioral)):
		worksheet[k].write_number(row, col,avg_results_behavioral[i])
		row = row + 1
	col = 11	
	row = 2
	for i in range(0, len(avg_results_textual)):
		worksheet[k].write_number(row, col,avg_results_textual[i])
		row = row + 1
workbook.close() 
