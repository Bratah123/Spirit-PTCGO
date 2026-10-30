from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ecard import damage_shift


card = PokemonCardDef(
    guid="146e3ddd-4caf-5341-b783-abb68ed118bd",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasGolduck.Name",
    display_name="Sabrina's Golduck",
    searchable_by=["Sabrina's Golduck", "Stage 1", "SabrinasGolduck"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="GYM2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasPsyduck.Name",
    family_id=54,
    abilities=[
        Attack(
            title="Damage Shift",
            game_text="Move 1 damage counter from each of your Pok\u00e9mon that has any on it to the Defending Pok\u00e9mon. (Don't apply Weakness and Resistance.)",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=damage_shift,
        ),
        Attack(
            title="Water Spray",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 20 more damage; if tails, this attack does 20 damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)
