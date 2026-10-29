from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f30154dd-6f1f-5085-be00-6c763ee0362f",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGraveler.Name",
    display_name="Alolan Graveler",
    searchable_by=["Alolan Graveler", "Stage 1", "AlolanGraveler"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGeodude.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Rollout",
            cost={},
            damage=30,
        ),
        Attack(
            title="Electroslug",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)