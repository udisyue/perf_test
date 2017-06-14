# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import price_types_pb2
import as_types_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='price_service.proto',
  package='price',
  serialized_pb='\n\x13price_service.proto\x12\x05price\x1a\x11price_types.proto\x1a\x0e\x61s_types.proto\"\xc1\x02\n\tPsRequest\x12\x11\n\tsearch_id\x18\x01 \x01(\t\x12\x12\n\nversion_id\x18\x02 \x01(\x05\x12\"\n\tuser_info\x18\x03 \x01(\x0b\x32\x0f.price.UserInfo\x12(\n\x0cservice_type\x18\x04 \x02(\x0e\x32\x12.price.ServiceType\x12(\n\x0clist_request\x18\x0b \x01(\x0b\x32\x12.price.ListRequest\x12,\n\x0e\x64\x65tail_request\x18\x0c \x01(\x0b\x32\x14.price.DetailRequest\x12.\n\x0f\x62ooking_request\x18\r \x01(\x0b\x32\x15.price.BookingRequest\x12\x37\n\x14price_update_request\x18\x0e \x01(\x0b\x32\x19.price.PriceUpdateRequest\"\x96\x02\n\nPsResponse\x12\x11\n\tsearch_id\x18\x01 \x01(\t\x12,\n\x0eservice_status\x18\x02 \x01(\x0b\x32\x14.el_v3.ServiceStatus\x12*\n\rlist_response\x18\x0b \x01(\x0b\x32\x13.price.ListResponse\x12.\n\x0f\x64\x65tail_response\x18\x0c \x01(\x0b\x32\x15.price.DetailResponse\x12\x30\n\x10\x62ooking_response\x18\r \x01(\x0b\x32\x16.price.BookingResponse\x12\x39\n\x15price_update_response\x18\x0e \x01(\x0b\x32\x1a.price.PriceUpdateResponse\"3\n\x0bListRequest\x12$\n\nquery_info\x18\x01 \x02(\x0b\x32\x10.el_v3.QueryInfo\"i\n\x0cListResponse\x12$\n\nlist_hotel\x18\x01 \x03(\x0b\x32\x10.price.ListHotel\x12\x33\n\x15region_promotion_info\x18\x02 \x03(\x0b\x32\x14.price.PromotionInfo\"5\n\rDetailRequest\x12$\n\nquery_info\x18\x01 \x02(\x0b\x32\x10.el_v3.QueryInfo\"o\n\x0e\x44\x65tailResponse\x12(\n\x0c\x64\x65tail_hotel\x18\x01 \x02(\x0b\x32\x12.price.DetailHotel\x12\x33\n\x15region_promotion_info\x18\x02 \x03(\x0b\x32\x14.price.PromotionInfo\"\\\n\x0e\x42ookingRequest\x12$\n\nquery_info\x18\x01 \x02(\x0b\x32\x10.el_v3.QueryInfo\x12$\n\ndetail_ota\x18\x02 \x01(\x0b\x32\x10.price.DetailOta\"p\n\x0f\x42ookingResponse\x12(\n\x0c\x64\x65tail_hotel\x18\x01 \x02(\x0b\x32\x12.price.DetailHotel\x12\x33\n\x15region_promotion_info\x18\x02 \x03(\x0b\x32\x14.price.PromotionInfo\"`\n\x12PriceUpdateRequest\x12$\n\nquery_info\x18\x01 \x01(\x0b\x32\x10.el_v3.QueryInfo\x12$\n\ndetail_ota\x18\x02 \x03(\x0b\x32\x10.price.DetailOta\"\x15\n\x13PriceUpdateResponse\"\xf5\x01\n\tOaRequest\x12\x11\n\tsearch_id\x18\x01 \x01(\t\x12\x12\n\nversion_id\x18\x02 \x01(\x05\x12\"\n\tuser_info\x18\x03 \x01(\x0b\x32\x0f.price.UserInfo\x12$\n\nquery_info\x18\x04 \x02(\x0b\x32\x10.el_v3.QueryInfo\x12\x14\n\x0crequest_type\x18\x05 \x02(\x05\x12\x0e\n\x06ota_id\x18\x06 \x02(\x05\x12\x19\n\x11ota_hotel_id_list\x18\x07 \x03(\t\x12\x10\n\x08is_exist\x18\x14 \x01(\x08\x12$\n\ndetail_ota\x18\x15 \x01(\x0b\x32\x10.price.DetailOta\"\xc2\x01\n\nOaResponse\x12\x11\n\tsearch_id\x18\x01 \x01(\t\x12,\n\x0eservice_status\x18\x02 \x01(\x0b\x32\x14.el_v3.ServiceStatus\x12)\n\x0f\x64\x65tail_ota_list\x18\x03 \x03(\x0b\x32\x10.price.DetailOta\x12$\n\nquery_info\x18\x04 \x01(\x0b\x32\x10.el_v3.QueryInfo\x12\"\n\tuser_info\x18\x05 \x01(\x0b\x32\x0f.price.UserInfo*V\n\x0bServiceType\x12\r\n\tLIST_TYPE\x10\x01\x12\x0f\n\x0b\x44\x45TAIL_TYPE\x10\x02\x12\x10\n\x0c\x42OOKING_TYPE\x10\x03\x12\x15\n\x11PRICE_UPDATE_TYPE\x10\x04\x32:\n\tPsService\x12-\n\x06Search\x12\x10.price.PsRequest\x1a\x11.price.PsResponse2:\n\tOaService\x12-\n\x06Search\x12\x10.price.OaRequest\x1a\x11.price.OaResponseB\x06\x80\x01\x01\x90\x01\x01')

