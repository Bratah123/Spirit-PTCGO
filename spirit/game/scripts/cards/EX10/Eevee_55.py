"""STUB: effect not implemented — do not guess mechanics.
Eevee (EX10 #55): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import energy_evolution_passive

card = PokemonCardDef(
    guid="624d2b0f-6dae-53ee-8d27-f72fbd3e6ebb",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="EX10",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Ability(
            title="Energy Evolution",
            game_text="Whenever you attach an Energy card from your hand to Eevee, you may search your deck for a card that evolves from Eevee that is the same type as the Energy card you attached to Eevee. Put that card onto Eevee. (This counts as evolving Eevee.) Shuffle your deck afterward. This power can't be used when you attach an Energy card to Eevee as part of an attack's effect.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            passive=energy_evolution_passive(),
        ),
        Attack(
            title="Tail Whap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)