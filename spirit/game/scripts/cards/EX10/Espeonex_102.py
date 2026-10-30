"""Espeon ex (EX10 #102)."""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    devo_flash_on_evolve, snap_tail_snipe, psyloop_trainers,
)

card = PokemonCardDef(
    guid="a1e8aff4-24ef-5ec5-9ba7-ca3da8b2072e",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espeonex.Name",
    display_name="Espeon ex",
    searchable_by=["Espeon ex", "Stage 1", "ex", "Espeonex"],
    subtypes=["Stage 1", "ex"],
    collector_number=102,
    set_code="EX10",
    rarity=Rarities.RareHoloEX,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Devo Flash",
            game_text="Once during your turn, when you play Espeon ex from your hand to evolve 1 of your Pok\u00e9mon, you may choose 1 Evolved Pok\u00e9mon on your opponent's Bench, remove the highest Stage Evolution card from that Pok\u00e9mon, and put it back into his or her hand.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_EVOLVE,
            effect=devo_flash_on_evolve(),
        ),
        Attack(
            title="Snap Tail",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=snap_tail_snipe(30),
        ),
        Attack(
            title="Psyloop",
            game_text="Does 60 damage plus 30 more damage for each Trainer card your opponent has in play.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=psyloop_trainers(60, 30),
        ),
    ],
)
