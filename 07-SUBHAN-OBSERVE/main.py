# (c) 2026 Mohammad Subhan Pasha - SUBHAN
class SubhanObserve:
    def __init__(self): self.logs=[]
    def log(self, p, t, l): self.logs.append((p,t,l,t*0.00003))
    def dashboard(self):
        total=sum(x[3] for x in self.logs)
        avg=sum(x[2] for x in self.logs)//max(1,len(self.logs))
        return {"total_calls": len(self.logs), "total_cost_usd": round(total,4), "avg_latency_ms": avg, "owner": "SUBHAN"}
if __name__ == "__main__":
    o=SubhanObserve(); o.log("Export report",1200,420); print(o.dashboard())
