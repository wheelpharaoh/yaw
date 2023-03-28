from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

import logger
log = logger.setup_applevel_logger()


def fibonacci(n: int) -> list[int]:
    """
    Return the first `n` Fibonacci numbers.
    pattern: 0, 1, 1, 2, 3, 5, 8, 13...
    formula: Xₙ = Xₙ₋₁ + Xₙ₋₂
        X₀ = 0
        X₁ = 1

    
    Parameters
    ----------
    n: int
        The desired number of terms from the sequence 

    Returns
    -------
    list
        The first `n` terms in fibonacci sequence
    """
    i = 0
    nums = []
    while (i <= n):
        if i <= 0:      # no terms
            pass
        elif i == 1:    # 1 term
            nums.append(0)
        elif i == 2:    # 2 terms
            nums.append(1)
        else:           # n terms
            index_previous_one = ((i-1)-1)
            index_previous_two = ((i-1)-2)
            nums.append(nums[index_previous_one] + nums[index_previous_two])
        i+=1
    return nums


class GetFibs(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urlparse(self.path).query
        params = parse_qs(query)

        if "n" not in params:
            self.send_response(422)
            return
        
        try:
            key = int(params["n"][0])
        except (IndexError, ValueError):
            self.send_response(422)

        log.debug('n={}'.format(key))

        nums = fibonacci(key)

        # convert nums from int to string list
        str_nums = [str(n) for n in nums]
        final_nums = ", ".join(str_nums)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(final_nums, "UTF-8"))
        return


if __name__ == "__main__":
    from http.server import HTTPServer

    httpd = HTTPServer(("", 8000), GetFibs)
    httpd.serve_forever()
