from django.urls import reverse
from rest_framework import status
from app.models import *
from app.tests.parenttest import ParentTest
from django.utils.crypto import get_random_string


class TestMapping(ParentTest):
    def test_mapping_encounter_by_midwife_no_previous_appointments(self):
        """
        Test mapping girl who has
        """
        request_data = {
            "GetInMapGirlBundibugyo16_midwife": {
                "GirlDemographic": [
                    {
                        "FirstName": [
                            "MukuluGirlTest"
                        ],
                        "LastName": [
                            "Muwalatest"
                        ],
                        "GirlsPhoneNumber": [
                            "0779281444"
                        ],
                        "DOB": [
                            "2004-02-26"
                        ]
                    }
                ],
                "GirlDemographic2": [
                    {
                        "NextOfKinNumber": [
                            "0779281822"
                        ]
                    }
                ],
                "GirlLocation": [
                    {
                        "county": [
                            "BUGHENDERA_COUNTY"
                        ],
                        "subcounty": [
                            "SINDILA"
                        ],
                        "parish": [
                            "NYANKONDA"
                        ],
                        "village": [
                            "BULYATA_II"
                        ]
                    }
                ],
                "Observations3": [
                    {
                        "marital_status": [
                            "married"
                        ],
                        "education_level": [
                            "primary_level"
                        ],
                        "MenstruationDate": [
                            "2020-02-28"
                        ]
                    }
                ],
                "Observations1": [
                    {
                        "bleeding": [
                            "no"
                        ],
                        "fever": [
                            "yes"
                        ]
                    }
                ],
                "Observations2": [
                    {
                        "swollenfeet": [
                            "no"
                        ],
                        "blurred_vision": [
                            "no"
                        ]
                    }
                ],
                "EmergencyCall": [
                    ""
                ],
                "ANCAppointmentPreviousGroup": [
                    {
                        "AttendedANCVisit": [
                            "no"
                        ]
                    }
                ],
                "ContraceptiveGroup": [
                    {
                        "UsedContraceptives": [
                            "no"
                        ],
                        "ReasonNoContraceptives": [
                            "None"
                        ]
                    }
                ],
                "ANCAppointmentGroup": [
                    {
                        "ANCDate": [
                            "2020-05-30"
                        ]
                    }
                ],
                "VouncherCardGroup": [
                    {
                        "VoucherCard": [
                            "no"
                        ]
                    }
                ],
                "meta": [
                    {
                        "instanceID": [
                            "uuid:21a505a9-2d17-4fed-a3ad-183343227eb3"
                        ]
                    }
                ]
            },
            "form_meta_data": {
                "GIRL_ID": "0",
                "USER_ID": self.chew.id
            }
        }
        url = reverse("mapping_encounter_webhook")
        request = self.client.post(url, request_data, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        appointments = Appointment.objects.filter(girl__first_name__icontains="MukuluGirlTest")
        self.assertEqual(appointments.count(), 1)
        # test that the appointment is within 2 weeks period
        self.assertLess(appointments.first().date.replace(tzinfo=None),
                        timezone.datetime(year=2020, month=6, day=14).replace(tzinfo=None))

    def test_mapping_encounter_by_midwife_with_previous_appointments(self):
        """
        Test mapping girl who has
        """
        request_data = {
            "GetInMapGirlBundibugyo16_midwife": {
                "GirlDemographic": [
                    {
                        "FirstName": [
                            "MukuluGirlTest"
                        ],
                        "LastName": [
                            "Muwalatest" + get_random_string(length=3)
                        ],
                        "GirlsPhoneNumber": [
                            "0779281444"
                        ],
                        "DOB": [
                            "2004-02-26"
                        ]
                    }
                ],
                "GirlDemographic2": [
                    {
                        "NextOfKinNumber": [
                            "0779281822"
                        ]
                    }
                ],
                "GirlLocation": [
                    {
                        "county": [
                            "BUGHENDERA_COUNTY"
                        ],
                        "subcounty": [
                            "SINDILA"
                        ],
                        "parish": [
                            "NYANKONDA"
                        ],
                        "village": [
                            "BULYATA_II"
                        ]
                    }
                ],
                "Observations3": [
                    {
                        "marital_status": [
                            "married"
                        ],
                        "education_level": [
                            "primary_level"
                        ],
                        "MenstruationDate": [
                            "2020-02-28"
                        ]
                    }
                ],
                "Observations1": [
                    {
                        "bleeding": [
                            "no"
                        ],
                        "fever": [
                            "yes"
                        ]
                    }
                ],
                "Observations2": [
                    {
                        "swollenfeet": [
                            "no"
                        ],
                        "blurred_vision": [
                            "no"
                        ]
                    }
                ],
                "EmergencyCall": [
                    ""
                ],
                "ANCAppointmentPreviousGroup": [
                    {
                        "AttendedANCVisit": [
                            "yes"
                        ],
                        "ANCDatePrevious": [
                            "2020-04-14"
                        ]

                    }
                ],
                "ContraceptiveGroup": [
                    {
                        "UsedContraceptives": [
                            "no"
                        ],
                        "ReasonNoContraceptives": [
                            "None"
                        ]
                    }
                ],
                "ANCAppointmentGroup": [
                    {
                        "ANCDate": [
                            "2020-05-30"
                        ]
                    }
                ],
                "VouncherCardGroup": [
                    {
                        "VoucherCard": [
                            "no"
                        ]
                    }
                ],
                "meta": [
                    {
                        "instanceID": [
                            "uuid:21a505a9-2d17-4fed-a3ad-183343227eb3"
                        ]
                    }
                ]
            },
            "form_meta_data": {
                "GIRL_ID": "0",
                "USER_ID": self.chew.id
            }
        }
        url = reverse("mapping_encounter_webhook")
        request = self.client.post(url, request_data, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        appointments = Appointment.objects.filter(girl__first_name__icontains="MukuluGirlTest")
        self.assertEqual(appointments.count(), 2)
        # test that the appointment is within 2 weeks period
        self.assertLess(appointments.first().date.replace(tzinfo=None),
                        timezone.datetime(year=2020, month=6, day=14).replace(tzinfo=None))
