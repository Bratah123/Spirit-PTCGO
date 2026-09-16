from sqlalchemy import String
from sqlalchemy.orm import declarative_base

# MySQL requires a length for VARCHAR, including columns inferred from Mapped[str].
Base = declarative_base(type_annotation_map={
    str: String(255).with_variant(String(255, collation="utf8mb4_bin"), "mysql")
})
