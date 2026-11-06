from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.card_effects.ecard import count_basic_energy_types


card = PokemonCardDef(
    guid="2deff919-9ea6-5755-b211-f13c53158418",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hooh.Name",
    display_name="Ho-oh",
    searchable_by=["Ho-oh", "Basic", "Hooh"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="NEO3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=250,
    abilities=[
        Attack(
            title="Rainbow Burn",
            game_text="This attack does 30 damage plus 10 more damage for each type of Basic Energy card, if any, attached to Ho-Oh.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_basic_energy_types, 10, base=30),
        ),
    ],
)
