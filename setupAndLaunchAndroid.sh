
#count=1
if [ $# -eq 2 ];
then
  cd ../android-mobile
  git fetch
  git checkout release/$1 || exit 1
  git pull

  emulator -avd $2 -writable-system &
  emul=$!
  echo "$emul before appium"
  sleep 5
  if ps -p $emul > /dev/null
  then
  appium server --allow-insecure chromedriver_autodownload &
  appium=$!
    echo "$emul emulator pid"
    sleep 45
    adb kill-server
    adb start-server
    adb uninstall ru.app.androidmobile
    ./gradlew :app:installApiAppDebug -Dorg.gradle.java.home=$JAVA_11 || exit 1
    cd ../qa_tests_mobile

    trap "kill -9 '$appium' $emul" SIGINT
  else
    echo "Emul didnt start"
    exit 1
  fi
else
echo "No parameters found. "
fi
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
if [[ $2 == *'12_OS'* ]]; then
  os='12'
elif [[ $2 == *'11_OS'* ]]; then
  os='11'
elif [[ $2 == *'10_OS'* ]]; then
  os='10'
elif [[ $2 == *'8_OS'* ]]; then
  os='8'
elif [[ $2 == *'5_OS'* ]]; then
  os='5'
fi
echo $os
pytest -v --html=report.html --self-contained-html --os=$os --timeout=360
deactivate
rm -r venv/
kill -2 $$
#exit
