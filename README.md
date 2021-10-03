Azure Key Vault build
===
1.환경 세팅
----

    ./create_env.txt

:: 해당 파일 명령어들 실행
:: 참고로 az keyvault create --name <your-unique-keyvault-name> --resource-group KeyVault-PythonQS-rg 에서 <your-unique-keyvault-name>는 고유 naming을 하면 된다.
![Azurekeyvaulbuild1](https://user-images.githubusercontent.com/76723331/135743789-1a6a1b0a-728c-4213-b0ed-e1f248da5cdf.png)

+ Azure portal에서 생성된 리소스와 key vault 확인 가능
![Azurekeyvaulbuild3리소스생성및키볼트생성 portal](https://user-images.githubusercontent.com/76723331/135744391-2046a173-a36b-48e5-93f2-e3f42957a475.png)


2.액세스 정책
-----
  
+ 생성된 key vault에 가서 액세스 정책을 추가 해줘야함.
  
![Azurekeyvaulbuild키볼트액세스정책1](https://user-images.githubusercontent.com/76723331/135744221-7f3e924d-7798-4dd6-aee5-f65fb307ad0b.png)
![Azurekeyvaulbuild키볼트액세스정책2](https://user-images.githubusercontent.com/76723331/135744225-263b0187-c723-4914-bfcf-29aeb843db2e.png)
  
3.python 스크립트 실행
-----
    ./kv_secrets.py
+ key vault에 비밀 생성 예제 스크립트를 작성한 후 cmd 환경에서 실행한다.
![Azurekeyvaulbuild 예제파일 실행](https://user-images.githubusercontent.com/76723331/135744279-522495e3-5506-4514-a261-da6fa57fae30.png)
::그런데 이렇게 실행하면 생성 후 바로 delete 기능이 수행되기 때문에, if문을 추가하여 포탈에서 확인할 수 있게끔 제어를 걸어보았다.

![Azurekeyvaulbuild 포탈 확인을 위한 제어장치 추가](https://user-images.githubusercontent.com/76723331/135744313-a27d2909-4d19-486c-904b-e150b0fa8cd4.png)
이렇게 되면, delete 연산을 바로 진행하지 않기 때문에 Azure portal에서 비밀을 확인할 수 있다.
![Azurekeyvaulbuild 포탈에서 비밀 확인](https://user-images.githubusercontent.com/76723331/135744325-7ddc116d-7065-4dcb-accf-ed8e3d58954b.png)
