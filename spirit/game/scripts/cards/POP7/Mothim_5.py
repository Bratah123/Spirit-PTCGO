from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import silver_wind, raging_scales

card = PokemonCardDef(
    guid="0ad6c0e5-cbac-5310-aec4-f5a21c78509b",
    key="POP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mothim.Name",
    display_name="Mothim",
    searchable_by=['Mothim', 'Stage 1', 'Mothim'],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="POP7",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Burmy.Name",
    family_id=414,
    abilities=[
        Attack(
            title="Silver Wind",
            game_text="During your next turn, if an attack does damage to the Defending Pokémon (after applying Weakness and Resistance), that attack does 40 more damage.",
            cost={},
            effect=silver_wind(40),
        ),
        Attack(
            title="Raging Scales",
            game_text="If Mothim has any damage counters on it, this attack does 30 damage plus 40 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=raging_scales(30, 40),
        ),
    ],
)
