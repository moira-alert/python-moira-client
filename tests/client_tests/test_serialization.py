import pytest
from pydantic import BaseModel, ConfigDict, Field, ValidationError
from pydantic.experimental.missing_sentinel import MISSING


class BaseConfig:
    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
    )


class NullableRequiredDefaultValueCaseModel(BaseModel, BaseConfig):
    prop_schema: str | None = Field("default_string_value")


class NotNullableRequiredDefaultValueCaseModel(BaseModel, BaseConfig):
    prop_schema: str = Field("default_string_value")


class NullableRequiredNoDefaultValueCaseModel(BaseModel, BaseConfig):
    prop_schema: str | None


class NotNullableRequiredNoDefaultValueCaseModel(BaseModel, BaseConfig):
    prop_schema: str


class NullableNotRequiredDefaultValueCaseModel(BaseModel, BaseConfig):
    prop_schema: str | MISSING | None = Field("default_string_value")


class NotNullableNotRequiredDefaultValueCaseModel(BaseModel, BaseConfig):
    prop_schema: str | MISSING = Field("default_string_value")


class NullableNotRequiredNoDefaultValueCaseModel(BaseModel, BaseConfig):
    prop_schema: str | MISSING | None = Field(default=MISSING)


class NotNullableNotRequiredNoDefaultValueCaseModel(BaseModel, BaseConfig):
    prop_schema: str | MISSING = Field(default=MISSING)


class TestNullableRequiredDefaultValueCaseModel:
    def test_default(self) -> None:
        model_object = NullableRequiredDefaultValueCaseModel()  # type: ignore[call-arg]
        assert model_object.model_dump() == {"prop_schema": "default_string_value"}

    def test_custom(self) -> None:
        model_object = NullableRequiredDefaultValueCaseModel(prop_schema="my_string")
        assert model_object.model_dump() == {"prop_schema": "my_string"}

    def test_null(self) -> None:
        model_object = NullableRequiredDefaultValueCaseModel(prop_schema=None)
        assert model_object.model_dump() == {"prop_schema": None}


class TestNotNullableRequiredDefaultValueCaseModel:
    def test_default(self) -> None:
        model_object = NotNullableRequiredDefaultValueCaseModel()  # type: ignore[call-arg]
        assert model_object.model_dump() == {"prop_schema": "default_string_value"}

    def test_custom(self) -> None:
        model_object = NotNullableRequiredDefaultValueCaseModel(prop_schema="my_string")
        assert model_object.model_dump() == {"prop_schema": "my_string"}

    def test_null(self) -> None:
        with pytest.raises(ValidationError):
            NotNullableRequiredDefaultValueCaseModel(prop_schema=None)  # type: ignore[arg-type]


class TestNullableRequiredNoDefaultValueCaseModel:
    def test_no_value(self) -> None:
        with pytest.raises(ValidationError):
            NullableRequiredNoDefaultValueCaseModel()  # type: ignore[call-arg]

    def test_custom(self) -> None:
        model_object = NullableRequiredNoDefaultValueCaseModel(prop_schema="my_string")
        assert model_object.model_dump() == {"prop_schema": "my_string"}

    def test_null(self) -> None:
        model_object = NullableRequiredNoDefaultValueCaseModel(prop_schema=None)
        assert model_object.model_dump() == {"prop_schema": None}


class TestNotNullableRequiredNoDefaultValueCaseModel:
    def test_no_value(self) -> None:
        with pytest.raises(ValidationError):
            NotNullableRequiredNoDefaultValueCaseModel()  # type: ignore[call-arg]

    def test_custom(self) -> None:
        model_object = NotNullableRequiredNoDefaultValueCaseModel(prop_schema="my_string")
        assert model_object.model_dump() == {"prop_schema": "my_string"}

    def test_null(self) -> None:
        with pytest.raises(ValidationError):
            NotNullableRequiredNoDefaultValueCaseModel(prop_schema=None)  # type: ignore[arg-type]


class TestNullableNotRequiredDefaultValueCaseModel:
    def test_default(self) -> None:
        model_object = NullableNotRequiredDefaultValueCaseModel()  # type: ignore[call-arg]
        assert model_object.model_dump() == {"prop_schema": "default_string_value"}

    def test_custom(self) -> None:
        model_object = NullableNotRequiredDefaultValueCaseModel(prop_schema="my_string")
        assert model_object.model_dump() == {"prop_schema": "my_string"}

    def test_null(self) -> None:
        model_object = NullableNotRequiredDefaultValueCaseModel(prop_schema=None)
        assert model_object.model_dump() == {"prop_schema": None}


class TestNotNullableNotRequiredDefaultValueCaseModel:
    def test_default(self) -> None:
        model_object = NotNullableNotRequiredDefaultValueCaseModel()  # type: ignore[call-arg]
        assert model_object.model_dump() == {"prop_schema": "default_string_value"}

    def test_custom(self) -> None:
        model_object = NotNullableNotRequiredDefaultValueCaseModel(prop_schema="my_string")
        assert model_object.model_dump() == {"prop_schema": "my_string"}

    def test_null(self) -> None:
        with pytest.raises(ValidationError):
            NotNullableNotRequiredDefaultValueCaseModel(prop_schema=None)


class TestNullableNotRequiredNoDefaultValueCaseModel:
    def test_no_value(self) -> None:
        model_object = NullableNotRequiredNoDefaultValueCaseModel()
        assert model_object.model_dump() == {}

    def test_custom(self) -> None:
        model_object = NullableNotRequiredNoDefaultValueCaseModel(prop_schema="my_string")
        assert model_object.model_dump() == {"prop_schema": "my_string"}

    def test_null(self) -> None:
        model_object = NullableNotRequiredNoDefaultValueCaseModel(prop_schema=None)
        assert model_object.model_dump() == {"prop_schema": None}


class TestNotNullableNotRequiredNoDefaultValueCaseModel:
    def test_no_value(self) -> None:
        model_object = NotNullableNotRequiredNoDefaultValueCaseModel()
        assert model_object.model_dump() == {}

    def test_custom(self) -> None:
        model_object = NotNullableNotRequiredNoDefaultValueCaseModel(prop_schema="my_string")
        assert model_object.model_dump() == {"prop_schema": "my_string"}

    def test_null(self) -> None:
        with pytest.raises(ValidationError):
            NotNullableNotRequiredNoDefaultValueCaseModel(prop_schema=None)
