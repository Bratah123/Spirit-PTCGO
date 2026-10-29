from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage
from spirit.game.card_effects.sm4 import tlc, tlc_condition


card = PokemonCardDef(
    guid="9994afde-cdf6-578a-960c-72acaefd928e",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milotic.Name",
    display_name="Milotic",
    searchable_by=["Milotic", "Stage 1", "Milotic"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="SM4",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    family_id=349,
    abilities=[
        Attack(
            title="TLC",
            game_text="Shuffle 1 of your opponent's Benched Pok\u00e9mon that has any damage counters on it and all cards attached to it into their deck.",
            cost={PokemonTypes.WATER: 1},
            effect=tlc,
            condition=tlc_condition,
        ),
        Attack(
            title="Ocean Cyclone",
            game_text="This attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            # STUB: attack effect not implemented
            effect=spread_damage(10, also_base=True),
        ),
    ],
)