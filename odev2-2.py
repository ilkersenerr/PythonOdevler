class WebPush:
    opt_in: bool
    def __init__(self, platform, opt_in, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform = platform
        self.opt_in = opt_in
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type
    def send_push(self):
        return "Push gonderildi "
class TriggerPush(WebPush):
    trigger_page: str
    def __init__(self, trigger_page, platform, opt_in, global_frequency_capping, start_date, end_date, language, push_type):
        self.trigger_page = trigger_page
        super().__init__(platform, opt_in, global_frequency_capping, start_date, end_date, language, push_type)
class BulkPush(WebPush):
    send_date: int
    def __init__(self, send_date, platform, opt_in, global_frequency_capping, start_date, end_date, language, push_type):
        self.send_date = send_date
        super().__init__(platform, opt_in, global_frequency_capping, start_date, end_date, language, push_type)
class SegmentPush(WebPush):
    segment_name: str
    def __init__(self, segment_name, platform, opt_in, global_frequency_capping, start_date, end_date, language, push_type):
        self.segment_name = segment_name
        super().__init__(platform, opt_in, global_frequency_capping, start_date, end_date, language, push_type)
class PriceAlertPush(WebPush):
    price_info: int
    discount_rate: float
    def __init__(self, price_info, discount_rate, platform, opt_in, global_frequency_capping, start_date, end_date, language, push_type):
        self.price_info = price_info
        self.discount_rate = discount_rate
        super().__init__(platform, opt_in, global_frequency_capping, start_date, end_date, language, push_type)
    def discount_price(self):
        return self.price_info - (self.price_info * self.discount_rate)
class InstockPush(WebPush):
    stock_info: bool
    def __init__(self, stock_info, platform, opt_in, global_frequency_capping, start_date, end_date, language, push_type):
        self.stock_info = stock_info
        super().__init__(platform, opt_in, global_frequency_capping,start_date, end_date, language, push_type)
    def stock_update(self):
        if self.stock_info:
            return False
        else:
            return True
new_trigger_push = TriggerPush(
    'Product Page', 'Mobile', False, 3, '01.01.2020', '01.02.2020', 'TR', 'Trigger')
new_bulk_push = BulkPush('01.02.2020', 'Mobile', False,
                         3, '01.01.2020', '01.02.2020', 'TR', 'Bulk')
new_segment_push = SegmentPush(
    'TestSegment', 'Mobile', False, 3, '01.01.2020', '01.02.2020', 'TR', 'Segment')
new_PriceAlertPush = PriceAlertPush(
    250, 0.5, 'TestSegment', 'Mobile', False, 3, '01.01.2020', '01.02.2020', 'TR')
new_InstockPush = InstockPush(
    False, 'TestSegment', 'Mobile', False, 3, '01.01.2020', '01.02.2020', 'TR')
print(new_trigger_push.send_push())
print(new_bulk_push.send_push())
print(new_segment_push.send_push())
print(new_PriceAlertPush.discount_price())
print(new_InstockPush.stock_update())