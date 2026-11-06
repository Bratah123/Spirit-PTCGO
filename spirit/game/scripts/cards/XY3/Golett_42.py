from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="0876d8f5-d05d-5e8e-89eb-f1fc4f7b3634",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    display_name="Golett",
    searchable_by=["Golett", "Basic", "Golett"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="XY3",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=622,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Rock Smash",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)