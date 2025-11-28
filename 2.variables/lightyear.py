# 평균 거리 값 (단위: 킬로미터)
average_distance_km = 149597870.7
# 태양과 지구 사이의 평균 거리를 알려주는 문구 출력
print(f"태양과 지구 사이의 평균 거리는 약 {average_distance_km:.2f}킬로미터입니다.")
# 빛의 속도 (단위: 초당 킬로미터)
light_speed = 299792.458
# 평균 거리를 빛의 속도로 나누어 시간을 계산
time_in_seconds = average_distance_km / light_speed
# 계산된 시간을 시간, 분, 초로 변환
minutes, seconds = divmod(time_in_seconds, 60)
hours, minutes = divmod(minutes, 60)
# 결과 출력 (소수점 이하를 2자리로 제한)
print(f"태양에서 지구까지 빛이 도달하는 시간은 약 {hours:.0f}시간{minutes:.0f}분 {seconds:.2f}초 입니다.")