_SERVICETYPE = descriptor.EnumDescriptor(
  name='ServiceType',
  full_name='price.ServiceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='LIST_TYPE', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DETAIL_TYPE', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='BOOKING_TYPE', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PRICE_UPDATE_TYPE', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1772,
  serialized_end=1858,
)


LIST_TYPE = 1
DETAIL_TYPE = 2
BOOKING_TYPE = 3
PRICE_UPDATE_TYPE = 4



_PSREQUEST = descriptor.Descriptor(
  name='PsRequest',
  full_name='price.PsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='search_id', full_name='price.PsRequest.search_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='version_id', full_name='price.PsRequest.version_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_info', full_name='price.PsRequest.user_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='service_type', full_name='price.PsRequest.service_type', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='list_request', full_name='price.PsRequest.list_request', index=4,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='detail_request', full_name='price.PsRequest.detail_request', index=5,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='booking_request', full_name='price.PsRequest.booking_request', index=6,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='price_update_request', full_name='price.PsRequest.price_update_request', index=7,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=66,
  serialized_end=387,
)


_PSRESPONSE = descriptor.Descriptor(
  name='PsResponse',
  full_name='price.PsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='search_id', full_name='price.PsResponse.search_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='service_status', full_name='price.PsResponse.service_status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='list_response', full_name='price.PsResponse.list_response', index=2,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='detail_response', full_name='price.PsResponse.detail_response', index=3,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='booking_response', full_name='price.PsResponse.booking_response', index=4,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='price_update_response', full_name='price.PsResponse.price_update_response', index=5,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=390,
  serialized_end=668,
)


_LISTREQUEST = descriptor.Descriptor(
  name='ListRequest',
  full_name='price.ListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='query_info', full_name='price.ListRequest.query_info', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=670,
  serialized_end=721,
)


_LISTRESPONSE = descriptor.Descriptor(
  name='ListResponse',
  full_name='price.ListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='list_hotel', full_name='price.ListResponse.list_hotel', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='region_promotion_info', full_name='price.ListResponse.region_promotion_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=723,
  serialized_end=828,
)


_DETAILREQUEST = descriptor.Descriptor(
  name='DetailRequest',
  full_name='price.DetailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='query_info', full_name='price.DetailRequest.query_info', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=830,
  serialized_end=883,
)


_DETAILRESPONSE = descriptor.Descriptor(
  name='DetailResponse',
  full_name='price.DetailResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='detail_hotel', full_name='price.DetailResponse.detail_hotel', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='region_promotion_info', full_name='price.DetailResponse.region_promotion_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=885,
  serialized_end=996,
)


_BOOKINGREQUEST = descriptor.Descriptor(
  name='BookingRequest',
  full_name='price.BookingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='query_info', full_name='price.BookingRequest.query_info', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='detail_ota', full_name='price.BookingRequest.detail_ota', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=998,
  serialized_end=1090,
)


_BOOKINGRESPONSE = descriptor.Descriptor(
  name='BookingResponse',
  full_name='price.BookingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='detail_hotel', full_name='price.BookingResponse.detail_hotel', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='region_promotion_info', full_name='price.BookingResponse.region_promotion_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1092,
  serialized_end=1204,
)


