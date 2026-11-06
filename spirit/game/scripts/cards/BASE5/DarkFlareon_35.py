from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on, damage_per
from spirit.game.card_effects.ecard import has_fire_energy_attached, playing_with_fire


card = PokemonCardDef(
    guid="a73c0a55-4f0f-532e-a010-c820ce4143b0",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkFlareon.Name",
    display_name="Dark Flareon",
    searchable_by=["Dark Flareon", "Stage 1", "DarkFlareon"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Rage",
            game_text="Does 10 damage plus 10 more damage for each damage counter on Dark Flareon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), 10, base=10),
        ),
        Attack(
            title="Playing with Fire",
            game_text="Use this attack only if there are any Fire Energy cards attached to Dark Flareon. Flip a coin. If heads, discard 1 of those Energy cards and this attack does 30 damage plus 20 more damage; if tails, this attack does 30 damage.",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            damage_operator="+",
            condition=has_fire_energy_attached,
            effect=playing_with_fire,
        ),
    ],
)
