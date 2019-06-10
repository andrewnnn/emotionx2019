from pathlib import Path

def get_project_root() -> Path:
    """Returns project root folder."""
    return Path(__file__)

def myscorer(y_test, y_pred):
    # micro average (precision, recall, f1) of anger, joy, sadness
    classes_names = ["anger", "joy", "neutral", "sadness"]
    
    angersum = len([ x for x in y_pred if x == "anger"])
    joysum = len([ x for x in y_pred if x == "joy"])
    sadsum = len([ x for x in y_pred if x == "sadness"])
    
    angertot = len([ x for x in y_test if x == "anger"])
    joytot = len([ x for x in y_test if x == "joy"])
    sadtot = len([ x for x in y_test if x == "sadness"])

    prec = precision_score(y_test, y_pred, average=None)
    recall = recall_score(y_test, y_pred, average=None)
    f1 = f1_score(y_test, y_pred, average=None)
    
    print("Anger\t\t -> # pred: {}/{},\t prec: {:.3f}, recall: {:.3f}, f1: {:.3f}".format(
        angersum, angertot, prec[0], recall[0], f1[0]))
    print("Joy\t\t -> # pred: {}/{},\t prec: {:.3f}, recall: {:.3f}, f1: {:.3f}".format(
        joysum, joytot, prec[1], recall[1], f1[1]))
    print("Sadness\t\t -> # pred: {}/{},\t prec: {:.3f}, recall: {:.3f}, f1: {:.3f}".format(
        sadsum, sadtot, prec[3], recall[3], f1[3])) 
    print("Micro\t\t -> # pred: {}/{},\t prec: {:.3f}, recall: {:.3f}, f1: {:.3f}".format(
        angersum+joysum+sadsum, angertot+joytot+sadtot, (prec[0]+prec[1]+prec[3])/3, 
        (recall[0]+recall[1]+recall[3])/3,
        (f1[0]+f1[1]+f1[3])/3 ))