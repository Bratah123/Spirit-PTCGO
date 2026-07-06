from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="416d73c5-8c62-5d88-a94f-564673022e2e",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meloetta.Name",
    display_name="Meloetta",
    searchable_by=["Meloetta", "Basic", "Fusion Strike", "Meloetta"],
    subtypes=["Basic", "Fusion Strike"],
    collector_number=124,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=648,
    abilities=[
        Attack(
            title="Melodious Echo",
            game_text="This attack does 70 damage for each Fusion Strike Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)