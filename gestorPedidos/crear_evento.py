from oauth import get_calendar_service
from datetime import datetime, timedelta


def main():
   # creates one hour event tomorrow 10 AM ART
   service = get_calendar_service()

   d = datetime.now().date()
   tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=1)).isoformat()

   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": 'Licitacion',
           "description": 'Prueba de apertura de licitacion',
           "start": {"dateTime": start, "timeZone": 'America/Argentina/Buenos_Aires'},
           "end": {"dateTime": end, "timeZone": 'America/Argentina/Buenos_Aires'},
       }
   ).execute()

   print("Created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])

if __name__ == '__main__':
    main()