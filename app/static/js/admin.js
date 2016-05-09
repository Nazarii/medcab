/**
 * Created by viktor on 5/9/16.
 */
var calendarSettings = {
    customButtons: {
        addButton: {
            text: 'Додати',
            click: function() {
                window.open("add-patient.html", "_self");
            }
        }
    },
    header: {
        left: 'prev,next addButton',
        center: '',
        right: 'month,agendaWeek,agendaDay'
    },
    editable: true,
    eventLimit: true, // allow "more" link when too many events
    fixedWeekCount: false,
    defaultView: 'agendaDay',
    minTime: "07:00:00",
    maxTime: "21:00:00",
    contentHeight: "auto",
    views: {
        week: {
            hiddenDays: [0, 6]
        }
    },
    //events: 'get_events.php',
    events: [
        {
            title: 'All Day Event',
            start: '2016-03-01'
        },
        {
            title: 'Long Event',
            start: '2016-03-07',
            end: '2016-03-10'
        },
        {
            title: 'Meeting',
            start: '2016-03-07T10:30:00',
            end: '2016-03-07T12:30:00'
        },
        {
            title: 'Dinner',
            start: '2016-03-12T20:00:00'
        },
        {
            title: 'Click for Google',
            url: 'http://google.com/',
            start: '2016-03-28'
        }
    ]
};

$(document).ready(function() {

    $('#calendar1, #calendar2, #calendar3').fullCalendar(calendarSettings);

});