"""Lopunny (POP9 #9)."""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ex import jazzed_heal_if_evolved


card = PokemonCardDef(
    guid="339e140c-b208-56e7-a848-8e88c0907bc0",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lopunny.Name",
    display_name="Lopunny",
    searchable_by=["Lopunny", "Stage 1", "Lopunny"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="POP9",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name",
    family_id=427,
    abilities=[
        Attack(
            title="Jump Kick",
            game_text="Does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=snipe_attack(20)
        ),
        Attack(
            title="Jazzed",
            game_text="If Lopunny evolved from Buneary during this turn, remove all damage counters from Lopunny.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=jazzed_heal_if_evolved()
        ),
    ]
)