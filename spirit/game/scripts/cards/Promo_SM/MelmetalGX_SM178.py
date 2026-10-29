from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.card_effects.smp import iron_force_gx, metal_blast


card = PokemonCardDef(
    guid="95696891-373f-50df-bb36-b613d5a4b601",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MelmetalGX.Name",
    display_name="Melmetal-GX",
    searchable_by=["Melmetal-GX", "Stage 1", "GX", "MelmetalGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=178,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    family_id=808,
    abilities=[
        Ability(
            title="Hard Coat",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Metal Blast",
            game_text="This attack does 20 more damage times the amount of Metal Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=110,
            damage_operator="+",
            effect=metal_blast,
        ),
        Attack(
            title="Iron Force-GX",
            game_text="Attach any number of Metal Energy cards from your discard pile to this Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 1},
            effect=iron_force_gx,
        ),
    ],
)