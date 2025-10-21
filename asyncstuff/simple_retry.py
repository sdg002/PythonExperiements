"""
We are using tenacity and trying to understand the retry decorator options
We have a simple function which is designed to throw a division by zero error

What did we learn
-----------------

With stop specified
-------------------
@tn.retry(wait=tn.wait_exponential(), stop=tn.stop_after_attempt(5), after=tn.after_log(logging.getLogger(__name__), logging.WARNING))
2025-08-04 07:46:07,678 - INFO - Before sleep
2025-08-04 07:46:08,190 - WARNING - Finished call to '__main__.main' after 0.500(s), this was the 1st time calling it.
2025-08-04 07:46:09,206 - INFO - Before sleep
2025-08-04 07:46:09,723 - WARNING - Finished call to '__main__.main' after 2.032(s), this was the 2nd time calling it.
2025-08-04 07:46:11,738 - INFO - Before sleep
2025-08-04 07:46:12,254 - WARNING - Finished call to '__main__.main' after 4.578(s), this was the 3rd time calling it.
2025-08-04 07:46:16,269 - INFO - Before sleep
2025-08-04 07:46:16,785 - WARNING - Finished call to '__main__.main' after 9.094(s), this was the 4th time calling it.
2025-08-04 07:46:24,798 - INFO - Before sleep
2025-08-04 07:46:25,298 - WARNING - Finished call to '__main__.main' after 17.610(s), this was the 5th time calling it.

Without stop
-------------
@tn.retry(wait=tn.wait_exponential(), after=tn.after_log(logging.getLogger(__name__), logging.WARNING))
Continues for ever

"""
import asyncio
import logging
import sys
import tenacity as tn

#@tn.retry(wait=tn.wait_exponential(multiplier=1, min=4, max=10), stop=tn.stop_after_attempt(5), after=tn.after_log(logging.getLogger(__name__), logging.WARNING))
#@tn.retry(wait=tn.wait_exponential(), after=tn.after_log(logging.getLogger(__name__), logging.WARNING))
@tn.retry(wait=tn.wait_exponential(), stop=tn.stop_after_attempt(5), after=tn.after_log(logging.getLogger(__name__), logging.WARNING))
async def main_with_default_exponential():
    logging.info("Before sleep")
    await asyncio.sleep(delay=0.5)
    logging.info("After sleep")
    x=1/0

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )    
    #you were here, log the time for better comparison
    try:
        asyncio.run(main_with_default_exponential())
        sys.exit(0)
    except Exception as e:
        logging.error(f"Exception occurred: {e}", exc_info=True)
        sys.exit(1)
