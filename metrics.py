import pandas as pd


metrics = pd.read_csv('metrics.csv')

wer = metrics['wer'].mean()
cer = metrics['cer'].mean()

ke_all = metrics['ke_all'].mean()
ke_fix = metrics['ke_fix'].mean()
ke_sac = metrics['ke_sac'].mean()
ke_pso = metrics['ke_pso'].mean()

ks_all = metrics['ks_all'].mean()
ks_fix = metrics['ks_fix'].mean()
ks_sac = metrics['ks_sac'].mean()
ks_pso = metrics['ks_pso'].mean()

print ("WER: %f" % wer)
print ("CER: %f" % cer)
print ("KE_all: %f" % ke_all)
print ("KE_fix: %f" % ke_fix)
print ("KE_sac: %f" % ke_sac)
print ("KE_pso: %f" % ke_pso)
print ("KS_all: %f" % ks_all)
print ("KS_fix: %f" % ks_fix)
print ("KS_sac: %f" % ks_sac)
print ("KS_pso: %f" % ks_pso)

with open('metrics_combined.csv', 'w') as f:
    f.write('%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n' % (wer, cer,
                                                    ke_all, ke_fix, ke_sac, ke_pso,
                                                    ks_all, ks_fix, ks_sac, ks_pso))
