# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_counts = Counter()

        for domain in cpdomains:
            dom_data = domain.split(" ")
            hold_temp_dom = dom_data[1].split(".")
            cur_dom = ""
            for i in range(len(hold_temp_dom) - 1, -1, -1):
                comma = ""
                if i < len(hold_temp_dom) - 1:
                    comma = "."
                cur_dom = hold_temp_dom[i] + comma + cur_dom
                domain_counts[cur_dom] += int(dom_data[0])
        result = []
        for domain in domain_counts:
            result.append(str(domain_counts[domain]) + " " + domain)
        return result