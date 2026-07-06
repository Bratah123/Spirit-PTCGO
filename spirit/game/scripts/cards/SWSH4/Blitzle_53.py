from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="80117752-5a22-55ee-a457-d2ec57313350",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name",
    display_name="Blitzle",
    searchable_by=["Blitzle", "Basic", "Blitzle"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="SWSH4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=522,
    abilities=[
        Attack(
            title="Zap Kick",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
    ],
)