from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, flip_damage
from spirit.game.card_effects.ecard import removal_pulse


card = PokemonCardDef(
    guid="c4c37128-2a13-538e-8941-71685ab1fcb5",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysPoliwhirl.Name",
    display_name="Misty's Poliwhirl",
    searchable_by=["Misty's Poliwhirl", "Stage 1", "MistysPoliwhirl"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MistysPoliwag.Name",
    family_id=60,
    abilities=[
        Attack(
            title="Rapids",
            game_text="If the Defending Pok\u00e9mon has any Energy cards attached to it, flip a coin. If heads, choose 1 of those Energy cards and discard it.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=removal_pulse,
        ),
        Attack(
            title="Water Punch",
            game_text="Flip a number of coins equal to the number of Water Energy attached to Misty's Poliwhirl. This attack does 30 damage plus 10 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=flip_damage(
                coins_from=count_energy("self", energy_type=PokemonTypes.WATER),
                bonus_per_heads=10,
            ),
        ),
    ],
)
