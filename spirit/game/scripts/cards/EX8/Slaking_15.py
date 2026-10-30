"""STUB: effect not implemented — do not guess mechanics.
Slaking (EX8 #15): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import amnesia, lazy_aura_vs_ex, lazy_headbutt_asleep


card = PokemonCardDef(
    guid="6b9c1692-fd74-5571-913e-4933f14febc0",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slaking.Name",
    display_name="Slaking",
    searchable_by=["Slaking", "Stage 2", "Slaking"],
    subtypes=["Stage 2"],
    collector_number=15,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    family_id=287,
    abilities=[
        Ability(
            title="Lazy Aura",
            game_text="As long as Slaking is your Active Pok\u00e9mon, any damage done by attacks from your opponent's Pok\u00e9mon-ex is reduced by 30 (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=lazy_aura_vs_ex(),
        ),
        Attack(
            title="Amnesia",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=amnesia,
        ),
        Attack(
            title="Lazy Headbutt",
            game_text="Slaking is now Asleep.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=70,
            # STUB: attack effect not implemented
            effect=lazy_headbutt_asleep(),
        ),
    ],
)