_PRICEUPDATEREQUEST = descriptor.Descriptor(
  name='PriceUpdateRequest',
  full_name='price.PriceUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='query_info', full_name='price.PriceUpdateRequest.query_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='detail_ota', full_name='price.PriceUpdateRequest.detail_ota', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1206,
  serialized_end=1302,
)


_PRICEUPDATERESPONSE = descriptor.Descriptor(
  name='PriceUpdateResponse',
  full_name='price.PriceUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1304,
  serialized_end=1325,
)


_OAREQUEST = descriptor.Descriptor(
  name='OaRequest',
  full_name='price.OaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='search_id', full_name='price.OaRequest.search_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='version_id', full_name='price.OaRequest.version_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_info', full_name='price.OaRequest.user_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='query_info', full_name='price.OaRequest.query_info', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='request_type', full_name='price.OaRequest.request_type', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ota_id', full_name='price.OaRequest.ota_id', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ota_hotel_id_list', full_name='price.OaRequest.ota_hotel_id_list', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_exist', full_name='price.OaRequest.is_exist', index=7,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='detail_ota', full_name='price.OaRequest.detail_ota', index=8,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1328,
  serialized_end=1573,
)


_OARESPONSE = descriptor.Descriptor(
  name='OaResponse',
  full_name='price.OaResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='search_id', full_name='price.OaResponse.search_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='service_status', full_name='price.OaResponse.service_status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='detail_ota_list', full_name='price.OaResponse.detail_ota_list', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='query_info', full_name='price.OaResponse.query_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_info', full_name='price.OaResponse.user_info', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1576,
  serialized_end=1770,
)

_PSREQUEST.fields_by_name['user_info'].message_type = price_types_pb2._USERINFO
_PSREQUEST.fields_by_name['service_type'].enum_type = _SERVICETYPE
_PSREQUEST.fields_by_name['list_request'].message_type = _LISTREQUEST
_PSREQUEST.fields_by_name['detail_request'].message_type = _DETAILREQUEST
_PSREQUEST.fields_by_name['booking_request'].message_type = _BOOKINGREQUEST
_PSREQUEST.fields_by_name['price_update_request'].message_type = _PRICEUPDATEREQUEST
_PSRESPONSE.fields_by_name['service_status'].message_type = as_types_pb2._SERVICESTATUS
_PSRESPONSE.fields_by_name['list_response'].message_type = _LISTRESPONSE
_PSRESPONSE.fields_by_name['detail_response'].message_type = _DETAILRESPONSE
_PSRESPONSE.fields_by_name['booking_response'].message_type = _BOOKINGRESPONSE
_PSRESPONSE.fields_by_name['price_update_response'].message_type = _PRICEUPDATERESPONSE
_LISTREQUEST.fields_by_name['query_info'].message_type = as_types_pb2._QUERYINFO
_LISTRESPONSE.fields_by_name['list_hotel'].message_type = price_types_pb2._LISTHOTEL
_LISTRESPONSE.fields_by_name['region_promotion_info'].message_type = price_types_pb2._PROMOTIONINFO
_DETAILREQUEST.fields_by_name['query_info'].message_type = as_types_pb2._QUERYINFO
_DETAILRESPONSE.fields_by_name['detail_hotel'].message_type = price_types_pb2._DETAILHOTEL
_DETAILRESPONSE.fields_by_name['region_promotion_info'].message_type = price_types_pb2._PROMOTIONINFO
_BOOKINGREQUEST.fields_by_name['query_info'].message_type = as_types_pb2._QUERYINFO
_BOOKINGREQUEST.fields_by_name['detail_ota'].message_type = price_types_pb2._DETAILOTA
_BOOKINGRESPONSE.fields_by_name['detail_hotel'].message_type = price_types_pb2._DETAILHOTEL
_BOOKINGRESPONSE.fields_by_name['region_promotion_info'].message_type = price_types_pb2._PROMOTIONINFO
_PRICEUPDATEREQUEST.fields_by_name['query_info'].message_type = as_types_pb2._QUERYINFO
_PRICEUPDATEREQUEST.fields_by_name['detail_ota'].message_type = price_types_pb2._DETAILOTA
_OAREQUEST.fields_by_name['user_info'].message_type = price_types_pb2._USERINFO
_OAREQUEST.fields_by_name['query_info'].message_type = as_types_pb2._QUERYINFO
_OAREQUEST.fields_by_name['detail_ota'].message_type = price_types_pb2._DETAILOTA
_OARESPONSE.fields_by_name['service_status'].message_type = as_types_pb2._SERVICESTATUS
_OARESPONSE.fields_by_name['detail_ota_list'].message_type = price_types_pb2._DETAILOTA
_OARESPONSE.fields_by_name['query_info'].message_type = as_types_pb2._QUERYINFO
_OARESPONSE.fields_by_name['user_info'].message_type = price_types_pb2._USERINFO
DESCRIPTOR.message_types_by_name['PsRequest'] = _PSREQUEST
DESCRIPTOR.message_types_by_name['PsResponse'] = _PSRESPONSE
DESCRIPTOR.message_types_by_name['ListRequest'] = _LISTREQUEST
DESCRIPTOR.message_types_by_name['ListResponse'] = _LISTRESPONSE
DESCRIPTOR.message_types_by_name['DetailRequest'] = _DETAILREQUEST
DESCRIPTOR.message_types_by_name['DetailResponse'] = _DETAILRESPONSE
DESCRIPTOR.message_types_by_name['BookingRequest'] = _BOOKINGREQUEST
DESCRIPTOR.message_types_by_name['BookingResponse'] = _BOOKINGRESPONSE
DESCRIPTOR.message_types_by_name['PriceUpdateRequest'] = _PRICEUPDATEREQUEST
DESCRIPTOR.message_types_by_name['PriceUpdateResponse'] = _PRICEUPDATERESPONSE
DESCRIPTOR.message_types_by_name['OaRequest'] = _OAREQUEST
DESCRIPTOR.message_types_by_name['OaResponse'] = _OARESPONSE

class PsRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PSREQUEST
  
  # @@protoc_insertion_point(class_scope:price.PsRequest)

class PsResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PSRESPONSE
  
  # @@protoc_insertion_point(class_scope:price.PsResponse)

class ListRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LISTREQUEST
  
  # @@protoc_insertion_point(class_scope:price.ListRequest)

class ListResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LISTRESPONSE
  
  # @@protoc_insertion_point(class_scope:price.ListResponse)

class DetailRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DETAILREQUEST
  
  # @@protoc_insertion_point(class_scope:price.DetailRequest)

class DetailResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DETAILRESPONSE
  
  # @@protoc_insertion_point(class_scope:price.DetailResponse)

class BookingRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BOOKINGREQUEST
  
  # @@protoc_insertion_point(class_scope:price.BookingRequest)

class BookingResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BOOKINGRESPONSE
  
  # @@protoc_insertion_point(class_scope:price.BookingResponse)

class PriceUpdateRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PRICEUPDATEREQUEST
  
  # @@protoc_insertion_point(class_scope:price.PriceUpdateRequest)

class PriceUpdateResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PRICEUPDATERESPONSE
  
  # @@protoc_insertion_point(class_scope:price.PriceUpdateResponse)

class OaRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OAREQUEST
  
  # @@protoc_insertion_point(class_scope:price.OaRequest)

class OaResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OARESPONSE
  
  # @@protoc_insertion_point(class_scope:price.OaResponse)


_PSSERVICE = descriptor.ServiceDescriptor(
  name='PsService',
  full_name='price.PsService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1860,
  serialized_end=1918,
  methods=[
  descriptor.MethodDescriptor(
    name='Search',
    full_name='price.PsService.Search',
    index=0,
    containing_service=None,
    input_type=_PSREQUEST,
    output_type=_PSRESPONSE,
    options=None,
  ),
])

class PsService(service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _PSSERVICE
class PsService_Stub(PsService):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _PSSERVICE


_OASERVICE = descriptor.ServiceDescriptor(
  name='OaService',
  full_name='price.OaService',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=1920,
  serialized_end=1978,
  methods=[
  descriptor.MethodDescriptor(
    name='Search',
    full_name='price.OaService.Search',
    index=0,
    containing_service=None,
    input_type=_OAREQUEST,
    output_type=_OARESPONSE,
    options=None,
  ),
])

class OaService(service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _OASERVICE
class OaService_Stub(OaService):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _OASERVICE

# @@protoc_insertion_point(module_scope)
