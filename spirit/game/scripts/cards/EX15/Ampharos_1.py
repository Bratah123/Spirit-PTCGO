"""STUB: effect not implemented — do not guess mechanics.
Ampharos δ (EX15 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import delta_circle, holon_veil_treat_as_delta_passive
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="b3915546-f3e3-52e7-b9b8-e9fe1214e210",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name",
    display_name="Ampharos δ",
    searchable_by=["Ampharos \u03b4", "Stage 2", "Ampharos"],
    subtypes=["Stage 2"],
    collector_number=1,
    set_code="EX15",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=181,
    abilities=[
        Ability(
            title="Holon Veil",
            game_text="Treat each Basic Pok\u00e9mon and Evolution card in your deck, in your discard pile, in your hand, and in play as a Pok\u00e9mon that has \u03b4 on its card.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=holon_veil_treat_as_delta_passive(),
        ),
        Attack(
            title="Delta Circle",
            game_text="Does 20 damage plus 10 more damage for each Pok\u00e9mon you have in play that has \u03b4 on its card.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=delta_circle(20, 10),
        ),
    ],
)