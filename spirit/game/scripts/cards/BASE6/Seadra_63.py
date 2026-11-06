from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import unused_energy_bonus
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="c1453eb3-b792-57b1-ab02-c9e9afce6a87",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    display_name="Seadra",
    searchable_by=["Seadra", "Stage 1", "Seadra"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="BASE6",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name",
    family_id=116,
    abilities=[
        Attack(
            title="Water Gun",
            game_text="Does 20 damage plus 10 more damage for each Water Energy attached to Seadra but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unused_energy_bonus(10, 20, energy_type=PokemonTypes.WATER),
        ),
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Seadra.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=flip_protection(prevent=True, effects_too=True),
        ),
    ],
)
