import scrapy
import requests

class EvdSpiderSpider(scrapy.Spider):
    name = "evd_spider"
    allowed_domains = ["ev-database.org", 'proxy.scrapeops.io']
    start_urls = ["https://ev-database.org/compare/second-hand-used-electric-vehicle-archive#sort:path~type~order=.date_from~number~asc|rs-price:prev~next=10000~100000|rs-range:prev~next=0~1000|rs-fastcharge:prev~next=0~1500|rs-acceleration:prev~next=2~23|rs-topspeed:prev~next=110~350|rs-battery:prev~next=10~200|rs-towweight:prev~next=0~2500|rs-eff:prev~next=100~350|rs-safety:prev~next=-1~5|paging:currentPage=0|paging:number=10"]


    def parse(self, response):
        vehicles = response.css('div.list-item')
        base_url = "https://ev-database.org"  # Base URL

        for vehicle in vehicles:
            # Skip the advertisement blocks
            if vehicle.css('ins.adsbygoogle'):
                continue

            name_parts = vehicle.css('h2 a.title span::text').getall()
            name = ' '.join(part.strip() for part in name_parts)
            link = vehicle.css('h2 a.title::attr(href)').get()
            available_since = vehicle.css('div.current::text').get(default='').strip()
            battery = vehicle.css('span.battery::text').get(default='').strip() + " kWh"
            price_per_km = vehicle.css('span.price-range::text').get(default='').strip() + " /km of range"
            acceleration = vehicle.css('span.acceleration::text').get(default='').strip()
            top_speed = vehicle.css('span.topspeed::text').get(default='').strip() + " km/h"
            range_real = vehicle.css('span.erange_real::text').get(default='').strip() + " km"
            efficiency = vehicle.css('span.efficiency::text').get(default='').strip() + " Wh/km"
            fastcharge_speed = vehicle.css('span.fastcharge_speed_print::text').get(default='').strip() + " km/h"

            prices = vehicle.css('div.price_buy span')
            price_germany = prices.css('span.country_de::text').get(default='').strip()
            price_netherlands = prices.css('span.country_nl::text').get(default='').strip()
            price_uk = prices.css('span.country_uk::text').get(default='').strip()

            vehicle_data = {
                'Name': name,
                'Link': base_url + link if link else '',
                'Available_Since': available_since,
                'Battery': battery,
                'Price_Per_km': price_per_km,
                'Acceleration': acceleration,
                'Top_Speed': top_speed,
                'Range_Real': range_real,
                'Efficiency': efficiency,
                'Fastcharge_Speed': fastcharge_speed,
                'Price_Germany': price_germany,
                'Price_Netherlands': price_netherlands,
                'Price_UK': price_uk,
            }

            #Follow the link to the detailed page
            full_link = base_url + link
            request = scrapy.Request(full_link, callback=self.parse_vehicle_details)
            request.meta['vehicle_data'] = vehicle_data
            yield request


        # Follow the "Next" button link if it exists
        next_page = response.css('div.jplist-pagingnext button.jplist-next::attr(data-number)').get()
        if next_page:
            next_page_url = response.urljoin(f'?paging:currentPage={next_page}')
            yield response.follow(next_page_url, self.parse)

    def parse_vehicle_details(self, response):
        vehicle_data = response.meta['vehicle_data']

        vehicle_data.update({
            "City - Cold Weather":response.css('div.inline-block table tr:contains("City - Cold Weather") td:nth-child(2)::text').get().strip(),
            "Highway - Cold Weather":response.css('div.inline-block table tr:contains("Highway - Cold Weather") td:nth-child(2)::text').get().strip(),
            "Combined - Cold Weather":response.css('div.inline-block table tr:contains("Combined - Cold Weather") td:nth-child(2)::text').get().strip(),
            "Nominal Capacity": response.css('div.inline-block table tbody tr:nth-child(1) td:nth-child(2)::text').get(),
            "Number of Cells" : response.css('div#battery tr:contains("Number of Cells") td:nth-child(2)::text').get(default='').strip(),
            "Architecture": response.css('div#battery tr:contains("Architecture") td:nth-child(2)::text').get(default='').strip(),
            "Warranty Period": response.xpath('//div[@class="inline-block"]//table//tr[td[contains(text(), "Warranty Period")]]/td[2]/text()').get().strip(),
            "Warranty Mileage":response.xpath('//div[@class="inline-block"]//table//tr[td[contains(text(), "Warranty Mileage")]]/td[2]/text()').get().strip(),
            "Useable Capacity":response.xpath('//div[@class="inline-block"]//table//tr[td[contains(text(), "Useable Capacity")]]/td[2]/text()').get().strip(),
            "Cathode Material":response.css('div#battery tr:contains("Cathode Material") td:nth-child(2)::text').get(default='').strip(),
            "Pack Configuration": response.css('div#battery tr:contains("Pack Configuration") td:nth-child(2)::text').get(default='').strip(),
            "Nominal Voltage":response.css('div#battery tr:contains("Nominal Voltage") td:nth-child(2)::text').get(default='').strip(),
            "Form Factor": response.css('div#battery tr:contains("Form Factor") td:nth-child(2)::text').get(default='').strip(),
            "Name / Reference":response.css('div#battery tr:contains("Name / Reference") td:nth-child(2)::text').get(default='').strip(),
            "Acceleration": response.xpath('//div[@class="inline-block"]//table//tr[td[contains(text(), "Acceleration")]]/td[2]/text()').get().strip(),
            "Total Toeque": response.css('div#performance tr:contains("Total Torque") td:nth-child(2)::text').get(default='').strip(),
            'Total Power':response.css('div.inline-block table tr:contains("Total Power") td:nth-child(2)::text').get().strip(),
            'Drive': response.css('div.inline-block td:contains("Drive") + td::text').get(),
            'Battery Type': response.css('#battery tr:nth-child(2) td:nth-child(2)::text').get(),
            'Nominal Capacity': response.css('#battery tr:nth-child(1) td:nth-child(2)::text').get(),
            'Charge Port': response.css('#charging tr:nth-child(1) td:nth-child(2)::text').get(),
            'Port Location': response.css('#charging tr:nth-child(2) td:nth-child(2)::text').get(),
            "Charge_time" : response.css('div#charging tr:contains("Charge Time") td:nth-child(2)::text').get(default='').strip(),
            'Charge Speed':response.css('div.inline-block td:contains("Charge Speed") + td::text').get(),
            'Gross Vehicle Weight':response.css('div.inline-block table tr:contains("Gross Vehicle Weight") td:nth-child(2)::text').get().strip(),
            'Weight Unladen (EU)':response.css('div#dimensions tr:contains("Weight Unladen (EU)") td:nth-child(2)::text').get(default='').strip(),
            'Wheelbase': response.xpath('//div[@class="inline-block"]//table//tr[td[contains(text(), "Wheelbase")]]/td[2]/text()').get().strip(),
            'Max_Payload':response.xpath('//div[@class="inline-block"]//table//tr[td[contains(text(), "Max. Payload")]]/td[2]/text()').get().strip(),
            "Car Body":response.xpath('//div[@class="inline-block"]//table//tr[td[contains(text(), "Car Body")]]/td[2]/text()').get().strip(),
            "Segment" :response.xpath('//div[@class="inline-block"]//table//tr[td[contains(text(), "Segment")]]/td[2]/text()').get().strip(),
            'Body length':response.css('div.data-table td:contains("Length") + td::text').get(),
            'Body width': response.css('div.data-table td:contains("Width") + td::text').get(),
            'Body Height': response.css('div.data-table td:contains("Height") + td::text').get(),
            "Isofix" :response.xpath('//div[@class="inline-block"]//table//tr[td[contains(text(), "Isofix")]]/td[2]/text()').get().strip(),
            "Platform":response.xpath('//div[@class="inline-block"]//table//tr[td[contains(text(), "Platform")]]/td[2]/text()').get().strip(),
            'Weight Unladen': response.xpath('//div[@class="inline-block"]//table//tr[td[contains(text(), "Weight Unladen (EU)")]]/td[2]/text()').get().strip(),
            'Seats':response.css('div.inline-block td:contains("Seats") + td::text').get(),

    
         })

        yield vehicle_data